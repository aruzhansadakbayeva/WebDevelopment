a = input()
a = a.split()
a = [int(i) for i in a]
for i in range(len(a)//2):
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = b

print(a)