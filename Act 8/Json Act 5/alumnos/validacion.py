import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "alumnos": {
            "type": "object",
            "properties": {
                "alumno": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nif": {"type": "string"},
                            "resultado": {"type": "string", "enum": ["apto", "No apto"]},
                            "observaciones": {"type": "string"},
                            "ip": {"type": "string", "format": "ipv4"},
                            "mac": {"type": "string", "pattern": "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"}
                        },
                        "required": ["nif", "resultado"]
                    }
                }
            },
            "required": ["alumno"]
        }
    },
    "required": ["alumnos"]
}



# Archivo JSON a validar
archivo_json = '''
{
  "alumnos": {
    "alumno": [
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
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema


validate(instance=datos_json, schema=schema)