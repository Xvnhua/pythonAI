"""
列表类型是一种 序列类型
即 可以通过下标访问元素，按照特定顺序排列的序列
"""
from numpy.ma.extras import average

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

### 案例 1 sum函数、min,max,average
print("接下来输入10个数字")
int_list1 = []
aver = 0
for i in range(10):
    a = int(input(f'number {i}:'))
    int_list1.append(a)
    aver += a
int_list1.sort()
print(int_list1)
aver /=10
# 直接用sum函数 sum函数接收任何可迭代对象，第二个参数是累加的初始值
avr2 = sum(int_list1) /10

print("avr2:",avr2)
print(f'最小值：{int_list1[0]},最大值：{int_list1[-1]}')
print(f'平均值avr1:{aver}')

# len() 求list 元素个数
# 也可以用min,max获取最大最小值

### 案例2 in 表达式，解包/组包操作
# 合并两个列表中的元素，并进行去重处理
numblist1 = [19,23,54,64,875,20,109,232,123,54]
numblist2 = [55,80,72,35,60,123,54,29,91]

numblist3 = []
for numb in numblist1:
    if numb not in numblist3:
        numblist3.append(numb)
for numb in numblist2:
    if numb not in numblist3:
        numblist3.append(numb)
numblist3.sort()
print(numblist3)

## 解包+组包操作 用*进行解包操作（解开成单独的元素））
numblist4 = [*numblist1,*numblist2]
print(numblist4)

## 加法operator
numblist5 = numblist1 + numblist2

### 案例3 列表推导式
# 提取所有偶数，并计算其平方，组成一个新的列表
# [f(i) for i in 序列/列表]
sq = [i for i in range(1,21)]
sqr = [i**2 for i in sq if i%2==0]
sql = [i*j for i in range(1,21) for j in range(1,21)]
print(sqr)
print(sql)