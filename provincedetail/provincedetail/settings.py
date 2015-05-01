# -*- coding: utf-8 -*-

# Scrapy settings for provincedetail project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'provincedetail'

SPIDER_MODULES = ['provincedetail.spiders']
NEWSPIDER_MODULE = 'provincedetail.spiders'
ITEM_PIPELINES={'provincedetail.pipelines.ProvincedetailPipeline':900}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'provincedetail (+http://www.yourdomain.com)'
