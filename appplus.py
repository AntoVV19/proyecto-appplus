# appplus.py - v1.0
def mostrar_menu():
    print("\n--SISTEMA DE GESTIÓN DE TAREAS V1.0--")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Exportar tareas a TXT")
    print("4. Salir")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la descripción de la tarea: ")
            tarea.append(tarea)
            print("Tarea agregada con exito.")

        elif opcion == "2":
            print("\n--Lista de Tareas--")
            for idx, t in enumerate(tareas, 1):
                print(f"{idx}.{t}")

        elif opcion == "3":
          with open("tareas.txt", "w") as f:
                for t in tareas:
                    f.write(f"{t}\n")
                    print("Tareas exportadas a 'tareas.txt'.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    