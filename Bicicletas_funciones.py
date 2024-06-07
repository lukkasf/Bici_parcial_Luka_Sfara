from FUNCIONES_DEF import *


def guardar_csv(nombre_archivo: str, datos: list):
    """Guarda los datos proporcionados en un archivo CSV, convirtiendo todas las letras a mayúsculas.

    Args:
        nombre_archivo (str): El nombre del archivo CSV.
        datos (list): Los datos a guardar en el archivo CSV.
    """
    if validar_str(nombre_archivo):
        with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
            for fila in datos:
                linea = ",".join(fila) + "\n"
                archivo.write(linea)

bicicletas_lista = abrir_csv("bicicletas.csv")

def asignar_tiempo(bicicletas_lista):
    import random
    for bicicleta in bicicletas_lista[1:]:
        tiempo = random.randint(50, 120)
        bicicleta[-1] = str(tiempo)
    return bicicletas_lista

def mostrar_lista_sin_corchetes(lista: list) -> None:
    """
    Imprime los datos de la lista de bicicletas sin los corchetes y con la velocidad.

    Args:
        lista (list): La lista de bicicletas.

    Returns:
        None
    """
    for fila in lista:
        elementos_fila = []
        for elemento in fila:
            elementos_fila.append(str(elemento))
        print(" ".join(elementos_fila))

def mostrar_lista_sin_velocidades(lista: list) -> None:
    """
    Imprime los datos de la lista de bicicletas sin los corchetes y sin la velocidad.

    Args:
        lista (list): La lista de bicicletas.

    Returns:
        None
    """
    for fila in lista:
        elementos_fila = []
        for i, elemento in enumerate(fila):
            if i != 3:  # Excluir la velocidad (índice 3)
                elementos_fila.append(str(elemento))
        print(" ".join(elementos_fila))


bicicletas_lista = asignar_tiempo(bicicletas_lista)

def ganador(bicicletas_lista: list) -> None:
    """
    Determina al ganador de la carrera y muestra su nombre y tiempo.

    Args:
        bicicletas_lista (list): La lista de bicicletas en formato [id_bike, nombre, tipo, tiempo].

    Returns:
        None
    """
    menor_tiempo = float('inf')
    nombres_ganadores = []
    for bicicleta in bicicletas_lista:
        if bicicleta[0] == 'id_bike':
            continue
        tiempo_actual = int(bicicleta[-1])
        if tiempo_actual < menor_tiempo:
            menor_tiempo = tiempo_actual
            nombres_ganadores = [bicicleta[1]]
        elif tiempo_actual == menor_tiempo:
            nombres_ganadores.append(bicicleta[1])

    if len(nombres_ganadores) == 1:
        print(f"El ganador es {nombres_ganadores[0]} con un tiempo de {menor_tiempo} minutos.")
    else:
        nombres = ", ".join(nombres_ganadores)


def filtrar_por_tipo(bicicletas_lista: list, tipo_bicicleta: str) -> list:
    """
    Filtra las bicicletas de la lista según el tipo especificado.

    Args:
        bicicletas_lista (list): La lista de bicicletas en formato [id_bike, nombre, tipo, tiempo].
        tipo_bicicleta (str): El tipo de bicicleta a filtrar.

    Returns:
        list: Una lista con las bicicletas del tipo especificado.
    """
    bicicletas_filtradas = []
    for bicicleta in bicicletas_lista:
        if bicicleta[2] == tipo_bicicleta:
            bicicletas_filtradas.append(bicicleta)
    return bicicletas_filtradas


def promedio_por_tipo(bicicletas_lista: list) -> dict:
    """
    Calcula el promedio de tiempo por cada tipo de bicicleta.

    Args:
        bicicletas_lista (list): La lista de bicicletas en formato [id_bike, nombre, tipo, tiempo].

    Returns:
        dict: Un diccionario con el promedio de tiempo por tipo de bicicleta.
    """
    tipos = {}
    for bicicleta in bicicletas_lista[1:]:
        tipo = bicicleta[2]
        tiempo = int(bicicleta[3])  
        if tipo in tipos:
            tipos[tipo][0] += tiempo
            tipos[tipo][1] += 1
        else:
            tipos[tipo] = [tiempo, 1]

    promedios = {}
    for tipo, (total_tiempo, cantidad) in tipos.items():
        promedios[tipo] = total_tiempo / cantidad

    return promedios


def ordenamiento_tipo_tiempo(bicicletas_lista: list) -> list:
    """
    Ordena la lista de bicicletas primero por tipo y luego por tiempo ascendente.

    Args:
        bicicletas_lista (list): La lista de bicicletas en formato [id_bike, nombre, tipo, tiempo].

    Returns:
        list: La lista de bicicletas ordenadas por tipo y tiempo.
    """
    if bicicletas_lista[0][0] == 'id_bike':
        bicicletas_lista = bicicletas_lista[1:]

    for i in range(len(bicicletas_lista)):
        for j in range(i + 1, len(bicicletas_lista)):
            if bicicletas_lista[i][2] > bicicletas_lista[j][2] or (bicicletas_lista[i][2] == bicicletas_lista[j][2] and int(bicicletas_lista[i][3]) > int(bicicletas_lista[j][3])):
                bicicletas_lista[i], bicicletas_lista[j] = bicicletas_lista[j], bicicletas_lista[i]

    return bicicletas_lista

ordenamiento = ordenamiento_tipo_tiempo(bicicletas_lista)

guardar_json(ordenamiento, "Ordenamiento.json")