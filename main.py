import mysql.connector
from mysql.connector import errorcode
import time

cursor = None
cnx = None


def conectar_base():
    """Establece la conexión a la base de datos MySQL."""
    global cnx, cursor

    db_config = {
        "user": "root",
        "password": "",
        "host": "Localhost",
        "database": "telo"
    }

    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        print('\n--- Conexión establecida con éxito ---')
        return True

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('\nERROR: Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('\nERROR: La base de datos no existe! Asegúrate de crear "telo".')
        else:
            print(f"\nERROR al conectar: {err}")
        return False


def crear_tablas():
    """Crea las tablas 'Rubricas' y 'Criterios' si no existen."""
    global cnx, cursor

    TABLA_RUBRICAS = """
    CREATE TABLE IF NOT EXISTS Rubricas (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL UNIQUE
    );
    """

    TABLA_CRITERIOS = """
    CREATE TABLE IF NOT EXISTS Criterios (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        rubrica_id INT NOT NULL,
        nombre_criterio VARCHAR(255) NOT NULL,
        puntaje_maximo INT NOT NULL,
        FOREIGN KEY (rubrica_id) REFERENCES Rubricas(ID) ON DELETE CASCADE
    );
    """

    try:
        cursor.execute(TABLA_RUBRICAS)
        cursor.execute(TABLA_CRITERIOS)
        cnx.commit()
        print("Tablas 'Rubricas' y 'Criterios' verificadas/creadas.")
    except mysql.connector.Error as err:
        print(f"Error al crear tablas: {err}")


def insertar_rubrica(nombre_rubrica):
    """Inserta una nueva rúbrica y retorna su ID."""
    global cnx, cursor
    try:
        consulta = "INSERT INTO Rubricas (nombre) VALUES (%s)"
        cursor.execute(consulta, (nombre_rubrica,))
        cnx.commit()
        rubrica_id = cursor.lastrowid
        print(f"\n¡Rúbrica '{nombre_rubrica}' (ID: {rubrica_id}) creada con éxito!")
        return rubrica_id
    except mysql.connector.IntegrityError:
        print(f"\nADVERTENCIA: Ya existe una rúbrica con el nombre '{nombre_rubrica}'.")
        return None
    except mysql.connector.Error as err:
        print(f"Error al insertar rúbrica: {err}")
        return None


def insertar_criterio(rubrica_id, nombre_criterio, puntaje_maximo):
    """Inserta un nuevo criterio asociado a una rúbrica."""
    global cnx, cursor
    try:
        consulta = "INSERT INTO Criterios (rubrica_id, nombre_criterio, puntaje_maximo) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (rubrica_id, nombre_criterio, puntaje_maximo))
        cnx.commit()
        print(f"  - Criterio: '{nombre_criterio}' ({puntaje_maximo} pts) añadido.")
    except mysql.connector.Error as err:
        print(f"Error al insertar criterio: {err}")


def listar_rubricas():
    """Consulta y muestra una lista numerada de todas las rúbricas."""
    global cursor
    try:
        consulta = "SELECT ID, nombre FROM Rubricas ORDER BY ID"
        cursor.execute(consulta)
        rubricas = cursor.fetchall()

        if not rubricas:
            print("\nNo hay rúbricas guardadas.")
            return []

        print("\n--- Rúbricas Disponibles ---")
        for rubrica in rubricas:
            print(f"[{rubrica['ID']}] {rubrica['nombre']}")
        print("---------------------------")
        return rubricas

    except mysql.connector.Error as err:
        print(f"Error al listar rúbricas: {err}")
        return []


def obtener_rubrica_completa(rubrica_id):
    """Muestra el nombre de la rúbrica y todos sus criterios."""
    global cursor
    try:
        cursor.execute("SELECT nombre FROM Rubricas WHERE ID = %s", (rubrica_id,))
        rubrica_info = cursor.fetchone()

        if not rubrica_info:
            print(f"\nERROR: No se encontró la rúbrica con ID {rubrica_id}.")
            return

        rubrica_nombre = rubrica_info['nombre']

        consulta_criterios = """
        SELECT nombre_criterio, puntaje_maximo 
        FROM Criterios 
        WHERE rubrica_id = %s
        """
        cursor.execute(consulta_criterios, (rubrica_id,))
        criterios = cursor.fetchall()

        print(f"\n=============================================")
        print(f"RÚBRICA: {rubrica_nombre} (ID: {rubrica_id})")
        print("=============================================")
        if criterios:
            puntuacion_total = 0
            for i, criterio in enumerate(criterios, 1):
                print(f"  {i}. {criterio['nombre_criterio']}: {criterio['puntaje_maximo']} puntos")
                puntuacion_total += criterio['puntaje_maximo']
            print(f"\nTOTAL MÁXIMO DE LA RÚBRICA: {puntuacion_total} puntos")
        else:
            print("Esta rúbrica aún no tiene criterios asociados.")
        print("=============================================")

    except mysql.connector.Error as err:
        print(f"Error al mostrar rúbrica: {err}")


def flujo_crear_rubrica():
    """Flujo interactivo para crear una nueva rúbrica y sus criterios."""
    nombre = input("Ingrese el NOMBRE de la nueva rúbrica (ej: 'Proyecto Final'): ")
    rubrica_id = insertar_rubrica(nombre)

    if rubrica_id is None:
        return

    print("\n--- AÑADIR CRITERIOS ---")
    print("Ingrese el nombre del criterio y su puntaje máximo. Escriba 'fin' para terminar.")

    while True:
        criterio_nombre = input(f"Nombre del Criterio para '{nombre}' (o 'fin'): ").strip()
        if criterio_nombre.lower() == 'fin':
            break

        try:
            puntaje = int(input(f"Puntaje MÁXIMO para '{criterio_nombre}': "))
            if puntaje <= 0:
                print("El puntaje debe ser un número positivo.")
                continue
            insertar_criterio(rubrica_id, criterio_nombre, puntaje)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el puntaje.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


def flujo_ver_rubrica():
    """Flujo interactivo para seleccionar y mostrar una rúbrica."""
    rubricas = listar_rubricas()
    if not rubricas:
        return

    try:
        rubrica_id_str = input("\nIngrese el ID [número] de la rúbrica que desea ver: ").strip()
        if not rubrica_id_str.isdigit():
            print("Entrada inválida. Debe ingresar un número.")
            return

        rubrica_id = int(rubrica_id_str)

        if rubrica_id not in [r['ID'] for r in rubricas]:
            print(f"ADVERTENCIA: El ID {rubrica_id} no se encuentra en la lista actual.")
        obtener_rubrica_completa(rubrica_id)

    except ValueError:
        print("Entrada inválida. Debe ingresar un número para el ID.")


def cerrar_base():
    """Cierra la conexión a la base de datos si está abierta."""
    global cnx
    if cnx and cnx.is_connected():
        cnx.close()
        print("\nLa conexión a la base de datos ha sido cerrada.")


def Menu():
    """Menú principal de la aplicación de gestión de rúbricas."""
    if not conectar_base():
        print("\nNo se pudo establecer la conexión. Saliendo del programa.")
        return

    crear_tablas()

    seguimos = True
    while seguimos:
        print("""
------------------------------------------------------
|             GESTOR DE RÚBRICAS DOCENTE             |
------------------------------------------------------
| 1 - Crear Nueva Rúbrica (y añadir criterios)       |
| 2 - Ver Lista de Rúbricas Guardadas                |
| 3 - Mostrar Rúbrica Completa (por ID)              |
| 4 - Salir                                          |
------------------------------------------------------
        """)

        opcion_str = input("Ingrese una opción (1-4): ").strip()

        if not opcion_str.isdigit():
            print("\nOpción inválida. Por favor, ingrese el número de la opción.")
            time.sleep(1)
            continue

        opcion = int(opcion_str)

        if opcion == 1:
            flujo_crear_rubrica()
        elif opcion == 2:
            listar_rubricas()
        elif opcion == 3:
            flujo_ver_rubrica()
        elif opcion == 4:
            print("\nCerrando programa. ¡Hasta pronto!")
            seguimos = False
        else:
            print("\nOpción no reconocida. Intente de nuevo.")

        if seguimos:
            time.sleep(2)

    cerrar_base()
    Menu()