
# impotamos "sqlite3" para manejar la base de datos

import sqlite3

def agregar_tarea():

    # Establecemos la conexión a la base de datos usando el contexto 'with' para asegurar el cierre correcto

    with sqlite3.connect("C:/Users/POWER/gestor.db") as tarea:
        try:

            # Obtenemos un cursor para ejecutar las consultas SQL

            consulta_cursor = tarea.cursor()

            # Solicitamos al usuario los detalles de la tarea

            usuario_titulo = str(input("Ingrese el titulo de la tarea: "))
            contenido_tarea= str(input("ingrese el contenido de la tarea: "))
            fecha_vencimiento = str(input("ingrese la fecha de vencimiento (DD/MM/YY): "))
            prioridad_tarea = str(input("ingrese un nivel de prioridad: "))
            tarea_completada = int(input("ponga 0 si la tarea esta completada y 1 si no: "))

            # Ejecutamos la consulta SQL para insertar los datos en la tabla 'Agregar_tareas'

            consulta_cursor.execute("INSERT INTO Agregar_tareas (Titulo,Descripcion,Fecha_vencimiento,Prioridad,Completado) VALUES (?,?,?,?,?)",(usuario_titulo,contenido_tarea,fecha_vencimiento,prioridad_tarea,tarea_completada))

            # Confirmamos (commit) la transacción para guardar los cambios en la base de datos

            tarea.commit()
            print("Datos ingresados correctamente")
            
        except ValueError as error:

            # Capturamos y manejamos cualquier excepción de tipo ValueError

            print(f"Error de digitacion: {error}")