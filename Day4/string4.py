#find the program hello123world
#o/p:6
str=input()
sum=0
count=0
for i in str:
    if(i.isnumeric()):
      count=int(i)
      sum+=count
print(sum)