class Tdl:
   def __init__(self,list_name,status):
      self.list_name=list_name
      self.status=status
      
  

A={}

print("TO-DO-LIST")


while(True):
   print("-"*30)
   ch=int(input("Enter one of the choices:\n\
      1.Add To-Do-List\n\
      2.status_change\n\
      3.Show all the tasks\n\
      4.exit\n-->"))
   if ch == 1:
      list_name=input("To-Do-List name:")
      status=input("1. PENDING(p)\n\2.(d)\n-->  ")
      tdlist=Tdl(list_name,status)
      A[list_name]=status
      
    
   elif ch == 2:
      list_name=input("To-Do-List name:")  
      if list_name in A:
         status=input("Enter the changes:")
         A[list_name]=status
         
      else:
         print("The entered task has not been entered.Please do add the task to the list." )


   elif ch == 3:
      print("p=PENDING and d=DONE")
      for i,j in enumerate(A):
         print(j,"-",A[j])

   elif ch == 4:
      print("Thank you for visiting.")
      break
          






              
