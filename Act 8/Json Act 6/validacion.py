import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "contenidos": {
            "type": "object",
            "properties": {
                "ud": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "@tipo": {"type": "string"},
                            "descripcion": {"type": "string"}
                        },
                        "required": ["@tipo", "descripcion"]
                    }
                }
            },
            "required": ["ud"]
        }
    },
    "required": ["nombre", "contenidos"]
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
          "nombre": "Desarrollo de Aplicaciones Multiplataforma",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Fundamentos de programación"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Programación orientada a objetos"
              }
            ]
          }
        },
        {
          "nombre": "Administración de Sistemas Gestores de Bases de Datos",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Modelos de datos y diseño de bases de datos"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Administración y optimización de bases de datos"
              }
            ]
          }
        },
        {
          "nombre": "Entornos de Desarrollo",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Desarrollo de software en entornos integrados"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Pruebas y mantenimiento de aplicaciones"
              }
            ]
          }
        },
        {
          "nombre": "Sistemas Informáticos",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Arquitectura de computadores"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Instalación y configuración de sistemas operativos"
              }
            ]
          }
        },
        {
          "nombre": "Empresa e Iniciativa Emprendedora",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Creación y gestión de empresas"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Plan de negocio"
              }
            ]
          }
        },
        {
          "nombre": "Despliegue de Aplicaciones Web",
          "contenidos": {
            "ud": [
              {
                "@tipo": "Teoría",
                "descripcion": "Desarrollo y despliegue de aplicaciones web"
              },
              {
                "@tipo": "Práctica",
                "descripcion": "Configuración de servidores web"
              }
            ]
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
