﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs()->dict:
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    modelo = {
        "grafo": None,
        "puntos_encuentro": None
    }

    modelo["grafo"] = gr.newGraph(
        datastructure='ADJ_LIST',
        directed=False,
        size=240000
    )

    modelo["puntos_encuentro"] = mp.newMap(
        numelements=240000,
        maptype='PROBING'
        )

    return modelo

# Funciones para agregar informacion al modelo

def load_data(data_structs:dict, filename_tracks:str, filename_individuals:str)->dict:
    """
    Función para cargar los datos de lo archivos al modelo
    """

    grafo = data_structs["grafo"]
    puntos_encuentro = data_structs["puntos_encuentro"]

    tracks_archivo = open(filename_tracks, "r", encoding="utf-8")
    registro =  tracks_archivo.readline().replace("\n", "").split(",")
    registro =  tracks_archivo.readline().replace("\n", "").split(",")
    while len(registro) > 1:
        location_long = str(round(float(registro[2]), 3)).replace("-", "m").replace(".", "p")
        location_lat = str(round(float(registro[3]), 3)).replace("-", "m").replace(".", "p")
        location_id = location_long + "_" + location_lat 
        individual_id = registro[9] + "_" + registro[8]
        punto_seguimiento = location_id + "_" + individual_id
        grafo = crear_vertice(grafo, punto_seguimiento)

        location_long = str(round(float(registro[2]), 4)).replace("-", "m").replace(".", "p")
        location_lat = str(round(float(registro[3]), 4)).replace("-", "m").replace(".", "p")
        location_id = location_long + "_" + location_lat 
        individual_id = registro[9] + "_" + registro[8]
        punto_seguimiento = location_id + "_" + individual_id
        if not mp.contains(puntos_encuentro, location_id):
            lista = lt.newList("ARRAY_LIST")
            lt.addLast(lista, punto_seguimiento)
            mp.put(puntos_encuentro, location_id, lista)
        else:
            lista = me.getValue(mp.get(puntos_encuentro, location_id))
            if not lt.isPresent(lista, punto_seguimiento):
                lt.addLast(lista, punto_seguimiento)
                mp.put(puntos_encuentro, location_id, lista)
                grafo = crear_vertice(grafo, location_id)
        registro =  tracks_archivo.readline().replace("\n", "").split(",")
    tracks_archivo.close()

    for key in mp.keySet(puntos_encuentro):
        if lt.size(me.getValue(mp.get(puntos_encuentro, key))) < 2:
            mp.remove(puntos_encuentro, key)

    data_structs["grafo"] = grafo
    data_structs["puntos_encuentro"] = puntos_encuentro

    return data_structs

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

# Funciones auxiliares

def crear_vertice(grafo, nombre_vertice: str):

    if not gr.containsVertex(grafo, nombre_vertice):
        gr.insertVertex(grafo, nombre_vertice)

    return grafo

def crear_arco(grafo, nombre_vertice_1: str, nombre_vertice_2:str, peso: float):
    gr.addEdge(grafo, nombre_vertice_1, nombre_vertice_2, peso)
    return grafo