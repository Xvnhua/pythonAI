# 类型注解
# 不强制限制类型赋值

a:int =699
socre: float =666.3
names:list[str] =['ZS','LS']
phones:set[str] = {'13131131133'}
options:dict[str,int] = {'count':0,'total':0}
goods:tuple[str,int,int] = ('手机',5999,1)

# 指定多集
namesB:list[str|int] =['ZS','LS']
a = '111'
print(a)

# 函数注解
def calll(pa1:int,pa2:dict[int,int])->int:
    return pa1+pa2

