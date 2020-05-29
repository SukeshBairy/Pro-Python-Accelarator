def maxmin(A):
   maxi = A[0]
   secondsmax = None
   mini = A[0]
   secondmini = None
   for item in A[1:]:       
      if item > maxi:
         secondsmax=maxi 
         maxi = item
      elif secondsmax == None or secondsmax < item:
         secondsmax = item
      elif item < mini:
         secondmini=mini
         mini = item
      elif secondmini == None or secondmini > item:
         secondmini = item
   print("Largest element is :", maxi)
   print("Second Largest element is :", secondsmax)
   print("Smallest element is :", mini)
   print("Second Smallest element is :", secondmini)

A=list()
n=int(input("Enter the size of the List :"))
print("Enter the number :")
for i in range(n):
   k=int(input(""))
   A.append(k)
maxmin(A)
