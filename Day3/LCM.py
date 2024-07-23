#LCM
a=int(input("enter 1st Number:"))
b=int(input("enter 2nd number:"))  
c=a*b
while b!=0:
     a,b=b,a%b
     gcd=a
print("GCD",gcd)
lcm=c//gcd
print("LCM",lcm)