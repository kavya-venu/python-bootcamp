# print the non repeating characters in a string
ans=""
str=input()
str2=""
for i in str:
    if(i not in str2):
        str2+=i
print(str2)
