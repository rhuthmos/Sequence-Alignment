import numpy as np

file = open("./Group26/protein.fa", "r")
#file2=file.read()
#print(file2)

filepath = './Group26/protein.fa'

protein1 = ''
protein2 = ''

counter = 0
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		if (line[0]=='>'):
			if (counter == 0 or counter==2):
				counter+=1
		elif (counter==1):
			protein1 = line
			counter+=1
		elif (counter==3):
			protein2 = line
			break
		line = fp.readline()

protein1 = str(protein1)
protein2 = str(protein2)
print(protein1)
print(protein2)

#sumMatrix = np.empty((len(protein1), len(protein2)), dtype = 'S1')
sumMatrix = []
for i in range(len(protein1)):
	arr = []
	for j in range(len(protein2)):
		arr.append(0)
	sumMatrix.append(arr)

# initialisation
for i in range(len(protein1)):
	for j in range(len(protein2)):
		if (protein1[i]==protein2[j]):
			sumMatrix[i][j] = 1
			#print("Value:", sumMatrix[i][j])
			#print(i," ",j)
		else:
			sumMatrix[i][j] = 0


#compute the matrix
def findMax(a,b):
	if (a>len(protein1)-1):
		return len(protein1), len(protein2)
	if (b>len(protein2)-1):
		return len(protein1), len(protein2)
	else:
		ansx = a
		ansy = b
		ans = 0
		i = a
		j = b
		while(i<len(protein1)):
			if (sumMatrix[i][j]>ans):
				ans = sumMatrix[i][j]
				ansx = i
				ansy = j
			
			i+=1
		i = a
		j = b
		while(j<len(protein2)):
			if (sumMatrix[i][j]>ans):
				ans = sumMatrix[i][j]
				ansx = i
				ansy = j
			j+=1
		return ansx, ansy


for j in range(len(protein2)-1, -1, -1):
	for i in range(len(protein1)-1, -1, -1):
		ax, ay = findMax(i+1, j+1)
		if (ax<len(protein1) and ay<len(protein2)):
			sumMatrix[i][j] += sumMatrix[ax][ay]

out1 = ''
out2 = ''

i = -1
j = -1

while(i<len(protein1) and j<len(protein2)):
	ax, ay = findMax(i+1, j+1)
	if (ax==i+1 and ax<len(protein1) and ay<len(protein2)):
		#gap in protein1
		out2 += protein2[j+1:ay+1]
		l = ay-j
		out1+=(" "*(l-1) + protein1[ax])
		
	elif(ay == j+1 and ax<len(protein1) and ay<len(protein2)):
		#gap in protein2
		out1 += protein1[i+1:ax+1]
		l = ax - i
		out2+=(" "*(l-1) + protein2[ay])
	
	
	j = ay
	i = ax

print(out1)
print(out2)

#print(sumMatrix)