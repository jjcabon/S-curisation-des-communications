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
    res=[0]*26
    for k in range(26):
        for i in range(n):
            if t[i]==tab_alphabet[k]:
                res[i]=res[i]+1
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
#########################################
t=list("maitrecorbeau")
n=len(t)
assert(codageCesar(t,n,5)==['r', 'f', 'n', 'y', 'w', 'j', 'h', 't', 'w', 'g', 'j', 'f', 'z'])
assert (decodageCesar(['r', 'f', 'n', 'y', 'w', 'j', 'h', 't', 'w', 'g', 'j', 'f', 'z'],n,5)==t)
print(decodageAuto(['r', 'f', 'n', 'y', 'w', 'j', 'h', 't', 'w', 'g', 'j', 'f', 'z'],n))
#assert(decodageAuto(['r', 'f', 'n', 'y', 'w', 'j', 'h', 't', 'w', 'g', 'j', 'f', 'z'],n)==t)
############################################
def codageVigenere(t,n,c,k):

    res=[]
    for i in range(n):
        j=i%k
        a=tab_alphabet.index(t[i])
        b=tab_alphabet.index(c[j])
        res.append(tab_alphabet[(a+b)%26])
    return res
t=['u','n','e','e','c','o','l','e','d','i','n','g','e','n','i','e','u','r','s','p','o','l','y','t','e','c','h','n','i','q','u','e','c','e','s','t','d','i','f','f','i','c','i','l','e']
n=len(t)
c=list("concours")
k=len(c)
print(codageVigenere(t,n,c,k))
#assert(codageVigenere(t,n,c,k)==list("gqbnsjfdahrevhziws"))
#############################################
def pgcd(a,b):
    if a<b:
        a,b=b,a
    if b==0 or a==b:
        return a
    else:
        return pgcd(b,a-b)
#################################################
def distanceEntreRepetition(t,n,i):
    k=i+1
    res=0
    while k<n-2:
        if (t[i],t[i+1]) ==(t[k],t[k+1]):
        #if t[i]==t[k]:
            return k-i
        k=k+1
    return res
#t=list("gqbnsjfdahrevhziws")

t=list("wbrgqicwrcyahytzpwdwswvkvrvhtctanszcwmtwuhvphyiwugnph")
n=len(t)
rep=[]
for i in range(n-1):
    rep.append(distanceEntreRepetition(t,n,i))
print(rep)






