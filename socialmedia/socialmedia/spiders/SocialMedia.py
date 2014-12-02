from scrapy.spider import Spider
from scrapy import Selector
from socialmedia.items import SocialMediaItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from urlparse import urlparse

class MySpider(Spider):
    name = 'smm'
    allowed_domains = ['*']
    start_urls = ['http://en.wikipedia.org/wiki/Social_media']
    def parse(self, response):
        items = []
        for link in response.xpath("//a"):
            item = SocialMediaItem()
            item['SourceTitle'] = link.xpath('/html/head/title').extract()
            item['TargetTitle'] = link.xpath('text()').extract()
            item['link'] = link.xpath('@href').extract()
            outbound = str(link.xpath('@href').extract())
            if 'http' in outbound:
                items.append(item)
        return items

