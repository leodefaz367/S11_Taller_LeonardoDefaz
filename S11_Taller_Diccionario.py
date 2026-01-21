# 1. Declarar el diccionario con clave y valor de los países y capitales de América Latina
print("Declarar paises y capitales en un diccionario")
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Bolivia": "Sucre",
    "Brasil": "Brasilia",
    "Chile": "Santiago"
}
print(paises_capitales)

# 2. Acceder a un valor del diccionario
print("\nAcceso del valor")
print(paises_capitales["Argentina"])

# 3. Agregar un elemento al diccionario
print("\nAgregar elemento")
paises_capitales["Peru"] = "Lima"
print(paises_capitales)

# 4. Modificar un elemento del diccionario
print("\nModificar elemento")
paises_capitales["Argentina"] = "B. Aires"
print(paises_capitales)

# 5. Eliminar un elemento del diccionario
print("\nEliminar elemento")
paises_capitales.pop("Brasil")
print(paises_capitales)

# 6. Eliminar un elemento con popitem
print("\nEliminar con popitem")
paises_capitales.popitem()
print(paises_capitales)

# 7. Usando listas, asignar valores según el índice
print("\nUso de listas")
lista = ["Argentina", "Bolivia", "Brasil", "Chile"]
diccionario = {
    lista[0]: "Buenos Aires",
    lista[1]: "Sucre",
    lista[2]: "Brasilia",
    lista[3]: "Santiago"
}
print(diccionario)

# 8. Acceder por índice y por clave
print("\nAcceso por indice y clave")
print(diccionario[lista[1]])     # Por índice
print(diccionario["Argentina"])  # Por clave

# Mostrar valores
for valor in diccionario.values():
    print(valor)

# 9. Crear diccionario jugador con diferentes tipos de datos
print("\nJugador")
jugador = {
    "nombre": "Alexis",
    "apellido": "Chasi",
    "edad": 19,
    "partidosJugados": 4,
    "partidosGanados": 2
}
print(jugador)

# 10. Agregar clave-valor con lista
print("\nValor tipo lista")
jugador["detalleAnios"] = [2020, 2022, 2025]
print(jugador)

# 11. Agregar clave-valor con diccionario
print("\nValor tipo diccionario")
jugador["detalleAnios"] = {
    "temporadas": [2020, 2021, 2022, 2023, 2024]
}
print(jugador)

# 12. Consultar claves
print("\nClaves del diccionario")
for clave in jugador.keys():
    print(clave)

# 13. Consultar valores
print("\nValores del diccionario")
for valor in jugador.values():
    print(valor)

# 14. Longitud del diccionario
print("\nLongitud del diccionario")
print(len(jugador))
#15. Recorrer e imprimir claves

print("\nRecorrer e imprimir claves")
for clave in jugador.keys():
    print(clave)

# 16. Recorrer e imprimir clave y valor
print("\nRecorrer con items")
for clave, valor in jugador.items():
    print(clave, ":", valor)

# 17. Diccionario de divisas
print("======Diccionario de divisas=====")

monedas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}

moneda = input("Ingrese una divisa: ")

if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está")

# 18. Diccionario USUARIO
print( "======Diccionario USUARIO=====")
persona = {}

persona["nombre"] = input("Nombre: ")
persona["edad"] = input("Edad: ")
persona["direccion"] = input("Direccion: ")
persona["telefono"] = input("Telefono: ")

print(
    persona["nombre"], "tiene", persona["edad"], "años, vive en",
    persona["direccion"], "y su numero de telefono es",
    persona["telefono"]
)


