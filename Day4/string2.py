# check how many vomels are there in a sting
'''str1=input()
c=0
check=['a','e','i','o','u']
for i in str1:
   if(i in check):
     c+=1
print(c)'''
 
vomel="aeiou"
consonent="bcdfghijklmnpqrstvwxyz"
count=0
c=0
i=input()
inp=i.lower()
for i in inp:
    if(i in vomel):
        count+=1
for i in inp:
    if(i in consonent):
        c+=1
print(count)
print(c)

