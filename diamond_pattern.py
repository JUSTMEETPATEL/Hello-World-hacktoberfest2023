N = int(input("Enter the number"))
for i in range(0,N+2):
    if i %2 != 0:
        m = (N - i)//2
        t = ' ' * m
        s = '*' * i
        print(t,s,t)
    else: 
        pass
for i in range(N,0,-1):
    if i %2 != 0:
        m = (N - i)//2
        t = ' ' * m
        s = '*' * i
        print(t,s,t)
    else: 
        pass
