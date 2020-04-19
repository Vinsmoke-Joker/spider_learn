import requests


session = requests.session()
post_url="http://www.renren.com/PLogin.do"
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 使用session发送post请求，cookie保存在其中
session.post(post_url,data=data,headers=headers)
# 使用session进行请求登录后才能访问的地址
r = session.get("http://www.renren.com/410043129/profile",headers=headers)
print(r.status_code)
with open('./data/renren/renren1.html','w') as f:
    f.write(r.content.decode())
