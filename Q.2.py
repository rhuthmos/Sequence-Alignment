import sys
print(sys.argv)
temp = "C:/Users/dell/Desktop/IQB/GROUPWISE -IQB/Group25/"
f = open(temp+sys.argv[2], "r")
a=f.read()
l=len(a)

print(l)


# FOR HEADER
k=0 
for i in range(6,l-5) :
	if (a[i:i+5]=="TITLE") :
		k=i ;
		break ;
#print(k)
header = a[0:k]
print(header)


# FOR TITLE
p=0 
for j in range(k,l-6) :
	if (a[j:j+6]=="COMPND") :
		p=j ;
		break ;
#print(p)
title = a[k:p]
print(title)


# FOR RESOLUTION
m=0 
n=0
for j in range(0,l-10) :
	if (a[j:j+10]=="RESOLUTION") :
		m=j ;
		break ;
for j in range(m,l-6) :
	if (a[j:j+6]=="REMARK") :
		n=j ;
		break ;

resolution = a[m:n]
print(resolution)

file = open(sys.argv[4], "x") 
file.write(header)
file.write(title)
file.write(resolution)
file.close()