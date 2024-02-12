import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "informe": {
            "type": "object",
            "properties": {
                "fecha": {"type": "string", "format": "date"},
                "cabecera": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "trimestre": {"type": "string", "pattern": "^[1-4]$"}
                                },
                                "required": ["trimestre"]
                            }
                        }
                    },
                    "required": ["region"]
                },
                "datos": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "trimestre": {"type": "string", "pattern": "^[1-4]$"},
                                    "libros_vendidos": {"type": "integer"}
                                },
                                "required": ["trimestre"]
                            }
                        }
                    },
                    "required": ["region"]
                }
            },
            "required": ["fecha", "cabecera", "datos"]
        }
    },
    "required": ["informe"]
}



# Archivo JSON a validar
archivo_json = '''
{
  "informe": {
    "fecha": "2024-02-01",
    "cabecera": {
      "region": [
        { "trimestre": "1" },
        { "trimestre": "2" },
        { "trimestre": "3" }
      ]
    },
    "datos": {
      "region": [
        { "trimestre": "1", "libros_vendidos": 150 },
        { "trimestre": "2" },
        { "trimestre": "3", "libros_vendidos": 200 },
        { "trimestre": "4", "libros_vendidos": 180 },
        { "trimestre": "1" },
        { "trimestre": "2", "libros_vendidos": 220 },
        { "trimestre": "3" },
        { "trimestre": "4", "libros_vendidos": 190 },
        { "trimestre": "1", "libros_vendidos": 160 },
        { "trimestre": "2" },
        { "trimestre": "3", "libros_vendidos": 210 },
        { "trimestre": "4", "libros_vendidos": 175 }
      ]
    }
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema


validate(instance=datos_json, schema=schema)
