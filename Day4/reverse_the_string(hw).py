# reverse the number of string
# example hello1234world
#o/p:4321
str3=input()
str2=""
for i in str3:
    if(i not in str2):
        str2+=i
print(str2)
print(str2[::-1])