x = int(input("Please enter the value of x"))
if x<0 :
    print("X is a Negative number")
elif x>0:
    print("X is a Postive number")
elif x==0:
    print("X is equal to 0")
else :
    print("Not Defined")

if True:
    print("PASS")
else:   #DeadCode
    print("FAIL")

    #WAP to find out the highest number

a=5100
b=200
c=300

if a>b and a>c:
    print("A is the highest number")
elif b>c:
    print("B is the highest number")
else:
    print("C is the highest number")

total = int(input("Enter the total value:"))

if(total<100):
    total = total+20
elif(total>=100 and total<=500):
    total = total+50
else:
    total=total+100
print(total)#no concat
print("total = "+str(total))#str
print(f'{"total = "}{total}') #fString