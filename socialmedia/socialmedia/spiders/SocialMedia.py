from scrapy.spider import Spider
from scrapy import Selector
from socialmedia.items import SocialMediaItem
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class MySpider(Spider):
    name = 'smm'
    allowed_domains = ['*']
    start_urls = ['http://en.wikipedia.org/wiki/Social_media']
    rules = (
             Rule(SgmlLinkExtractor(allow=()), callback="parse_items", follow= True),
             )
    def parse_items(self, response):
        items = []
        #Define keywords present in metadata to scrap the webpage
        keywords = ['social media','social business','social networking','social marketing','online marketing','social selling',
            'social customer experience management','social cxm','social cem','social crm','google analytics','seo','sem',
            'digital marketing','social media manager','community manager']
        for link in response.xpath("//a"):
            item = SocialMediaItem()
            #Extract webpage keywords 
            metakeywords = link.xpath('//meta[@name="keywords"]').extract()
            #Compare keywords and extract if one of the defined keyboards is present in the metadata
            if (keywords in metaKW for metaKW in metakeywords):
                    item['SourceTitle'] = link.xpath('/html/head/title').extract()
                    item['TargetTitle'] = link.xpath('text()').extract()
                    item['link'] = link.xpath('@href').extract()
                    outbound = str(link.xpath('@href').extract())
                    if 'http' in outbound:
                        items.append(item)
        return items
