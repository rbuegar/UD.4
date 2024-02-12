import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
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



# Archivo JSON a validar
archivo_json = '''
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
