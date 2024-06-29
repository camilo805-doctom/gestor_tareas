import sqlite3
import pandas as pd

def ver_tareas():
    with sqlite3.connect("C:/Users/POWER/gestor.db") as mostrar_tarea:
        consulta_cursor = mostrar_tarea.cursor()
        consulta_cursor.execute("SELECT * FROM Agregar_tareas")
        resultado = consulta_cursor.fetchall()
    resultado_df = pd.DataFrame(resultado)
    print(resultado_df)