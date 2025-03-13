#not accepting any i/p not returning any o/p
def fun1():
    a=10
    b=20
    c=a+b
    print(c)
fun1()
#not accepting any i/p  returning the o/p
def fun2():
    a=10
    b=20
    c=a+b
    return(c)
result2=fun2()
print(result2)
#accepting  i/p not returning the o/p
def fun3(a,b):
    c=a+b
    print(c)
n1=20
n2=50

fun3(n1,n2)

#accepting  i/p  returning the o/p
def fun4(a,b):
   
    c=a+b
    return(c)

n1=1000
n2=5000

fun4(n1,n2)
result2=fun4(n1,n2)
print(result2)
