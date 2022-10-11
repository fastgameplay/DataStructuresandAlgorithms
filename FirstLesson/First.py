def Calculate(a,b,c):
    return len([i for i in range(a,b+1) if i%c == 0])

print(Calculate(1,2,1))