# -*- coding: utf-8 -*-

# Scrapy settings for nationtest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nationtest'

SPIDER_MODULES = ['nationtest.spiders']
NEWSPIDER_MODULE = 'nationtest.spiders'
ITEM_PIPELINES={'nationtest.pipelines.NationtestPipeline':800}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nationtest (+http://www.yourdomain.com)'