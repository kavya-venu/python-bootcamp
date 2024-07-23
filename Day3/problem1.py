#  password verifier mr x is trying to create a new password.these are the required conditions for creating a new password' these are
# condition 1 min len 8 max len 15
# condition 2 only @ and / is allowed is a password
# condition 3  no spaces are allowed
# condition 4 only alpha num are allowed
#condition 5 you are supposed to print weak if the length is exact 8,medium if the leng is b/w 8-12 an`d strong if the length is b/w 12 to 15.
password=input()
n=len(password)
if len(password) < 8:
    print("weak")
elif len(password) >= 8 and len(password) <=12:
    print("medium")
elif len(password) > 12 and len(password) <= 15:
   
    
