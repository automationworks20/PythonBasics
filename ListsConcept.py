score =[10,20,67,50,90]
print(score)

print(score[0])
print(score[4])
print(score[-1])
#0-4
#-1 to -5

str = print(score[:])#New Copy

print(score + [1 , 2 , 3])
print(score + ["A"])

number = [1,2,3,4,5]
number[2] = 90
print(number)

#append

number.append(100)
print(number)

number.append(7**3)
print(number)

name = ['a','b','c','d','e','f']
print(name)

name[2:5] = ['C','D','F']

print(name)

name[2:5] = []

print(name)

name[:] = []

print(name)

#Nested Lists

a = ['a', 'b', 'c']
n =[1,2,3]
x =[a,n]

print(x)

print(x[0][1])
print(x[1][2])