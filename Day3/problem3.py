#swap a number(a=10 b=20) a=a+b-a(10+20-10)=
'''a=int(input())
b=int(input())
a=a+b-a
b=a+b-a
print(a)
print(b)'''

#sum of natural number
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
