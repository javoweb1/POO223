print("Hola mundo")
nombre="Juan"
apellido='Perez'
edad=22
estatura=1.66
print(nombre[0])
print(nombre[0:3])
print(nombre[2:])
#Listas o Arreglos
unalista=[22,33,44,55]
unalista[2] = 123
print(unalista)
#Tupla
unatupla=(66,77,88,99)
#unatupla[2]=123
print("Escribe tu nombre")
estudiante = input("DEsde el input doy instrucciones")
edad = int(input("Ingresa tu edad"))
print("El año próximo tendrás "+ str(edad+1)+ "años")
if(edad<=18):
    print("Es menor de edad")
else:
    print("Es mayor de edad")
    if(edad>65):
            print("Es mayor de edad")
i=0
while(i<20):
    print("Es uyn ciclo"+ str(i))
    if(i==10):
        print("Es igual a 10")
    i = i+1
#FAQ
for elemento in unalista:
    print(elemento)
        