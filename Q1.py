f = open("DNA.txt", "r")
a=f.read()
l=len(a)
k=0
for i in range(0,l):
    if(a[i]=='5'):
        k=i
        break

R=''
for j in range(k+2,l):
    if(a[j]=='T'):
        R=R+'U'
    elif(a[j]=='\n'):
        R=R
    else:
        R=R+a[j]

    
#print(R)
#print(k)



GC = { 'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'U', 'ACC':'U', 'ACG':'U', 'ACU':'U', 'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R','CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R','GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G','UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S','UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_','UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W', }

LoR = len(R)
prot = ''
for q in range(0,LoR):
    if(q%3==2):
        cod = R[q-2]+R[q-1]+R[q]
        prot = prot + GC[cod]

print(prot)


