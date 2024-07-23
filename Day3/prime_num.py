#prime number or not
a=int(input("enter a number:"))
count=0
r=a**0.5
if (a==1):
    print("not a prime number")
elif (a==2):
    print("it is a prime number")
for i in range(2,int(r+1)):
    if(a%i==0):
        count=1
        break
if count==0:
    print("it is a prime number")
else:
    print("not a prime number")