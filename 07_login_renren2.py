import requests



post_url="http://www.renren.com/PLogin.do"
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
           'Cookie':'anonymid=k8v5uhsj4nfqoc; depovince=ZGQT; jebecookies=0e780292-6d5e-41e9-80ed-19c286f6ab65|||||; _r01_=1; JSESSIONID=abcqnmtCnAKsBff_sPNfx'}


r = requests.get("http://www.renren.com/410043129/profile",headers=headers)
print(r.status_code)
with open('./data/renren/renren2.html','w') as f:
    f.write(r.content.decode())
