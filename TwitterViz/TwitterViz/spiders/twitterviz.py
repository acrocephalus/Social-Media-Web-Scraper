from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.spiders import Spider
from scrapy import Selector
from TwitterViz.items import TwitterVizItem
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from urlparse import urlparse

class MySpider(CrawlSpider):
    name = "tv"
    login_page = 'https://twitter.com/login?hide_message=true&redirect_after_login=%2Facrocephalus'
    allowed_domains = []
    start_urls = ["https://twitter.com/Acrocephalus/followers"]
     
    def parse_items(self, response):
        items = []
        item['Username'] = link.xpath('//span[@class="u-linkComplex-target"]').extract()
        