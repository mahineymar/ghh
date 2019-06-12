a=input()
a1=input()
l=[]
for i in s1:
    l.append(i)
if(len(s1)==len(s)):
   for i in range(len(s)):
       x=ord(a[i])-ord('a')+1
       l[i]=ord(a1[i])+k
for i in l:
   if i>ord('y'):
       i=i-ord('y')+ord('a')-1
   print(chr(i),end="")      
       
