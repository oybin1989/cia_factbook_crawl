# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NationtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    country=scrapy.Field()
    gdp=scrapy.Field()
    background=scrapy.Field()

    pass
#可以多定义几个类
