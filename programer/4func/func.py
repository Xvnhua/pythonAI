def f1(param1, param2):
    return param1 + param2


# return 可以不写


def le():
    print('-------------------------------------------------')


ret = f1(1, 2)
print(ret)
le()


# 传参和返回值
# 多返回值会封装到元组之中
def f2(pp1):
    return pp1 + 1, pp1 + 2


print(f2(1))
## 内置函数
print(round(6.3331, 1))


# 函数说明文档
def f33(pa1, pa2):
    '''
    这是函数的注释文档
    :param pa1:加数1
    :param pa2:加数2
    :return :pa1+pa2:和
    '''
    return pa1 + pa2


f33(1, 2)

# global 关键字 使参数操作变为操作对应的全局参数
# 主要用于修改状态信息

numb1 =1
def ff():
    global numb1
    numb1+=1
ff()
print("numb1:",numb1)

# 传参 方式
# 位置传参
# 关键字传参
f33(pa2=1,pa1 =2)
# 混合使用
f33(1,pa2 = 1)

# 默认参数，定义时可以不用传参
def f55(a,v=2,c=3):
    print(a,v,c)
f55(1)
f55(1,2)

# 不定长参数
# *args 封装多个数据为元组
print('f66')
def f66(a=1,b=2,*args):
    print(a,b,args)
    return
f66(1,2,3,4,5)

# **关键字传递
# **args封装为一个 dict (键值对)
def f77(a = 3 ,**kwargs):
    print (a,kwargs)

f77(1,ad = '1',ab = '2')

def p1(x,y):
    print(x+y)

def p2(x,y):
    print(x-y)
# 函数参数
def calc(x,y,oper):
    return oper(x,y)

calc(1,2,p1)
calc(1,2,p2)
# calc(1,1,1)


# 匿名函数
add = lambda x,y:x+y
# 作为一个高阶函数的参数使用

pt = lambda :print('----------------')

pt()

data_list = ['C++','C','JAVA','GO','RUST','JAVASCRIPT','PYTHON','JACK']
print(data_list)
data_list.sort(key  = lambda x:len(x))
print(data_list)

## 案例

# n的阶乘
def jiejie(x):
    if(x<0):
        print('Must be positive')
        return -1
    if x==0:
        return 1
    else:
        return x * jiejie(x-1)
print(jiejie(-1))

# 电商计算器

def cal_to_cost(name:str = 'default',cost:int = 0,numb:int = 0,优惠券:int = 0,积分:int = 0,运费:int = 0):
    total = cost * numb +运费
    sub = 0
    if total>=5000:
        if 优惠券<=total:
            total -= 优惠券
        total -= 积分//100
        if total <0:
            return 0
    return total
















