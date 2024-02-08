import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "universidad": {
            "type": "object",
            "properties": {
                "facultad": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nombre": {"type": "string"},
                            "estudiantes": {
                                "type": "object",
                                "properties": {
                                    "estudiante": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "matricula": {"type": "string"},
                                                "nombre": {"type": "string"},
                                                "edad": {"type": "integer"},
                                                "promedio": {"type": "number"}
                                            },
                                            "required": ["matricula", "nombre"]
                                        }
                                    }
                                },
                                "required": ["estudiante"]
                            }
                        },
                        "required": ["nombre", "estudiantes"]
                    }
                }
            },
            "required": ["facultad"]
        }
    },
    "required": ["universidad"]
}

# Función para validar el JSON
def validar_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("El JSON es válido.")
    except Exception as e:
        print(f"El JSON no es válido: {e}")


json_data = '''
{
    "universidad": {
      "facultad": [
        {
          "nombre": "Ingeniería",
          "estudiantes": {
            "estudiante": [
              { "matricula": "1001", "nombre": "Carlos Pérez", "edad": 21, "promedio": 85 },
              { "matricula": "1002", "nombre": "Ana Gómez" }
            ]
          }
        },
        {
          "nombre": "Ciencias Sociales",
          "estudiantes": {
            "estudiante": [
              { "matricula": "2001", "nombre": "Mario Rodríguez", "edad": 22, "promedio": 78 },
              { "matricula": "2002", "nombre": "Laura Martínez", "edad": 20, "promedio": 92 }
            ]
          }
        }
      ]
    }
  }
  '''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
