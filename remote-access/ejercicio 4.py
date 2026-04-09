import pickle

class Auto:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __repr__(self):
        return f"El auto {self.modelo} tiene placa {self.placa}"

# Crear objetos
autos = [
    Auto("Mazda", "ABC123"),
    Auto("Mercedes", "ABC153"),
    Auto("BMW", "ABC113"),
    Auto("Foton", "ABC143"),
    Auto("Maserati", "ABC124")
]

try:
    # Guardar lista de autos
    with open("autos.pkl", "wb") as archivo:
        pickle.dump(autos, archivo)
    print("Autos guardados correctamente")

    # Leer lista de autos
    with open("autos.pkl", "rb") as archivo:
        autos_recuperados = pickle.load(archivo)

    print("Autos recuperados:")

    for auto in autos_recuperados:
        print(auto)

except Exception as e:
    print("Error:", e)