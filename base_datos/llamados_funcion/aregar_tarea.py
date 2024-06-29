import sqlite3

def agregar_tarea():
    with sqlite3.connect("C:\Users\POWER\gestor_tareas_2") as tarea:
        try:
            consulta_cursor = tarea.cursor()
            usuario_titulo = str(input("Ingrese el titulo de la tarea: "))
            contenido_tarea= str(input("ingrese el contenido de la tarea: "))
            fecha_vencimiento = str(input("ingrese la fecha de vencimiento (DD/MM/YY): "))
            prioridad_tarea = str(input("ingrese un nivel de prioridad: "))
            tarea_completada = int(input("ponga 0 si la tarea esta completada y 1 si no: "))
            consulta_cursor.execute("INSERT INTO Agregar_tareas (Tareas) VALUES (?,?,?,?,?)",(usuario_titulo,contenido_tarea,fecha_vencimiento,prioridad_tarea,tarea_completada))
            tarea.commit()
            print("Datos ingresados correctamente")
        except ValueError as error:
            print(f"Error de digitacion: {error}")