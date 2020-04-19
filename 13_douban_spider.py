import requests
import json

class DoubanSpider(object):
    def __init__(self):
        self.url_temp = [{
                'url_temp':'https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18&loc_id=108288',
                'country':'US'
            },
            {
                'url_temp': 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_korean/items?start={}&count=18&loc_id=108288&_=1586607250051',
                'country': 'Korea'
            }]
        self.hearders = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer':'https://m.douban.com/tv/american'  # 请求头中的内容
        }

    def parse_url(self,url):  # 2.发送请求，获取响应
        print(url)
        response = requests.get(url,headers = self.hearders)
        return response.content.decode()

    def get_content_list(self,json_str):  # 3.提取数据
        dict_ret = json.loads(json_str)
        print(dict_ret)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list,total

    def save_content_list(self,content_list,country):   # 4.保存
        with open('./data/douban/douban.txt','a',encoding='utf-8') as f:
            for content in content_list:
                content['country'] = country
                f.write(json.dumps(content,ensure_ascii=False))
                f.write('\n')  # 写入换行符进行换行
        print('保存成功')

    def run(self):  # 实现主要逻辑
        for url_temp in self.url_temp:
            num = 0
            total = 100  # 假设total为100  下方提取后，total会被覆盖
            while num<total+18:
                # 1.start_url
                url = url_temp['url_temp'].format(num)
                # 2.发送请求，获取响应
                json_str = self.parse_url(url)
                # 3.提取数据
                content_list,total = self.get_content_list(json_str)
                # 4.保存
                self.save_content_list(content_list,url_temp['country'])
                # 5.构造下一页url,进入循环
                num+=18

if __name__=='__main__':
    douban = DoubanSpider()
    douban.run()