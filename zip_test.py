#program to test the newly learnt zip feature in python
difference = 0
a = [1,2,3,4,5]
b = [6,7,8,9,10]
for i,j in zip(a,b):
	difference += j-i
print(difference)