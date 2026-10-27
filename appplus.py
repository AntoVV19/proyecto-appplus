# appplus.py - v1.0
def mostrar_menu():
    print("\n--SISTEMA DE GESTIÓN DE TAREAS V1.0--")
    print("1. Agregar tarea con prioridad")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese prioridad (Alta/Media/Baja): ")
            tareas.append({"desc": tarea, "prio": prioridad})
            print("Tarea registrada correctamente.")

        elif opcion == "2":
            print("\n--Lista de Tareas--")
            for idx, t in enumerate(tareas, 1):
                print(f"{idx}. [{t['prio']}] {t['desc']}")

        elif opcion == "3":
            try:
                idx = int(input("Número de tarea a eliminar: ")) - 1
                if 0 <= idx < len(tareas):
                    eliminada = tareas.pop(idx)
                    print(f"Tarea '{eliminada['desc']}' eliminada.")
                else:
                    print("Índice no válido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()