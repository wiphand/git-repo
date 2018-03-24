s="send + more"# = money"
cyfry=[9,8,7,6,5,4,3,2,1,0]
dictMain={}
def analyze(s):
    
    functions=[]
    s=list(s)
    iter=0
    for x in s:
        if(x.isalpha()):
            dictMain[x] = dictMain.setdefault(x,cyfry.pop())
        elif(x!=" "):
            functions+=x
    print(dictMain,functions)

    return

def evalu(String):
    value=0
    String = list(String)
    String = String[::-1]
    print(String)
    values = [dictMain.setdefault(x,0) for x in String]
    print(values)
    temp=1
    for x in values:
        value+=int(x)*temp
        temp*=10
    return value

analyze(s)
print(evalu("bat"))