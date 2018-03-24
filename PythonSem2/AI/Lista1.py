s = "0010001000"
print(s[2]=="1")

def opt_dist(s,n):
    bestSol=[n]
    if s.count("1")<s.count("0"):
        invTarget = "1"
    else:
        invTarget = "0"
    for bit in range(len(s)):
        if s[bit] == invTarget:
            print(s,bit)
            for plusminusn in range(n,-1,-1):
                print(plusminusn)
                temp = list(s)
                nmbSwaps = 0
                if bit-plusminusn >=0:
                    for toswap in range(len(s)):
                        
                        if toswap > bit-plusminusn-1 and toswap < bit-plusminusn+n:
                            #print("in boundary", plusminusn, toswap)
                            if(temp[toswap]!="1"):
                                #print("not 1")
                                temp[toswap] = swap(temp[toswap])
                                nmbSwaps+=1
                        else:
                            #print("out boundary", plusminusn, toswap)
                            if(temp[toswap]!="0"):
                                #print("not 0")
                                temp[toswap] = swap(temp[toswap])
                                nmbSwaps+=1
                        
                    
                    if (temp.count("1") == n):
                        print(temp,nmbSwaps)
                        bestSol.append(nmbSwaps)
    print(bestSol,min(bestSol))

                            

def swap(bit):
    if bit == "1":
        return "0"
    else:
        return "1"

opt_dist(s,5)