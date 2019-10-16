def arerage(m,n):
    return (m+n)/2
def sum(a,b,*c):
    total=a+b
    for n in c:
        total=total+n
    return total
def max(a,b,*c):
    max_value=a
    if max_value<b:
        max_value=b
    for n in c:
        if max_value<n:
            max_value=n
    return max_value
a=1;b=2
a,b=b,a
print(a+arerage(a,b))
print(sum(1,2))
print(max(1,2,3,4,5,6))