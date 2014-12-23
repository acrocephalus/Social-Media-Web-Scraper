from scrapy.spider import Spider
from scrapy import Selector
from socialmedia.items import SocialMediaItem
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from urlparse import urlparse

class MySpider(CrawlSpider):
    name = 'smm'
    allowed_domains = []
    f = open("/home/acrocephalus/GitHub/Social-Media-Web-Scraper/socialmedia/Links.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    rules = (
            Rule(SgmlLinkExtractor(deny=('statcounter.com/','wikipedia','play.google','books.google.com','github.com','amazon','bit.ly','wikimedia','mediawiki','creativecommons.org',
                                         'extensions.joomla.org','contact','about','careers','jobs','itunes.apple','apple','microsoft','clevnet.bibliocommons.com',
                                         'feedproxy.google.com','feeds.feedburner.com','enable.java')), callback="parse_items", follow= True),
             )
    def parse_items(self, response):
        items = []
        #Define keywords present in body text to scrap the webpage
        keywords = ['social media','social business','social networking','social marketing','online marketing','social selling',
            'social customer experience management','social cxm','social cem','social crm','google analytics','seo','sem',
            'digital marketing','social media manager','community manager','content marketing']
        #Extract webpage content 
        bodyText = response.xpath('//body//p//text() | //body//h1//text() | //body//h2//text() | //body//h3//text()').extract()
        #Compare keywords and extract if one of the defined keyboards is present in the body
        if any(key in metakey for key in keywords for metakey in bodyText):
            for link in response.xpath("//a"):
                item = SocialMediaItem()
                item['SourceTitle'] = link.xpath('//title/text()').extract()
                item['SourceDomain'] = urlparse((link.xpath('//link[@rel="canonical"]/@href').extract()  or [''])[0]).hostname
                item['link'] = link.xpath('@href').extract()
                item['TargetDomain'] = urlparse((link.xpath('@href').extract() or [''])[0]).hostname
                item['TargetTitle'] = link.xpath('text()').extract()
                outbound = str(link.xpath('@href').extract())
                if 'http' in outbound:
                    items.append(item)
                    print item
        return items
