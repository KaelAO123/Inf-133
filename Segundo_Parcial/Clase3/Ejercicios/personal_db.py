# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("tu_base_de_datos.db")





















try :
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
    
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

try :
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
    
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")

try :
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
    
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL,
        nivel TEXT NOT NULL);
        """
    )
    
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")

conn.execute(
    """
    
    """
)