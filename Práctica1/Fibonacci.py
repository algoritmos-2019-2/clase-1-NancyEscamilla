num = int(input("¿Cuantos terminos necesitas?"))
x=0
y=1
for i in range(num):
   print(x)
   t=y #Se va haciendo un bucle
   y=x+y #Def una función para la sucesión
   x=t  #Tomando valores de f(n-1) + f(n-2)
