# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ProvincecrawlPipeline(object):
    file=open('urls.jl',"wb")
    def _init_(self):
        self.file=self;
    def process_item(self, provinceitem, provinceUrlr):
        item=provinceitem
        line=json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item
