def fibonacci(fibnum):
    list=[]
    a=0
    b=1
    for num in range(fibnum):
        list.append(a)
        c=a+b
        a=b
        b=c
    return list

fiblist=fibonacci(10)
print(fiblist)