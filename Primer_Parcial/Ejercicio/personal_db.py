# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("Ejercicio/personal.db")


try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")
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

try :
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
    
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre,fecha_creacion)
    VALUES ('Ventas','10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre,fecha_creacion)
    VALUES ('Marketing','11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Gerente de Ventas','Senior',10-04-2020)
"""
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Analista de Marketing','Junior',11-04-2020)
"""
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Representante de Ventas','Junior',12-04-2020)
"""
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,cargo_id,departamento_id,fecha_creacion)
    VALUES ('Juan','Gonzalez', 'Perez','15-05-2023',1,1,'')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,cargo_id,departamento_id,fecha_creacion)
    VALUES ('Maria','Lopez', 'Martinez','20-06-2023',2,2,'')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
    VALUES ('1','3000','01-04-2024','30-04-2025','')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
    VALUES ('2','3500','01-07-2023','30-04-2024','')
    """
)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, SALARIOS.salario
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id = EMPLEADOS.id 
    """
)
for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS on EMPLEADOS.cargo_id = CARGOS.id
    """
)
for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, SALARIOS.salario, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id = EMPLEADOS.id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS on EMPLEADOS.cargo_id = CARGOS.id
    """
)
for row in cursor:
    print(row)

conn.execute(
    """
    UPDATE CARGOS
    SET nombre = 'Representante de Ventas'
    WHERE id = 2
    """
)
for row in cursor:
    print(row)

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM CARGOS
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM DEPARTAMENTOS
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)


conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Representante de Ventas','Junior',12-04-2020)
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,cargo_id,departamento_id,fecha_creacion)
    VALUES ('Carlos','Sanchez', 'Rodriguez','09-04-2024',2,2,'')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
    VALUES ('2','3500','05-05-2023','30-04-2025','')
    """
)


conn.commit()
conn.close()