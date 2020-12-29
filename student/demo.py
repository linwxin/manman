import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("./学生成绩.csv", encoding="gbk")
# 简单预处理
df.fillna(0, inplace=True)

X_cols = []
for e in df.columns.tolist():
    if "_num" in e:
        X_cols.append(e)

print(X_cols)

Y_cols = ["stu_total_score"]
X = df.loc[:, X_cols]
Y = df.loc[:, Y_cols]

# 标准化
Y_scale = Y.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
X_scale = X.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
X_scale.fillna(0, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X_scale, Y_scale, test_size=0.20, random_state=0)  # 划分数据

# 进行回归
model = sm.OLS(y_train.astype(float), sm.add_constant(X_train.astype(float))).fit()
print(model.params)
print(model.pvalues)


# print(df)
# df.to_csv("./处理后.csv", encoding="gbk", index=None)
