i = int(input())
lis = list(map(int,input().strip().split()))[:i]
mx=max(lis[0],lis[1])
secondmax=min(lis[0],lis[1])
n =len(lis)
for i in range(2,n):
    if lis[i]>mx:
        secondmax=mx
        mx=lis[i]
    elif lis[i]>secondmax and \
        mx != lis[i]:
        secondmax=lis[i]
 
print(str(secondmax))