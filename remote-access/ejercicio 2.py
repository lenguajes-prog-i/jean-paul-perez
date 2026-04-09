import pickle

# Datos del estudiante
datos = {
    "nombre": "Cortes Perez Andres Steven",
    "materia": "Lenguaje de Programacion I",
    "notas": [1, 2.5, 2.5, 3],
}

try:
    # Guardar datos en archivo (serialización)
    with open("data.pkl", "wb") as archivo:
        pickle.dump(datos, archivo)
    print("Datos guardados correctamente")

    # Leer datos del archivo (deserialización)
    with open("data.pkl", "rb") as archivo:
        datos_estudiantes = pickle.load(archivo)

    print("Datos recuperados:")
    print(datos_estudiantes)

except Exception as e:
    print("Error:", e)