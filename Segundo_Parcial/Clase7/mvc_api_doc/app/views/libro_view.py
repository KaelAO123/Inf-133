def render_libro_list(librs):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "edicion": libro.edicion,
            "disponibilidad":libro.disponibilidad,
        }
        for libro in librs
    ]


def render_libro_detail(libro):
    # Representa los detalles de un libro como un diccionario
    return {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "edicion": libro.edicion,
        "disponibilidad":libro.disponibilidad,
    }
