#your given with a coma separated natural numbers 1 to 10 print the even numbers
my_list=list(map(int,input().split(",")))
 for i in range(1,len(my_list),2):
    print(my_list[i])