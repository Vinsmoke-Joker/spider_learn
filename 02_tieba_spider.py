import requests

class TiebaSpider(object):
    def __init__(self,tiema_name):
        self.tieba_name = tiema_name
        # https: // tieba.baidu.com / f?kw = % E6 % B5 % B7 % E8 % B4 % BC % E7 % 8E % 8B & ie = utf - 8 & pn = 50
        self.url_temp = 'https://tieba.baidu.com/f?kw ='+tiema_name+'&ie=utf-8&pn={}'
        # 构造headers
        self.heards = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    def get_url_list(self):
        # 1.构造run列表
        url_list = list()
        for i in range(1000):
            url_list.append(self.url_temp.format(i*50)) # 每次获取页码数为50
        # 或者 return [self.temp.format(i*50) for i in range(1000)]
        return url_list

    def parse_url(self,url): # 发送请求，获取响应
        print(url)
        response = requests.get(url,headers = self.heards)
        return response.content.decode()

    def save_html(self,html_str,page_num):  # 保存html字符串
        file_path = './data/tieba/{}-第{}页.html'.format(self.tieba_name,page_num)
        with open(file_path,'w',encoding='utf-8') as f:  # xx 第一页.html
            f.write(html_str)
    def run(self): # 实现主要逻辑
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历发送请求，获取相应
        for url in url_list:
            html_str = self.parse_url(url)
        # 3.保存
        page_num = url_list.index(url)+1 # index从0开始 因此+1
        self.save_html(html_str,page_num)
if __name__ =='__main__':
    tieba_spider = TiebaSpider('海贼王')
    tieba_spider.run()