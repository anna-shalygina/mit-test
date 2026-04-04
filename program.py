n=int(input())
def fib(n):
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    res=[0,1]
    for i in range(2,n):
        res.append(res[i-1]+res[i-2])
    return res
num=fib(n)
for i in num:
    print(i)
