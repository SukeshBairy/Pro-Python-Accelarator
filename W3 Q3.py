s=input("Enter the string")
n=""
count=0

for i in range(len(s)):
	if s[i].isupper()==False:
		n=n+s[i]
		count=count+1
	else:
		if count==0:
			n=n+s[i]
		else:
			n=n+" "
			n=n+s[i]
print(n)				
					

					