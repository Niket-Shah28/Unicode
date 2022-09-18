def binary(n1,n2):
    d={}
    for i in range(n1,n2):
      a=[]
      f=[]
      k=0
      count=0
      while (i!=0):
         f.append(i)
         l=i%2
         a.append(l)
         count=count+1
         i=int (i/2)
      for j in range(0,count-1):
        if a[j]==1 and a[j+1]==1:
            break

        j=j+1
      if j==count-1:
         d.update({f[k]:bool(0)})
      else:
         d.update({f[k]:bool(1)})  
      k=k+1  
    return d
a={}
print("Enter two numbers:")   
n1=int (input()) 
n2=int (input())
a=binary(n1,n2)
print(a)
