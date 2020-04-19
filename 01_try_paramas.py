import requests
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
paramas = {'wd':'爬虫'}
# 或者手动拼接url
# url_temp = 'https://www.baidu.com/s?wb={}'.format('爬虫')
url_temp = 'https://www.baidu.com/s?'
r = requests.get(url_temp,headers=headers,params=paramas)
print(r.status_code)
print(r.request.url)

