import json
from jsonschema import validate

# Esquema JSON
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
                                    "trimestre": {"type": "string"}
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
                                    "trimestre": {"type": "string"},
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

# Función para validar el JSON
def validar_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("El JSON es válido.")
    except Exception as e:
        print(f"El JSON no es válido: {e}")


json_data = '''
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

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
