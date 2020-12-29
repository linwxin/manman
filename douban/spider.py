from bs4 import BeautifulSoup  # 网页解析, 获取数据
import re  # 正则表达式, 进行文字匹配
import urllib.request, urllib.error  #  指定URL, 获取网页数据
import xlwt

"""
正则基础知识:
    普通字符：
        [0-9] : 代表数字0-9
        [a-z] : 代表字母a-z
        . : 代表所有字符
        \d : 所有数字
    限定符:
        * : 限定符,
        + : 限定词
        ? : 限定符, 代表匹配0次或1次

    示例1：假如字符串为 "jcbka41237t83221jbkbn"
        r"[0-9]" : 返回 ['4', '1', '2', '3', '7', '8', '3', '2', '2', '1']
        r"[0-9]*" : 返回 ['41237', '83221']
        r"[0-9]*?" : 返回 ['41237']
        r"[a-z]*" : 返回 ['jcbka', 't', 'jbkbn']
        r"[a-z]*?" : 返回 ['jcbka', 't', 'jbkbn']
        
    示例2: "<a href="http://www.baidu.com"> <a href="http://www.bilibili.com">"
        r'<a href=".*?">' : ['<a href="http://www.baidu.com">']
        r'<a href=".*">' : ['<a href="http://www.baidu.com"> <a href="http://www.bilibili.com">']
        r'<a href="(.*)">' : ['http://www.baidu.com"> <a href="http://www.bilibili.com']
        r'<a href="(.*?)">' : ['http://www.baidu.com', http://www.bilibili.com']
"""
findLink = re.compile(r'<a href=".*?">')  # 匹配以 <a href=" 开头, "> 结尾, 中间为任意字符, 只匹配一次
"""
re.S 让换行符\n 制表符\t 等特殊符号直接识别成字符串
r'<img.*src="(.*?)"' -> 匹配 <img多个字符src="任意多个字符", 只匹配一次,提取出括号位置的字符 
"""
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
"""
提取出<span class="rating_num" property="v:average">和</span>之间的所有字符
示例：<span class="rating_num" property="v:average">9.7</span> -> 9.7
"""
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
"""
提取出<span>和人评价</span>之间的所有数字
示例：<span>2219387人评价</span> -> 2219387
"""
findJudgeNum = re.compile(r'<span>(\d*)人评价</span>')
findAbstract = re.compile(r'<span class="inq">(.*)</span>')  # 提取简介
findInfo = re.compile(r'<p class="">(.*?)</p>', re.S)  # 提取影片信息  导演之类的



"""
功能：用于获取页面内容
"""
def askURL(url):
    head = {  # 用字典构造请求头参数
        #  用于伪造成浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    """
    urllib.request.Request() 意思是 调用urllib库中的reqeust包的Request方法来构造一个请求器
    """
    req = urllib.request.Request(url, headers=head, method="GET")  # 构造请求器, 请求方法为GET, 请求头参数为 head字典 定义的参数
    html = ""

    res = urllib.request.urlopen(req)  # 发送请求, 获取页面
    html = res.read().decode("utf-8")  # 获取页面结果并进行转码

    return html

"""
获取所需信息
"""
def getData(baseUrl):
    datalist = []  # 定义变量, 作为存爬取数据的容器
    for i in range(0, 10):  # i 为页码取值范围为0到9, 第0页即第1页，从第1页开始循环, 直到第10页
        """
        i=0时, https://movie.douban.com/top250?start=0, 即第1-25条电影信息
        i=1时, https://movie.douban.com/top250?start=25, 即第26-50条电影信息
        ...
        i=9时, https://movie.douban.com/top250?start=225, 即第226-250条电影信息
        """
        url = baseUrl + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")  # 对网页内容以 html.parser规则 进行格式化读取
        """
        soup.find_all("div", class_="item")
            功能：找出所有存在 "item" 属性的 div 结构, 例如:
                <div class="item">
                    <div class="pic">
                        <em class="">1</em>
                        <a href="https://movie.douban.com/subject/1292052/">
                            <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" class="">
                        </a>
                    </div>
                    ....
                </div>
                以上就是一个完整的<div>结构
        for item in soup.find_all("div", class_="item"):
            功能：对所有找出的 <div> 结构的东西进行处理
        
        """
        for item in soup.find_all("div", class_="item"):
            data = []  # 保存一部电影的所有信息, 信息格式为["中文名", "外文名", "详情页地址", "图片地址", "评分", "评价人数", "简介"]
            item = str(item)  # 将<div></div>变成字符串
            # 提取片名
            """
            re.findall(findTitle, item)
                功能： 利用re库中的findall()方法, 按照 findTitle 的正则规则, 从item提取出片名
            """
            titles = re.findall(findTitle, item)  # 片名有可能时中文或者是外文名, 有可能有多个
            if len(titles) >= 2:  # 提取出来的片名如果有两个, 意味着第1个是中文名, 第2个是外文名
                ctitle = titles[0]  # 将中文名赋值给ctitle
                data.append(ctitle)  # 将中文名存到 data 中
                """
                titles[1].replace("/", "").strip()
                    功能：将 titles[1] 中的 "/" 删除, 并用strip()方法将前后空格删除
                .strip()
                    功能：去掉字符串前后空格, 例如：" abc d " -> "abc d"
                """
                otitle = titles[1].replace("/", "").strip()  # 将外文片名存入otitle
                data.append(otitle)  # 将外文片名存入data
            else:  # 只有中文名
                data.append(titles[0])  # 直接加入
                data.append(" ")  # 外文名为空, 用空格占位
            link = re.findall(findLink, item)[0]  # 获取详情页地址
            data.append(link)  # 加入详情页地址
            imgSrc = re.findall(findImgSrc, item)[0]  # 获取图片地址
            data.append(imgSrc)  # 将图片地址加入data

            score = re.findall(findScore, item)[0]  # 获取评分
            data.append(score)  # 将评分加入data
            judgeNum = re.findall(findJudgeNum, item)[0]  # 获取评价人数
            data.append(judgeNum)  # 评价人数
            abstract = re.findall(findAbstract, item)
            if len(abstract) != 0:
                abstract = abstract[0].replace("。", "")  # 删除中文句号
            else:
                abstract = " "
            data.append(abstract)
            info = re.findall(findInfo, item)[0]  # 获取简介
            data.append(info.strip())

            datalist.append(data)  # 将一条完整的电影信息存入datalist

    return datalist

# 保存数据
def saveData(path, datalist):
    book = xlwt.Workbook(encoding="utf-8")  # 新建一个工作簿
    """
    book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    功能：
        创建一个sheet, sheet名称为 "豆瓣电影Top250", 写入时覆盖原来内容(cell_overwrite_ok=True)
    """
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("影片中文名", "影片外文名", "电影详情链接", "图片链接",  "评分", "评分数", "概况", "相关信息")  # 设置列名
    for i in range(0, len(col)):  # 写入第一行内容, 即将列名一个一个写入到sheet内
        sheet.write(0, i, col[i])
    #  将 datalist(所有电影信息) 内容按行写入
    for i in range(0, len(datalist)):
        print("第 %d 条"%(i+1))
        data = datalist[i]  # 获取第i部电影内容
        for j in range(len(col)):  # 将第i部的内容写入到第i+1行
            sheet.write(i+1, j, data[j])  # 在第i+1行写入第j列的信息
    book.save(path)  # 保存工作簿

"""
将各个功能集合到main()函数中
"""
def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 获取爬取信息
    datalist = getData(baseurl)
    # 保存数据
    save_path = "./豆瓣电影top250.xls"  # 保存地址
    saveData(save_path, datalist)

if __name__ == "__main__":
    main()