# import 模块名
# import 模块名 as 别名  可以使用 别名.函数名/变量名/类名
# from 模块名 import 函数名/变量名/类名
# from 模块名 import 函数名/变量名/类名 as 别名
# from 模块名 import * 直接使用功能名即可

def sum(a,b):
    return a+b

# 测试函数
# __name__ 内置变量 python 中的内置变量，表示当前模块的名字
# (直接运行当前模块，__name__为"__main__")
# 当模块被导入是，__name__为模块名字
print(__name__)

if __name__ == "main":
    # from 模块名 import 函数名/变量名/类名
    sum(1,2)

## __all__ 在模块定义时
# 定义此变量控制其他python文件用 import *可导入的内容
__all__ = ['sum']
