#测试全局变量 局部变量
import sys
'''
sum=5
def add(a=1,b=3):
    print(a,b)
    print (sum)  #仅仅访问 
add(4,8)
print (sum)

'''

'''
sum=5
def add(a=1,b=3):
    print (a,b)
         #内部函数有引用外部函数的同名变量或者全局变量,并且对这个变量有修改.那么python会认为它是一个局部变量
    sum=b+a #在函数内部修改
    print (sum)
    return sum
print(add(4,8))
print(sum)

'''
'''
sum=5
def add(a=1,b=3):
    print (a,b)
    print (sum)  #内部函数引用同名变量，并且修改这个变量。python会认为它是局部变量。因为在此处print之前，没有定义sum变量，所以会报错（建议与情况一比较，备注：此处只是比上例先print sum）
    sum=b+a
    print (sum)
    return sum
print(add(4,8))
print(sum)
'''
