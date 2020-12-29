import urllib.request, urllib.error  # 指定URL, 获取网页数据

"""
示例代码:
    用于获取页面内容
"""


url = "https://movie.douban.com/top250?start=0&filter="

head = {  # 用字典构造请求头参数, 用于伪造成浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
"""
urllib.request.Request() 意思是 调用urllib库中的reqeust包的Request方法来构造一个请求器
"""
req = urllib.request.Request(url, headers=head, method="GET")  # 构造请求器, 请求方法为GET, 请求头参数为 head字典 定义的参数
html = ""
try:
    res = urllib.request.urlopen(req)  # 发送请求, 获取页面
    html = res.read().decode("utf-8")  # 获取页面结果并进行转码
    with open("./temp/页面内容.txt", "w", encoding="utf-8") as f:  # 将页面写到 temp/页面内容.txt 文件当中
        f.write(html)
except urllib.error.URLError as e:  # 请求失败, 进行异常处理
    if hasattr(e, "code"):  # 如果有错误码
        print(e.code)  # 打印错误码, 错误码诸如 404(找不到页面) 500(服务器错误)
    if hasattr(e, "reason"):
        print(e.reason)  # 打印发生错误的原因



