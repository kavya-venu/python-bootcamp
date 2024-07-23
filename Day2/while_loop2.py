#find the sum of square of a digits in a given number.
# 1*2*3=14
'''n=int(input())
sum=0
while n>0:
  d=n%10
  sum=sum+d**2
  n=n//10
print(sum)'''

#sum of even
n=int(input())
sum=0
while n>0:
    d=n%10
    if(d%2==0):
        sum+=d
    n=n//10
print(sum)
