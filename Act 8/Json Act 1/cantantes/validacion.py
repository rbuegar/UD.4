import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "nombre": {
    "type": "string",
    "minLength": 1
    },
    "genero": {
    "type": "string",
    "minLength": 1
    },
    "albumes": {
    "type": "integer",
    "minimum": 0
    },
    "popularidad": {
    "type" : "string",
    "minLength": 1
    }
    }
    
   }

# Archivo JSON a validar
archivo_json = '''
{
          "nombre": "Beyoncé",
          "genero": "Pop/RyB",
          "albumes": "6",
          "popularidad": "Alta"
        },
        {
          "nombre": "Ed Sheeran",
          "genero": "Pop",
          "albumes": "",
          "popularidad": "Alta"
        },
        {
          "nombre": "Adele",
          "genero": "Pop/Soul",
          "albumes": "4",
          "popularidad": "Alta"
        },
        {
          "nombre": "Drake",
          "genero": "Rap/RyB",
          "albumes": "7",
          "popularidad": "Alta"
        },
        {
          "nombre": "Taylor Swift",
          "genero": "Country/Pop",
          "albumes": "9",
          "popularidad": "Alta"
        },
        {
          "nombre": "Justin Bieber",
          "genero": "Pop/RyB",
          "albumes": "6",
          "popularidad": "Alta"
        },
        {
          "nombre": "Ariana Grande",
          "genero": "Pop/RyB",
          "albumes": "5",
          "popularidad": "Alta"
        },
        {
          "nombre": "Post Malone",
          "genero": "Rap/Pop",
          "albumes": "4",
          "popularidad": "Alta"
        },
        {
          "nombre": "Shawn Mendes",
          "genero": "Pop",
          "albumes": "3",
          "popularidad": "Alta"
        },
        {
          "nombre": "Dua Lipa",
          "genero": "Pop",
          "albumes": "2",
          "popularidad": "Alta"
        }
      ]
    }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.