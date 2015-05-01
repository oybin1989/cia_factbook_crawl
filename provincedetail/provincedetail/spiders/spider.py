import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from provincedetail.items import ProvincedetailItem
import json

class MySpider(CrawlSpider):
    name = 'provincedetail'
    file=open('output.jl')                # load urls of countries.
    jsons=file.readlines()
    countries={}
    urls=[]
    countryname=[]
    for i in jsons:
        t=eval(i)
        urls.append(t['url'])
        countryname.append(t['country'])
    start_urls = urls
    def parse(self, response):
        item=ProvincedetailItem()
        hxs = HtmlXPathSelector(response)
        print response.url
        province1=hxs.xpath('//tr[@class="o" and count(following::h4[contains(text(),"Further subdivisions")])=1]/child::td[1]/text()').extract()
        province2=hxs.xpath('//tr[@class="e" and count(following::h4[contains(text(),"Further subdivisions")])=1]/child::td[1]/text()').extract()
        province3=hxs.xpath('//tr[@class="e" and count(following::h4[contains(text(),"Territorial extent")])=1]/child::td[1]/text()').extract()
        #province4=hxs.xpath('//tr[@class="e" and count(following::h4[contains(text(),"Territorial extent")])=1]/child::td[1]/text()').extract()
        province5=hxs.xpath('//tr[@class="o" and count(following::h4[contains(text(),"Territorial extent")])=1]/child::td[1]/text()').extract()
        #province6=hxs.xpath('//tr[@class="o" and count(following::h4[contains(text(),"Territorial extent")])=1]/child::td[1]/text()').extract()
        #province7=hxs.xpath('//tr[@class="e" and count(following::h4[contains(text(),"Origins of names:")])=1]/child::td[1]/text()').extract()
        #province8=hxs.xpath('//tr[@class="o" and count(following::h4[contains(text(),"Origins of names:")])=1]/child::td[1]/text()').extract()
        province0=hxs.xpath('//tr[@class="o" and count(following::li[contains(strong,"HASC")])=1]/child::td[1]/text()').extract()
        province9=hxs.xpath('//tr[@class="e" and count(following::li[contains(strong,"HASC")])=1]/child::td[1]/text()').extract()
        #t=province1+province2+province3+province4+province5+province6+province7+province8
        t=province0+province9+province1+province2+province3+province5
        item['province']=list(set(t))
        item['url']=response.url
        yield item
        pass
