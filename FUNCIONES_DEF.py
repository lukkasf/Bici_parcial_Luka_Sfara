import os
from decimal import Decimal

# VALIDADORAS

def validar_lista(lista: list) -> bool:
    """Valida si el argumento dado es una lista.

    Args:
        lista (list): La lista a validar.

    Returns:
        bool: True si la lista es válida, False de lo contrario.
    """
    if not isinstance(lista, list):
        raise TypeError("ERROR: Se esperaba una lista")
    return True

def validar_entero(entero: int) -> bool:
    """Valida si el argumento dado es un entero.

    Args:
        entero (int): El entero a validar.

    Returns:
        bool: True si el entero es válido, False de lo contrario.
    """
    if not isinstance(entero, int):
        raise(TypeError("ERROR: Se esperaba un entero"))
    return True
    
def validar_lista_no_vacia(lista: list) -> bool:
    """Valida si la lista dada no está vacía.

    Args:
        lista (list): La lista a validar.

    Returns:
        bool: True si la lista no está vacía, False de lo contrario.
    """
    if not len(lista) == 0:
        raise(ValueError("ERROR: La lista NO está vacía"))
    return True

def validar_lista_vacia(lista: list) -> bool:
    """Valida si la lista dada está vacía.

    Args:
        lista (list): La lista a validar.

    Returns:
        bool: True si la lista está vacía, False de lo contrario.
    """
    if not len(lista) > 0:
        raise(ValueError("ERROR: La lista está vacía"))
    return True

def validar_bool(valor: bool) -> bool:
    """Valida si el argumento dado es un booleano.

    Args:
        valor (bool): El booleano a validar.

    Returns:
        bool: True si el valor es un booleano, False de lo contrario.
    """
    if not isinstance(valor, bool):
        raise(TypeError("ERROR: Se esperaba un booleano"))
    return True

def validar_str(valor: str) -> bool:
    """Valida si el argumento dado es una cadena de texto.

    Args:
        valor (str): La cadena de texto a validar.

    Returns:
        bool: True si el valor es una cadena de texto, False de lo contrario.
    """
    if not isinstance(valor, str):
        raise(TypeError("ERROR: Se esperaba una cadena de texto"))
    return True

# --------------------------------------------------------------------------
# LISTAS

def mostrar_lista(lista: list) -> None:
    """Muestra los elementos de la lista.

    Args:
        lista (list): La lista a mostrar.
    """
    if validar_lista(lista):
        for el in lista:
            print(el, end=" ")
        print()

def filtrar_lista(filtradora, lista: list) -> list:
    """Filtra los elementos de la lista según una función dada.

    Args:
        filtradora: La función utilizada para filtrar.
        lista (list): La lista a filtrar.

    Returns:
        list: La lista filtrada.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            aux = []
            for ele in lista:
                if filtradora(ele):
                    aux.append(ele)
            return aux

def swapeadora_de_listas(parametro, lista: list) -> None:
    """Intercambia los elementos de una lista según un parámetro.

    Args:
        parametro: El parámetro utilizado para comparar los elementos.
        lista (list): La lista a ordenar.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if parametro(lista[i], lista[j]):
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def cargar_lista_enteros_random(lista: list, cantidad: int, desde: int, hasta: int) -> None:
    """Carga la lista con enteros aleatorios.

    Args:
        lista (list): La lista a cargar.
        cantidad (int): La cantidad de enteros a generar.
        desde (int): El valor mínimo del rango de generación.
        hasta (int): El valor máximo del rango de generación.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            if validar_entero(cantidad) and validar_entero(desde) and validar_entero(hasta):
                from random import randint
                for _ in range(cantidad):
                    lista.append(randint(desde, hasta))

def crear_lista_enteros_random(cant: int, desde: int, hasta: int) -> list:
    """Crea una lista de enteros aleatorios.

    Args:
        cant (int): La cantidad de enteros a generar.
        desde (int): El valor mínimo del rango de generación.
        hasta (int): El valor máximo del rango de generación.

    Returns:
        list: La lista de enteros aleatorios creada.
    """
    validar_entero(cant, desde, hasta)
    lista = []
    cargar_lista_enteros_random(lista, cant, desde, hasta)
    return lista

def mapear_lista(procesadora, lista: list) -> list:
    """Mapea los elementos de la lista según una función dada.

    Args:
        procesadora: La función utilizada para procesar los elementos.
        lista (list): La lista a mapear.

    Returns:
        list: La lista resultante del mapeo.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            lista_retorno = []
            for el in lista:
                lista_retorno.append(procesadora(el))
            return lista_retorno
    
def totalizar_lista(lista: list) -> int:
    """Calcula la suma total de los elementos de la lista.

    Args:
        lista (list): La lista a totalizar.

    Returns:
        int: La suma total de los elementos.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            total = 0
            for elem in lista:
                total += elem
            return total

def calcular_promedio(lista: list) -> int:
    """Calcula el promedio de los elementos de la lista.

    Args:
        lista (list): La lista de la cual se calculará el promedio.

    Returns:
        int: El promedio de los elementos de la lista.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            promedio = totalizar_lista(lista) / len(lista)
            return promedio

def calcular_mayor_in_lista(lista: list) -> float:
    """Calcula el mayor elemento en la lista.

    Args:
        lista (list): La lista de la cual se calculará el mayor elemento.

    Returns:
        float: El mayor elemento de la lista.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            elemento_mayor = lista[0]
            for elm in lista:
                if elm > elemento_mayor:
                    elemento_mayor = elm
            return elemento_mayor
    
def calcular_menor_in_lista(lista: list) -> float:
    """Calcula el menor elemento en la lista.

    Args:
        lista (list): La lista de la cual se calculará el menor elemento.

    Returns:
        float: El menor elemento de la lista.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            elemento_menor = lista[0]
            for elm in lista:
                if elm < elemento_menor:
                    elemento_menor = elm
            return elemento_menor

def entero_in_lista(lista: list, target: int) -> bool:
    """Verifica si un entero está presente en la lista.

    Args:
        lista (list): La lista en la que se buscará.
        target (int): El entero a buscar.

    Returns:
        bool: True si el entero está presente en la lista, False de lo contrario.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            if validar_entero(target):
                for elem in lista:
                    if elem == target:
                        return True
                return False

def buscar_in_lista(lista: list, target: int) -> int:
    """Busca un elemento en la lista y devuelve su índice si se encuentra.

    Args:
        lista (list): La lista en la que se buscará.
        target (int): El elemento a buscar.

    Returns:
        int: El índice del elemento si se encuentra, -1 si no se encuentra.
    """
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            esta = -1
            for i in range(len(lista)):
                if lista[i] == target:
                    esta = i
                    break
            return esta

def contar_in_lista(lista: list, target: int) -> int:
    """Cuenta cuántas veces aparece un elemento en la lista.

    Args:
        lista (list): La lista en la que se contará.
        target (int): El elemento a contar.

    Returns:
        int: El número de veces que aparece el elemento en la lista.
    """
    if validar_lista(lista):
        if validar_entero(target):
            if validar_lista_no_vacia(lista):
                contador = 0
                for elem in lista:
                    if elem == target:
                        contador += 1
                return contador

def sorteador(lista: list) -> None:
    """Selecciona aleatoriamente un índice de la lista.

    Args:
        lista (list): La lista de la cual se seleccionará el índice.

    Returns:
        None
    """
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            from random import randint
            i = randint(0, len(lista))
            return i

def ordenar_lista_ascendente(lista: list) -> None:
    """Ordena la lista en orden ascendente.

    Args:
        lista (list): La lista a ordenar.

    Returns:
        None
    """
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] > lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def ordenar_lista_descendente(lista: list) -> None:
    """Ordena la lista en orden descendente.

    Args:
        lista (list): La lista a ordenar.

    Returns:
        None
    """
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] < lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def ordenar_lista(lista: list, tipo: bool) -> None:
    """Ordena la lista en orden ascendente o descendente según el tipo.

    Args:
        lista (list): La lista a ordenar.
        tipo (bool): True para orden ascendente, False para orden descendente.

    Returns:
        None
    """
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            if validar_bool(tipo):
                if tipo == True:
                    ordenar_lista_ascendente(lista)
                else:
                    ordenar_lista_descendente(lista)

def promediar_listas(lista_a: list, lista_b: list, lista_promedios: list) -> None:
    """Calcula el promedio de dos listas y los almacena en otra lista.

    Args:
        lista_a (list): La primera lista.
        lista_b (list): La segunda lista.
        lista_promedios (list): La lista donde se almacenarán los promedios.

    Returns:
        None
    """
    if validar_lista(lista_a) and validar_lista(lista_b) and validar_lista(lista_promedios): 
        if validar_lista_no_vacia(lista_a) and validar_lista_no_vacia(lista_b):
            if validar_lista_vacia(lista_promedios):
                for i in range(len(lista_a)):
                    num_1 = lista_a[i]
                    num_2 = lista_b[i]
                    prom = calcular_promedio(num_1, num_2)
                    lista_promedios.append(prom)

def for_each_lista(funcion: int, lista: list) -> None:
    """Aplica una función a cada elemento de la lista y actualiza la lista.

    Args:
        funcion (int): La función a aplicar.
        lista (list): La lista a modificar.

    Returns:
        None
    """
    if validar_entero(funcion):
        if validar_lista(lista):
            nueva_lista = []
            if validar_lista(lista):
                for el in lista:
                    nueva_lista.append(funcion(el))
                lista[:] = nueva_lista

def reduce_lista(funcion, lista):
    None

def ordenar_lista(criterio, lista: list) -> None:
    pass

def busqueda_binaria(target: int, lista: list) -> int:
    """Busca un elemento en una lista ordenada usando el algoritmo de búsqueda binaria.

    Args:
        target (int): El elemento a buscar.
        lista (list): La lista ordenada en la que se buscará.

    Returns:
        int: El índice del elemento si se encuentra, -1 si no se encuentra.
    """
    if validar_entero(target):
        if validar_lista(lista):
            inf = 0
            sup = len

def filtrar_lista(filtradora: int, lista: list) -> list:
    """Filtra los elementos de la lista según una función dada.

    Args:
        filtradora (int): La función utilizada para filtrar.
        lista (list): La lista a filtrar.

    Returns:
        list: La lista filtrada.
    """
    if validar_entero(filtradora):
        if validar_lista(lista):    
            aux = []
            for ele in lista:
                if filtradora(ele):
                    aux.append(ele)
            return aux

def mapear_lista(procesadora: int, lista: list) -> list:
    """Mapea los elementos de la lista según una función dada.

    Args:
        procesadora (int): La función utilizada para procesar los elementos.
        lista (list): La lista a mapear.

    Returns:
        list: La lista resultante del mapeo.
    """
    if validar_entero(procesadora):
        if validar_lista(lista):
            lista_retorno = []
            for elm in lista:
                lista_retorno.append(procesadora(elm))
            return lista_retorno
        
def mapear_campo(lista: list, campo: str) -> list:
    """Mapea un campo específico de los elementos de la lista.

    Args:
        lista (list): La lista de la cual se extraerán los campos.
        campo (str): El nombre del campo a extraer.

    Returns:
        list: Una lista con los valores del campo especificado.
    """
    if validar_lista(lista):
        if validar_str(campo):
            lista_retorno = []
            for el in lista:
                lista_retorno.append(el[campo])
            return lista_retorno

def continuar():
    """Pausa la ejecución y espera a que el usuario presione una tecla."""
    input("Presione una tecla para continuar...")

def enter():
    """Imprime una línea en blanco."""
    print()

def limpiar_terminal():
    """Limpia la pantalla de la terminal."""
    if os.name == 'nt':
        os.system('cls')

def convertir_a_float(lista: list) -> list:
    """Convierte los elementos de una lista a valores de punto flotante.

    Args:
        lista (list): La lista a convertir.

    Returns:
        list: La lista convertida a valores de punto flotante.
    """
    if validar_lista(lista):
        lista_convertida = []
        for elemento in lista:
            lista_convertida.append(Decimal(elemento))
        return lista_convertida

def get_path_actual(nombre_archivo: str):
    """Obtiene la ruta completa de un archivo en el directorio actual.

    Args:
        nombre_archivo (str): El nombre del archivo.

    Returns:
        str: La ruta completa del archivo.
    """
    if validar_str(nombre_archivo):
        directorio_actual = os.path.dirname(__file__)
        return os.path.join(directorio_actual, nombre_archivo)

def abrir_csv(nombre_archivo: str):
    """Abre un archivo CSV y lee su contenido.

    Args:
        nombre_archivo (str): El nombre del archivo CSV.

    Returns:
        list: Una lista con los datos del archivo CSV.
    """
    if validar_str(nombre_archivo):
        with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        datos = [linea.strip().split(",") for linea in lineas]
        return datos

def guardar_csv_mayusculas(nombre_archivo: str, datos: list):
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

def cargar_json(nombre_archivo: str):
    """Carga los datos de un archivo JSON.

    Args:
        nombre_archivo (str): El nombre del archivo JSON.

    Returns:
        list: Los datos del archivo JSON.
    """
    if validar_str(nombre_archivo):
        import json
        with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    return datos

def guardar_json(datos: list, nombre_archivo: str):
    """Guarda los datos proporcionados en un archivo JSON.

    Args:
        datos (list): Los datos a guardar en el archivo JSON.
        nombre_archivo (str): El nombre del archivo JSON.
    """
    if validar_str(nombre_archivo):
        import json
        with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
    
def imprimir_lista(lista):
    for elemento in lista:
        print(' '.join(map(str, elemento)))
#----------------------------------------------------------------

# lista = [2,4,6,8,32,44,53,128,35]
# for_each_lista(lambda a : a * 2,lista)
# print(lista)

# numeros = [5,7,8,9,7,5,43]

# # try:
# #     swapeadora_de_listas(lambda a , b : a > b ,lista)
# # except TypeError as e:
# #     print(e)

# # print(lista)

# numeros = [5,7,8,9,7,5,43]

# lista = mapear_lista(lambda impares : impares * 2, filtrar_lista(lambda n : n % 2 != 0, numeros))

# print(lista)
