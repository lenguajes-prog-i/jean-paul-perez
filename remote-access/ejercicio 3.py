import pickle

class Auto:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __repr__(self):
        return f"El auto {self.modelo} tiene placa {self.placa}"

# Crear objetos
auto = Auto("Mazda", "ABC123")
auto1 = Auto("Mazda1", "ABC153")
auto2 = Auto("Mazda2", "ABC113")
auto3 = Auto("Mazda3", "ABC143")
auto4 = Auto("Mazda4", "ABC124")

try:
    # Guardar un objeto
    with open("autos.pkl", "wb") as archivo:
        pickle.dump(auto, archivo)
    print("Auto guardado correctamente")

    # Leer objeto
    with open("autos.pkl", "rb") as archivo:
        auto_recuperado = pickle.load(archivo)

    print("Auto recuperado:")
    print(auto_recuperado)

except Exception as e:
    print("Error:", e)