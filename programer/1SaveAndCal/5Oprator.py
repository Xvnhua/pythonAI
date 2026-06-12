a,b = 10,3

# 涉及到float会有精度损失
# 算术运算符

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%3)
# 优先级
# 最优先计算 ** 幂次
# 第二优先计算 * / //
# 最后计算 + -
print("0.1 + 10 / 4 ** 2 = ",0.1 + 10 / 4 ** 2)


# 赋值运算

# 1. =
# 2. operator + = 衍生赋值

# *比较运算

# 逻辑运算

print(1 >2 and 1>0)
print(1 >2 or 1>0)
print(not 1>2)