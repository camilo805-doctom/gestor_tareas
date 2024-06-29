import sqlite3

def actualizar_tareas():
    with sqlite3.connect("C:\Users\POWER\gestor_tareas\gestor.db") as actualizar:
        try:
            consulta_cursor = actualizar.cursor()
            usuario_titulo = str(input("Ingrese el titulo del recordatorio: "))
            actualizar_contenido = str(input("Ingrese nueva informacion a la tarea: "))
            consulta_cursor.execute("SELECT * FROM Agregar_tareas WHERE Titulo = ?",(usuario_titulo,))
            consulta_cursor.execute("UPDATE Agregar_tareas SET Tareas = ? WHERE Titulo = ?",(actualizar_contenido, usuario_titulo))
            actualizar.commit()
            print("Datos actualizados")
        except ValueError as error:
            print(f"Error de digitacion: {error} ")
    