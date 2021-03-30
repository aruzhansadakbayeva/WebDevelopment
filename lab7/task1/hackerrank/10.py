string=str(input())
max_width=int(input())

def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        s += string[c:c+max_width] + "\n"
    return s

wrap(string,max_width)