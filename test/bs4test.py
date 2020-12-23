from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")  # 设置解析器黑html.parser

# 1. Tag 标签及其内容, 默认拿到它找到的第一个结果
print(bs.a)
print(bs.a.attrs)  # 拿到标签的所有属性
# 2. 是个NavigableString
print(bs.title.string)  # 只要其中的内容
print(type(bs.title.string))
# 2. BeautifulSoup
print(bs)
# 3. Comment 是一个特殊的NavigableString, 不包含注释符号

# 4. 遍历文档树
print(bs.head.contents[1])
print(bs.head.contents[1])

# 5. 文档搜索
# (1) find_all() 查找所有
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
# 正则表达式搜索, 使用search()方法来匹配内容
import re

tt_list = bs.find_all(re.compile("a"))  # 查找包含 a 的内容
print(t_list)


# 方法搜索: 传入一个函数(方法), 根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_atrr("name")
#
#
# f_list = bs.find_all(name_is_exists)
# print(f_list)

# 正则表达式
print(re.findall("[A-Z]", "ASDaDFGAa"))
print(re.findall("[A-Z]+", "ASDaDFGAa"))  # 直到不符合的输出

# sub
# 找到a, 并用A来替换
print(re.sub("a", "A", "abcdcasd"))
# 建议在正则表达式中, 被比较的字符前面加上r, 不用担心转义字符的问题
a = r"\aabd-\'"
print(a)