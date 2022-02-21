# Ejercicio 1: Para este ejercicio, escribirás una lógica condicional 
# que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido. 
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, 
# y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
# Un asteroide se acerca, y viaja a una velocidad de 49 km/s
#Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
#Escribe una expresión de prueba para calcular si necesita una advertencia.
#Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
VelocidadAsteroide = 49 #km/s
VelocidadPeligro = 25 #Km/s
if VelocidadAsteroide >= VelocidadPeligro:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print("No hay peligro")

# Ejercicio 2:Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s,
#a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la lógica
#condicional que usa declaraciones if, else, y elif para alertar a las personas de 
#todo el mundo que deben buscar un asteroide en el cielo.¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!
#Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
#Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
#Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
Asteroide = 19 #Km/s
AsteroideVisible = 20 #Km/s
if Asteroide > AsteroideVisible:
    print("El asteroide es visible")
elif Asteroide < AsteroideVisible:
    print("El asteroide es visible")
else:
    print("El asteroide no es visible") 

# Ejercicio 3: Operadores and y or
#Los asteroides de menos de 25 metros 
#en su dimensión más grande probablemente se quemarán a medida que entren en la atmósfera de la Tierra.
#Si una pieza de un asteroide que es más grande que 25 metros pero más 
#pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
#También discutimos en el ejercicio anterior que:
#La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior 
# a 25 kilómetros por segundo (km/s) merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces 
# produce un rayo de luz que se puede ver desde la Tierra.
#Usando toda esta información, escribe un programa que emita la advertencia o información correcta a la gente de la Tierra, 
#según la velocidad y el tamaño de un asteroide. Utiliza instrucciones if, else, y elif, así como los operadores and y or.
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
AsteroideBase = 25 #Metros
TamañoMaximo = 1000 #Metros
Tamaño = 40
Velocidad = 25
if  Velocidad > 25 and Tamaño > 25:
    print("¡Advertencia! Meteoro extremadamente peligroso colisionara con la tierra y es visible desde el espacio")
elif Velocidad >= 20:
    print("Meteoro visible en el cielo")
elif Tamaño < 25:
    print("No hay problema")
else:
    print("No hay problema")

# Variacion
Tamaño2 = int(input("Tamaño del meteorito es: " ))
Velocidad2 = int(input("Velocidad del meteorito es: "))
if  Tamaño2 >= AsteroideBase:
    if Tamaño2 <= TamañoMaximo and Velocidad2 >= AsteroideVisible:
        if Velocidad2 > VelocidadPeligro:
            print("¡Advertencia! Meteoro extremadamente peligroso colisionara con la tierra y es visible desde el espacio")
        else:
            print("Meteoro grande visible acercandose pero no peligroso")
    else:
        print("Meteoro acercandose pero no es visible ni peligroso")
else:
    if Velocidad2 >= AsteroideVisible:
        if Velocidad2 > VelocidadPeligro:
            print ("¡Advertencia! Meteoro pequeño se acerca a la tierra y es visible en el espacio al igual que peligroso")
        else:
            print("Meteoro acercandose pero no es peligroso pero si visible")
    else:
        print("Meteoro pequeño acercandose, pero no es visible ni peligroso")