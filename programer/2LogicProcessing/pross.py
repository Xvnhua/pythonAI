#############################################################################################################
# if - elif - else
a = input("Please enter a option\n")
if a == "1":
    print("instruction 1")
elif a == "2":
    print("instruction 2")
else:
    print("default instruction")
############################################################################################################
# match - case模式匹配
match a:
    case "1":
        print("instruction 1")
    case "2":
        print("instruction 2")
    case _:
        print("default instruction")
# case _: 默认执行相当于 default
 ############################################################################################################
# while  - continue/break - else
# 实际上Bool是int的子类，0 被视为 False，1 被视为 True
a = 10
while a-1:
    a -=1
    if a == 5:
        continue
    if a == 4:
        break
    print (a)
else:
    #条件为Flase循环正常结束时执行
    print("default instruction")

###############################################################################################################
# for index in RangeSpace - continue/break  - else
# 取决于 RangeSpace 的容量
for _s in "这是一个字符串":
    print(_s,end=" ")
print()
for i in range(10,20,2):
    print(i,end=" ")
print()
for i in range(21,18,-1):
    print (i ,end=" ")

