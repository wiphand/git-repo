a="aabdbcca"
b="abcdca"
    
def NWP(x,z):
    if(len(z)==0 or len(x)==0):
        return ""
    elif(x[-1] == z[-1]):
        print("true")
        return NWP(x[:-1],z[:-1])+x[-1]
    else:
        temp = NWP(x[:-1],z)
        temp2 = NWP(x,z[:-1])
        """if(x.find(z[-1])!=-1):
            temp2 = temp2+z[-1]
        elif(z.find(x[-1])!=-1):
            temp = temp+x[-1]"""
        print("test:",temp,temp2)
        if(len(temp)<len(temp2)):
            return temp2
        else:
            return temp




print(NWP(a,b))