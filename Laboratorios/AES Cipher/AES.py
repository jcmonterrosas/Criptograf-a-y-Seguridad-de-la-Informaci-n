import pyaes
import hashlib
import base64
import sys

def execution(keySelect):
    password = str(input("Ingrese la clave: ")).encode('utf-8') # Unicode-objects must be encoded before hashing
    hashed = hashlib.sha256(password).digest() # Se utiliza un algoritmo hash para manejar la clave el cual retorna una cadena de caracteres de 32-bytes
    iv = "InitializationVe" # Para el modo de operacion OFB, se necesita un vector aleatoreo de inicializacion de 16-bytes
    if keySelect == 1: # Segun la preferencia del usuario, se modifica el tamaño de la llave a utilizar
        key = hashed[:16] # Del hash, se seleccionan 128 bits
    elif keySelect == 2:
        key = hashed[:24] # Del hash, se seleccionan 192 bits
    else: 
        key = hashed # Del hash, se seleccionan 256 bits

    aes = pyaes.AESModeOfOperationOFB(key, iv = iv) # Se inicializa el cifrado mediante el modo de operacion "Output Feedback"(OFB), puesto que este permite ingresar un texto plano de cualquier longitud, sin requerir de padding

    ruta = input("Ingrese la ruta, nombre y extension de la imagen: ") 
    image = open(ruta, 'rb') # Se crea un archivo de modo lectura que contiene la imagen
    image_read = image.read() # Se lee la imagen convirtiendola en su representacion en bytes

    print("Cifrando imagen, espere por favor")
    image_encrypt = aes.encrypt(image_read)

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

    input("Decodificando Imagen en Base64, presione Enter para continuar")
    image_base64dec = base64.b64decode(image_base64en)

    if image_base64en != image_base64dec:
        print("Imagen decodificada desde Base64")
    else:
        print("Error decodificando la imagen cifrada")
        sys.exit()

    #aes = pyaes.AESModeOfOperationCBC(key, iv = iv) # El modo de operacion CBC mantiene el estado, por lo cual se requiere crear una nueva instacion para descifrar 
    aes = pyaes.AESModeOfOperationOFB(key, iv = iv)

    print("Descifrando imagen, espere por favor")
    image_decrypt = aes.decrypt(image_base64dec)

    if image_decrypt == image_read:
        print("Imagen descifrada!!!")
    else:
        print("Error descifradando")
        sys.exit()

    ruta = input("Ingrese la ruta, nombre y extension donde desea que se guarde la imagen: ")
    image_result = open(ruta, 'wb') # Se crea archivo de modo escritura que contendra la imagen resultante
    image_result.write(image_decrypt) # Se guarda la informacion de la imagen desencriptada

    print("Imagen generada en la ruta especificada, ya puede terminar el programa.\n")

print ("AES")
while(1): 
    print("Selecione el modo de operación del algoritmo")
    accion = int(input(" 1) 128 bits \n 2) 192 bits \n 3) 256 bits \n 4) Terminar \n"))
    if accion == 1:
        execution(1)
    elif accion == 2:
        execution(2)
    elif accion == 3:
        execution(3)
    elif accion == 4:
        exit()
    else:
        print("Elija una opción adecuada")