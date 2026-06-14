# 定义
class Oha:
    # 静态属性
    total = 0
    it  = 'Oha'
    # 构造函数
    def __init__(self,name='default',age=-1,segment=0):
        # 实例属性
        self.name = name
        self.age = age
        self.segment = segment
    # 实例方法
    def running(self):
        print('it\'s running')
    # 魔法方法，指__init__这种的特殊时刻特殊方法，由python解释器自动调用
    # __init 初始化方法
    # __str 字符串表示方法
    # __eq 比较两个方法是否相等
    # __lt/le/gt/ge  比较大小，但是默认自定义对象无法进行比较
    # == 默认基于对象的内存地址进行比较
    def __str__(self):
        return f"{self.name}::{self.age}::{self.segment}"


# 实例可以随意添加属性
ob1 = Oha('张三',18,0)
ob1.arr = [1,2,2]
print(ob1.arr)
ob1.Arrtext ="一个动态添加的属性"

print("print(ob1)",ob1)
# <__main__.Oha object at 0x0000014ACED2EAE0>
print(ob1.__dict__) # 将对象中的所有属性以字典的形式输出
# {'arr': [1, 2, 2], 'Arrtext': '一个动态添加的属性'}
ob1.running()
