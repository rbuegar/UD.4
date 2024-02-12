import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "telefono": {
            "type": "integer",
            "minimum": 9
        },
        "fecha": {
            "type": "string",
            "format": "date",
            "minimum": 1
        },
        "hora": {
            "type": "integer",
            "minimum": 1
        },
        "mensaje": {
            "type": "string",
            "minLength": 1
        }
    },
    "required": ["telefono", "fecha", "hora", "mensaje"]
}


# Archivo JSON a validar
archivo_json = ''' 
{
          "telefono": "955 55 66 55",
          "fecha": "1/7/2011",
          "hora": "23:55",
          "mensaje": "Juego 1: Tetris"
        },
        {
          "telefono": "745 15 56 11",
          "fecha": "22/9/2020",
          "hora": "09:22",
          "mensaje": "Juego 2 : Arkanoid"
        },
        {
          "telefono": "842 25 22 00",
          "fecha": "10/11/2023",
          "hora": "21:48",
          "mensaje": "Juego 3 : Comecocos"
        }
        '''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
