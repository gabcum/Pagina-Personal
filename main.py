from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()



#Datos base de un proyecto 
class proyecto(BaseModel):
    id_url: str
    curos: str
    titulo: str
    descripcion: str
    componentes: List[str]
    fotos: List[str]

#Base de datos provicional de proyectos
base_de_datos_proyectos = [
    proyecto(
        id_url="circuitos-electricos-2",
        curos="Circuitos Electricos 2",
        titulo="Proyecto de Circuitos Electricos 2",
        descripcion="Que hace el proyecto de Circuitos Electricos 2",
        componentes=["Componente 1", "Componente 2", "Componente 3"],
        fotos=["URL de las fotos del proyecto de Circuitos Electricos 2"]
    ),
    proyecto(
        id_url="electronica-1",
        curos="Electronica 1",
        titulo="Proyecto de Electronica 1",
        descripcion="Que hace el proyecto de Electronica 1",
        componentes=["Componente A", "Componente B", "Componente C"],
        fotos=["URL de las fotos del proyecto de Electronica 1"]
    ),
    proyecto(
        id_url="electronica-2",
        curos="Electronica 2",
        titulo="Proyecto de Electronica 2",
        descripcion="Que hace el proyecto de Electronica 2",
        componentes=["Componente X", "Componente Y", "Componente Z"],
        fotos=["URL de las fotos del proyecto de Electronica 2"]
    )
]
@app.get("/")
def pagina_principal():
    return {
        "message": "¡Bienvenido a mi portafolio backend!",
        "author" : "Gabriel Andres Cumes de León",
        "description": "Portafolio de proyectos de Ingeniería Electrónica en la USAC.",
        "contact": "tucorreo@gmail.com",
        "foto_personal": "/imagenes/perfil.jpg"
    }

@app.get("/proyectos/categoria")
def listar_proyectos():
    return {
        "message": "Mis proyectos",
        "categorias_disponibles": [ 
            "circuitos-electricos-2", "electronica-2"
        ]
    }

@app.get("/proyectos/categoria/{curso_url}")
def buscar_proyecto(curso_url: str):
    # ¡Adiós a los if/elif! Aquí usamos un ciclo para buscar en la base de datos
    for proy in base_de_datos_proyectos:
        if proy.id_url == curso_url:
            return proy
            
    # Si termina de buscar y no encuentra nada, devuelve error
    return {
        "message": "Categoría no encontrada",
        "error": f"El curso '{curso_url}' no existe en la base de datos."
    }

@app.post("/proyectos/nuevo")
def agregar_proyecto(nuevo_proyecto: proyecto):
    
    #Verificar si existe el proyecto en la base de datos
    for proy in base_de_datos_proyectos:
        if proy.id_url == nuevo_proyecto.id_url:
            raise HTTPException(
                status_code=400, 
                detail=f"El proyecto con id_url '{nuevo_proyecto.id_url}' ya está registrado."
            )
        else:
            continue
    # Si no existe, agregarlo a la base de datos
    base_de_datos_proyectos.append(nuevo_proyecto)
    return {
        "message": "Proyecto agregado exitosamente",
        "proyecto": nuevo_proyecto
    }

    