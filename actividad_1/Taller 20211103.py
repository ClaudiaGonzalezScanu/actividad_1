"""Aprendiendo condicionales en Python"""
Pepe = 13
Juanito = 15
if Pepe > Juanito:
    print("Pepe es mayor que Juanito")
elif Pepe == Juanito:
    print("Pepe es igual a Juanito")
else:
    print("Ninguna de las condiciones anteriores se cumple") 
Maria = "final de condicion"
color = 216
if color == 216:
    print("el color es 216")
#aprendiendo bucles
a,b = 0,1
while b <= 10:
    print(b)
    a,b = b,a+b
"""Contando el contenido de una variable con el bucle for"""
mensaje = "Hola queridas compañeras"
for posicion,contenido in enumerate(mensaje):
       print(posicion, contenido)
numeros =[0,1,2,3,4]
for i in numeros:
    print(i)
    if i!=0:
        print(i)
    else:
     print("no llegue a ejecutarme")
#aprendiendo una función en Python con la serie fibonachi
def fibonachi(numeros):
    a,b = 0,1
    resultado = [] #esto es un array vacio
    while b < numeros:
        resultado.append(b)
        a,b = b,a+b
    return resultado
#invocando a la función fibonachi
print(fibonachi(20))



    
    