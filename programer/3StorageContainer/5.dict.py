# 实际上就是hashmap
# 使用 key:value 存储数据

# 定义
# 可以存储完全不同的类型，但是key不能是可变类型比如 list\set\dict,可以是str,int,float,tuple
d1 = {'key1':'value1',2:2,True:'value3'}
d2 = {}
d3 = dict()

# 可以直接通过 key索引获取/修改value
print(d1['key1'])
d1['key1'] = 322
print(d1['key1'])

d1[2] = '1111'
print(d1)
# 常用方法
# 1. 添加/修改 dict[key] = value 如果key 不存在则添加
# 2. .pop(key) 删除 对应的Key并返回value
# 3. 查询

## [key]
## .get(key)
gtk = d1.get('key1')
print(gtk)
## .keys() 获取所有的key
a = d1.keys()
print(a)
print(type(a))
for i in a:
    print(i)
    print(type(i))
## .values() 获取所有的values
b = d1.values()
print(b)

## .items() 获取所有的 键值对
id1 = d1.items()
for i in id1:
    print(i,type(i),end=" ")
print()

for k,v in d1.items():
    print(f"{k}:{v}")

# 案例1
