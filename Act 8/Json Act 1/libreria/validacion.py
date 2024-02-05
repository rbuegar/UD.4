import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "titulo": {
    "type": "string",
    "minLength": 1
    },
    "autor": {
    "type": "string",
    "minLength": 1
    },
    "genero": {
    "type": "string",
    "minLength": 1
    },
    "publicacion": {
    "type": "integer",
    "minimum": 0
    },
    "precio": {
    "type" : "integer",
    "minimun": 0
    }
    }
    
   }

# Archivo JSON a validar
archivo_json = '''
 {
          "titulo": "El señor de los anillos",
          "autor": "J.R.R. Tolkien",
          "genero": "Fantasía",
          "publicacion": "1954",
          "precio": "20.00"
        },
        {
          "titulo": "Cien años de soledad",
          "autor": "Gabriel García Márquez",
          "genero": "Realismo mágico",
          "publicacion": "1967",
          "precio": "15.50"
        },
        {
          "titulo": "1984",
          "autor": "George Orwell",
          "genero": "Ciencia ficción",
          "publicacion": "1949",
          "precio": "18.75"
        },
        {
          "titulo": "Orgullo y prejuicio",
          "autor": "Jane Austen",
          "genero": "Novela romántica",
          "publicacion": "1813",
          "precio": "12.00"
        },
        {
          "titulo": "Don Quijote de la Mancha",
          "autor": "Miguel de Cervantes",
          "genero": "Novela picaresca",
          "publicacion": "1605",
          "precio": "22.50"
        },
        {
          "titulo": "Harry Potter y la piedra filosofal",
          "autor": "J.K. Rowling",
          "genero": "Fantasía",
          "publicacion": "1997",
          "precio": "25.00"
        },
        {
          "titulo": "Crónica de una muerte anunciada",
          "autor": "Gabriel García Márquez",
          "genero": "Realismo mágico",
          "publicacion": "1981",
          "precio": "14.25"
        },
        {
          "titulo": "Matar a un ruiseñor",
          "autor": "Harper Lee",
          "genero": "Novela",
          "publicacion": "1960",
          "precio": "16.80"
        },
        {
          "titulo": "Fundación",
          "autor": "Isaac Asimov",
          "genero": "Ciencia ficción",
          "publicacion": "1951",
          "precio": "19.99"
        },
        {
          "titulo": "Los juegos del hambre",
          "autor": "Suzanne Collins",
          "genero": "Ciencia ficción",
          "publicacion": "2008",
          "precio": "17.30"
        }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.