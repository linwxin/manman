import pandas as pd

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 读取文件 DataFrame
df = pd.read_csv("./学生成绩.csv", encoding="gbk")


# 简单处理
df = df.fillna(0)  # df = df.fillna(0)


# 条件查询
df_lib = df[(df["stu_type"] == 1) | (df["stu_total_score"] > 400)]

df_sci = df[df["stu_type"] == 2]

# 按行查询
stu_name = df.loc[:, ["user_name", "stu_total_score"]]

# 简单计算
stu_total_score = df.loc[:, ["stu_total_score"]]
print(stu_total_score.median())  # 中位数
print(stu_total_score.max())  # 最大值
print(stu_total_score.min())  # 最小值
print(stu_total_score.mean())  # 均值

# 去重
df_sigle = df.drop_duplicates(subset=["stu_type"], keep="first")
# print(df_sigle)

# 排序
df_sort = df.sort_values(by="stu_total_score", ascending=True)  # 降序
print(df_sort)
