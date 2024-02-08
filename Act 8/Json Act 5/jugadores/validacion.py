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
        "estado": {
            "type": "string",
            "enum": ["activo", "retirado"]
        },
        "observaciones": {
            "type": "string"
        },
        "nombre": {
            "type": "string"
        },
        "equipo": {
            "type": "string"
        }
    },
    "required": ["nif", "estado", "nombre", "equipo"],
    "anyOf": [
        {"required": ["observaciones"]},
        {"not": {"required": ["observaciones"]}}
    ]
}

# Función para validar el JSON
def validar_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("El JSON es válido.")
    except Exception as e:
        print(f"El JSON no es válido: {e}")

# JSON de ejemplo
json_data = '''
    {
          "nif": "12345678A",
          "estado": "activo",
          "observaciones": "Gran desempeño en la temporada actual.",
          "nombre": "Lionel Messi",
          "equipo": "Paris Saint-Germain"
        },
        {
          "nif": "98765432B",
          "estado": "retirado",
          "nombre": "Cristiano Ronaldo",
          "equipo": "Manchester United"
        },
        {
          "nif": "11122333C",
          "estado": "activo",
          "nombre": "Neymar Jr.",
          "equipo": "Paris Saint-Germain"
        },
        {
          "nif": "44556677D",
          "estado": "activo",
          "nombre": "Robert Lewandowski",
          "equipo": "Bayern Munich"
        },
        {
          "nif": "88990011E",
          "estado": "retirado",
          "observaciones": "Lesión grave durante la última temporada.",
          "nombre": "Sergio Ramos",
          "equipo": "Paris Saint-Germain"
        },
        {
          "nif": "22334455F",
          "estado": "activo",
          "nombre": "Mohamed Salah",
          "equipo": "Liverpool"
        },
        {
          "nif": "66778899G",
          "estado": "retirado",
          "observaciones": "Decisión personal de retirarse después de una carrera exitosa.",
          "nombre": "Andrés Iniesta",
          "equipo": "Vissel Kobe"
        },
        {
          "nif": "11223344H",
          "estado": "activo",
          "nombre": "Kylian Mbappé",
          "equipo": "Paris Saint-Germain"
        },
        {
          "nif": "55667788I",
          "estado": "activo",
          "nombre": "Kevin De Bruyne",
          "equipo": "Manchester City"
        },
        {
          "nif": "99001122J",
          "estado": "retirado",
          "observaciones": "Se retiró al finalizar la última temporada.",
          "nombre": "Xavi Hernandez",
          "equipo": "Al-Sadd"
        }
    
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
