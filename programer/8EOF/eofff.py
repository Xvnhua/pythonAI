# 捕获异常：处理完异常，程序继续执行
try:
    int(input('Please enter a int:'))
    print(1/0)
# 逐个except进行匹配
except ValueError as e:
    print('invalid input,int only\n',e)
except NameError as a:
    print(a)
except ZeroDivisionError as e:
    print(f'0不能做除数，{e}')
except Exception as e:
    print(f'捕获所有异常{e}')
finally:# 无论是否正常运行都会运行（无论是否捕获）
    print('goodbye')
    # 资源释放~


# 异常传递
# 在函数调用中层层上报，直到有人处理，或者程序崩溃
# 这个过程是自动的
# 一般写 try except优先考虑在高层写