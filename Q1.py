f = open("DNA.txt", "r")
a=f.read()
l=len(a)
k=0
for i in range(0,l):
    if(a[i]==5):
        k=i
        break

R=''
for j in range(k,l):
    if(a[j]=='T'):
        R=R+'U'
    else:
        R=R+a[j]

    
print(R)
