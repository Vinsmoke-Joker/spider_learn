import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
data = {
    'from':'zh',
    'to':'en',
    'query':'人生苦短，我用python',
    'transtype':'translang',
    'simple_means_flag':'3',
    'sign':'289133.35420',
    'token':'f2b7a65c8ee1d5616a50492eb2439099',
    'domain':'common'
}
post_url = 'https://fanyi.baidu.com/sug'
r = requests.post(post_url,headers=headers,data=data)
print(r.content.decode())