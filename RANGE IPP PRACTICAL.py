def fact(n):
    p=1
    while n>=1:
        p*=n
        n-=1
    return p
for i in range(1,11):
    print("factorail of {} is {}".format(i,fact(i)))
print("PRESENTED BY HARSH")
