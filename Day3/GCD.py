# sort elements first half in ascending order and second half in descending.
#list=list(map(int,input().split()))

#GCD of 2 number.
a=int(input("enter 1stn umber:"))
b=int(input("enter 2nd number:"))  
while b!=0:
     a,b=b,a%b
print("GCD of 2 number is:",a)                                                    