import json
import requests
url = 'http://www.renren.com/PLogin.do'
html_str = requests.get(url)

# json.loads把json转化为python类型
ret1 = json.loads(html_str)

# json.dumps  把python类型转化为json

with open() as f:
    # ensure_ascii=False,即解码,indent=2即首行缩进2字符
    f.write(json.dumps(ret1,ensure_ascii=False,indent=2))