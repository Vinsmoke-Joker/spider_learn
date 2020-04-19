import requests
import json

class BaiduTranslate(object):
    def __init__(self,trans_str):
        self.lang_detect_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_str = trans_str
        self.headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        self.trans_url = 'https://fanyi.baidu.com/basetrans'

    def parse_url(self,url,data): # 1.2发送post请求，获取响应
        response = requests.post(url,data=data,headers = self.headers)
        return json.loads(response.content.decode())

    def get_ret(self,dict_response): # 4.提取翻译结果
        # ret = dict_response['trans'][0]['dst']
        ret = dict_response  # error 997
        print('result is ret:',ret)

    def run(self): # 实现主要逻辑
        # 1.获取语言类型
            # 1.1准备post url和data
        lang_detect_data = {'query':self.trans_str}
            # 1.2发送post请求，获取响应
            # 1.3提取语言类型
        lang = self.parse_url(self.lang_detect_url,lang_detect_data)['lan']

        # 2.准备post数据
        trans_data = {
            'query':self.trans_str,
            'from':'zh',
            'to':'en',
            'token':'f2b7a65c8ee1d5616a50492eb2439099',
            'sign':'232427.485594'
        } if lang =='zh' else {'query':self.trans_str,'from':'en','to':'zh'}
        # 3.发送post请求，获取响应
        dict_response = self.parse_url(self.trans_url,trans_data)
        # 4.提取翻译结果
        self.get_ret(dict_response)

if __name__=='__main__':
    trans_str = input('输入要翻译的内容:')
    baidu_trans = BaiduTranslate(trans_str)
    baidu_trans.run()