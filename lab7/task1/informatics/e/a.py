a=int(input())
b=int(input())
c=int(input())
d=int(input())

def min4(a, b, c, d):
    mas = [a,b,c,d]
    mas.sort()
    return mas[0]
 

print(min4(a,b,c,d))
