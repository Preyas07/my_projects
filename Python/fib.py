n=int(input("Enter no. of terms:"))
f1=0
f2=1
c=2
if n==1:
   print(f1)
elif n==2:
   print(f1,'\n',f2,sep='')
else:
   print(f1,'\n',f2,sep='')
while c<n:
   f=f1+f2
print(f)
f1,f2=f2,f1
c+=1