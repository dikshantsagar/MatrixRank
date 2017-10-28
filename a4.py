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
			
			print(a[k][k])

			if a[k][k]!=0:
				
				if k==0:
			
					fac1=a[0][0]/a[0][1]
					a=Row_Transformation(a,-fac1,0,1)
					fac2=a[0][0]/a[0][2]
					a=Row_Transformation(a,-fac2,0,2)

				elif k==1:
					fac1=a[1][1]/a[1][0]
					a=Row_Transformation(a,-fac1,1,0)
					fac2=a[1][1]/a[1][2]
					a=Row_Transformation(a,-fac2,1,2)


				elif k==2:
					fac1=a[2][2]/a[2][0]
					a=Row_Transformation(a,-fac1,2,0)
					fac2=a[2][2]/a[2][1]
					a=Row_Transformation(a,-fac2,2,1)



			elif a[k][k]==0:
				rank=rank-1
				if k==0:
					if a[1][0]!=0:
						a=swapRows(a,0,1)
						
					elif a[2][0]!=0:
						a=swapRows(a,0,2)
					
				elif k==1:
					if a[1][2]!=0:
						a=swapRows(a,1,2)
						




				k-=1
	
	return rank


hal=matrixrank(mat)

print(hal)
print(mat)


