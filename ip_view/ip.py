import requests
ip = input("请输入ip地址：")
url = "http://m.ip138.com/ip.asp?ip=" + ip
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
