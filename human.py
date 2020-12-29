
class Human:
    age = 1
    sex = "female"
    name = ""

    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name
        print("构造函数被创建")

    def walk(self):
        print(self.name + " 往前走了一步")

    def eat(self):
        print(self.name + " 吃了东西")

