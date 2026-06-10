# 自动去重的无序可修改
# 定义集合
s1 = {"c","d",'E'}
S2 = set()
m3 = {}# {} 定义表示空字典
print(f"S2 tpye{type(S2)}")
print(f"m3 tpye{type(m3)}")

# 方法
# .add()
s1.clear()
s1.add("a")
# .remove() 移除指定元素，如果没有就报错
s1.remove('a')
# .pop() 随机删除元素并返回
s1.add('a')
s1.add('c')
s1.add('b')
pp=s1.pop() # 真随机删，每次执行结果不大一样
print(pp)

# .clear() 清空集合
# .difference() ****** 求两个集合的差集，（调用者-）
sa = {'a','e','g'}
print(sa.difference(s1))

# .union 求并集
su = sa.union(s1)
print(f'type={type(su)}')
print(su)
# .intersection() 求交集
si = sa.intersection(s1)
print(si)
# 集合推导式
see = {i for i in si}
print(see)

# 案例1 set运算 可以直接用 & | - 直接进行运算
sessionset = [
    {'张三','李四','找钱','孙李'},
    {'张三', '王五', '大超', '找钱'},
    {'张三', '123', '找钱', '大超'},
    {'张三', '21', '45', '123'},
]
all_set = sessionset[0] & sessionset[1] &sessionset[2] &sessionset[3]
print(all_set)
print(sessionset[0] | sessionset[1])
# 求各个人选课数
alst = set()
for i in sessionset:
    alst |= i

seslist = []
for i in sessionset:
    seslist += [*i]
print(seslist)
for i in alst:
    print(f"{i}一共选了{seslist.count(i)}门课")