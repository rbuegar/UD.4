import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "jugadores": {
            "type": "object",
            "properties": {
                "jugador": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nif": {"type": "string"},
                            "estado": {"type": "string", "enum": ["activo", "retirado"]},
                            "observaciones": {"type": "string"},
                            "nombre": {"type": "string"},
                            "equipo": {"type": "string"}
                        },
                        "required": ["nif", "estado", "nombre", "equipo"]
                    }
                }
            },
            "required": ["jugador"]
        }
    },
    "required": ["jugadores"]
}


# Archivo JSON a validar
archivo_json = '''
{
  "jugadores": {
    "jugador": [
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
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema


validate(instance=datos_json, schema=schema)