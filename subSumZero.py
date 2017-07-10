# Find a sub sequece, in a input suquence, of which sum is zero. 
import numpy as np

def sum2zero(S):
	
	X = np.array([])
	for i in range(0,len(S)):
		j = i
		check = False
		while check == False:
			j = j +1
			if j == len(S):
				break
			if sum(S[i:j]) == 0:
				X = np.append(X,(i,j))
				Check = True
	print X


	return X


S = [-1, 3, -4, 1, 2, 1, 4, 6]

sum2zero(S)
