# 变化的量

# 1. 一次性定义多变量
a,b = "a","b"
print(a,b)
你的 = "你的"
print(你的)

# 2. 利用多变量 进行交换
a,b = b,a
print(a,b)
a,b = b,a # 交换回

a,b,你的 = 你的,a,b  #三值交换
print (a,b,你的)

# 3. Type()
# 变量本身是没有类型的，type 输出的是变量中存储的数据的类型
tp = type(你的)
print(tp)
print(type('hello'))
print(type(1.0))
print(type(None))
print(type(False))
print(type(True))

# 4. isinstance() ,检查数据是否属于指定的类型，返回的是一个bool值
numb = 10;
print(isinstance(numb,int))
print(isinstance(numb,str))
