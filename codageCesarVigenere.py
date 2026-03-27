# Créé par enseignant, le 27/03/2026 en Python 3.7
import string
alphabet=string.ascii_lowercase
tab_alphabet=list(alphabet)

########################################
def codageCesar(t,n,d):
    code=[]
    for k in range(n):
        v=t[k]
        i=0
        while tab_alphabet[i]!=v:
            i+=1
        i+=d
        while i>25:
            i-=26
        while i<0:
            i+=26
        code.append(tab_alphabet[i])
    return code
def decodageCesar(t,n,d):
    d=0-d
    return codageCesar(t,n,d)
#########################################
def frequence(t,n):
    res=(0)*26
    for k in range(26):
        for i in range(n):
            if t[i]==tab_alphabet[k]:
                res[k]+=1
    return res
def decodageAuto(t,n):
    tab=frequence(t,n)
    max=tab[0]
    imax=0
    for k in range(26):
        if tab[k]>max:
            imax=k
            max=tab[k]

    d=imax-4
    return decodageCesar(t,n,d)





t=list("maitrecorbeau")
n=len(t)
print(codageCesar(t,n,5))