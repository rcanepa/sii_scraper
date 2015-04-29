import scrapy
from sii_uta.items import SiiUtaItem

class SiiUtaSpider(scrapy.Spider):
    name = "sii_uta"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.sii.cl/pagina/valores/uta.htm"
    ]

    def parse(self, response):
        thead_trs = response.xpath("//div[@id='contenido']/table/thead/tr")
        tbody_trs = response.xpath("//div[@id='contenido']/table/tbody/tr")
        tds = thead_trs[2].xpath(".//td")
        item = SiiUtaItem()
        item['year'] = tds[0].xpath(".//text()").re("\d+")
        item['value'] = tds[1].xpath(".//text()").re("\d+.\d+")
        print item
        yield item

        for tr in tbody_trs:
            item = SiiUtaItem()
            tds = tr.xpath(".//td")
            item['year'] = tds[0].xpath(".//text()").re("\d+")
            item['value'] = tds[1].xpath(".//text()").re("\d+.\d+")
            print item
            yield item
        
        