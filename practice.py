def arerage(m,n):
    return (m+n)/2
def sum(a,b,*c):
    total=a+b
    for n in c:
        total=total+n
    return total
a=1;b=2
a,b=b,a
print(a+arerage(a,b))
print(sum(1,2))
print(sum(1,2,3,4))
print(sum(1,2,3,4,5,6))