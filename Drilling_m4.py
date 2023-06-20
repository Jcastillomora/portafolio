#Importacion de libreria csv
import csv
#Definicion de clases 
#Clase Vehiculo
class Vehiculo():
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self):
        archivo = open('vehiculos.csv', 'a', newline='')
        datos = [(self.__class__, self.__dict__)]
        clase = type(self)
        if clase == object:
            datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    #Cree un método que lea del archivo vehiculos.csv con el nombre leer_datos_csv(self) y que imprima por pantalla la clasificación del vehículo:

    def leer_datos_csv(self):
        with open('vehiculos.csv', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            datos = [(self.__class__, self.__dict__)]
            for fila in (lector_csv):
                clase = fila[0]
                clase = clase.replace("<class '__main__.", "")
                clase = clase.replace("'>", "")
                print("Lista de " + clase + ":")  
                print(fila[1])
                print("")
   
#Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc"
    
#Clase Particular que hereda de Auto
class Particular(Auto):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puestos = n_puestos
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, {self.n_puestos} puestos"
    
#Clase Carga que hereda de Auto
class Carga(Auto):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, {self.carga} kg"
    
#Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.n_ruedas} ruedas, {self.tipo}"
    
#Clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo, n_radios, cuadro, motor):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.n_radios = n_radios
        self.cuadro = cuadro
        self.motor = motor
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.n_ruedas} ruedas, {self.tipo}, {self.n_radios} radios, {self.cuadro}, {self.motor}"

#parte 1
#manejo de errores try except al ingreso de datos
lista_autos = []
try:
    n = int(input("Cuantos vehiculos desea insertar: "))
    for i in range(n):
        marca = input(f"Inserte la marca del automovil {i+1}: ")
        modelo = input("Inserte el modelo: ")
        n_ruedas = int(input("Inserte el numero de ruedas: "))
        velocidad = int(input("Inserte la velocidad: "))
        cilindrada = int(input("Inserte la cilindrada en cc: "))
        auto = Auto(marca, modelo, n_ruedas, velocidad, cilindrada)
        lista_autos.append(auto)
        print("")

except TypeError as error:
    print("Error, debe ingresar un numero entero...", type(error).__name__)

except ValueError as error:
    print("Error, debe ingresar un numero entero", type(error).__name__)

except Exception as error:
    print("Error desconocido", type(error).__name__)
    print("")

print("**"*50)
print("Imprimiendo por pantalla los Vehiculos: \n")
for i in range(n):
    print(f"El vehiculo {i+1} es un {lista_autos[i].marca} {lista_autos[i].modelo} con {lista_autos[i].n_ruedas} ruedas, {lista_autos[i].velocidad} km/h, {lista_autos[i].cilindrada} cc")
print("**"*50)

#se agregan las instancias del ejercicio, parte 2:
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

#mostrar las instancias
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

#verificar la relacion existente entre la clase Motocicleta con todas las clases anteriores
print("**"*50)
print("Motocicleta es instancia con relacion a Vehiculo: ",isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relacion a Auto: ",isinstance(motocicleta, Auto))
print("Motocicleta es instancia con relacion a Particular: ",isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relacion a Carga: ",isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relacion a Bicicleta: ",isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relacion a Motocicleta: ",isinstance(motocicleta, Motocicleta))
print("**"*50)
#parte 3, se guardan los siguientes objetos en un archivo csv
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)


lista_vehiculos = [particular, carga, bicicleta, motocicleta]
#con este ciclo guardamos los datos de cada instancia en el archivo csv
for instancia in lista_vehiculos:
    instancia.guardar_datos_csv()

#parte 4, se lee el archivo csv y se imprimen los datos
print(instancia.leer_datos_csv())




