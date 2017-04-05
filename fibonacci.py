def fibonacci(n):
 t=f+s 
 f=s
 s=t
 if i<=n:
  i+=1
  print(t,'\t')
  fibonacci(n)
 else:
  print ("end") 
f=0
s=1
print ("first",n,"fibonacci numbers are",f,'\t',s,'\t')
n=int(input("enter limit"))
fibonacci(n)
