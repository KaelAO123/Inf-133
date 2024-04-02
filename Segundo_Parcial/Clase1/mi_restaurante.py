# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")
# Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio DOUBLE NOT NULL,
    categoria TEXT NOT NULL);
    """
)

# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 10.99, 'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99, 'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi', 12.99, 'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada', 6.99, 'Vegetariana')
    """
)
# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# PLATOS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

# Crear tablas de estudiantes
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (5)
    """
)
# Consultar datos de estudiantes
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# MESAS:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')

# Crear tabla de matriculación
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)

# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (mesa_id, plato_id, cantidad, fecha) 
    VALUES (2, 3, 1, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (mesa_id, plato_id, cantidad, fecha)
    VALUES (3, 1, 3, '2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (mesa_id, plato_id, cantidad, fecha)
    VALUES (4, 4, 3, '2024-04-02')
    """
)
# Consultar datos de matriculación
print("\nPEDIDOS DI KAI:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, MESAS.numero, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)


# print("\n##################################################################")
# print("PARTE 2")
# print("\n####\tACTUALIZAR\t####")
# print("\nPLATOS ACTUALIZADOS:")
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )
# for row in cursor:
#     print(row)
# print("\nPLATOS:")
# conn.execute(
#     """
#     UPDATE PLATOS
#     SET precio = 9.99
#     WHERE id = 2
#     """
# )
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )
# for row in cursor:
#     print(row)
# print("############################################")
# # Listar datos de matriculación
# print("\n####\tACTUALIZAR\t####")
# print("\nPLATOS ACTUALIZADOS:")
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )
# for row in cursor:
#     print(row)
# print("\nPLATOS:")
# conn.execute(
#     """
#     UPDATE PLATOS
#     SET categoria = 'Fusion'
#     WHERE id = 3
#     """
# )
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )
# for row in cursor:
#     print(row)
# print("############################################")
# # Listar datos de matriculación
# print("\n####\ELIMINAR\t####")
# print("\nPLATOS ELIMINADOS:")
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )
# for row in cursor:
#     print(row)
# conn.execute(
#     """
#     DELETE FROM PLATOS
#     WHERE id = 4
#     """
# )
# print("\nPLATOS:")
# cursor = conn.execute(
#     "SELECT * FROM PLATOS"
# )

# for row in cursor:
#     print(row)
# print("############################################")
# print("\n####\ELIMINAR\t####")
# cursor = conn.execute(
#     "SELECT * FROM PEDIDOS"
# )
# for row in cursor:
#     print(row)
# print("\nPEDIDOS ELIMINADOS:")

# conn.execute(
#     """
#     DELETE FROM PEDIDOS
#     WHERE id = 3
#     """
# )

# # Listar datos de matriculación
# print("\nPEDIDOS:")
# cursor = conn.execute(
#     "SELECT * FROM PEDIDOS"
# )

# for row in cursor:
#     print(row)
# print("############################################")


# # Cerrar conexión
conn.close()









# #Por que no usas el visual de gith
# #





