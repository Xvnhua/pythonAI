# 1. 定义
str1 = ''
str2 = ""
str3 = '''
    使用
    三引号
    定义多行文本
'''

# 2. 转义str
a1 = '\''
a2 = "\""
a3 = '''\n'''
a4 = '\t'

# 3. str 拼接

# a. 直接连续写

st1 = "第一个字符串" "第二个字符串"
print(st1)

# 不能直接连续写 字符串和变量
# st2 = "str:" st1
# print(st2)

# b. 加号拼接

st2 = "st2:"+ st1
print(st2)
# st2 = "st2:"+ st1 + 1 ❌ 无法自动转换类型至字符串
st2 = "st2:"+ st1 + str(1)
print(st2)

# c. 占位符拼接(字符串格式化)

print("大家好我是%s,今年%s岁,在学%s" %("夏夏","18","PythonAI") )

# d. f"asldjflsadf{name}sadfsdafsdf"格式化

name = "夏夏"
id = "孩子"
dd = f"aaaaaaaa{name+"的"}{id}"
print(dd)