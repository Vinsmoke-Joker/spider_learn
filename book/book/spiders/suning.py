# -*- coding: utf-8 -*-
import scrapy
import re


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://list.suning.com/1-502325-0.html']
    def __init__(self):
        self.i = 0

    def parse(self, response):
        # print(self.i)
        # 获取大分类分组
        li_list = response.xpath("//div[@id='filter-results']/ul/li")
        # print(li_list)
        with open('./book.txt','a',encoding='utf-8') as f:
            f.write('正在写入第%d页内容' % (self.i+1))
            f.write('\n')
            self.i +=1
            for li in li_list:
                item = dict()
                item['introduce'] = li.xpath(".//img[@class='search-loading']/@alt").extract_first()
                item['price'] = li.xpath(".//div[@class='res-info']/p[1]/text()").extract()
                item["img"] = li.xpath(".//div[@class ='img-block']/a/img/@src2").extract_first()
                item['img'] = 'https:'+item['img']
                item["store_name"] = li.xpath(".//div[@class='res-info']/p[4]/a/text()").extract_first()
                item["book_href"] = li.xpath(".//div[@class='res-info']/p[2]/a/@href").extract_first()
                item['book_href'] = 'https:'+item['book_href']

                f.write(str(item))
                f.write('\n')
                print('第%d页爬取完'% (self.i+1))
                # 翻页-共100页
                while self.i < 4:
                    print('正在爬取第%d页' % (self.i+1))
                    next_url = 'https://list.suning.com/1-502325-' + str(self.i) + '-0-0-0-0-14-0-4.html'
                    # print(next_url)
                    yield scrapy.Request(
                        next_url,
                        callback=self.parse,
                    )
            # yield item

