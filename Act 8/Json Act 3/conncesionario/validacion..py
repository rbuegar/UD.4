import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "concesionario": {
            "type": "object",
            "properties": {
                "coche": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "codigo": {"type": "string"},
                            "marca": {"type": "string"},
                            "modelo": {"type": "string"},
                            "matricula": {"type": "string"},
                            "potencia": {"type": "string"},
                            "plazas": {"type": "string"},
                            "puertas": {"type": "string"}
                        },
                        "required": ["codigo", "marca", "modelo", "matricula", "potencia", "plazas", "puertas"]
                    }
                }
            },
            "required": ["coche"]
        }
    },
    "required": ["concesionario"]
}



# Archivo JSON a validar
archivo_json = '''
{
  "concesionario": {
    "coche": [
      {
        "codigo": "C001",
        "marca": "Toyota",
        "modelo": "Corolla",
        "matricula": "ABC123",
        "potencia": "150",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C002",
        "marca": "Ford",
        "modelo": "Focus",
        "matricula": "XYZ789",
        "potencia": "120",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C003",
        "marca": "Honda",
        "modelo": "Accord",
        "matricula": "DEF456",
        "potencia": "180",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C004",
        "marca": "Chevrolet",
        "modelo": "Malibu",
        "matricula": "GHI789",
        "potencia": "160",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C005",
        "marca": "Volkswagen",
        "modelo": "Passat",
        "matricula": "JKL012",
        "potencia": "140",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C006",
        "marca": "Hyundai",
        "modelo": "Sonata",
        "matricula": "MNO345",
        "potencia": "170",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C007",
        "marca": "Nissan",
        "modelo": "Altima",
        "matricula": "PQR678",
        "potencia": "130",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C008",
        "marca": "BMW",
        "modelo": "3 Series",
        "matricula": "STU901",
        "potencia": "200",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C009",
        "marca": "Mercedes-Benz",
        "modelo": "C-Class",
        "matricula": "VWX234",
        "potencia": "190",
        "plazas": "5",
        "puertas": "4"
      },
      {
        "codigo": "C010",
        "marca": "Audi",
        "modelo": "A4",
        "matricula": "YZA567",
        "potencia": "180",
        "plazas": "5",
        "puertas": "4"
      }
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)


