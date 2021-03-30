n = int(input())
arr = list(map(int, input().split()))
for i in range(0, n-1):
    elem = arr[i]
    index = i
    if index % 2 == 0:
        print(arr[index], end = ' ')