# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NationreleaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author=scrapy.Field()
    country=scrapy.Field()
    background=scrapy.Field()
    geo=scrapy.Field()
    PeopleandSociety=scrapy.Field()
    government=scrapy.Field()
    economy=scrapy.Field()
    energy=scrapy.Field()
    communications=scrapy.Field()
    transportation=scrapy.Field()
    transnational_issue=scrapy.Field()
    military=scrapy.Field()
    pass
