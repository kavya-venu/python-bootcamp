# print all capital letter in s given string
str=input()
for i in str:
    if(ord(i)>=65 and ord(i)<=91):
         print(i,end=" ")