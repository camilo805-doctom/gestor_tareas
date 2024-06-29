import sqlite3

def completar_tarea():
    with sqlite3.connect("C:\Users\POWER\gestor_tareas\gestor.db") as completar:
        try:
            consulta_cursor = completar.cursor()
            tarea_completada = str(input("Ingrese el titulo de la tarea completada: "))
            consulta_cursor.execute("SELECT * FROM Agregar_tarea WHERE Titulo = ?", (tarea_completada,))
            consulta_cursor.execute("UPDATE Agregar_tareas SET Completada = 1 Where Titulo = ?",(tarea_completada,))
            completar.commit()
            print("tarea marcada como completada")
        except ValueError as error:
            print(f"Error de digitacion: {error}")