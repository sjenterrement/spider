import urllib.request
import time
import re
from lxml import etree
def load_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
    res = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(res).read()
    content = etree.HTML(html)
    prices = []
    price_list = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i')
    content_list = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
    #print(content_list)
    for i in range(1,31):
        try:
            prices.append(price_list[i-1].text)
            link_page = re.split(r":",content_list[i-1])[1]
            content_list[i-1]=link_page
        except Exception as e:
            continue
    #print(content_list)
    #print(prices)
    k = 0
    for j in content_list:
        new_url = "https:"+j
        load_link_page(new_url, headers, prices[k])
        k = k + 1

def load_link_page(url, headers, price):
    res = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(res).read()
    content = etree.HTML(html)
    targets = content.xpath('//div[@class="p-parameter"]/ul[@class="parameter2 p-parameter-list"]/li')
    phones = []
    for phone in targets:
        phones.append(phone.text)
    result = []
    name = phones[0]
    other = phones[1:]
    result.append(name)
    result.append("价格: " + price)
    result.append(other)
    print(result)

def samsung_spider(url, depth):
    for i in range(depth):
        print("正在抓取第{}页".format(i+1))
        pageUrl = url + str(i*2+1)
        time.sleep(2)
        load_page(pageUrl)

def main():
    url = 'https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8' \
          '&wq=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&page='
    result = []
    depth = 2
    samsung_spider(url, depth)


main()
