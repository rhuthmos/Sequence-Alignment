import numpy as np
import copy
import sys

argl = sys.argv
filepath=argl[1]

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
			protein1 = line[:-1]
			counter+=1
		elif (counter==3):
			protein2 = line[:-1]
			break
		line = fp.readline()

protein1 = str(protein1)
protein2 = str(protein2)
print("PROTEIN1 : ",protein1)
print("PROTEIN2 : ", protein2)

#sumMatrix = np.empty((len(protein1), len(protein2)), dtype = 'S1')
sumMatrix = []
for i in range(len(protein2)):
	arr = []
	for j in range(len(protein1)):
		arr.append(0)
	sumMatrix.append(arr)


# initialisation
for i in range(len(protein2)):
	for j in range(len(protein1)):
		if (protein2[i]==protein1[j]):
			sumMatrix[i][j] = 1
			#print("Value:", sumMatrix[i][j])
			#print(i," ",j)
		else:
			sumMatrix[i][j] = 0

dotplot = copy.deepcopy(sumMatrix)
protein1list =  [" "] + [char for char in protein1]
dotplot.insert(0, protein1list)

for i in range(1, len(dotplot)):
	dotplot[i].insert(0, protein2[i-1])
	for j in range(1, len(dotplot[i])):
		if (sumMatrix[i-1][j-1] == 1):
			dotplot[i][j] = "."
		else:
			dotplot[i][j] = " "
print("DOTPLOT: ")
print(dotplot)
with open("dotplot.txt", "w") as txt_file:
    for line in dotplot:
        txt_file.write(" ".join(line) + "\n")


#compute the matrix
def findMax(a,b):
	if (a>len(protein2)-1):
		return len(protein2), len(protein1)
	if (b>len(protein1)-1):
		return len(protein2), len(protein1)
	else:
		ansx = a
		ansy = b
		ans = 0
		i = a
		j = b
		while(j<len(protein1)):
			if (sumMatrix[i][j]>ans):
				ans = sumMatrix[i][j]
				ansx = i
				ansy = j
			j+=1
		i = a
		j = b

		while(i<len(protein2)):
			if (sumMatrix[i][j]>ans):
				ans = sumMatrix[i][j]
				ansx = i
				ansy = j
			
			i+=1
		

		return ansx, ansy

for j in range(len(protein1)-1, -1, -1):
	for i in range(len(protein2)-1, -1, -1):
		ax, ay = findMax(i+1, j+1)
		if (ax<len(protein2) and ay<len(protein1)):
			sumMatrix[i][j] += sumMatrix[ax][ay]


sumMatrixOut = copy.deepcopy(sumMatrix)
protein1list =  [" "] + [" " + char for char in protein1]
sumMatrixOut.insert(0, protein1list)

for i in range(1, len(sumMatrixOut)):
	sumMatrixOut[i].insert(0, protein2[i-1])
	for j in range(1, len(sumMatrixOut[0])):
		sumMatrixOut[i][j] = '0'*(2 - len(str(sumMatrix[i-1][j-1]))) + str(sumMatrix[i-1][j-1])

print("SUM-MATRIX :")
print(sumMatrixOut)
with open("sumMatrixOut.txt", "w") as txt_file:
    for line in sumMatrixOut:
        txt_file.write(" ".join(line) + "\n")

        

out1 = ''
out2 = ''

i = -1
j = -1

while(i<len(protein2) and j<len(protein1)):
	ax, ay = findMax(i+1, j+1)
	if (ax==i+1 and ax<len(protein2) and ay<len(protein1)):
		#gap in protein2
		out1 += protein1[j+1:ay+1]
		l = ay-j
		out2+=(" "*(l-1) + protein2[ax])
		
	elif(ay == j+1 and ax<len(protein2) and ay<len(protein1)):
		#gap in protein1
		out2 += protein2[i+1:ax+1]
		l = ax - i
		out1+=(" "*(l-1) + protein1[ay])
	
	
	j = ay
	i = ax

print(out1)
print(out2)

score = 0

for i in range(len(out1)):
	if (out1[i]==out2[i]):
		score+=1
print("Total Score : ", score)
print("Total Length : ", len(out1))
print("Percentage identity : ", (score/len(out1))*100)

with open("Alignment.txt", "w") as txt_file:
    txt_file.write(out1 + "\n")
    txt_file.write(out2 + "\n")
    


#print(sumMatrix)
