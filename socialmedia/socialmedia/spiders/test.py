from socialmedia.items import SocialMediaItem
from scrapy.contrib.spiders import CrawlSpider

class MySpyder(CrawlSpider):
    name = "test"
    allowed_domains = ["jeffbullas.com"]
    start_urls = [
    "http://www.jeffbullas.com/2014/12/19/10-ways-to-succeed-in-the-new-age-of-mobile-content-marketing/"]

    def parse(self, response):
        #print response.xpath('//body//p//text()').extract()
        text = response.xpath('//body//p//text() | //body//h1//text() | //body//h2//text() | //body//h3//text()').extract()
        text =str(text)
        print unicode(text,'utf-8')
        with open("test.txt", "w") as f:
            f.write(text)
        
