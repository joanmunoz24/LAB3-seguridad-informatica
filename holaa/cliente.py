import socket
from secrets import token_bytes
from pyDes import des, CBC, PAD_PKCS5
import binascii
 
archivo = open ('mensajeentrada.txt','r')
mensaje = archivo.read()
archivo.close()

KEY= 'mHAxsLYz'
def des_encrypt(s):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


p=10343
a=8941
clave=int(input("Ingrese su clave privada: "))
cpublica=(a**clave)%p
print("La clave publica del cliente es: ",cpublica)
cservidor=int(input("Ingrese la clave puclica del servidor: "))
puerto=(cservidor**clave)%p


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = puerto


c = socket.socket()

c.connect((SERVER_ADDRESS, SERVER_PORT))


print("Conectado al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))

data=des_encrypt(mensaje.encode())


# Enviamos


c.send(data)

data = c.recv(2000)


c.close()
