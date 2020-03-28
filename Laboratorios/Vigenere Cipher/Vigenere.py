import sys

def formatoClave(mensaje):#Esta funcion da el formato que requiere el cifrado vigenere a la clave   
    clave = input("Ingrese la clave : ").upper().replace(" ", "")
    if not clave.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    if len(mensaje) == len(clave): #Si la clave es igual de larga al mensaje no es encesario repetirla
        return(clave) 
    else: #Si no, se repite caracter a caracter tantas veces como la diferencia entre la longitud del mensaje y la clave
        for i in range(len(mensaje) - len(clave)): 
            clave += clave[i % len(clave)] #Se agrega al final de la clave el caracter correspondiente ciclicamente
    return(clave) 
    #alfabeto = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def cifrar():        
    mensaje = input("Ingrese mensaje : ").upper().replace(" ", "")
    if not mensaje.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    clave = formatoClave(mensaje)
    #Para el cifrado se utiliza la siguiente expresion algebraica: Cifrado[i] = (Mensaje[i] + Clave[i]) mod 26, para calcular el desplazamiento del caracter, luego se suma 65 que es el codigo ascii de la letra 'A' para ubicar el caracter correcto del alfabeto. 
    cifrado = ""
    for i in range(len(mensaje)): 
        #Se utiliza la funcion ord() que viene integrada en python para obtener el codigo ascii de cada caracter 
        aux = ((ord(mensaje[i]) + 
             ord(clave[i])) % 26) + 65
        cifrado += chr(aux) 
    
    print("Texto cifrado : " + cifrado )       
                 
def descifrar():  #descifrarion
    mensaje = input("Ingrese el texto cifrado : ").upper().replace(" ", "")
    if not mensaje.isalpha(): #Si los caracteres ingresados no son alfabeticos, se termina el programa
        print("Ingrese solo caracteres del alfabeto")
        sys.exit()
    clave = formatoClave(mensaje)
    #Para el descifrado se utiliza la siguiente expresion algebraica: Di = (Ei - Ki + 26) mod 26, el resto del procedimiento es igual que en el cifrado.
    texto = ""
    for i in range(len(mensaje)): 
        aux = ((ord(mensaje[i]) - 
             ord(clave[i]) + 26) % 26) + 65
        texto += chr(aux)

    print("Texto plano : " + texto )       

print ("Vigenere")
accion = int(input(" 1.Cifrar \n 2.Descifrar \n"))
if accion == 1:
    cifrar()
elif accion == 2:
    descifrar()
else:
    print("Elija una opción adecuada")

#### Parametros para propar
# clave: relations
# Mensaje: to be or not to be that is the question
# Mensaje encriptado: KSMEHZBBLKSMEMPOGAJXSEJCSFLZSY

# clave: CRYPTO
# Mensaje: THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME
# Mensaje encriptado: VYCGXWURQTVFGKNPLGCXCQXVKEBIASRZAINFGWPPFS