# 相对于list
# 元素是可重复、有序、可以修改的The 'Blank' component can only be nested in the 'Row,Column,Flex' parent component. <ArkTSCheck>
# 如果要记录一些数据不能被修改只能被查询
# 一旦定义完成不可修改，元祖可以重复、有序、不可以修改

# 定义
TupleName = (1,2,3,4,4)

# 定义空Tuple
None_Tuple = ()
None_Tuple = tuple()

# 方法：
# .count()
# .index()匹配到第一次出现的位置

# 组包与解包 定义元祖其实就是一个组包的过程中
# 组包
t1 = (1,2,5,6)
t2 = 1,2,5,6

# 解包
a,b,c,d = t1

print(t1)
print(t2)

# (*)扩展解包
x , *y,z = t1
print(x)
print(y)# 收集剩余的所有元素
print(z)

# 多变量交换也是用的tuple的组包解包操作

a,b,c = 10 ,12 ,13
a,b,c = c,a,b
# 这实际上就是一个组包再解包的操作

# 案例1
ywmax,sxmax,yymax = 0,0,0
ywmin,sxmin,yymin = 100,100,100

students = (
    (tuple("S001 王林 85 92 78".split(" "))),
    (tuple("S002 王4 99 56 84".split(" "))),
    (tuple("S003 王5 26 33 56".split(" "))),
    (tuple("S001 王6 0 35 15".split(" "))),
    (tuple("S001 王7 11 78 35".split(" "))),
    (tuple("S001 王8 89 86 45".split(" ")))
)
# 可以推导式来批量获取二级元素
Chinese_Scores = [s[2] for s in students]
Math_Scores = [s[3] for s in students]
English_Scores = [s[4] for s in students]

# 直接用解包遍历,直接得到对应的
for sn,xm,yw,sx,yy in students:

    yw,sx,yy = int(yw),int(sx),int(yy)
    # max
    ywmax = max(ywmax,yw)
    sxmax = max(sxmax,sx)
    yymax = max(yymax,yy)
    # min
    ywmin = min(ywmin,yw)
    sxmin = min(sxmin,sx)
    yymin = min(yymin,yy)

    aver = (yw+sx+yy)/3
    print(f"{xm}:总分={yw+sx+yy},均分={aver}")
    if aver>90:
        print(xm)
print(f"语文:max={ywmax},min={ywmin}")
print(f"数学:min={sxmax},min={sxmin}")
print(f"英语:max={yymax},min={yymin}")


