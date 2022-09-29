# Al comenzar la carrera, obtendremos varias opciones, para el vehículo.
# 1.- Ingresar ubicación GPS, LATITUD
# 2.- Ingresar ubicación GPS, LONGITUD
# 3.- Encender el vehículo.
# 4.- Acelerar vehículo
# 5.- Apagar Vehículo
# 6.- Girar Vehículo.
#SHORTCUTS MAS UTILIZADOS VSCODE
# CTRL K + C
lat_ini = input("Ingrese Latitud inicial")
lon_ini = input("Ingrese Longitud inicial")
encendido = False
velocidad = 0

def encenderapagar():
    global encendido
    encendido = not(encendido)
    print("El estado del vehiculo es: " + str(encendido))

def acelerar():
    global velocidad
    velocidad = velocidad + 10
    print("La velocidad del vehiculo es: " + str(velocidad))
def finCarrera():
    lat_fin = input("Ingrese Latitud final")
    lon_fin = input("Ingrese Longitud final")
    #ACA REALIZA EL CALCULO
    
encenderapagar()
encenderapagar()
encenderapagar()
encenderapagar()
encenderapagar()
acelerar()
acelerar()
acelerar()
acelerar()

