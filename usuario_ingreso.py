import sqlite3

from base_datos.llamados_funcion.aregar_tarea import agregar_tarea
from base_datos.llamados_funcion.ver_tareas import ver_tareas
from base_datos.llamados_funcion.actualizar_tareas import actualizar_tareas
from base_datos.llamados_funcion.eliminar_tareas import eliminar_tareas

while True:
        print("""
            Bienvenido al gestor de tareas:
            1. Agregar tarea.
            2. Ver tareas.
            3. Actualizar tareas.
            3. Completar tareas.
            4. Eliminar tareas.
            6. Salir
            """)
        try:
            usuario = int(input("Ingrese una opcion: "))
            if usuario == 1:
                agregar_tarea()
            elif usuario == 2:
                 ver_tareas()
            elif usuario == 3:
                 actualizar_tareas()
            elif usuario == 4:
                eliminar_tareas()
            elif usuario == 6:
                 print("Gracias por administrar sus tareas")
                 break
                 
        except ValueError:
             print("Entrada invalida")
        except sqlite3.Error as error:
              print(f"Error en la base de datos: {error}")