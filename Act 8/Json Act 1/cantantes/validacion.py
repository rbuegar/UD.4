import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "discografica": {
            "type": "object",
            "properties": {
                "cantante": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nombre": {"type": "string"},
                            "genero": {"type": "string"},
                            "albumes": {"type": "string"},
                            "popularidad": {"type": "string"}
                        },
                        "required": ["nombre", "genero", "albumes", "popularidad"]
                    }
                }
            },
            "required": ["cantante"]
        }
    },
    "required": ["discografica"]
}



# Archivo JSON a validar
archivo_json = '''
{
    "discografica": {
      "cantante": [
        {
          "nombre": "Beyoncé",
          "genero": "Pop/RyB",
          "albumes": "6",
          "popularidad": "Alta"
        },
        {
          "nombre": "Ed Sheeran",
          "genero": "Pop",
          "albumes": "5",
          "popularidad": "Alta"
        },
        {
          "nombre": "Adele",
          "genero": "Pop/Soul",
          "albumes": "4",
          "popularidad": "Alta"
        },
        {
          "nombre": "Drake",
          "genero": "Rap/RyB",
          "albumes": "7",
          "popularidad": "Alta"
        },
        {
          "nombre": "Taylor Swift",
          "genero": "Country/Pop",
          "albumes": "9",
          "popularidad": "Alta"
        },
        {
          "nombre": "Justin Bieber",
          "genero": "Pop/RyB",
          "albumes": "6",
          "popularidad": "Alta"
        },
        {
          "nombre": "Ariana Grande",
          "genero": "Pop/RyB",
          "albumes": "5",
          "popularidad": "Alta"
        },
        {
          "nombre": "Post Malone",
          "genero": "Rap/Pop",
          "albumes": "4",
          "popularidad": "Alta"
        },
        {
          "nombre": "Shawn Mendes",
          "genero": "Pop",
          "albumes": "3",
          "popularidad": "Alta"
        },
        {
          "nombre": "Dua Lipa",
          "genero": "Pop",
          "albumes": "2",
          "popularidad": "Alta"
        }
      ]
    }
  }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

