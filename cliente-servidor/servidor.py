import socket

HOST = "127.0.0.1"
PORT = 5002

# Crear socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Enlazar IP y puerto
    servidor.bind((HOST, PORT))
    servidor.listen()
    print("Servidor esperando conexión...")

    # Aceptar conexión
    conexion, direccion = servidor.accept()
    print(f"Conexión establecida desde {direccion}")

    # Recibir datos
    data = conexion.recv(1024).decode()
    print("Mensaje recibido:", data)

    # Enviar respuesta
    respuesta = "Mensaje recibido correctamente"
    conexion.sendall(respuesta.encode())

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar conexiones
    conexion.close()
    servidor.close()
    print("Servidor cerrado")