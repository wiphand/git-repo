wyniki=[]
w="aaaa"
max=1
ws=list(w)
wyniki+=[[]]
print(ws , wyniki)
wyniki[0] += '1'
wyniki[0] += ws[0]
print(wyniki)
for i in range(1,len(ws)):
    if(int(wyniki[len(wyniki)-1][0]==4) and (len(wyniki[i-1])-1>len(ws))):
        print("break")

        break
    for k in wyniki:
        ##print("k:",k)
        if(int(k[0])==max and ws[i] not in k):
            k[0]=str(max+1)
        elif(int(k[0])==max+1):
            pass
        else:
            if ws[i] not in k:
                k[0]=str(int(k[0])+1)
            k.append(ws[i])
        print("k:",k)
    print("Wynik:",wyniki)
    if(ws[i]!=ws[i-1]):
        wyniki.append(['1'])
        wyniki[len(wyniki)-1] += ws[i]
    print("Wynik:",wyniki)

currentBiggest=0
index=-1
for j in range(len(wyniki)):
    #print((len(wyniki[j])-1))
    #print(int(wyniki[j][0]))
    if ((len(wyniki[j])-1)>=currentBiggest and int(wyniki[j][0])==max):
        index = j
        currentBiggest=len(wyniki[j])-1
        #print(index,currentBiggest)

if(index != -1):
    print(wyniki[index])
##print(wyniki)
    