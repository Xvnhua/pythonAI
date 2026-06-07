"""
列表类型是一种 序列类型
即 可以通过下标访问元素，按照特定顺序排列的序列
"""

# 定义
列表名称 = [1,2,3,4,5,6,7,8,9,10]
for i in 列表名称:
    print(i)
# 可以存储不同类型的元素
# 元素有序，可以重复，可以修改
# 使用 下标来进行索引（可以使用反向索引）
print(列表名称[-1])# 最后一个元素
for i in range(-1,-1-len(列表名称),-1):
    print(列表名称[i])

乱类型 = [1.2,True,306,None,'String']
print(乱类型)

 # 删除
del 乱类型[2]
for i in 乱类型:
    print(i)
print(乱类型)

# 切片
# 序列[begin:end:step]
s = 乱类型[-4::2]
print(s)

# end处是开区间
a = ['a','c','b','d','e','f','g']
print(a[0:4:2])

# 常见方法

# .append()追加
a.append('追加元素1')
print(a[-1])

# .insert() 指定索引插入
a.insert(3,'1插入元素')
print(a[3])
print(a)

# .remove() 移除列表中第一个匹配的值
a.remove('追加元素1')
print(a)

# .pop 删除一个指定索引的元素，未指定则删除最后一个，返回弹出的元素
a.append('追加元素2')
print(a.pop())

# .sort() 同类型元素排序（通过 operator进行）
a.sort()
print(a)

# print(乱类型)
# 乱类型.sort()
# print(乱类型)

# .reverse() 反转列表元素
a.reverse()
print(a)