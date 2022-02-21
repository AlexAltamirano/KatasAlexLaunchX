# Ejercicio1 - Utilizar operadores aritméticos
Tierra = 149597870
Júpiter = 778547200

# Distancia entre ambos
Dist = Tierra - Júpiter
print(abs(Dist))
millas = Dist * 0.621
print(abs(round(millas)))

# Ejercicio 2: convierte cadenas en números y usa valores absolutos
# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")
P1 = input("Ingresa distancia del planeta 1: ")
P2 = input("Ingresa distancia del planeta 2: ")

# Convierte las cadenas de ambos planetas a números enteros
P1 = int(P1)
P2 = int(P2)

# Realizar el cálculo y determinar el valor absoluto
dist_p = abs(P1 - P2)
print(dist_p)

# Convertir de KM a Millas
VM= dist_p * 0.621
print(VM)
