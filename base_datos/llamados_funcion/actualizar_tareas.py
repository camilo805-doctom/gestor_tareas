
# impotamos "sqlite3" para manejar la base de datos

import sqlite3

def actualizar_tareas():

    # Establecemos la conexión a la base de datos usando el contexto 'with' para asegurar el cierre correcto

    with sqlite3.connect("C:/Users/POWER/gestor.db") as actualizar:
        try:

            # Obtenemos un cursor para ejecutar las consultas SQL

            consulta_cursor = actualizar.cursor()

            # Solicitamos al usuario el título de la tarea que desea actualizar

            usuario_titulo = str(input("Ingrese el titulo del recordatorio: "))

            # Solicitamos al usuario la nueva información para la tarea

            actualizar_contenido = str(input("Ingrese nueva informacion a la tarea: "))

            # Verificamos si la tarea con el título proporcionado existe en la tabla 'Agregar_tareas'

            consulta_cursor.execute("SELECT * FROM Agregar_tareas WHERE Titulo = ?",(usuario_titulo,))

            # Actualizamos la tarea con la nueva información proporcionada

            consulta_cursor.execute("UPDATE Agregar_tareas SET Tareas = ? WHERE Titulo = ?",(actualizar_contenido, usuario_titulo))

            # Confirmamos (commit) la transacción para guardar los cambios en la base de datos

            actualizar.commit()
            print("Datos actualizados")

        except ValueError as error:

            # Capturamos y manejamos cualquier excepción de tipo ValueError
            
            print(f"Error de digitacion: {error} ")
    