# -*- coding: utf-8 -*-

# Scrapy settings for socialmedia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'socialmedia'

SPIDER_MODULES = ['socialmedia.spiders']
NEWSPIDER_MODULE = 'socialmedia.spiders'
DEPTH_LIMIT = 50
DOWNLOAD_DELAY = 0.50
RETRY_ENABLED = False
CONCURRENT_REQUESTS = 600
COOKIES_ENABLED = False
AUTOTHROTTLE_ENABLED = True
REDIRECT_MAX_TIMES = 3
LOG_LEVEL = 'INFO'
REDIRECT_ENABLED = False
AJAXCRAWL_ENABLED = True
ITEM_PIPELINES = ['socialmedia.pipelines.JsonWithEncodingPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'socialmedia (+http://www.yourdomain.com)'
