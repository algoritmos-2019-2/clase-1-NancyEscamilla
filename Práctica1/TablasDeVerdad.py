booleanos = [False, True]

#Tabla or
print ('x/ty/tx or y')  #Los \t son tabuladores
for x in booleanos:
  for y in booleanos:
     print(x, y, x or y, sep = '/t')

print()


#Tabla and 
print('x/ty/tx and y')
for x in booleanos:
   for y in booleanos:
      print (x, y, x and y, sep = '/t')

print()

#Tabla not
print('x/tnot x')
for x in booleanos:
  print(x, not x,sep = '/t')

print() 
