# Use of Regular expression operations
import re 
user_name=input("Enter the User name:")
password=input("Enter a Password:")
flag = 0
while True:   
    if ((len(password)<8) or (len(password)>16)): 
        flag = -1
        print("Entered Password has either less than 8 characters or more than 16 characters. Please enter another Password.")
        break
        # Scan through string looking for the first location where the regular expression pattern produces a match
    elif not re.search("[a-z]", password): 
        flag = -1
        print("Missing lowercase character . Use atleast 1 letter [a-z]")
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        print("Missing uppercase character . Use atleast 1 letter [A-Z]")
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        print("Use atleast 1 number [0-9].")
        break
    elif not re.search("[_@$#]", password):    
        flag = -1
        print("Use atleast one special character [_@$#]") 
        break
    else: 
        flag = 0
        print("Valid Password")
        print( f"Hello {user_name}! you have succesfully logged in. ")  
        break
  
if flag ==-1: 
    print("InValid Password")
    
