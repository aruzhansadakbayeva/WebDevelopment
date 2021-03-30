n = int(input())
arr = list(map(int, input().split()))
for i in range(0, n-1):
    elem = arr[i]
    if elem % 2 == 0:
        print(elem, end = ' ')