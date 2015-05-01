import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from provincecrawl.items import ProvincecrawlItem
import json

class MySpider(CrawlSpider):
    name = "provinceUrl"
    allowed_domains = ['www.statoids.com/']
    start_urls = ['http://www.statoids.com/la.html','http://www.statoids.com/lb.html','http://www.statoids.com/lc.html','http://www.statoids.com/ldf.html','http://www.statoids.com/lg.html','http://www.statoids.com/lhj.html','http://www.statoids.com/lkl.html','http://www.statoids.com/lm.html','http://www.statoids.com/lno.html','http://www.statoids.com/lpr.html','http://www.statoids.com/ls.html','http://www.statoids.com/ltu.html','http://www.statoids.com/lvz.html']
    def parse(self, response):
        item=ProvincecrawlItem()
        hxs = HtmlXPathSelector(response)
        item['country']=hxs.xpath('//tr[@class="o" or @class="e"]/following::td[1]/text()').re('\w.*')
        item['url']='http://www.statoids.com/'+hxs.xpath('//tr[@class="o" or @class="e"]/following::td[1]/following::a[1]/@href').re('u...html')
        yield item
        pass
