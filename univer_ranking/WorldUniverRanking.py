import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[4].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^20}"
    print(tplt.format("排名", "学校", "评分", chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/ARWU2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    num = input("输入学校个数：")
    printUnivList(uinfo, int(num))

main()
