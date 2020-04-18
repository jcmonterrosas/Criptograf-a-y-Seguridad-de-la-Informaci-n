import numpy as np
from numpy.linalg import inv

def rotacion(Matriz, Sentido):
    aux = [fila[:] for fila in Matriz]
    longitud = len(Matriz)
    if Sentido:
        for i in range(0,longitud):
            for j in range(0,longitud):
                aux[i][j] = Matriz[longitud-1-j][i]
        return aux
    else:
        for i in range(0,longitud):
            for j in range(0,longitud):
                aux[longitud-1-j][i] = Matriz[i][j]
        return aux

def validar (celda,matriz):
    valido = 0
    if(matriz[celda[0]][celda[1]]!=1):
        valido = 1
        for i in range(4):
            matriz = np.rot90(matriz, k=1)
            matriz[celda[0]][celda[1]] = 1
    return valido, matriz

def nozeros(matriz,tam):
    valid = 1
    for i in range (tam):
        for j in range(tam):
            if(matriz[i][j]==0):
                valid = 0
                break
    return valid

def formatoMatriz(tamaño):
    Matriz = np.empty([tamaño, tamaño], dtype=str)
    aux = np.zeros((tamaño,tamaño))
    valid = 0
    if(tamaño%2!=0):
        med = int(tamaño/2)
        aux[med][med] = 1
    numcelda = 0
    print("\n Ingrese ubicacion de los hoyos: ")
    while(valid==0):
        celda = [int(input("Fila: "))-1,int(input("Columna: "))-1]
        v,aux = validar(celda,aux)
        if(v==0):
            print("La celda no es valida")
        else:
            Matriz[celda[0]][celda[1]] = 1
            numcelda += 1
        valid = nozeros(aux,tamaño)

    Matriz = list(Matriz)
    for i in range(len(Matriz)):
        Matriz[i] = list(Matriz[i])
        for j in range(len(Matriz[i])):
            Matriz[i][j] = int(Matriz[i][j]) if Matriz[i][j] != '' else 0

    return Matriz

def cifrar():
    tamaño = int(input("Ingrese el tamaño de la reticula : "))
    Sentido = int(input("Ingrese el sentido de la rotacion : "))
    mensaje = list(input("Ingrese mensaje : ").upper().replace(" ", ""))
    Matriz = formatoMatriz(tamaño)
    n = len(Matriz)
    T = [[0]*n for i in range(n)]
    o = 0
    for k in range(0,4):
        for i in range(0,n):
            for j in range (0,n):
                if Matriz[i][j] == 1:
                    T[i][j] = mensaje[o]
                    o += 1
        Matriz = rotacion(Matriz, Sentido)
    
    cifrado = ""
    for i in range(0,n):
        for j in range(0,n):
            cifrado += T[i][j]
    
    print("Texto cifrado : " + cifrado + "\n")  

def descifrar():
    tamaño = int(input("Ingrese el tamaño de la reticula : "))
    Sentido = int(input("Ingrese el sentido de la rotacion : "))
    mensaje = list(input("Ingrese mensaje : ").upper().replace(" ", ""))
    Matriz = formatoMatriz(tamaño)
    n = len(Matriz)
    T = [[0]*n for i in range(n)]
    k = 0
    for i in range(0,n):
        for j in range(0,n):
            T[i][j] = mensaje[k]
            k+=1
    
    texto = ""
    for k in range(0,4):
        for i in range(0,n):
            for j in range(0,n):
                if Matriz[i][j] == 1:
                    texto = texto + T[i][j]
        Matriz = rotacion(Matriz, Sentido)
    
    print("Texto plano : " + texto + "\n")  

print ("Turning Matriz")
while(1):
    accion = int(input(" 1.Cifrar \n 2.Descifrar \n 3.Terminar \n"))
    if accion == 1:
        cifrar()
    elif accion == 2:
        descifrar()
    elif accion == 3:
        exit()
    else:
        print("Elija una opción adecuada")

#### Parametros para probar
# Coordenadas: [1,1] [3,2] [3,4] [4,3]
# Tamaño de la reticula: 4
# Sentido: 0
# # Mensaje: JIM ATTACKS AT DAWN


# Mensaje encriptado: JKTDSAATWIAMCNAT
