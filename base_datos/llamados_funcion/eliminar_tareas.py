
# impotamos "sqlite3" para manejar la base de datos

import sqlite3

def eliminar_tareas():

    # Establecemos la conexión a la base de datos usando el contexto 'with' para asegurar el cierre correcto

    with sqlite3.connect("C:/Users/POWER/gestor.db") as eliminar:
        try:

            # Obtenemos un cursor para ejecutar las consultas SQL

            consulta_cursor = eliminar.cursor()

            # Solicitamos al usuario el título de la tarea que desea eliminar

            usuario_eliminar = str(input("Ingresa el titulo del recordatorio que desees eliminar: "))

            # Solicitamos al usuario el ID de la tarea que desea eliminar

            eliminar_contenido = int(input("Ingresa el ID de la tarea: "))

            # Eliminamos la tarea de la tabla 'Agregar_tareas' basada en el título proporcionado

            consulta_cursor.execute("DELETE FROM Agregar_tareas WHERE Titulo = ? ",(usuario_eliminar))

            # Eliminamos la tarea de la tabla 'Agregar_tareas' basada en el ID proporcionado

            consulta_cursor.execute("DELETE FROM Agregar_tareas WHERE TareaID = ?",(eliminar_contenido))

             # Confirmamos (commit) la transacción para guardar los cambios en la base de datos

            eliminar.commit()

            print("Datos eliminados correctamente")

        except ValueError as error:

            # Capturamos y manejamos cualquier excepción de tipo ValueError

            print(f"Error de digitacion: {error}")