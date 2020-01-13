# while Loop :

count=0
while(count<3):
    #print("Hello World")
    print(count)
    count = count+1
print("===========")
num =0
while(num<3):
    print("Hello Python")
    num=num+1
else:
    print("Bye Python")

print("===========")

# for loop :
name=["java","python",".net","c#"]
for i in name:
    print(i)

str = "I Love Python"
for i in str:
    print(i)

print("===========")

list = ["Automation", "Works"]
for index in range(len(list)):
    print (list[index])

#for loop with else:

CountryList = ["India", "Canada","USA","UAE"]
for index in range(len(CountryList)):
    print(CountryList[index])
else:
    print("CountryList is over")

CityList = ["Toronto", "Montreal","AMD","YYZ"]
for index in range(2):
    print(CityList[index])
else:
    print("CityList is over")

print("===========")

#nested for loop:

for i in range(1,5):
    for j in range(i):
        print(i,end='')
    print()