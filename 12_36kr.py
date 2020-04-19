import requests
from parse_url import parse_url
import re
import json
import pprint

url = 'https://36kr.com/'
html_str = parse_url(url)
ret = re.findall('<script>var props=(.*?)</script>',html_str)[0]
ret = json.loads(ret)
pprint(ret)