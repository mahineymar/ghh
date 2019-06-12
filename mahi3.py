a=input()
a1=input()
l=[]
for i in a1:
    l.append(i)
if(len(a1)==len(a)):
   for i in range(len(a)):
       k=ord(a[i])-ord('a')+1
       l[i]=ord(a1[i])+k
for i in l:
   if i>ord('z'):
       i=i-ord('z')+ord('a')-1
   print(chr(i),end="")      
       
