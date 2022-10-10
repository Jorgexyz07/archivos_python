# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

#SIEMPRE se debe importar el módulo csv para trabajar con archivos


import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    #1° Abrimos el archivo

    csvfile = open(archivo, "r")   #archivo es la variable donde se guardo "stock.csv"
                                   #"r" indica solamente lectura
    
    #2° Creamos una lista que contenga todos los datos del archivo 

    stock = list(csv.DictReader(csvfile))  

    #3° Cierro el archivo

    csvfile.close()    

    #Inicio la actividad solicitada

    cant_tornillos = 0  #Creo la variable que se usará para contar los tornillos
    cant_tuercas = 0
    cant_arandelas = 0

    for x in stock:     #Creo un bucle para recorrer el diccionario stock

        cant_tornillos += int(x["tornillos"])   #voy sumando la cantidad de tornillos con x y la key tornillos
        cant_tuercas += int(x["tuercas"])       #voy sumando la cantidad de tuercas con x y la key tuercas
        cant_arandelas += int(x["arandelas"])   #voy sumando la cantidad de arandelas con x y la key arandelas

    print("La cantidad total de tornillos es:", cant_tornillos)
    print("La cantidad total de arandelas es:", cant_arandelas)
    print("La cantidad total de tuercas es:", cant_tuercas)


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    #1° Abrimos el archivo

    csvfile = open("propiedades.csv", "r")  #Podría omitir "r" ya que por default viene ese método

    #2° Creamos una lista que contenga todos los datos del archivo

    depto = list(csv.DictReader(csvfile))

    #3° Cierro el archivo

    csvfile.close()

    #Inicio la actividad

    cant_2_amb = 0      #Creo mi contador para cantidad de 2 ambientes
    cant_3_amb = 0      #Creo mi contador para cantidad de 3 ambientes

    for x in range(len(depto)):     #Creo el bucle para recorrer el archivo
        datos = depto[x]            #Creo una variable que almacenará los datos del diccionario depto

        try:                        #Intento acceder a cada fila de ambientes para convertirlas a int si están llenas
            cant_amb = int(datos.get("ambientes"))   #Si la fila esta llena, convierto la expresión a un tipo int
            if cant_amb == 2:                       #Pregunto si la cantidad de ambientes es 2
                cant_2_amb += 1                     #Voy agregando 1 al contador
            elif cant_amb == 3:                   #Repito el procedimiento con 3 ambientes
                cant_3_amb += 1   
            else:
                pass
        except:                     #Si la fila está vacía continua sin que se rompa el programa
            print("La fila", x+2, "está vacía")    #Notifico que fila del archivo para la columna ambientes está vacía
                                                   #+2 debido a que la primera es el encabezado y luego empieza con 0

    print("Hay", cant_2_amb, "departamentos de dos ambientes.")
    print("Hay", cant_3_amb, "departamentos de tres ambientes.")
        




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
