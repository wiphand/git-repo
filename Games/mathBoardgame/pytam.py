def wybor_pytania(): #funkcja zawierająca pytania
    Ans= open("pytania.txt").readlines()
    return(Ans)
   
def odp_a(x): # funkcja dopasowująca odpowiedź a do numeru pytania
    A=open("odp_a.txt").readlines()
    return(A[x].rstrip('\n'))

def odp_b(x): # funkcja dopasowująca odpowiedź b do numeru pytania
    B=open("odp_b.txt").readlines()
    return(B[x].rstrip('\n'))

def odp_c(x): # funkcja dopasowująca odpowiedź c do numeru pytania
    C=open("odp_c.txt").readlines()
    return(C[x].rstrip('\n'))

def odp_d(x): # funkcja dopasowująca odpowiedź d do numeru pytania
    D=open("odp_d.txt").readlines()
    return(D[x].rstrip('\n'))

def numer_pytania(x): # funkcja znajdująca numer pytania
    Ans=open("pytania.txt").readlines()
    w=Ans.index(x)
    return(w)

def poprawne(x):
    numer=open("poprawna_odp.txt").readlines()
    return(numer[x].rstrip('\n')) 