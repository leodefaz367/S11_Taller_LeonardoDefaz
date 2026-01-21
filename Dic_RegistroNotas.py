notas = {}

def agregarNota(notas, materia, nota):
    notas[materia] = nota

def verNotas(notas):
    if not notas:
        print("No hay notas")
    else:
        for materia, nota in notas.items():
            print(materia, ":", nota)

def editarNota(notas, nuevaNota):
    materia = input("Materia: ")
    if materia in notas:
        notas[materia] = nuevaNota
        print("Nota actualizada")
    else:
        print("La materia no existe")

def eliminarNota(notas, materia):
    if materia in notas:
        notas.pop(materia)
        print("Nota eliminada")
    else:
        print("La materia no existe")

def menuNotas():
    while True:
        print("\nMENU")
        print("1. Agregar nota")
        print("2. Ver notas")
        print("3. Editar nota")
        print("4. Eliminar nota")
        print("5. Salir")

        opcion = int(input("Opcion: "))

        match opcion:
            case 1:
                materia = input("Materia: ")
                nota = float(input("Nota: "))
                agregarNota(notas, materia, nota)
                print("Nota guardada")

            case 2:
                verNotas(notas)

            case 3:
                nuevaNota = float(input("Nueva nota: "))
                editarNota(notas, nuevaNota)

            case 4:
                materia = input("Materia a eliminar: ")
                eliminarNota(notas, materia)

            case 5:
                print("Fin del programa")
                break

            case _:
                print("Opcion invalida")

menuNotas()
