#namejo_cadenas.py
'''
Este es un programa que muestra el uso de
argumentos de la función print() en python
'''
# Realizado como parte del curso de Python  FundaLAB
print("""
****************************************************************************
PROGRAMA PARA MOSTRAR ARGUMENTOS DE LA FUNCION PRINT()
REALIZADO POR JESUS M BECERRA JUNIO - 2023
****************************************************************************
""")
print("""****************************************************************************
OPERACIONES CON CADENAS: COMILLAS SIMPLES, DOBLES Y CARACTERES DE ESCAPE \"\\\"
****************************************************************************
    """)
#aquí el argumento end=" " reemplaza el \n para que imprima en la misma línea el próximo print()
#tambien se emplea el ";" para una segunda instrucción de python aunque esto no se recomienda
#solo es con fines didácticos
print("01. Comillas simples => print('hola mundo') => ", end=" ") ; print('hola mundo')
print("02. Comillas dobles => print(\"Hola mundo\") => ", end=" ") ; print("hola mundo")
print("03. Comillas simples entre comillas dobles => print(\"hola 'mundo'\") =>", end=" ") ; print("hola 'mundo'")
print("04. Comillas dobles entre comillas simples => print('hola \"mundo\"') =>", end=" ") ; print('hola "mundo"')
print("05. Comillas simples entre comillas simples => print('hola \\\'mundo\\\'') => ", end=" ") ; print('hola \'mundo\'')
print("06. Comillas dobles entre comillas dobles => print (\"hola \\\"mundo\\\"\") => ", end=" ") ; print ("hola \"mundo\"")
#fin del programa
print("\n****************************************************************************")
print("fin del programa.....")
print("****************************************************************************")
