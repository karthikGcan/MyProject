def recur_fibo(n,dict = {}): 
   #n = int(n) 
   #if not isinstance(n,int):
       #raise TypeError("Invalid input")
   if n < 2:
       return n

   elif n not in dict:
       dict[n] = recur_fibo(n-1) + recur_fibo(n-2)
   return dict[n]
#nterms = 10
   #for i in range(nterms):
#print(recur_fibo(nterms))

