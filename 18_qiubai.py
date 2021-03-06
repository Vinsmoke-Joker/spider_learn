import requests
from lxml import etree
import json



class QiubaiSpider(object):
    def __init__(self):
        self.url_temp = 'https://www.qiushibaike.com/text/page/{}/'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]  # 共13页内容

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers =self.headers)
        return response.content.decode()

    def  get_content_list(self,html_str):  # 提取数据
        content_list = list()
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@class='col1 old-style-col1']/div")  # 分组获取
        for div in div_list:
            item = dict()
            item['content'] = div.xpath(".//div[@class='content']/span/text()")
            item['content'] = [i.replace("\n",' ') for i in item['content']]
            item['author_gender'] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item['author_gender'] = item['author_gender'][0].split(' ')[-1].replace('icon','') if len(item['author_gender'])>0 else None
            item['author_age'] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item['author_age'] = item['author_age'][0] if len(item['author_age'])>0 else None
            item['content_img'] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item['content_img'] = 'https:'+ item['content_img'][0] if len(item['content_img'])>0 else None
            item['author_img'] = div.xpath(".//div[@class ='author clearfix' ]//img/@src")
            item['author_img'] = 'https:'+ item['author_img'][0] if len(item['author_img'])>0 else None
            item['stats-vote'] = div.xpath(".//div[@class='stats']/span/i/text()")
            item['stats-vote'] = item['stats-vote'][0] if len(item['stats-vote'])>0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list):  # 保存数据
        with open('./data/qiubai/qiubai.txt', 'a',encoding='utf-8')as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("/n")
        print('保存成功')

    def run(self):  # 实现主要逻辑
        # 1.url_list
        url_list = self.get_url_list()
        # 2.遍历,发送请求获取相应
        for url in url_list:
            html_str = self.parse_url(url)
        # 3.提取数据
        content_list = self.get_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)

if __name__ =='__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
