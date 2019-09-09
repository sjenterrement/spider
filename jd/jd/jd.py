# -*- coding: UTF-8 -*-
import requests
import re

samsung_list = []
result = []

# 获取所有三星商品url
for i in range(5):
    samsung_url = "https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F15127&page="+str(i+1)+"&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main"
    r = requests.get(samsung_url)
    r.encoding = r.apparent_encoding
    zhengze1 = "<a target=\"_blank\" href=\"\/\/(.+?)\" >"
    suan = re.findall(zhengze1, r.text)
    for i in range(len(suan)):
        samsung_list.append(suan[i])

# 获取每个商品url中的商品信息
for i in range(len(samsung_list)):
    url1 = "http://" + samsung_list[i]
    r1 = requests.get(url1)
    r1.encoding = r1.apparent_encoding
    name_zhengze = "<li title='(.+?)'>"
    name = re.findall(name_zhengze, r1.text,re.M | re.DOTALL)
    for i in range(len(name)):
        result.append(name[i])
print("获取完毕")

# 将结果保存为文件
file = open("result.txt","w")
for i in result:
    file.write(i)
    file.write("\n")
print("写入成功")
