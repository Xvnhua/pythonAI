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

# 案例1 邮箱格式验证
def check_mail(Mailstr):
    if not Mailstr.count('@')==1 or not Mailstr.count('.')>=1:
        print("邮箱格式错误")
        return False
    print('邮箱格式正确')
    return True

check_mail('')
check_mail('xiaxia@@qq.com')
check_mail('xiaxia@qq.com')
check_mail('xiaxia@qq.bat.com')

# 练习1 判断是否是回文串
def checkifhui(strr):
    if len(strr)%2!=0:
        return False
    while len(strr)!=0:
        if strr[0] != strr[-1]:
            return False
        strr = strr[1:len(strr)-1]
    return True
print(checkifhui('01100'))
print(checkifhui('101100'))
print(checkifhui('001100'))
