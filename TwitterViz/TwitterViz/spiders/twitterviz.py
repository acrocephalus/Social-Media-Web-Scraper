from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy import Selector
from TwitterViz.items import TwitterVizItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from urlparse import urlparse
from scrapy.http import FormRequest
from loginform import fill_login_form
import json
from selenium import webdriver
import time

class MySpider(CrawlSpider):

    login_user = 'acrocephalus'
    login_pass = 'oaCPGEfqPEj4umdyFShXBKBNSi6W'

    name = "tv"
    allowed_domains = ['twitter.com']
    start_urls = ["https://twitter.com/Acrocephalus/followers"]
    rules = (
         Rule(LinkExtractor(allow=('https://twitter\.com/.*'), restrict_xpaths=('(//span[@class="u-linkComplex-target"])')), callback='parse_items', follow=True),
     )

# define login parameters
    def parse(self, response):
        args, url, method = fill_login_form(response.url, response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args, callback=self.after_login)

    def after_login(self, response):
        print '\n **You are logged in** \n'

# you are logged in here 
        
        def __init__(self):
            CrawlSpider.__init__(self)
# use any browser you wish
            self.browser = webdriver.Firefox() 
    
        def __del__(self):
            self.browser.close()
        
        def parse_items(self, response):
            item = TwitterVizItem() 
            self.browser.get(response.url)
# let JavaScript Load
            time.sleep(3) 
# scrape dynamically generated HTML
            hxs = Selector(text=self.browser.page_source) 
            item['Follower'] = hxs.select('(//span[@class="u-linkComplex-target"])[position()>2]').extract()
            item['Follows'] = hxs.select('(//span[@class="u-linkComplex-target"])[position()=1]').extract()
            print item
            return item