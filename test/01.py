# 定义一个空的类
class Student():
    # 一个空类，pass代表跳过，此处pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 定义一个类，用来描述学习Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    # 需要注意：系统默认有一个self参赛
    def doHomework(self):
        print("I 在做作业")
        return None

# 实例化一个叫yueyue的同学
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()