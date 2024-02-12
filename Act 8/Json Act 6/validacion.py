import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "modulos": {
            "type": "object",
            "properties": {
                "modulo": {
                    "type": "array",
                    "items": {
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
                }
            },
            "required": ["modulo"]
        }
    },
    "required": ["modulos"]
}



# Archivo JSON a validar
archivo_json = '''
{
  "modulos": {
    "modulo": [
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
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema

validate(instance=datos_json, schema=schema)