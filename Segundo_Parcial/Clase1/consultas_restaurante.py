# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")


# Consultar datos de matriculación INNER JOIN
print("\nPEDIDOS:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id  ===
    """
)
for row in cursor:
    print(row)

# MATRICULAS:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-30')

# Consultar datos de matriculación LEFT JOIN
print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero, PEDIDOS.fecha
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    LEFT JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id;
    """
)
for row in cursor:
    print(row)

# MATRICULAS:
# ('Ingeniería en Informática', 'Juan')
# ('Licenciatura en Administración', 'María')
# ('Licenciatura en Contabilidad', None)

# Consultar datos de matriculación RIGHT JOIN


# MATRICULAS:
# ('Juan', 'Ingeniería en Informática')
# ('María', 'Licenciatura en Administración')
# (None, 'Licenciatura en Contabilidad')
