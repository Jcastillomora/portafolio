# Lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Definir la función hacer_grandioso()
def hacer_grandioso(nombre):
    # Verificar si el nombre es el de un mago
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        # Agregar la frase "El gran " al principio del nombre del mago
        return "El gran " + nombre
    else:
        # Si no es un mago, devolver el nombre original
        return nombre

# Definir la función imprimir_nombres()
def imprimir_nombres(nombres):
    # Imprimir cada nombre en una línea separada
    for nombre in nombres:
        print(nombre)


# Separar los nombres en los tres grupos
magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        # Si es un mago, agregarlo a la lista de magos
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        # Si es un científico, agregarlo a la lista de científicos
        cientificos.append(nombre)
    else:
        # Si no es un mago ni un científico, agregarlo a la lista de otros
        otros.append(nombre)

# Aplicar la función hacer_grandioso() a los magos
magos_grandiosos = []
for mago in magos:
    mago_grandioso = hacer_grandioso(mago)
    magos_grandiosos.append(mago_grandioso)

# Imprimir los nombres en cada grupo
print("Nombres completos:")
print("*********************")
imprimir_nombres(nombres)
print("*********************")
print("Magos grandiosos:")
imprimir_nombres(magos_grandiosos)
print("*********************")
print("Científicos:")
imprimir_nombres(cientificos)
print("*********************")
print("Otros:")
imprimir_nombres(otros)
print("*********************")
