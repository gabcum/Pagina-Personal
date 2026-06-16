from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def pagina_principal():
    return {
        "message": "¡Bienvenido a mi página principal!",
        "author" : "Tu Nombre",
        "description": "Esta es una página personal creada con FastAPI.",
        "contact": "email de contacto:",
        "foto_personal": "URL de la foto personal"
            }
@app.get("/proyectos/categoria")
def listar_proyectos():
    return {
        "message": "Mis proyectos",
        "categorias": [ 
            "Circuitos Electricos 2", "Electronica 1", "Electronica 2"
            ]
        }

@app.get("/proyectos/categoria/{curso}")
def proyectos_electronica(curso: str):
    if  curso == "circuitos-electricos-2":
        return {
            "message": "Proyecto de Circuitos Electricos 2",
            'descripcion': "Que hace el proyecto de Circuitos Electricos 2",
            'fotos' : "URL de las fotos del proyecto de Circuitos Electricos 2"

        }
    elif curso == "electronica-1":
        return {
            "message": "Proyecto de Electronica 1",
            'descripcion': "Que hace el proyecto de Electronica 1",
            'fotos' : "URL de las fotos del proyecto de Electronica 1"
        }
    elif curso == "electronica-2":
        return {
            "message": "Proyecto de Electronica 2",
            'descripcion': "Que hace el proyecto de Electronica 2",
            'fotos' : "URL de las fotos del proyecto de Electronica 2"
        }
    else:
        return {
            "message": "Categoría no encontrada",
            "error": "La categoría especificada no existe."
        }
