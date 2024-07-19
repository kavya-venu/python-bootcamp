#1.append
#2.pop
#3.sort
#4.print gm or print len of the list
my_list=list(map(str,input().split(",")))
print("enter the choice..\n 1.append\n 2.pop\n 3.sort\n 4.print gm or print len of the list")
ch=int(input())
if(ch==1):
    print("enter the element")
    ele=int(input())
    my_list.append(ele)
elif(ch==2):
    my_list.pop()
elif(ch==3):
    my_list.sort()
elif(ch==4):
    my=len(my_list)
    print(my)
else:
    print("enter the valid input")

