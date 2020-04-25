from pyDes import *
import base64
import sys
import matplotlib.pyplot as plt

image_base64en = ""

def encrypt():
    ruta = input("Ingrese la ruta, nombre y extension de la imagen: ")
    image = open(ruta, 'rb') # Se crea un archivo de modo lectura que contiene la imagen
    image_read = image.read() # Se lee la imagen convirtiendola en su representacion en bytes
    print("Cifrando imagen, espere por favor")
    image_encrypt = initDES.encrypt(image_read) 

    if image_read != image_encrypt:
        print("Imagen cifrada!!!")
    else:
        print("Error cifrando")
        sys.exit()

    input("Codificando en Base64, presione Enter para continuar")
    image_base64en = base64.b64encode(image_encrypt)

    if image_encrypt != image_base64en:
        print("Imagen codificada en Base64: \n\n", image_base64en, "\n")
    else:
        print("Error codificando en base64 la imagen cifrada")
        sys.exit()

    return image_base64en


def decrypt(image_base64en):
    #aux = input("Ingrese texto de la imagen cifrada y codifica en base 64 u oprima Enter para continuar con la imagen cifrada anteriormente: ")
    if image_base64en == "":
        print("Error, realice el cifrado primero o ingrese el texto de la imagen cifrada y codificada en Base64")
        sys.exit()
    #elif aux != "":
    #    image_base64en = aux

    input("Decodificando Imagen en Base64, presione Enter para continuar")
    image_base64dec = base64.b64decode(image_base64en)

    if image_base64en != image_base64dec:
        print("Imagen decodificada desde Base64")
    else:
        print("Error decodificando la imagen cifrada")
        sys.exit()

    print("Descifrando imagen, espere por favor")
    image_decrypt = initDES.decrypt(image_base64dec)

    if image_base64dec != image_decrypt:
        print("Imagen descifrada!!!")
    else:
        print("Error descifradando")
        sys.exit()

    ruta = input("Ingrese la ruta, nombre y extension donde desea que se guarde la imagen: ")
    image_result = open(ruta, 'wb') # Se crea archivo de modo escritura que contendra la imagen resultante
    image_result.write(image_decrypt) # Se guarda la informacion de la imagen desencriptada

    print("Imagen generada en la ruta especificada, ya puede terminar el programa.\n")

print ("DES")
key = input("Ingrese la clave (El tamaño tiene que ser de exactamente 8 bytes): ") # Se requieren 8 bytes para DES
initDES = des(key, CBC, "\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5) # Segun documentacion: Class initialization
while(1):
    accion = int(input(" 1.Cifrar \n 2.Descifrar \n 3.Terminar \n"))
    if accion == 1:
        image_base64en = encrypt()
    elif accion == 2:
        decrypt(image_base64en)
    elif accion == 3:
        exit()
    else:
        print("Elija una opción adecuada")