a,b,c=map(int,input().split())
s=(a+b+c)/2
i=s**.5
j=(s-a)**.5
k=(s-b)**.5
l=(s-c)**.5
A=i*j*k*l
print("%.2f" % A)