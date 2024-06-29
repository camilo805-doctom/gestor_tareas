import sqlite3

def eliminar_tareas():
    with sqlite3.connect("C:/Users/POWER/gestor.db") as eliminar:
        try:
            consulta_cursor = eliminar.cursor()
            usuario_eliminar = str(input("Ingresa el titulo del recordatorio que desees eliminar: "))
            eliminar_contenido = int(input("Ingresa el ID de la tarea: "))
            consulta_cursor.execute("DELETE FROM Agregar_tareas WHERE Titulo = ? ",(usuario_eliminar))
            consulta_cursor.execute("DELETE FROM Agregar_tareas WHERE TareaID = ?",(eliminar_contenido))
            eliminar.commit()
            print("Datos eliminados correctamente")
        except ValueError as error:
            print(f"Error de digitacion: {error}")