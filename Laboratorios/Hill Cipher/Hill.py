import sys
import numpy as np
from sympy import Matrix #Libreria externa, es necesario instalarla

#Valido solo para una clave que se pueda convertir en una matriz de 2x2
def formatoClave():
    clave = input("Ingrese la clave : ").upper().replace(" ", "")
    if not clave.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    clave = list(clave)
    for i in range(len(clave)): #Se convierte los caracteres de la calve en numeros, para poder operarlos
        clave[i] = int(ord(clave[i]) % 65)
    clave = np.reshape(np.array(clave),(2,2)) #Se convierte la clave en una matriz de 2x2
    return clave

def cifrar():
    mensaje = input("Ingrese mensaje : ").upper().replace(" ", "")
    if not mensaje.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    mensaje = list(mensaje)
    for i in range(len(mensaje)): #Se convierte los caracteres del mensaje en numeros, para poder operarlos
        mensaje[i] = int(ord(mensaje[i]) % 65) 
    mensaje = np.reshape(np.array(mensaje),(-1,2)) #Se convierte el mensaje en una matriz con una de sus dimenciones igual a 2, para poder operarla con la clave 
    clave = formatoClave()
    cifrado = np.reshape(np.dot(mensaje,clave),-1) #Se realiza la operacion cifrado = mensaje x clave y se convierte el resultado en un arreglo
    textoCifrado = ''

    for i in range(len(cifrado)): #Se convierte cada dato del arreglo al caracter correspondiente para formar el texto del mensaje cifrado 
        aux = (cifrado[i] % 26) + 65
        textoCifrado += chr(aux) 

    print("Texto cifrado : " + textoCifrado + " \n")  

def descifrar():
    mensaje = input("Ingrese mensaje : ").upper().replace(" ", "")
    if not mensaje.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    mensaje = list(mensaje)
    for i in range(len(mensaje)): #Se convierte los caracteres del mensaje en numeros, para poder operarlos
        mensaje[i] = int(ord(mensaje[i]) % 65)
    mensaje = np.reshape(np.array(mensaje),(-1,2)) #Se convierte el mensaje en una matriz con una de sus dimenciones igual a 2, para poder operarla con la clave 
    clave = Matrix(formatoClave()) #Se transforma el formato de la clave al necesario para utilizar lo necesario de la libreria sympy, en este caso "Matrix"
    clave_inv = clave.inv_mod(26) #Utilizando la implementacion de la libreria sympy, de la inversa modular, se consigue la inversa de la clave
    descifrado = np.reshape(np.dot(mensaje,clave_inv),-1) #Se realiza la operacion mensaje = cifrado x inversa_clave y se convierte el resultado en un arreglo
    textoPlano = ''

    for i in range(len(descifrado)):#Se convierte cada dato del arreglo al caracter correspondiente para formar el mensaje en texto plano 
        aux = (descifrado[i] % 26) + 65
        textoPlano += chr(aux) 

    print("Texto plano : " + textoPlano + " \n")  


print ("Hill")
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
# clave: lidh
# Mensaje: july
# Mensaje encriptado: DELW

# clave: lidh
# Mensaje: NUMBERTHEORYISEASY
# Mensaje encriptado: VKFZRVWTIAZSMISGKA

