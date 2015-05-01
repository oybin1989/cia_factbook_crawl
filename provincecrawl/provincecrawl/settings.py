# -*- coding: utf-8 -*-

# Scrapy settings for provincecrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'provincecrawl'

SPIDER_MODULES = ['provincecrawl.spiders']
NEWSPIDER_MODULE = 'provincecrawl.spiders'
ITEM_PIPELINES={'provincecrawl.pipelines.ProvincecrawlPipeline':900}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'provincecrawl (+http://www.yourdomain.com)'
