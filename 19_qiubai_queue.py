import requests
from lxml import etree
import json
import threading
from queue import Queue



class QiubaiSpider(object):
    def __init__(self):
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
        self.url_temp = 'https://www.qiushibaike.com/text/page/{}/'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1,14)]  # 共13页内容
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url,headers =self.headers)
            # return response.content.decode()
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def  get_content_list(self):  # 提取数据
        html_str = self.html_queue.get()
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
        self.content_queue.put(content_list)
        self.html_queue.task_done()
        return content_list

    def save_content_list(self):  # 保存数据
        while True:
            content_list = self.content_queue.get()
            with open('./data/qiubai/qiubai_queue.txt', 'a',encoding='utf-8')as f:
                for content in content_list:
                    f.write(json.dumps(content,ensure_ascii=False,indent=2))
                    f.write("/n")
                self.content_queue.task_done()
            print('保存成功')

    def run(self):  # 实现主要逻辑
        thread_list = list()
        # 1.url_list
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历,发送请求获取相应
        for i in range(3):
            t_parse = threading.Thread(target= self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        t_data = threading.Thread(target= self.get_content_list)
        thread_list.append(t_data)
        # 4.保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)  # 把子线程设置为守护线程，守护线程：该线程不重要，随主线程结束而结束
            t.start()
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 让主线程等待阻塞，等待队列的任务完成之后再完成
        print('主线程结束')

if __name__ =='__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
