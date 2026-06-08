# 可以存放任意数量的字符，可以用引号包裹
# str 不可变性，无法修改，是有序的，可迭代的
# 有迭代体的特性（切片、正反索引）

# 常用方法 注：不改变str本身
The_str = '_这是一个待使用的字符串的_'
print(The_str)

# .find()
print(The_str.find('的'))

# .count()
print(The_str.count('_'))

# .upper() ,lower 仅对字母操作

# .split() 按照指定分割符分割成列表
print(The_str.split('的'))

# .strip() 去除字符串中两段的空白字符或者指定字符
striped_str = The_str.strip()
print(striped_str)

# .repleace() 将指定子串替换为新的子串
replace_str = The_str.replace('_', '*')
replace_str = replace_str.replace('待使用', '新的')
print(replace_str)
# .startswith() 检查是否以指定子串开头，返回布尔值
print(replace_str.startswith('*'))
print(replace_str.startswith('_'))

