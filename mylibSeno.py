def factorial(n):
    if n == 0:
       return 1
    else
       return n * factorial(n-1)



def seno(x, n):
       i == 0
       suma = 0
       while i <n:
               aux = 2*i + 1
               suma = ((-1)**i/factorial(aux))*x**aux + suma
               i +=1
       return suma
      
print(seno(0,6))


def coseno(x, n):
      i = 0
      suma = 0
      while i <n:
              aux = 2*1
              suma = ((-1)**aux/factorial(aux))*x**aux + suma
              i +=1
      return suma

print(coseno(0,6))


def mult(e,lista):
         new=[]
         for i in lista:
               new.append(i*e)
         return new
print(mult(2., [2,3,4]))

