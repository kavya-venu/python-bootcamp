#write a program leap year in range.
s_year=int(input("enter a start year:"))
e_year=int(input("enter a end year:"))
for year in range(s_year,e_year+1):
    if year%100==0 or (year%4==0 and year%100!=0):
        print(year,end=" ")