from bisect import bisect
import socket
from secrets import token_bytes
from pyDes import des, CBC, PAD_PKCS5
import binascii





p=10343
a=8941
clave=int(input("Ingrese su clave privada: "))
cpublica=(a**clave)%p
print("La clave publica del servidor es: ",cpublica)
cservidor=int(input("Ingrese la clave puclica del cliente: "))
puerto=(cservidor**clave)%p

KEY= 'mHAxsLYz'
def des_decrypt(s):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de





SERVER_ADDRESS = '127.0.0.1'

  
SERVER_PORT = puerto
    
s = socket.socket()

  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((SERVER_ADDRESS, SERVER_PORT))


s.listen(5)

print("Escuchando en la dirección %s. Detenga el servidor con Ctrl-C" %
str((SERVER_ADDRESS, SERVER_PORT)))

print("Enviando mensaje del archivo de texto")
# Listo, ahora comenzamos a escuchar y capturar los datos que nos envíen los clientes
seguir=True
while seguir:
    c, addr = s.accept()
    print("\nConexion recibida desde %s" % str(addr))

    while seguir:
        data = c.recv(2000)
        print("Inormacion recibida '%s' desde el cliente" % data)

        print(data)

        mensaje_des=des_decrypt(data)

        enviado=mensaje_des.decode()

        archivo_enviar = open ('mensajerecibido.txt','w')
        archivo_enviar.write(enviado)
        archivo_enviar.close()

        c.close()

        seguir= False

