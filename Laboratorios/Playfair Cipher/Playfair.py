def clave():   
    clave = input("Ingrese la clave : ").upper().replace(" ", "")
    clave_ordenada = [] #Ingresar clave para ordenarla
    for caracter in clave: 
        if caracter not in clave_ordenada:
            if caracter == 'J':
                clave_ordenada.append('I')
            else:
                clave_ordenada.append(caracter)
    
    #Modificar el alfabeto segun la clave
    alfabeto = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    clave_ordenada.extend([e for e in alfabeto if e not in clave_ordenada])

    k = 0 #Rellenar matriz
    for i in range(0,5): 
        for j in range(0,5):
            matriz[i][j] = clave_ordenada[k]
            k += 1
            
def cifrar():        
    mensaje = input("Ingrese mensaje : ").upper().replace(" ", "")
    mensaje = [x for x in mensaje]
    for j in range(0 ,len(mensaje) + 1, 2): #Si un par de letras son iguales, la ultima se reemplaza por una X
        if j < len(mensaje) - 1:
            if mensaje[j] == mensaje[j + 1]:
                mensaje.insert(j + 1, 'X')

    if len(mensaje)%2 != 0: #Si el mensaje tiene una longitud impar, al final se agrega una X 
        mensaje.append('X')

    cifrado = []
    i = 0
    while i < len(mensaje): #Realizacion del algoritmo de cifrado
        caracter1 = []
        caracter1 = ubicacion(mensaje[i])
        caracter2 = []
        caracter2 = ubicacion(mensaje[i+1])
        if caracter1[0] == caracter2[0]: #Si los caracteres estan en la mismas fila
            #Se tiene en cuenta el modulo 5 para hacer las posiciones de la matriz ciclicas, es decir, para que el indice siguiente a 5, vuelva a ser 1
            cifrado.append(matriz[ caracter1[0] ][ (caracter1[1] + 1) % 5 ])
            cifrado.append(matriz[ caracter2[0] ][ (caracter2[1] + 1) % 5 ])
            cifrado.append(" ") 
        elif caracter1[1] == caracter2[1]: #Si los caracteres estan en la misma columna
            cifrado.append(matriz[ (caracter1[0] + 1) % 5 ][ caracter1[1] ])
            cifrado.append(matriz[ (caracter2[0] + 1) % 5 ][ caracter2[1] ])
            cifrado.append(" ")
        else: #Si los caracteres estan en diferentes posiciones
            cifrado.append(matriz[ caracter1[0] ][ caracter2[1] ])
            cifrado.append(matriz[ caracter2[0] ][ caracter1[1] ])
            cifrado.append(" ") 
        i = i + 2

    print("Texto cifrado : " + ''.join(map(str, cifrado)) )       
                 
def descifrar():  #descifrarion
    mensaje = input("Ingrese el texto cifrado : ").upper().replace(" ", "")

    texto = []
    i=0
    while i < len(mensaje): #Realizacion del algoritmo de descifrado
        caracter1 = []
        caracter1 = ubicacion(mensaje[i])
        caracter2 = []
        caracter2 = ubicacion(mensaje[i+1])
        if caracter1[0] == caracter2[0]: #Si los caracteres estan en la mismas fila
            texto.append(matriz[ caracter1[0] ][ (caracter1[1] - 1) % 5 ])
            texto.append(matriz[ caracter2[0] ][ (caracter2[1] - 1) % 5 ])
            texto.append(" ")
        elif caracter1[1] == caracter2[1]: #Si los caracteres estan en la misma columna
            texto.append(matriz[ (caracter1[0] - 1) % 5 ][ caracter1[1] ])
            texto.append(matriz[(caracter2[0] - 1 ) % 5][ caracter2[1] ])
            texto.append(" ")
        else: #Si los caracteres estan en diferentes posiciones
            texto.append(matriz[ caracter1[0] ][ caracter2[1] ])
            texto.append(matriz[ caracter2[0] ][ caracter1[1] ])
            texto.append(" ")  
        i = i + 2     

    print("Texto plano : " + ''.join(map(str, texto)) )       

def ubicacion(caracter): #Ubicacion de cada caracter en la matriz
    posicion = []
    if caracter == 'J':
        caracter = 'I'
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == caracter:
                posicion.append(i)
                posicion.append(j)
                return posicion

print ("Playfair")
matriz = [[0 for i in range(5)] for j in range(5)] #Inicializar la matriz 5*5
accion = int(input(" 1.Cifrar \n 2.Descifrar \n"))
clave()
if accion == 1:
    cifrar()
elif accion == 2:
    descifrar()
else:
    print("Elija una opción adecuada")

#### Parametros para propar
# clave: yoanpiz
# Mensaje para encriptar: this secret message is encrypted
# Mensaje para desencriptar: zo mh lc hy zk mn so nq dl kt oq cy ki ec lk so yi eq pq rx ey kr wm ns dl gy ld gf ab ya qn ye ap gn ix pg hy ys nb ht ec tl kf vn rp yt pu pf cy eb ya wm ki mp lf uz lh tc yh np ck kl ly yt ki gb dh cy ec rd gn cl go ih ye ty ki xo uy vn sc lx kf mx pw

# WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP