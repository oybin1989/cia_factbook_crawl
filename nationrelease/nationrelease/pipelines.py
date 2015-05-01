# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class NationreleasePipeline(object):
    file=open('details.jl',"wb")
    def _init_(self):
        self.file=self;
    def process_item(self, NationreleaseItem, nationDetailSpider):
        item=NationreleaseItem
        line=json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item
