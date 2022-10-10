a=input()
flag=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]==a[j] and i!=j :
            flag=1
if flag==0:
    print('Unique Number')
elif flag==1:
    print("Not Unique Number")