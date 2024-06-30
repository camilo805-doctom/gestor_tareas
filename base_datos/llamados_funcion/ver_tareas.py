
# impotamos "sqlite3" para manejar la base de datos

import sqlite3

# importamos "oandas" para visualizar la tabla con mas claridad

import pandas as pd


def ver_tareas():

     # Establecemos la conexión a la base de datos usando el contexto 'with' para asegurar el cierre correcto

    with sqlite3.connect("C:/Users/POWER/gestor.db") as mostrar_tarea:

        # Obtenemos un cursor para ejecutar las consultas SQL

        consulta_cursor = mostrar_tarea.cursor()

        # Ejecutamos la consulta SQL para obtener todas las tareas de la tabla 'Agregar_tareas'

        consulta_cursor.execute("SELECT * FROM Agregar_tareas")

        # Obtenemos todos los resultados de la consulta

        resultado = consulta_cursor.fetchall()
    
     # Convertimos el resultado en un DataFrame de pandas para una mejor visualización

    resultado_df = pd.DataFrame(resultado)

    # Imprimimos el DataFrame
    
    print(resultado_df)