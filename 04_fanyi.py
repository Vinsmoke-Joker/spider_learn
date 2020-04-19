# coding=utf-8
import requests
import json
import sys


# query_string = sys.argv[1]  # sys.argv[0]为py文件名,后面的值为跟着py文件输入的内容
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

post_data = {
    'query':'人生苦短，我用python',
    'from':'zh',
    'to':'en',
    'token':'f2b7a65c8ee1d5616a50492eb2439099',
    'sign':'289133.35420'
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())
# dict_ret = json.loads(r.content.decode())
# print(dict_ret)
# ret = dict_ret["trans"][0]["dst"]
# print("result is :",ret)