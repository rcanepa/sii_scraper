import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class UtaValue(scrapy.Item):
    year = scrapy.field()
    value = scrapy.field()


class MininovaSpider(CrawlSpider):

    name = 'sii'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.sii.cl/pagina/valores/uta.htm']
    # rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        t = UtaValue()
        t['year'] = response.xpath("//div[@id='contenido']/table/tr/td[0]/text()").extract()
        t['value'] = response.xpath("//div[@id='contenido']/table/tr/td[1]/text()").extract()
        return t
