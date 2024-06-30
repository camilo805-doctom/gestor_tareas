
# impotamos "sqlite3" para manejar la base de datos

import sqlite3

def completar_tarea():

    # Establecemos la conexión a la base de datos usando el contexto 'with' para asegurar el cierre correcto

    with sqlite3.connect("C:/Users/POWER/gestor.db") as completar:
        try:

            # Obtenemos un cursor para ejecutar las consultas SQL

            consulta_cursor = completar.cursor()

            # Solicitamos al usuario el título de la tarea que desea marcar como completada

            tarea_completada = str(input("Ingrese el titulo de la tarea completada: "))

            # Verificamos si la tarea con el título proporcionado existe en la tabla 'Agregar_tarea'

            consulta_cursor.execute("SELECT * FROM Agregar_tarea WHERE Titulo = ?", (tarea_completada,))

            # Actualizamos la tarea marcándola como completada (1)

            consulta_cursor.execute("UPDATE Agregar_tareas SET Completada = 1 Where Titulo = ?",(tarea_completada,))

            # Confirmamos (commit) la transacción para guardar los cambios en la base de datos

            completar.commit()
            print("tarea marcada como completada")
            
        except ValueError as error:

            # Capturamos y manejamos cualquier excepción de tipo ValueError

            print(f"Error de digitacion: {error}")