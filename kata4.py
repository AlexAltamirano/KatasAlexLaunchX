# Ejercicio 1: Transformar cadenas
#Hay varias operaciones que puedes realizar en las cadenas cuando las manipulamos. 
#En este ejercicio, usarás métodos de cadena para modificar el texto con hechos sobre la Luna 
#y luego extraerás información para crear un breve resumen.
#Nota Dedica unos minutos a tratar de encontrar una solución. 
#Luego desplázate hacia abajo hasta la parte inferior para ver si has logrado compilar 
# el programa de acuerdo con las especificaciones.
text = """Interesting facts about the Moon. 
The Moon is Earth's only satellite. 
There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. 
This yearly drift is not significant enough to cause immediate effects on Earth. 
The highest daylight temperature of the Moon is 127 C."""

# Primero, divide el texto en cada oración para trabajar con su contenido:
parts = text.split('\n')

# Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
key_words=["average", "temperature" , "distance"]

# Crea un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
for item in parts:
    for key_word in key_words:
        if key_word in item:
            print(item)
            break

# Cambiar C a Celsius
for item in parts:
    for key_word in key_words:
        if key_word in item:
            print(item.replace(' C', ' Celsius'))
            break

# Ejercicio 2: Formateando Cadenas
#Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#Creamos titulo
titulo = "Gravity on " + name + " and " + planet
print(titulo.title())

#Multilinea
facts = f"""{'-'*80}
Nombre del planeta: {planet}
gravedad en {name}: {gravity*1000} m/s^2"""

#Union de cadenas
template = f"""{titulo.title()} {facts}"""
print(facts)

#Nuevos datos
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

#Comprobamos
print(facts)

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))