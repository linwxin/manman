from bs4 import BeautifulSoup  # 网页解析, 获取数据
import re  # 正则表达式, 进行文字匹配
import urllib.request, urllib.error  #  指定URL, 获取网页数据
import xlwt

# 正则规则
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudgeNum = re.compile(r'<span>(\d*)人评价</span>')
findAbstract = re.compile(r'<span class="inq">(.*)</span>')  # 概况
findInfo = re.compile(r'<p class="">(.*?)</p>', re.S)  # ? 是1次或0次





# 爬取网页
def getData(baseUrl):
    # 2. 解析数据
    datalist = []
    for i in range(0, 10):
        url = baseUrl + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2. 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 获取属性为item的div
            data = []  # 保存一部电影的所有信息
            item = str(item)
            # 写出正则规则
            titles = re.findall(findTitle, item)  # 片名有可能时中文或者是外文名, 有可能有多个
            if len(titles) >= 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "").strip()
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")
            link = re.findall(findLink, item)[0]  # 通过正则表达式查找指定字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)


            score = re.findall(findScore, item)[0]  # 获取评分
            data.append(score)
            judgeNum = re.findall(findJudgeNum, item)[0]
            data.append(judgeNum)  # 评价人数
            abstract = re.findall(findAbstract, item)
            if len(abstract) != 0:
                abstract = abstract[0].replace("。", "")
            else:
                abstract = " "
            data.append(abstract)
            info = re.findall(findInfo, item)[0]
            data.append(info.strip())

            datalist.append(data)

    return datalist

# 获取页面内容
def askURL(url):
    head = {  # 模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=head, method="GET")
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

# 3. 保存数据
def saveData(path, datalist):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)  # 写入时覆盖以前聂荣
    col = ("影片中文名", "影片外文名", "电影详情链接", "图片链接",  "评分", "评分数", "概况", "相关信息")
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        print("第 %d 条"%(i+1))
        data = datalist[i]
        for j in range(len(col)):
            sheet.write(i+1, j, data[j])
    book.save(path)

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页
    datalist = getData(baseurl)
    # 保存数据
    save_path = "./豆瓣电影top250.xls"
    saveData(save_path, datalist)

if __name__ == "__main__":
    baseUrl = "http://paper.jyb.cn/zgjyb/html/2020-11/01/node_4.htm"
    print(askURL(baseUrl))