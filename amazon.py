import requests
url = "https://www.amazon.cn/gp/product/B07TVRD4PZ/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-4&pf_rd_r=XDZRFEHVVC77YHZG0014&pf_rd_t=101&pf_rd_p=dbd64bfb-5bb2-4e9e-9846-8a9ee9bab123&pf_rd_i=144154071"
try:
    #kv = {'user-agent':'Mozilla/5.0'}
    #r = requests.get(url, headers=kv)
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
