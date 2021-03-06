import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from nationtest.items import  NationtestItem


class MySpider(CrawlSpider):
    name = 'nationLinkSpider'
    allowed_domains = ['https://www.cia.gov/library/publications/the-world-factbook/'];
    start_urls = ['https://www.cia.gov/library/publications/the-world-factbook/']

    def parse(self, response):
        BASEURL = 'https://www.cia.gov/library/publications/the-world-factbook/'
        item=NationtestItem()
        for r in response.selector.xpath('//option'):
            url=r.re('geos/[^^x]+.html')
            print(url)
            if(len(url)!=0):
                country=r.xpath('text()').extract()
                URL = BASEURL + url[0]
                item['url']=URL;
                item['country']=country[0];
                #item['gdp']=0;
                print (country)
                print URL
                yield item


            
            



