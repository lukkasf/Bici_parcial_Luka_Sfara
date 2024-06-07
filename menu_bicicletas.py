from Bicicletas_funciones import *
from time import sleep

salir = False
flag_velocidades = True

while not salir:
    print("           Carrera")
    print("1. Imprimir bicicletas")
    print("2. Tiempo de la carrera")
    print("3. Ganador de la carrera")
    print("4. Seleccione tipo de Bicicleta")
    print("5. Promedio de tiempos por tipo")
    print("6. Mostrar posiciones")
    print("7. Guardar posiciones")
    print("8. Salir")
    enter()
    opcion = input("Opcion: ")

    match opcion:
        case '1':
            if flag_velocidades:
                mostrar_lista_sin_velocidades(bicicletas_lista)
            else:
                mostrar_lista_sin_corchetes(bicicletas_lista)
            continuar()
            limpiar_terminal()
        case '2':
            bicicletas_lista = asignar_tiempo(bicicletas_lista)
            print("Tiempos asignados correctamente.")
            flag_velocidades = False
            continuar()
            limpiar_terminal()
        case '3':
            ganador(bicicletas_lista)
            continuar()
            limpiar_terminal()
        case '4':
            while True:
                tipo_seleccionado = input("Ingrese el tipo de bicicleta a filtrar (BMX, MTB, PLAYERA, PASEO): ")
                if tipo_seleccionado in {"BMX", "MTB", "PLAYERA", "PASEO"}:
                    bicicletas_filtradas = filtrar_por_tipo(bicicletas_lista, tipo_seleccionado)
                    imprimir_lista(bicicletas_filtradas)
                    guardar_csv(f"{tipo_seleccionado}.csv", bicicletas_filtradas)
                    print(f"Bicicletas del tipo '{tipo_seleccionado}' guardadas en {tipo_seleccionado}.csv'") 
                    break
                else:
                    print("Tipo de bicicleta no válido. Por favor, ingrese uno de los siguientes tipos: BMX, MTB, PLAYERA, PASEO")
            continuar()
            limpiar_terminal()
        case '5':
            promedios = promedio_por_tipo(bicicletas_lista)
            for tipo, promedio in promedios.items():
                print(f"Promedio de tiempo para {tipo}: {promedio} minutos")
            continuar()
            limpiar_terminal()
        case '6':
            ordenamiento = ordenamiento_tipo_tiempo(bicicletas_lista)
            for bicicleta in ordenamiento:
                print(bicicleta)
            continuar()
            limpiar_terminal()
        case '7':
            guardar_json(ordenamiento, "Ordenamiento.json")
            print("Posiciones guardadas en 'Ordenamiento.json'")
            continuar()
            limpiar_terminal()
        case '8':
            enter()
            print("Cerrando")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            salir = True
        case _:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")