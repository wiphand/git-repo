"""Dla danego zbioru Xn = [1,2,3,..., n] i rodziny R = [S1, S2, S3, ..., Sk], gdzie Si to podzbiory Xn,

problem pokrycia zbioru polega na znalezieniu najmniejszej liczby zbiorów z R które sumują się do Xn.

Napisz dwa algorytmy rozwiązujące ten problem:

-zachłanny, który w każdym kroku stara się wybrać zbiór z R pokrywający najwięcej niepokrytych elementów (0.4pkt)

-naiwny, sprawdzający wszystkie podzbiory z R (0.4pkt)

-znajdź takie n i taką rodzinę R, gdzie pierwszy algorytm nie daje optymalnego wyniku (0.2pkt)"""

x=[1,2,3,4,5,6]
n=6
R=[[1,2,3],[1,3],[2,5],[4,6]]
def sPodz(n,x,R):
    database=[["",""]]
    result=[]
    while(result!=x):
        niePokr=list(x)
        dostPodZ=list(R)
        for y in database:
            if(len(y)==0):
                break
            try:
                dostPodZ.remove(y[0])
            except ValueError:
                pass
        database.append([])
        while(len(niePokr)!=0 and len(dostPodZ)!=0):
            database[-1].append(max(dostPodZ,key=len))
            dostPodZ.remove(max(dostPodZ,key=len))
        test=[]
        for k in range(len(database[-1])):
                for j in database[-1][k]:
                    test.append(j)
        #print(test)
        if (set(test)==set(x) and len(test)==len(x)):
            print(test)
    print(database,result)
    
sPodz(n,x,R)

def naiwFn(n,x,R):
    subs = []
    for i in range(len(R)):
        n = i+1
        while n <= len(R):
            subs.append([])
            sub = R[i:n]
            print(sub)
            for k in range(len(sub)):
                for j in sub[k]:
                    subs[-1].append(j)
            n += 1
    print(subs)
    for test in subs:
        if (set(test)==set(x) and len(test)==len(x)):
            print(test)

#naiwFn(n,x,R)