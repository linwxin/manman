from bs4 import BeautifulSoup  # 网页解析, 获取数据
import re  # 正则表达式, 进行文字匹配
import urllib.request, urllib.error  #  指定URL, 获取网页数据
import xlwt

# 0. 介绍库
"""
bs4：解析请求的
re: 正则
urlib: 发送请求
xlwt: excel操作工具
"""
# 1. 发送给请求
baseurl = "https://movie.douban.com/top250?start="
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
datalist = []
for i in range(10):
    url = baseurl + str(i*25)
    req = urllib.request.Request(url, headers=head, method="GET")
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")

    # 2. 获取html文件
    # 3. 解析请求，获取想要的数据
    findTitle = re.compile('<span class="title">(.*)</span>')
    findLink = re.compile('<a href="(.*)">')
    bs = BeautifulSoup(html, "html.parser")
    items = bs.find_all("div", class_="item")
    for item in items:
        data = []
        title = re.findall(findTitle, str(item))
        data.append(title)
        link = re.findall(findLink, str(item))
        data.append(link)
        datalist.append(data)

# 存储
col = ["影片名", "详情链接"]
workbook = xlwt.Workbook(encoding="utf-8")
sheet = workbook.add_sheet("豆瓣Top250")
for i in range(len(col)):
    sheet.write(0, i, col[i])
for i in range(len(datalist)):
    for j in range(len(col)):
        sheet.write(i+1, j, datalist[i][j])

workbook.save("豆瓣top250.xls")



# 4. 保存数据