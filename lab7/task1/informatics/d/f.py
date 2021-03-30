n = int(input())
sum=0
arr = list(map(int, input().split()))
for i in range(0, n-1):
    
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        sum+=1
        print(sum)