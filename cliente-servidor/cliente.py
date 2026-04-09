import socket

HOST = "192.168.137.1"
PORT = 5005

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectarse al servidor
    cliente.connect((HOST, PORT))
    print("Conectado al servidor")

    # Pedir mensaje al usuario
    mensaje = input("Ingrese mensaje: ")

    # Enviar mensaje
    cliente.sendall(mensaje.encode())

    # Recibir respuesta
    respuesta = cliente.recv(1024).decode()
    print("Respuesta del servidor:", respuesta)

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar conexión
    cliente.close()
    print("Conexión cerrada")