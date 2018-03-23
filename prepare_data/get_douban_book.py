from bs4 import BeautifulSoup
import requests
import pymysql


# 初始url
url_start = 'https://www.douban.com/'

# 获取这个页面的链接并保存下来
cata = []

html = requests.get(url_start)
bsobj = BeautifulSoup(html.text)
# 先找到父标签
url_lists = bsobj.find_all("a", {"target": "_blank"})
for url_list in url_lists:
    print(url_list)

