import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "codigo": {
            "type": "string",
            "pattern": "^C\\d{3}$"
        },
        "marca": {
            "type": "string"
        },
        "modelo": {
            "type": "string"
        },
        "matricula": {
            "type": "string",
            "pattern": "^[A-Z]{3}\\d{3}$"
        },
        "potencia": {
            "type": "string"
        },
        "plazas": {
            "type": "string"
        },
        "puertas": {
            "type": "string"
        }
    },
    "required": ["codigo", "marca", "modelo", "matricula", "potencia", "plazas", "puertas"]
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
    '''
    


# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.