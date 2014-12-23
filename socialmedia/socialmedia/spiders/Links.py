from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from socialmedia.items import SocialMediaItem

class MySpider(CrawlSpider):
    name = 'links'
    allowed_domains = ['twitter.com']
    start_urls = ['http://www.twitter.com']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
        item = SocialMediaItem()
        item['url'] = response.url
        return item