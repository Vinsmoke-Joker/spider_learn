import requests
from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''
html = etree.HTML(text)
print(html)
# 查看element对象中包含的字符串 etree.tostring()
print(etree.tostring(html).decode())

# 获取class=item-1中a的herf
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

# 获取class=item-1中li的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)
# 每个li是一个新闻，把url和文本组成字典
for href in ret1:
    item = dict()
    item['href'] = href
    item['title'] = ret2[ret1.index(href)]
    print(item)

ret3 = html.xpath("//li[@class='item-1']")
print(ret3)
# 分组，对每个li标签进行分组后，再对每组分别写xpath
for i in ret3:
    item=dict()
    item['title'] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()"))>0 else None
    item['href'] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href"))>0 else None
    print(item)