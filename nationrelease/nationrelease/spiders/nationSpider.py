import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from nationrelease.items import  NationreleaseItem


class MySpider(CrawlSpider):
    name = 'nationDetailSpider'
    file=open('urls.jl')                # load urls of countries.
    jsons=file.readlines()
    UrlList=[]
    t=0;
    for j in jsons:
        t=eval(j)
        UrlList.append(t['url'])        # parse json and store them in a list.
    allowed_domains = ['https://www.cia.gov/library/publications/the-world-factbook/'];
    start_urls = UrlList

    def parse(self, response):
        item=NationreleaseItem()
        hxs = HtmlXPathSelector(response)

        item['background']=hxs.xpath('//h2[@sectiontitle="Introduction"]/../following::*[1]/div[@class="category_data"]/text()').extract()

        item['country']=hxs.xpath('//h2[@sectiontitle="Introduction"]/span[@class="region"]/text()').extract()
        item['author']=["This data is crawled from CIA's factbook.And scrapy scripts for this fetching is designed by Wubin Ouyang","Email:oybin1989@hotmail.com" , "Website: http://benouyang.com/wordpress.","Done at 2015/4/28"]

        # Geography
        item['geo']={}
        geoTemp=item['geo']
        geoTemp['Location']=hxs.xpath('//h2[@sectiontitle="Geography"]/../following::*[6]/text()').extract()
        geoTemp['Geographic Coordinate']=hxs.xpath('//div[a="Geographic coordinates:"]/following::*[1]/text()').extract()
        geoTemp['Map Reference']=hxs.xpath('//div[a="Map references:"]/following::*[1]/text()').extract()
        geoTemp['Area']={}
        AreaTemp=geoTemp['Area']
        AreaTemp['total']=hxs.xpath('//div[a="Area:"]//following::span[text()="total: "][1]/following-sibling::*[1]/text()').extract()
        AreaTemp['land']=hxs.xpath('//div[a="Area:"]//following::span[text()="land: "][1]/following-sibling::*[1]/text()').extract()
        AreaTemp['water']=hxs.xpath('//div[a="Area:"]//following::span[text()="water: "][1]/following-sibling::*[1]/text()').extract()
        AreaTemp['note']=hxs.xpath('//div[a="Area:"]/following::span[text()="note: " and following::a[2]="Area - comparative:"][1]/following::*[1]/text()').extract()
        AreaTemp['country comparison to the world:']=hxs.xpath('//div[a="Area:"]/following::span[text()="country comparison to the world:  " and following::a[1]="Area - comparative:"][1]/following::a[1]/text()').extract()
        geoTemp['Area-comparative']=hxs.xpath('//div[a="Area - comparative:"]/following::*[1]/text()').extract()
        geoTemp['Land boundaries']={}
        LandBdTemp=geoTemp['Land boundaries']
        LandBdTemp['total']=hxs.xpath('//div[a="Land boundaries:"]/following::span[contains(text(),"total") and preceding::a[2]="Land boundaries:"]/following::*[1]/text()').extract()
        LandBdTemp['border countries']=hxs.xpath('//div[a="Land boundaries:"]/following::span[contains(text(),"border countries") and preceding::a[2]="Land boundaries:"]/following::*[1]/text()').extract()
        LandBdTemp['note']=hxs.xpath('//div[a="Land boundaries:"]/following::span[contains(text(),"note") and preceding::a[2]="Land boundaries:"]/following::*[1]/text()').extract()
        geoTemp['Coastline']=hxs.xpath('//div[a="Coastline:"]/following::*[1]/text()').extract()
        geoTemp['Maritime Claims']={}
        MaritimeTemp=geoTemp['Maritime Claims']
        MaritimeTemp['territorial sea']=hxs.xpath('//span[contains(text(),"territorial sea")]/following::*[1]/text()').extract()
        MaritimeTemp['contiguous zone']=hxs.xpath('//span[contains(text(),"contiguous zone")]/following::*[1]/text()').extract()
        MaritimeTemp['exclusive economic zone']=hxs.xpath('//span[contains(text(),"exclusive economic zone")]/following::*[1]/text()').extract()
        MaritimeTemp['continental shelf']=hxs.xpath('//span[contains(text(),"continental shelf")]/following::*[1]/text()').extract()
        MaritimeTemp['exclusive fishing zone']=hxs.xpath('//span[contains(text(),"exclusive fishing zone")]/following::*[1]/text()').extract()
        geoTemp['Climate']=hxs.xpath('//div[a="Climate:"]/following::*[1]/text()').extract()
        geoTemp['Terrain']=hxs.xpath('//div[a="Terrain:"]/following::*[1]/text()').extract()
        geoTemp['Irrigated land']=hxs.xpath('//div[a="Irrigated land:"]/following::*[1]/text()').extract()
        geoTemp['Total renewable water resources']=hxs.xpath('//div[a="Total renewable water resources:"]/following::*[1]/text()').extract()
        geoTemp['Environment - current issues']=hxs.xpath('//div[a="Environment - current issues:"]/following::*[1]/text()').extract()
        geoTemp['Geography - note']=hxs.xpath('//div[a="Geography - note:"]/following::*[1]/text()').extract()
        geoTemp['Elevation extremes']={'lowest point':hxs.xpath('//span[contains(text(),"lowest point")]/following::span[1]/text()').extract(),"highest point":hxs.xpath('//span[contains(text(),"highest point")]/following::span[1]/text()').extract()}
        geoTemp['Land use']={'arable land':hxs.xpath('//span[contains(text(),"arable land")]/following::span[1]/text()').extract(),"permanent crops":hxs.xpath('//span[contains(text(),"permanent crops")]/following::span[1]/text()').extract(),"other":hxs.xpath('//span[contains(text(),"other") and count(following::a[contains(text(),"Irrigated land")])=1]/following::span[1]/text()').extract()}
        geoTemp['Freshwater withdrawal (domestic/industrial/agricultural)']={'total':hxs.xpath('//div[contains(a,"Freshwater withdrawal (domestic/industrial/agricultural")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Natural hazards")])=1]/following::span[1]/text()').extract(),'per capita':hxs.xpath('//div[contains(a,"Freshwater withdrawal (domestic/industrial/agricultural")]/following::span[contains(text(),"per") and count(following::a[contains(text(),"Natural hazards")])=1]/following::span[1]/text()').extract()}
        geoTemp['Natural hazards']=hxs.xpath('//div[a="Natural hazards:"]/following::*[1]/text()').extract()
        geoTemp['Environment - international agreements']={'party to':hxs.xpath('//div[contains(a,"international agreements")]/following::span[contains(text(),"party to") and count(following::a[contains(text(),"Geography - note")])=1]/following::span[1]/text()').extract(),'signed, but not ratified':hxs.xpath('//div[contains(a,"international agreements")]/following::span[contains(text(),"signed, but not ratified") and count(following::a[contains(text(),"Geography - note")])=1]/following::span[1]/text()').extract()}
        # Geography done

        # People and Society
        item['PeopleandSociety']={}
        PaSTemp=item['PeopleandSociety']
        PaSTemp['Religions']=hxs.xpath('//div[a="Religions:"]/following::*[1]/text()').extract()
        PaSTemp['Populations']={}
        PopuTemp=PaSTemp['Populations']
        PopuTemp['amount']=hxs.xpath('//div[a="Population:"]/following::*[1]/text()').extract()
        PopuTemp['note']=hxs.xpath('//div[a="Population:"]/following::*[1]/following::span[text()="note: " and following::span[1]="country comparison to the world:  "]/text()').extract()
        PopuTemp['country comparison to the world']=hxs.xpath('//div[a="Population:"]/following::span[text()="country comparison to the world:  "][1]/following::a[1]/text()').extract()
        PaSTemp['Major urban areas - population']=hxs.xpath('//div[a="Major urban areas - population:"]/following::*[1]/text()').extract()
        PaSTemp['Mother mean age at first birth']=hxs.xpath('//div[contains(a,"mean age")]/following::div[1]/text()').extract()
        PaSTemp['Maternal mortality rate']=hxs.xpath('//div[contains(a,"Maternal mortality rate")]/following::div[1]/text()').extract()
        PaSTemp['Total fertility rate']=hxs.xpath('//div[contains(a,"Total fertility rate")]/following::div[1]/text()').extract()
        PaSTemp['Contraceptive prevalence rate']=hxs.xpath('//div[contains(a,"Contraceptive prevalence rate")]/following::div[1]/text()').extract()
        PaSTemp['Health expenditures']=hxs.xpath('//div[contains(a,"Health expenditures")]/following::div[1]/text()').extract()
        PaSTemp['Physician density']=hxs.xpath('//div[contains(a,"Physicians density")]/following::div[1]/text()').extract()
        PaSTemp['Hospital bed density']=hxs.xpath('//div[contains(a,"Hospital bed density")]/following::div[1]/text()').extract()
        PaSTemp['HIV/AIDS - adult prevalence rate']=hxs.xpath('//div[contains(a,"HIV/AIDS - adult prevalence rate")]/following::div[1]/text()').extract()
        PaSTemp['HIV/AIDS - people living with HIV/AIDS']=hxs.xpath('//div[contains(a,"HIV/AIDS - people living with HIV/AIDS")]/following::div[1]/text()').extract()
        PaSTemp['HIV/AIDS - deaths']=hxs.xpath('//div[contains(a,"HIV/AIDS - deaths")]/following::div[1]/text()').extract()
        PaSTemp['Obesity - adult prevalence rate']=hxs.xpath('//div[contains(a,"Obesity - adult prevalence rate")]/following::div[1]/text()').extract()
        PaSTemp['Children under the age of 5 years underweight']=hxs.xpath('//div[contains(a,"Children under the age of 5 years underweight")]/following::div[1]/text()').extract()
        PaSTemp['Education expenditures']=hxs.xpath('//div[contains(a,"Education expenditures")]/following::div[1]/text()').extract()
        PaSTemp['Ethnic groups']=hxs.xpath('//div[contains(a,"Ethnic groups")]/following::div[1]/text()').extract()
        PaSTemp['Languages']=hxs.xpath('//div[contains(a,"Languages:")]/following::div[1]/text()').extract()
        PaSTemp['Population growth rate']=hxs.xpath('//div[contains(a,"Population growth rate")]/following::div[1]/text()').extract()
        PaSTemp['Birth rate']=hxs.xpath('//div[contains(a,"Birth rate")]/following::div[1]/text()').extract()
        PaSTemp['Death rate']=hxs.xpath('//div[contains(a,"Death rate")]/following::div[1]/text()').extract()
        PaSTemp['Net migration rate']=hxs.xpath('//div[contains(a,"Net migration rate")]/following::div[1]/text()').extract()
        # set attribute of people and society
        PaSTemp['Nationality']={'noun':hxs.xpath('//div[contains(a,"Nationality")]/following::span[contains(text(),"noun") and count(following::a[contains(text(),"Ethnic groups")])=1]/following::span[1]/text()').extract(),'adjective':hxs.xpath('//div[contains(a,"Nationality")]/following::span[contains(text(),"adjective") and count(following::a[contains(text(),"Ethnic groups")])=1]/following::span[1]/text()').extract()}
        PaSTemp['Age structure']={'0-14 years':hxs.xpath('//div[contains(a,"Age structure")]/following::span[contains(text(),"0-14 years") and count(following::a[contains(text(),"Dependency ratios:")])=1]/following::span[1]/text()').extract(),'15-24 years':hxs.xpath('//div[contains(a,"Age structure")]/following::span[contains(text(),"15-24 years") and count(following::a[contains(text(),"Dependency ratios:")])=1]/following::span[1]/text()').extract(),'25-54 years:':hxs.xpath('//div[contains(a,"Age structure")]/following::span[contains(text(),"25-54 years") and count(following::a[contains(text(),"Dependency ratios:")])=1]/following::span[1]/text()').extract(),'55-64 years':hxs.xpath('//div[contains(a,"Age structure")]/following::span[contains(text(),"55-64 years") and count(following::a[contains(text(),"Dependency ratios:")])=1]/following::span[1]/text()').extract()}
        PaSTemp['Dependency ratios']={'total dependency ratio':hxs.xpath('//div[contains(a,"Dependency ratios")]/following::span[contains(text(),"total dependency ratio") and count(following::a[contains(text(),"Median age")])=1]/following::span[1]/text()').extract(),'youth dependency ratio':hxs.xpath('//div[contains(a,"Dependency ratios")]/following::span[contains(text(),"youth dependency ratio") and count(following::a[contains(text(),"Median age")])=1]/following::span[1]/text()').extract(),'elderly dependency ratio':hxs.xpath('//div[contains(a,"Dependency ratios")]/following::span[contains(text(),"elderly dependency ratio") and count(following::a[contains(text(),"Median age")])=1]/following::span[1]/text()').extract(),'potential support ratio':hxs.xpath('//div[contains(a,"Dependency ratios")]/following::span[contains(text(),"potential support ratio") and count(following::a[contains(text(),"Median age")])=1]/following::span[1]/text()').extract()}
        PaSTemp['Median age']={'total':scrapy.Field(),'male':scrapy.Field(),'female':scrapy.Field()}
        PaSTemp['Median age']['total']=hxs.xpath('//div[contains(a,"Median age")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Population growth rate")])=1]/following::span[1]/text()').extract()
        PaSTemp['Median age']['male']=hxs.xpath('//div[contains(a,"Median age")]/following::span[text()="male: " and count(following::a[contains(text(),"Population growth rate")])=1]/following::span[1]/text()').extract()
        PaSTemp['Median age']['female']=hxs.xpath('//div[contains(a,"Median age")]/following::span[contains(text(),"female") and count(following::a[contains(text(),"Population growth rate")])=1]/following::span[1]/text()').extract()

        PaSTemp['Urbanization']={'urban population':scrapy.Field(),'rate of urbanization':scrapy.Field()}
        PaSTemp['Urbanization']['urban population']=hxs.xpath('//div[contains(a,"Urbanization")]/following::span[contains(text(),"urban population") and count(following::a[contains(text(),"Major urban areas - population")])=1]/following::span[1]/text()').extract()
        PaSTemp['Urbanization']['rate of urbanization']=hxs.xpath('//div[contains(a,"Urbanization")]/following::span[contains(text(),"rate of urbanization:") and count(following::a[contains(text(),"Major urban areas - population")])=1]/following::span[1]/text()').extract()

        PaSTemp['Sex ratio']={'at birth':scrapy.Field(),'0-14 years':scrapy.Field(),'15-24 years':scrapy.Field(),'25-54 years':scrapy.Field(),'55-64 years':scrapy.Field(),'65 years and over':scrapy.Field(),'total population':scrapy.Field()}
        PaSTemp['Sex ratio']['0-14 years']=hxs.xpath('//div[contains(a,"Sex ratio")]/following::span[contains(text(),"0-14 years") and count(following::a[contains(text(),"mean age at first birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Sex ratio']['15-24 years']=hxs.xpath('//div[contains(a,"Sex ratio")]/following::span[contains(text(),"15-24 years") and count(following::a[contains(text(),"mean age at first birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Sex ratio']['25-54 years']=hxs.xpath('//div[contains(a,"Sex ratio")]/following::span[contains(text(),"25-54 years") and count(following::a[contains(text(),"mean age at first birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Sex ratio']['55-64 years']=hxs.xpath('//div[contains(a,"Sex ratio")]/following::span[contains(text(),"55-64 years") and count(following::a[contains(text(),"mean age at first birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Sex ratio']['65 years and over']=hxs.xpath('//div[contains(a,"Sex ratio")]/following::span[contains(text(),"65 years and over") and count(following::a[contains(text(),"mean age at first birth")])=1]/following::span[1]/text()').extract()

        PaSTemp['Infant mortality rate']={'total':scrapy.Field(),'male':scrapy.Field(),'female':scrapy.Field(),'country comparison to the world':scrapy.Field()}
        PaSTemp['Infant mortality rate']['total']=hxs.xpath('//div[contains(a,"Infant mortality rate")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Life expectancy at birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Infant mortality rate']['male']=hxs.xpath('//div[contains(a,"Infant mortality rate")]/following::span[text()="male: " and count(following::a[contains(text(),"Life expectancy at birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Infant mortality rate']['female']=hxs.xpath('//div[contains(a,"Infant mortality rate")]/following::span[contains(text(),"female") and count(following::a[contains(text(),"Life expectancy at birth")])=1]/following::span[1]/text()').extract()
        PaSTemp['Infant mortality rate']['country comparison to the world']=hxs.xpath('//div[contains(a,"Infant mortality rate")]/following::span[contains(text(),"country comparison to the world") and count(following::a[contains(text(),"Life expectancy at birth")])=1]/following::span[1]/text()').extract()

        PaSTemp['Life expectancy at birth']={'total population':scrapy.Field(),'male':scrapy.Field(),'female':scrapy.Field(),'country comparison to the world':scrapy.Field()}
        PaSTemp['Life expectancy at birth']['total population']=hxs.xpath('//div[contains(a,"Life expectancy at birth")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Total fertility rate")])=1]/following::span[1]/text()').extract()
        PaSTemp['Life expectancy at birth']['female']=hxs.xpath('//div[contains(a,"Life expectancy at birth")]/following::span[contains(text(),"female") and count(following::a[contains(text(),"Total fertility rate")])=1]/following::span[1]/text()').extract()
        PaSTemp['Life expectancy at birth']['country comparison to the world']=hxs.xpath('//div[contains(a,"Life expectancy at birth")]/following::span[contains(text(),"country comparison to the world") and count(following::a[contains(text(),"Total fertility rate")])=1]/following::span[1]/text()').extract()
        PaSTemp['Life expectancy at birth']['male']=hxs.xpath('//div[contains(a,"Life expectancy at birth")]/following::span[text()="male: " and count(following::a[contains(text(),"Total fertility rate")])=1]/following::span[1]/text()').extract()


        PaSTemp['Drinking water source']={'improved':scrapy.Field(),'unimproved':scrapy.Field()}
        PaSTemp['Drinking water source']['improved']=hxs.xpath('//div[contains(a,"Drinking water")]/following::span[text()="improved: "][1]/following::div[count(following::div[contains(span,"unimproved")])=2 and count(following::div[contains(a,"Sanitation facility")])=1 and contains(text(),"%")]/text()').extract()
        PaSTemp['Drinking water source']['unimproved']=hxs.xpath('//div[contains(a,"Drinking water")]/following::span[text()="improved: "][1]/following::div[count(following::div[contains(span,"unimproved")])=1 and count(following::div[contains(a,"Sanitation facility")])=1 and contains(text(),"%")]/text()').extract()

        PaSTemp['Sanitation facility access']={'improved':scrapy.Field(),'unimproved':scrapy.Field()}
        PaSTemp['Sanitation facility access']['improved']=hxs.xpath('//div[contains(a,"Sanitation")]/following::span[text()="improved: "][1]/following::div[count(following::div[contains(a,"HIV/AIDS - adult prevalence rate:")])=1 and count(following::span[text()="unimproved: "])=1 and contains(text(),"%")]/text()').extract()
        PaSTemp['Sanitation facility access']['unimproved']=hxs.xpath('//div[contains(a,"Sanitation")]/following::span[text()="unimproved: "][1]/following::div[count(following::div[contains(a,"HIV/AIDS - adult prevalence rate:")])=1 and contains(text(),"%")]/text()').extract()

        PaSTemp['School life expectancy (primary to tertiary education)']={'total':scrapy.Field(),'male':scrapy.Field(),'female':scrapy.Field()}
        PaSTemp['School life expectancy (primary to tertiary education)']['total']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"youth ages")])=1]/following::span[1]/text()').extract()
        PaSTemp['School life expectancy (primary to tertiary education)']['male']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[text()="male: " and count(following::a[contains(text(),"youth ages")])=1]/following::span[1]/text()').extract()
        PaSTemp['School life expectancy (primary to tertiary education)']['female']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[contains(text(),"female") and count(following::a[contains(text(),"youth ages")])=1]/following::span[1]/text()').extract()

        PaSTemp['Unemployment, youth ages 15-24']={'total':scrapy.Field(),'male':scrapy.Field(),'female':scrapy.Field()}
        PaSTemp['Unemployment, youth ages 15-24']['total']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[contains(text(),"total") and count(following::h2[contains(text(),"Government ::  ")])=1]/following::span[1]/text()').extract()
        PaSTemp['Unemployment, youth ages 15-24']['male']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[text()="male: " and count(following::h2[contains(text(),"Government ::  ")])=1]/following::span[1]/text()').extract()
        PaSTemp['Unemployment, youth ages 15-24']['female']=hxs.xpath('//div[contains(a,"School life expectancy")]/following::span[contains(text(),"female") and count(following::h2[contains(text(),"Government ::  ")])=1]/following::span[1]/text()').extract()

        #People and society part done

        # Government
        item['government']={}
        governTemp=item['government']
        governTemp['Government type']=hxs.xpath('//div[contains(a,"Government type")]/following::div[1]/text()').extract()
        governTemp['Administrative divisions']=hxs.xpath('//div[contains(a,"Administrative divisions")]/following::div[1]/text()').extract()
        governTemp['Dependent areas']=hxs.xpath('//div[contains(a,"Dependent areas")]/following::div[1]/text()').extract()
        governTemp['Independence']=hxs.xpath('//div[contains(a,"Independence")]/following::div[1]/text()').extract()
        governTemp['National holiday']=hxs.xpath('//div[contains(a,"National holiday")]/following::div[1]/text()').extract()
        governTemp['Legal system']=hxs.xpath('//div[contains(a,"Legal system")]/following::div[1]/text()').extract()
        governTemp['Constitution']=hxs.xpath('//div[contains(a,"Constitution")]/following::div[1]/text()').extract()
        governTemp['International law organization participation']=hxs.xpath('//div[contains(a,"International law organization participation")]/following::div[1]/text()').extract()
        governTemp['Suffrage']=hxs.xpath('//div[contains(a,"Suffrage")]/following::div[1]/text()').extract()
        governTemp['International organization participation']=hxs.xpath('//div[contains(a,"International organization participation")]/following::div[1]/text()').extract()
        governTemp['Flag description']=hxs.xpath('//div[contains(a,"Flag description")]/following::div[1]/text()').extract()
        governTemp['National symbol']=hxs.xpath('//div[contains(a,"National symbol")]/following::div[1]/text()').extract()
        governTemp['Political parties and leaders']=hxs.xpath('//div[contains(a,"Political parties and leaders:")]/following::div[count(following::div[contains(a,"Political pressure")])=1]/text()').extract()

        # set of government
        governTemp['Country name']={'conventional long form':scrapy.Field(),'conventional short form':scrapy.Field(),'local long form':scrapy.Field(),'local short form':scrapy.Field(),'former':scrapy.Field(),'abbreviation':scrapy.Field()}
        governTemp['Country name']['conventional long form']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"conventional long form") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()
        governTemp['Country name']['conventional short form']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"conventional short form") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()
        governTemp['Country name']['local long form']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"local long form") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()
        governTemp['Country name']['local short form']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"local short form") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()
        governTemp['Country name']['former']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"former") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()
        governTemp['Country name']['abbreviation']=hxs.xpath('//div[contains(a,"Country name")]/following::span[contains(text(),"abbreviation") and count(following::a[contains(text(),"Government type")])=1]/following::span[1]/text()').extract()

        governTemp['Capital']={'name':scrapy.Field(),'geographic coordinates':scrapy.Field(),'time difference':scrapy.Field(),'daylight saving time':scrapy.Field(),'note':scrapy.Field()}
        governTemp['Capital']['name']=hxs.xpath('//div[contains(a,"Capital")]/following::span[contains(text(),"name") and count(following::a[contains(text(),"Administrative divisions")])=1]/following::span[1]/text()').extract()
        governTemp['Capital']['geographic coordinates']=hxs.xpath('//div[contains(a,"Capital")]/following::span[contains(text(),"geographic coordinates") and count(following::a[contains(text(),"Administrative divisions")])=1]/following::span[1]/text()').extract()
        governTemp['Capital']['time difference']=hxs.xpath('//div[contains(a,"Capital")]/following::span[contains(text(),"time difference") and count(following::a[contains(text(),"Administrative divisions")])=1]/following::span[1]/text()').extract()
        governTemp['Capital']['daylight saving time']=hxs.xpath('//div[contains(a,"Capital")]/following::span[contains(text(),"daylight saving time") and count(following::a[contains(text(),"Administrative divisions")])=1]/following::span[1]/text()').extract()
        governTemp['Capital']['note']=hxs.xpath('//div[contains(a,"Capital")]/following::span[contains(text(),"note") and count(following::a[contains(text(),"Administrative divisions")])=1]/following::span[1]/text()').extract()

        governTemp['Executive branch']={'chief of state':scrapy.Field(),'head of government':scrapy.Field(),'cabinet':scrapy.Field(),'elections':scrapy.Field(),'election results':scrapy.Field()}
        governTemp['Executive branch']['chief of state']=hxs.xpath('//div[contains(a,"Executive branch")]/following::span[contains(text(),"chief of state") and count(following::a[contains(text(),"Legislative branch")])=1]/following::span[1]/text()').extract()
        governTemp['Executive branch']['head of government']=hxs.xpath('//div[contains(a,"Executive branch")]/following::span[contains(text(),"head of government") and count(following::a[contains(text(),"Legislative branch")])=1]/following::span[1]/text()').extract()
        governTemp['Executive branch']['cabinet']=hxs.xpath('//div[contains(a,"Executive branch")]/following::span[contains(text(),"cabinet") and count(following::a[contains(text(),"Legislative branch")])=1]/following::span[1]/text()').extract()
        governTemp['Executive branch']['elections']=hxs.xpath('//div[contains(a,"Executive branch")]/following::span[contains(text(),"elections") and count(following::a[contains(text(),"Legislative branch")])=1]/following::span[1]/text()').extract()
        governTemp['Executive branch']['election results']=hxs.xpath('//div[contains(a,"Executive branch")]/following::span[contains(text(),"election results") and count(following::a[contains(text(),"Legislative branch")])=1]/following::span[1]/text()').extract()

        governTemp['Legislative branch']={'description':scrapy.Field(),'elections':scrapy.Field(),'cabinet':scrapy.Field(),'election results':scrapy.Field()}
        governTemp['Legislative branch']['description']=hxs.xpath('//div[contains(a,"Legislative branch")]/following::span[contains(text(),"description") and count(following::a[contains(text(),"Judicial branch")])=1]/following::span[1]/text()').extract()
        governTemp['Legislative branch']['elections']=hxs.xpath('//div[contains(a,"Legislative branch")]/following::span[contains(text(),"elections") and count(following::a[contains(text(),"Judicial branch")])=1]/following::span[1]/text()').extract()
        governTemp['Legislative branch']['cabinet']=hxs.xpath('//div[contains(a,"Legislative branch")]/following::span[contains(text(),"cabinet") and count(following::a[contains(text(),"Judicial branch")])=1]/following::span[1]/text()').extract()
        governTemp['Legislative branch']['election results']=hxs.xpath('//div[contains(a,"Legislative branch")]/following::span[contains(text(),"election results") and count(following::a[contains(text(),"Judicial branch")])=1]/following::span[1]/text()').extract()


        governTemp['Judicial branch']={'highest court':scrapy.Field(),'judge selection and term of office':scrapy.Field(),'subordinate court':scrapy.Field()}
        governTemp['Judicial branch']['highest court']=hxs.xpath('//div[contains(a,"Judicial branch")]/following::span[contains(text(),"highest court") and count(following::a[contains(text(),"Political parties and leaders")])=1]/following::span[1]/text()').extract()
        governTemp['Judicial branch']['judge selection and term of office']=hxs.xpath('//div[contains(a,"Judicial branch")]/following::span[contains(text(),"judge selection and term of office") and count(following::a[contains(text(),"Political parties and leaders")])=1]/following::span[1]/text()').extract()
        governTemp['Judicial branch']['subordinate court']=hxs.xpath('//div[contains(a,"Judicial branch")]/following::span[contains(text(),"subordinate court") and count(following::a[contains(text(),"Political parties and leaders")])=1]/following::span[1]/text()').extract()

        governTemp['National anthem']={'name':scrapy.Field(),'lyrics/music':scrapy.Field(),'note':scrapy.Field(),'mp3':scrapy.Field()}
        governTemp['National anthem']['name']=hxs.xpath('//div[contains(a,"National anthem")]/following::span[contains(text(),"name") and count(following::div[@class="audio-player"])=1]/following::span[1]/text()').extract()
        governTemp['National anthem']['lyrics/music']=hxs.xpath('//div[contains(a,"National anthem")]/following::span[contains(text(),"lyrics/music") and count(following::div[@class="audio-player"])=1]/following::span[1]/text()').extract()
        governTemp['National anthem']['note']=hxs.xpath('//div[contains(a,"National anthem")]/following::span[contains(text(),"note") and count(following::div[@class="audio-player"])=1]/following::span[1]/text()').extract()
        if(len(hxs.xpath('//audio/@src').re('/.*'))>0):
            governTemp['National anthem']['mp3']='https://www.cia.gov/library/publications/the-world-factbook'+hxs.xpath('//audio/@src').re('/.*')[0]
        #government done

        # Economy

        item['economy']={}
        econTemp=item['economy']
        econTemp['Economy overview']=hxs.xpath('//div[contains(a,"Economy - overview")]/following::div[1]/text()').extract()
        econTemp['GDP (purchasing power parity)']=hxs.xpath('//div[contains(a,"GDP (purchasing power parity)")]/following::div[contains(text(),"$") and count(following::div[contains(a,"GDP (official exchange rate):")])=1]/text()').extract()
        econTemp['GDP (official exchange rate)']=hxs.xpath('//div[contains(a,"GDP (official exchange rate):")]/following::div[1]/text()').extract()
        econTemp['GDP - real growth rate']=hxs.xpath('//div[contains(a,"GDP - real growth rate")]/following::div[contains(text(),"%") and count(following::div[contains(a,"GDP - per capita (PPP):")])=1]/text()').extract()
        econTemp['GDP - per capita (PPP)']=hxs.xpath('//div[contains(a,"GDP - per capita")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Gross national saving:")])=1]/text()').extract()
        econTemp['Gross national saving']=hxs.xpath('//div[contains(a,"Gross national saving")]/following::div[contains(text(),"%") and count(following::div[contains(a,"GDP - composition, by end use")])=1]/text()').extract()
        econTemp['Agriculture - products']=hxs.xpath('//div[contains(a,"Agriculture - products:")]/following::div[1]/text()').extract()
        econTemp['Industries']=hxs.xpath('//div[contains(a,"Industries")]/following::div[1]/text()').extract()
        econTemp['Industrial production growth rate']=hxs.xpath('//div[contains(a,"Industrial production growth rate")]/following::div[1]/text()').extract()
        econTemp['Labor force']=hxs.xpath('//div[contains(a,"Labor force")]/following::div[1]/text()').extract()
        econTemp['Unemployment rate']=hxs.xpath('//div[contains(a,"Unemployment rate")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Population below poverty line")])=1]/text()').extract()
        econTemp['Population below poverty line']=hxs.xpath('//div[contains(a,"Population below poverty line")]/following::div[1]/text()').extract()
        econTemp['Distribution of family income - Gini index']=hxs.xpath('//div[contains(a,"Distribution of family income - Gini index")]/following::div[count(following::div[contains(a,"Budget:")])=1]/text()').extract()
        econTemp['Taxes and other revenues']=hxs.xpath('//div[contains(a,"Taxes and other revenues")]/following::div[1]/text()').extract()
        econTemp['Budget surplus (+) or deficit (-)']=hxs.xpath('//div[contains(a,"Budget surplus (+) or deficit (-)")]/following::div[1]/text()').extract()
        econTemp['Fiscal year']=hxs.xpath('//div[contains(a,"Fiscal year")]/following::div[1]/text()').extract()
        econTemp['Exports - commodities']=hxs.xpath('//div[contains(a,"Exports - commodities")]/following::div[1]/text()').extract()
        econTemp['Exports - partners']=hxs.xpath('//div[contains(a,"Exports - partners")]/following::div[1]/text()').extract()
        econTemp['Imports - commodities']=hxs.xpath('//div[contains(a,"Imports - commodities")]/following::div[1]/text()').extract()
        econTemp['Imports - partners']=hxs.xpath('//div[contains(a,"Imports - partners")]/following::div[1]/text()').extract()
        econTemp['Public debt']=hxs.xpath('//div[contains(a,"Public debt")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Fiscal year")])=1]/text()').extract()
        econTemp['Inflation rate (consumer prices)']=hxs.xpath('//div[contains(a,"Inflation rate (consumer prices)")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Central bank discount rate:")])=1]/text()').extract()
        econTemp['Central bank discount rate']=hxs.xpath('//div[contains(a,"Central bank discount rate")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Commercial bank prime lending rate")])=1]/text()').extract()
        econTemp['Commercial bank prime lending rate']=hxs.xpath('//div[contains(a,"Commercial bank prime lending rate")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Stock of narrow money")])=1]/text()').extract()
        econTemp['Stock of narrow money']=hxs.xpath('//div[contains(a,"Stock of narrow money")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Stock of broad money")])=1]/text()').extract()
        econTemp['Stock of broad money']=hxs.xpath('//div[contains(a,"Stock of broad money")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Stock of domestic credit")])=1]/text()').extract()
        econTemp['Stock of domestic credit']=hxs.xpath('//div[contains(a,"Stock of domestic credit")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Market value of publicly traded shares")])=1]/text()').extract()
        econTemp['Market value of publicly traded shares']=hxs.xpath('//div[contains(a,"Market value of publicly traded shares")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Current account balance:")])=1]/text()').extract()
        econTemp['Current account balance']=hxs.xpath('//div[contains(a,"Current account balance")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Exports:")])=1]/text()').extract()
        econTemp['Exports']=hxs.xpath('//div[contains(a,"Exports")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Exports - commodities")])=1]/text()').extract()
        econTemp['Imports']=hxs.xpath('//div[contains(a,"Imports")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Imports - commodities")])=1]/text()').extract()
        econTemp['Reserves of foreign exchange and gold']=hxs.xpath('//div[contains(a,"Reserves of foreign exchange and gold")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Debt - external")])=1]/text()').extract()
        econTemp['Debt - external']=hxs.xpath('//div[contains(a,"Debt - external")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Stock of direct foreign investment - at home")])=1]/text()').extract()
        econTemp['Stock of direct foreign investment - at home']=hxs.xpath('//div[contains(a,"Stock of direct foreign investment - at home")]/following::div[contains(text(),"$") and count(following::div[contains(a,"Stock of direct foreign investment - abroad")])=1]/text()').extract()


        # set of economy part

        econTemp['GDP - composition, by end use']={'household consumption':scrapy.Field(),'government consumption':scrapy.Field(),'investment in fixed capital':scrapy.Field(),'investment in inventories':scrapy.Field(),'exports of goods and services':scrapy.Field(),'imports of goods and services':scrapy.Field()}
        econTemp['GDP - composition, by end use']['household consumption']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"household consumption") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by end use']['government consumption']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"government consumption") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by end use']['investment in fixed capital']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"investment in fixed capital") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by end use']['exports of goods and services']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"exports of goods and services") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by end use']['imports of goods and services']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"imports of goods and services") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by end use']['investment in inventories']=hxs.xpath('//div[contains(a,"GDP - composition, by end use")]/following::span[contains(text(),"investment in inventories") and count(following::a[contains(text(),"GDP - composition, by sector of origin:")])=1]/following::span[1]/text()').extract()


        econTemp['GDP - composition, by sector of origin']={'agriculture':scrapy.Field(),'industry':scrapy.Field(),'services':scrapy.Field()}
        econTemp['GDP - composition, by sector of origin']['agriculture']=hxs.xpath('//div[contains(a,"GDP - composition, by sector of origin")]/following::span[contains(text(),"agriculture") and count(following::a[contains(text(),"Agriculture - products:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by sector of origin']['industry']=hxs.xpath('//div[contains(a,"GDP - composition, by sector of origin")]/following::span[contains(text(),"industry") and count(following::a[contains(text(),"Agriculture - products:")])=1]/following::span[1]/text()').extract()
        econTemp['GDP - composition, by sector of origin']['services']=hxs.xpath('//div[contains(a,"GDP - composition, by sector of origin")]/following::span[contains(text(),"services") and count(following::a[contains(text(),"Agriculture - products:")])=1]/following::span[1]/text()').extract()

        econTemp['Labor force - by occupation']={'farming, forestry, and fishing':scrapy.Field(),'manufacturing, extraction, transportation, and crafts':scrapy.Field(),'managerial, professional, and technical':scrapy.Field(),'sales and office':scrapy.Field(),'other services':scrapy.Field(),'agriculture':scrapy.Field(),'industry':scrapy.Field(),'services':scrapy.Field,'construction and public works':scrapy.Field(),'trade':scrapy.Field(),'government':scrapy.Field()}
        econTemp['Labor force - by occupation']['farming']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"farming") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['manufacturing, extraction, transportation, and crafts']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"manufacturing, extraction, transportation, and crafts") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['managerial, professional, and technical']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"managerial, professional, and technical") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['sales and office']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"sales and office") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['other services']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"other") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['agriculture']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"agriculture") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['industry']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"industry") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['services']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"services") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['construction and public works']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"construction and public works") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['government']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"government") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()
        econTemp['Labor force - by occupation']['trade']=hxs.xpath('//div[contains(a,"Labor force - by occupation")]/following::span[contains(text(),"trade") and count(following::a[contains(text(),"Unemployment rate:")])=1]/following::span[1]/text()').extract()

        econTemp['Household income or consumption by percentage share']={'lowest 10%':scrapy.Field(),'highest 10%':scrapy.Field()}
        econTemp['Household income or consumption by percentage share']['lowest 10%']=hxs.xpath('//div[contains(a,"Household income or consumption by percentage share")]/following::span[contains(text(),"lowest 10%") and count(following::a[contains(text(),"Distribution of family income - Gini index")])=1]/following::span[1]/text()').extract()
        econTemp['Household income or consumption by percentage share']['highest 10%']=hxs.xpath('//div[contains(a,"Household income or consumption by percentage share")]/following::span[contains(text(),"highest 10%") and count(following::a[contains(text(),"Distribution of family income - Gini index")])=1]/following::span[1]/text()').extract()


        econTemp['Budget']={'revenues':scrapy.Field(),'expenditures':scrapy.Field()}
        econTemp['Budget']['revenues']=hxs.xpath('//div[contains(a,"Budget")]/following::span[contains(text(),"revenues") and count(following::a[contains(text(),"Taxes and other revenues")])=1]/following::span[1]/text()').extract()
        econTemp['Budget']['expenditures']=hxs.xpath('//div[contains(a,"Budget")]/following::span[contains(text(),"expenditures") and count(following::a[contains(text(),"Taxes and other revenues")])=1]/following::span[1]/text()').extract()

        econTemp['Exchange rate']=hxs.xpath('//div[contains(a,"Exchange rates:")]/following::div[count(following::h2[contains(text(),"Energy ::")])=1]/text()').extract()

        # economy part done

        # Energy
        item['energy']={}
        enegTemp=item['energy']
        enegTemp['Electricity - production']=hxs.xpath('//div[contains(a,"Electricity - production")]/following::div[1]/text()').extract()
        enegTemp['Electricity - consumption']=hxs.xpath('//div[contains(a,"Electricity - consumption")]/following::div[1]/text()').extract()
        enegTemp['Electricity - exports']=hxs.xpath('//div[contains(a,"Electricity - exports")]/following::div[1]/text()').extract()
        enegTemp['Electricity - imports']=hxs.xpath('//div[contains(a,"Electricity - imports")]/following::div[1]/text()').extract()
        enegTemp['Electricity - installed generating capacity']=hxs.xpath('//div[contains(a,"Electricity - installed generating capacity")]/following::div[1]/text()').extract()
        enegTemp['Electricity - from fossil fuels']=hxs.xpath('//div[contains(a,"Electricity - from fossil fuels")]/following::div[1]/text()').extract()
        enegTemp['Electricity - from nuclear fuels']=hxs.xpath('//div[contains(a,"Electricity - from nuclear fuels")]/following::div[1]/text()').extract()
        enegTemp['Electricity - from hydroelectric plants']=hxs.xpath('//div[contains(a,"Electricity - from hydroelectric plants")]/following::div[1]/text()').extract()
        enegTemp['Electricity - from other renewable sources']=hxs.xpath('//div[contains(a,"Electricity - from other renewable sources")]/following::div[1]/text()').extract()
        enegTemp['Crude oil - production']=hxs.xpath('//div[contains(a,"Crude oil - production")]/following::div[1]/text()').extract()
        enegTemp['Refined petroleum products - production']=hxs.xpath('//div[contains(a,"Refined petroleum products - production")]/following::div[1]/text()').extract()
        enegTemp['Refined petroleum products - consumption']=hxs.xpath('//div[contains(a,"Refined petroleum products - consumption")]/following::div[1]/text()').extract()
        enegTemp['Crude oil - proved reserves']=hxs.xpath('//div[contains(a,"Crude oil - proved reserves")]/following::div[1]/text()').extract()
        enegTemp['Refined petroleum products - exports']=hxs.xpath('//div[contains(a,"Refined petroleum products - exports")]/following::div[1]/text()').extract()
        enegTemp['Refined petroleum products - imports']=hxs.xpath('//div[contains(a,"Refined petroleum products - imports")]/following::div[1]/text()').extract()
        enegTemp['Natural gas - production']=hxs.xpath('//div[contains(a,"Natural gas - production")]/following::div[1]/text()').extract()
        enegTemp['Natural gas - consumption']=hxs.xpath('//div[contains(a,"Natural gas - consumption")]/following::div[1]/text()').extract()
        enegTemp['Natural gas - exports']=hxs.xpath('//div[contains(a,"Natural gas - exports")]/following::div[1]/text()').extract()
        enegTemp['Natural gas - imports']=hxs.xpath('//div[contains(a,"Natural gas - imports")]/following::div[1]/text()').extract()
        enegTemp['Natural gas - proved reserves']=hxs.xpath('//div[contains(a,"Natural gas - proved reserves")]/following::div[1]/text()').extract()
        enegTemp['Carbon dioxide emissions from consumption of energy']=hxs.xpath('//div[contains(a,"Carbon dioxide emissions from consumption of energy")]/following::div[1]/text()').extract()

        #energy part done

        # Communications
        item['communications']={}
        comcTemp=item['communications']
        comcTemp['Telephones - main lines in use']=hxs.xpath('//div[contains(a,"Telephones - main lines in use")]/following::div[1]/text()').extract()
        comcTemp['Telephones - mobile cellular']=hxs.xpath('//div[contains(a,"Telephones - mobile cellular")]/following::div[1]/text()').extract()
        comcTemp['Broadcast media']=hxs.xpath('//div[contains(a,"Broadcast media")]/following::div[1]/text()').extract()
        comcTemp['Radio broadcast stations']=hxs.xpath('//div[contains(a,"Radio broadcast stations")]/following::div[1]/text()').extract()
        comcTemp['Television broadcast stations']=hxs.xpath('//div[contains(a,"Television broadcast stations")]/following::div[1]/text()').extract()
        comcTemp['Telephone system']={}
        comcTemp['Internet country code']=hxs.xpath('//div[contains(a,"Internet country code")]/following::div[1]/text()').extract()
        comcTemp['Internet hosts']=hxs.xpath('//div[contains(a,"Internet hosts")]/following::div[1]/text()').extract()
        comcTemp['Internet users']=hxs.xpath('//div[contains(a,"Internet users")]/following::div[1]/text()').extract()

        #set of communication

        comcTemp['Telephone system']={'general assessment':scrapy.Field(),'domestic':scrapy.Field(),'international':scrapy.Field()}
        comcTemp['Telephone system']['general assessment']=hxs.xpath('//div[contains(a,"Telephone system")]/following::span[contains(text(),"general assessment") and count(following::a[contains(text(),"Broadcast media")])=1]/following::span[1]/text()').extract()
        comcTemp['Telephone system']['domestic']=hxs.xpath('//div[contains(a,"Telephone system")]/following::span[contains(text(),"domestic") and count(following::a[contains(text(),"Broadcast media")])=1]/following::span[1]/text()').extract()
        comcTemp['Telephone system']['international']=hxs.xpath('//div[contains(a,"Telephone system")]/following::span[contains(text(),"international") and count(following::a[contains(text(),"Broadcast media")])=1]/following::span[1]/text()').extract()

        #communication part done

        # Transportations
        item['transportation']={}
        transpTemp=item['transportation']
        transpTemp['Airports']=hxs.xpath('//div[contains(a,"Airports")]/following::div[1]/text()').extract()

        transpTemp['Airports with paved runways']={'total':scrapy.Field(),'over 3,047 m':scrapy.Field(),'2,438 to 3,047 m':scrapy.Field(),'1,524 to 2,437 m':scrapy.Field(),'914 to 1,523 m':scrapy.Field(),'under 914 m':scrapy.Field()}
        transpTemp['Airports with paved runways']['total']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports with paved runways']['over 3,047 m']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"over 3,047 m") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports with paved runways']['2,438 to 3,047 m']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"2,438 to 3,047 m") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports with paved runways']['1,524 to 2,437 m']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"1,524 to 2,437 m") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports with paved runways']['914 to 1,523 m']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"914 to 1,523 m") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports with paved runways']['under 914 m']=hxs.xpath('//div[contains(a,"Airports - with paved runways:")]/following::span[contains(text(),"under 914 m") and count(following::a[contains(text(),"Airports - with unpaved runways:")])=1]/following::span[1]/text()').extract()


        transpTemp['Airports - with unpaved runways']={'total':scrapy.Field(),'over 3,047 m':scrapy.Field(),'2,438 to 3,047 m':scrapy.Field(),'1,524 to 2,437 m':scrapy.Field(),'914 to 1,523 m':scrapy.Field(),'under 914 m':scrapy.Field()}
        transpTemp['Airports - with unpaved runways']['total']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports - with unpaved runways']['over 3,047 m']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"over 3,047 m") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports - with unpaved runways']['2,438 to 3,047 m']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"2,438 to 3,047 m") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports - with unpaved runways']['1,524 to 2,437 m']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"1,524 to 2,437 m") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports - with unpaved runways']['914 to 1,523 m']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"914 to 1,523 m") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()
        transpTemp['Airports - with unpaved runways']['under 914 m']=hxs.xpath('//div[contains(a,"Airports - with unpaved runways")]/following::span[contains(text(),"under 914 m") and count(following::a[contains(text(),"Heliports:")])=1]/following::span[1]/text()').extract()



        transpTemp['Railways']={'total':scrapy.Field(),'broad gauge':scrapy.Field(),'standard gauge':scrapy.Field(),'narrow gauge':scrapy.Field()}
        transpTemp['Railways']['total']=hxs.xpath('//div[contains(a,"Railways")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Roadways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Railways']['broad gauge']=hxs.xpath('//div[contains(a,"Railways")]/following::span[contains(text(),"broad gauge") and count(following::a[contains(text(),"Roadways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Railways']['standard gauge']=hxs.xpath('//div[contains(a,"Railways")]/following::span[contains(text(),"standard gauge") and count(following::a[contains(text(),"Roadways:")])=1]/following::span[1]/text()').extract()
        transpTemp['Railways']['narrow gauge']=hxs.xpath('//div[contains(a,"Railways")]/following::span[contains(text(),"narrow gauge") and count(following::a[contains(text(),"Roadways:")])=1]/following::span[1]/text()').extract()


        transpTemp['Roadways']={'total':scrapy.Field(),'paved':scrapy.Field(),'unpaved':scrapy.Field()}
        transpTemp['Roadways']['total']=hxs.xpath('//div[contains(a,"Roadways")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Waterways")])=1]/following::span[1]/text()').extract()
        transpTemp['Roadways']['paved']=hxs.xpath('//div[contains(a,"Roadways")]/following::span[contains(text(),"paved") and count(following::a[contains(text(),"Waterways")])=1]/following::span[1]/text()').extract()
        transpTemp['Roadways']['unpaved']=hxs.xpath('//div[contains(a,"Roadways")]/following::span[contains(text(),"unpaved") and count(following::a[contains(text(),"Waterways")])=1]/following::span[1]/text()').extract()



        transpTemp['Merchant marine']={'total':scrapy.Field(),'by type':scrapy.Field(),'foreign-owned':scrapy.Field(),'registered in other countries':scrapy.Field(),'country comparison to the world':scrapy.Field()}
        transpTemp['Merchant marine']['total']=hxs.xpath('//div[contains(a,"Merchant marine")]/following::span[contains(text(),"total") and count(following::a[contains(text(),"Ports and terminals:")])=1]/following::span[1]/text()').extract()
        transpTemp['Merchant marine']['foreign-owned']=hxs.xpath('//div[contains(a,"Merchant marine")]/following::span[contains(text(),"foreign-owned") and count(following::a[contains(text(),"Ports and terminals:")])=1]/following::span[1]/text()').extract()
        transpTemp['Merchant marine']['registered in other countries']=hxs.xpath('//div[contains(a,"Merchant marine")]/following::span[contains(text(),"registered in other countries") and count(following::a[contains(text(),"Ports and terminals:")])=1]/following::span[1]/text()').extract()
        transpTemp['Merchant marine']['by type']=hxs.xpath('//div[contains(a,"Merchant marine")]/following::span[contains(text(),"by type") and count(following::a[contains(text(),"Ports and terminals:")])=1]/following::span[1]/text()').extract()
        transpTemp['Merchant marine']['country comparison to the world']=hxs.xpath('//div[contains(a,"Merchant marine")]/following::span[contains(text(),"country comparison to the world") and count(following::a[contains(text(),"Ports and terminals:")])=1]/following::span[1]/text()').extract()


        transpTemp['Ports and terminals']=hxs.xpath('//div[contains(a,"Ports and terminals")]/following::span[contains(text(),"port") and count(following::h2[contains(text(),"Military ::  ")])=1]/following::span[1]/text()').extract()


        transpTemp['Heliports']=hxs.xpath('//div[contains(a,"Heliports")]/following::div[1]/text()').extract()
        transpTemp['Pipelines']=hxs.xpath('//div[contains(a,"Pipelines")]/following::div[1]/text()').extract()
        transpTemp['Waterways']=hxs.xpath('//div[contains(a,"Waterways")]/following::div[1]/text()').extract()

        #transportation part done



        # Military
        item['military']={}
        miliTemp=item['military']
        miliTemp['Military branches']=hxs.xpath('//div[contains(a,"Military branches")]/following::div[1]/text()').extract()
        miliTemp['Military service age and obligation']=hxs.xpath('//div[contains(a,"Military service age and obligation")]/following::div[1]/text()').extract()
        miliTemp['Military expenditures']=hxs.xpath('//div[contains(a,"Military expenditures")]/following::div[contains(text(),"%") and count(following::div[contains(a,"Disputes - international")])=1]/text()').extract()

        miliTemp['Manpower available for military service']={'males age 16-49':scrapy.Field(),'females age 16-49':scrapy.Field()}
        miliTemp['Manpower available for military service']['males age 16-49']=hxs.xpath('//div[contains(a,"Manpower available for military service")]/following::span[text()="males age 16-49: " and count(following::a[contains(text(),"Manpower fit for military service")])=1]/following::span[1]/text()').extract()
        miliTemp['Manpower available for military service']['females age 16-49']=hxs.xpath('//div[contains(a,"Manpower available for military service")]/following::span[text()="females age 16-49: " and count(following::a[contains(text(),"Manpower fit for military service")])=1]/following::span[1]/text()').extract()

        miliTemp['Manpower fit for military service']={'males age 16-49':scrapy.Field(),'females age 16-49':scrapy.Field()}
        miliTemp['Manpower fit for military service']['males age 16-49']=hxs.xpath('//div[contains(a,"Manpower fit for military service")]/following::span[text()="males age 16-49: " and count(following::a[contains(text(),"Manpower reaching militarily significant age annually")])=1]/following::span[1]/text()').extract()
        miliTemp['Manpower fit for military service']['females age 16-49']=hxs.xpath('//div[contains(a,"Manpower fit for military service")]/following::span[text()="females age 16-49: " and count(following::a[contains(text(),"Manpower reaching militarily significant age annually")])=1]/following::span[1]/text()').extract()


        miliTemp['Manpower reaching militarily significant age annually']={'males':scrapy.Field(),'females':scrapy.Field()}
        miliTemp['Manpower reaching militarily significant age annually']['males']=hxs.xpath('//div[contains(a,"Manpower reaching militarily significant age annually")]/following::span[text()="male: " and count(following::a[contains(text(),"Military expenditures:")])=1]/following::span[1]/text()').extract()
        miliTemp['Manpower reaching militarily significant age annually']['females']=hxs.xpath('//div[contains(a,"Manpower reaching militarily significant age annually")]/following::span[text()="female: " and count(following::a[contains(text(),"Military expenditures:")])=1]/following::span[1]/text()').extract()

        # military part done

        #Transnational Issues
        item['transnational_issue']={}
        transissuTemp=item['transnational_issue']
        transissuTemp['Disputes - international']=hxs.xpath('//div[contains(a,"Disputes - international")]/following::div[1]/text()').extract()
        transissuTemp['Illicit drugs']=hxs.xpath('//div[contains(a,"Illicit drugs")]/following::div[1]/text()').extract()

        transissuTemp['Refugees and internally displaced persons']={'stateless':scrapy.Field(),'refugees':scrapy.Field(),'IDPs':scrapy.Field()}
        transissuTemp['Refugees and internally displaced persons']['stateless']=hxs.xpath('//div[contains(a,"Refugees and internally displaced persons")]/following::span[contains(text(),"stateless") and count(following::footer)=1]/following::span[1]/text()').extract()
        transissuTemp['Refugees and internally displaced persons']['refugees']=hxs.xpath('//div[contains(a,"Refugees and internally displaced persons")]/following::span[contains(text(),"refugee") and count(following::footer)=1]/following::span[1]/text()').extract()
        transissuTemp['Refugees and internally displaced persons']['IDPs']=hxs.xpath('//div[contains(a,"Refugees and internally displaced persons")]/following::span[contains(text(),"IDP") and count(following::footer)=1]/following::span[1]/text()').extract()


        transissuTemp['Trafficking in persons']={'current situation':scrapy.Field(),'tier rating':scrapy.Field()}
        transissuTemp['Trafficking in persons']['current situation']=hxs.xpath('//div[contains(a,"Trafficking in persons")]/following::span[contains(text(),"current situation") and count(following::footer)=1]/following::span[1]/text()').extract()
        transissuTemp['Trafficking in persons']['tier rating']=hxs.xpath('//div[contains(a,"Trafficking in persons")]/following::span[contains(text(),"tier rating") and count(following::footer)=1]/following::span[1]/text()').extract()

        yield item


            
            



