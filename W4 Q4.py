n=input("Enter the text:")
n=n+""
# Creating two lists to store the data
l=[]
li=[]
# A variable to keep the count of each word
count=0
s=""
d={}


for i in range(0,len(n)):
	if n[i] == " ":
		for j in range(count,i):
			#print(count,i)
			s=s+n[j]
		l.append(s)
		s=""
		count=i+1


for i in l:
	d[i]=1


for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		if l[i] == l[j]:
			d[l[i]]=d[l[i]]+1
			break
for i,j in enumerate(d):
	print(j,":",d[j])			

		 	 	


