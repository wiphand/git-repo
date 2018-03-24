def hanoi(n,a,b,c):
    if(n==1):
        print (a+"->"+b)
    else:
        hanoi(n-1,a,c,b)
        print(a+"->"+b)
        hanoi(n-1,b,c,a)


print(hanoi(3,"A","C","B"))