import pickle

# Datos a serializar
datos = {"mensaje": "Hola"}

try:
    # Serialización
    datos_serializados = pickle.dumps(datos)
    print("Datos serializados:", datos_serializados)

    # Deserialización
    datos_recuperados = pickle.loads(datos_serializados)
    print("Datos recuperados:", datos_recuperados)

except Exception as e:
    print("Error:", e)