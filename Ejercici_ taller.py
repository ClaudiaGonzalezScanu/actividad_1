#este es un programa, que pregunta tu nombre, apellido, edad, direccion, fecha de nacimiento
#correo electronico y telefono. ademas debe sumar edad y agno de nacimiento
nombre = input("Buen día, estoy completando tu ficha, por favor, dime tu nombre: ")
apellido = input("cual es tu apellido?")
direccion = input("podrias decir tu direccion?")
fecha_de_nacimiento = input("y tu fecha de nacimiento")
edad = int(input("Por favor, dime tu edad"))
correo_electronico = input("tu correo electroni es")
telefono = input("Por favor, dime tu telefono")
year = int(input("POR FAVOR DIME TU AÑO DE NACIMIENTO:"))
#a continuacion sumare el year y edad
def sumar(a, b):
    suma = a + b
    return suma
resultado = sumar(year, edad)
print("Los datos del formulario son:   " .format(resultado))
