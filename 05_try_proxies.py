import requests


proxies = {
    'http':'http://101.132.39.115:8080'
}
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
r = requests.get('http://www.baidu.com',proxies=proxies,headers=headers)
print(r.status_code)