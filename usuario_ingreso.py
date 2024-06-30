import sqlite3

# Importamos las funciones necesarias desde sus respectivos módulos

from base_datos.llamados_funcion.aregar_tarea import agregar_tarea
from base_datos.llamados_funcion.ver_tareas import ver_tareas
from base_datos.llamados_funcion.actualizar_tareas import actualizar_tareas
from base_datos.llamados_funcion.eliminar_tareas import eliminar_tareas


# Bucle infinito para mantener el programa en ejecución

while True:
        
        # Mostramos el menú de opciones al usuario

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

            # Solicitamos al usuario que ingrese una opción

            usuario = int(input("Ingrese una opcion: "))

            # Llamamos a la función correspondiente según la opción seleccionada

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

                # Salimos del bucle y finalizamos el programa

                 break
                 
        except ValueError:
             
            # Capturamos y manejamos la excepción si el usuario ingresa un valor no numérico

             print("Entrada invalida")

        except sqlite3.Error as error:
              
            # Capturamos y manejamos cualquier error relacionado con la base de datos

              print(f"Error en la base de datos: {error}")