import math


def swapRows(a,row1,row2):
	temp=0
	for n in range(3):
		temp=a[row1][n]
		a[row1][n]=a[row2][n]
		a[row2][n]=temp
	print(a)
	return a



mat=[[10,20,10],[-20,-30,10],[30,50,0]]



def Row_Transformation(a,x,row1,row2):

	for n in range(3):
		a[row2][n]=a[row2][n]+(x*a[row1][n])

	return a


def matrixrank(a):
	
	rank=3
	for k in range(3):
		if a[k][k]!=0:


		elif a[k][k]==0:

			if a[k+1][0]==0 and a[k+1][1]==0 and a[k+1][0]:
				a=swapRows(a,k,2)
				rank-=1

			elif a[k+1][k]==0:
				a=swapRows(a,k,k+1)





