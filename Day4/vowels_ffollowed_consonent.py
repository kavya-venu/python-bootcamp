# vowels followed consonent
#kavya
#o/p: aakvy
str=input()
str1=""
str2=""
vomel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
for i in str:
    if(i in vomel):
        str1+=i
for i in str:
    if(i in consonent):
        str2+=i
print(str1+str2)

        