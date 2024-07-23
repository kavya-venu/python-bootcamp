#  input string ABC,4 
# (B,C,D,E),(C,D,E,F),(D,E,F,G) last character=EFG
# EFG
str=input()
for i in str:
    c=ord(i)+4
    print(chr(c))
    