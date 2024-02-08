import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "nif": {
            "type": "string",
            "pattern": "^[0-9]{8}[A-Za-z]$"
        },
        "resultado": {
            "type": "string",
            "enum": ["apto", "No apto"]
        },
        "observaciones": {
            "type": "string"
        },
        "ip": {
            "type": "string",
            "format": "ipv4"
        },
        "mac": {
            "type": "string",
            "pattern": "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
        }
    },
    "required": ["nif", "resultado"],
    "anyOf": [
        {"required": ["observaciones"]},
        {"required": ["ip"]},
        {"required": ["mac"]}
    ]
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
          "nif": "12345678A",
          "resultado": "apto",
          "observaciones": "Excelente desempeño en programación.",
          "ip": "192.168.1.2"
        },
        {
          "nif": "98765432B",
          "resultado": "No apto",
          "mac": "00:1A:2B:3C:4D:5E"
        },
        {
          "nif": "11122333C",
          "resultado": "apto",
          "ip": "192.168.1.5"
        },
        {
          "nif": "44556677D",
          "resultado": "apto",
          "mac": "AA:BB:CC:DD:EE:FF"
        },
        {
          "nif": "88990011E",
          "resultado": "No apto",
          "observaciones": "Problemas en la resolución de ejercicios prácticos.",
          "ip": "192.168.1.8"
        },
        {
          "nif": "22334455F",
          "resultado": "apto",
          "mac": "11:22:33:44:55:66"
        },
        {
          "nif": "66778899G",
          "resultado": "No apto",
          "observaciones": "Faltas continuas a clase.",
          "mac": "22:33:44:55:66:77"
        },
        {
          "nif": "11223344H",
          "resultado": "apto",
          "ip": "192.168.1.11"
        },
        {
          "nif": "55667788I",
          "resultado": "No apto",
          "mac": "33:44:55:66:77:88"
        },
        {
          "nif": "99001122J",
          "resultado": "apto",
          "ip": "192.168.1.14"
        }
    '''
 


# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
