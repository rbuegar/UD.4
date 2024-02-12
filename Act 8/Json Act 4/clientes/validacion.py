import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "gestoria": {
            "type": "object",
            "properties": {
                "sede": {
                    "type": "object",
                    "properties": {
                        "@codigo_sede": {"type": "string"},
                        "@nombre_empleado": {"type": "string"},
                        "@fecha_alta": {"type": "string", "format": "date"},
                        "cliente": {
                            "type": "object",
                            "properties": {
                                "codigo_cliente": {"type": "string"},
                                "descripcion_cliente": {"type": "string"},
                                "num_viviendas": {"type": "integer"},
                                "coste_vivienda": {"type": "number"},
                                "resumen_viviendas": {"type": "string"},
                                "plazo_alta_hacienda": {"type": "string", "format": "date"}
                            },
                            "required": ["codigo_cliente", "descripcion_cliente", "num_viviendas", "coste_vivienda", "resumen_viviendas", "plazo_alta_hacienda"]
                        }
                    },
                    "required": ["@codigo_sede", "@nombre_empleado", "@fecha_alta", "cliente"]
                }
            },
            "required": ["sede"]
        }
    },
    "required": ["gestoria"]
}



# Archivo JSON a validar
archivo_json = '''
{
  "gestoria": {
    "sede": {
      "@codigo_sede": "S001",
      "@nombre_empleado": "Juan",
      "@fecha_alta": "2024-01-25",
      "cliente": {
        "codigo_cliente": "ABC-123",
        "descripcion_cliente": "solvente",
        "num_viviendas": 3,
        "coste_vivienda": 150000.00,
        "resumen_viviendas": "Resumen de las viviendas",
        "plazo_alta_hacienda": "2024-02-01"
      }
    }
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema



validate(instance=datos_json, schema=schema)