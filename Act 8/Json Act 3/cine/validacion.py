import json
from jsonschema import validate

# Esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "codigo": {
            "type": "string",
            "pattern": "^\\d{3}$"
        },
        "nombre": {
            "type": "string"
        },
        "director": {
            "type": "string"
        },
        "fechaEstreno": {
            "type": "string",
            "format": "date"
        },
        "personajes": {
            "type": "string"
        },
        "salas": {
            "type": "string"
        },
        "compañiaCinematografica": {
            "type": "string"
        }
    },
    "required": ["codigo", "nombre", "director", "fechaEstreno", "personajes", "salas", "compañiaCinematografica"]
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
          "codigo": "001",
          "nombre": "El señor de los anillos: La comunidad del anillo",
          "director": "Peter Jackson",
          "fechaEstreno": "2001-12-19",
          "personajes": "Frodo, Aragorn, Gandalf",
          "salas": "Sala1, Sala2",
          "compañiaCinematografica": "New Line Cinema"
        },
        {
          "codigo": "002",
          "nombre": "La La Land",
          "director": "Damien Chazelle",
          "fechaEstreno": "2016-12-09",
          "personajes": "Mia, Sebastian",
          "salas": "Sala3, Sala4",
          "compañiaCinematografica": "Summit Entertainment"
        },
        {
          "codigo": "003",
          "nombre": "Inception",
          "director": "Christopher Nolan",
          "fechaEstreno": "2010-07-08",
          "personajes": "Cobb, Ariadne, Eames",
          "salas": "Sala5, Sala6",
          "compañiaCinematografica": "Warner Bros."
        },
        {
          "codigo": "004",
          "nombre": "Avengers: Endgame",
          "director": "Anthony and Joe Russo",
          "fechaEstreno": "2019-04-26",
          "personajes": "Iron Man, Captain America, Thor",
          "salas": "Sala7, Sala8",
          "compañiaCinematografica": "Marvel Studios"
        },
        {
          "codigo": "005",
          "nombre": "Harry Potter and the Sorcerer's Stone",
          "director": "Chris Columbus",
          "fechaEstreno": "2001-11-16",
          "personajes": "Harry, Hermione, Ron",
          "salas": "Sala9, Sala10",
          "compañiaCinematografica": "Warner Bros."
        },
        {
          "codigo": "006",
          "nombre": "The Shawshank Redemption",
          "director": "Frank Darabont",
          "fechaEstreno": "1994-09-23",
          "personajes": "Andy Dufresne, Red",
          "salas": "Sala11, Sala12",
          "compañiaCinematografica": "Columbia Pictures"
        },
        {
          "codigo": "007",
          "nombre": "The Dark Knight",
          "director": "Christopher Nolan",
          "fechaEstreno": "2008-07-18",
          "personajes": "Batman, Joker, Harvey Dent",
          "salas": "Sala13, Sala14",
          "compañiaCinematografica": "Warner Bros."
        },
        {
          "codigo": "008",
          "nombre": "Titanic",
          "director": "James Cameron",
          "fechaEstreno": "1997-12-19",
          "personajes": "Jack, Rose",
          "salas": "Sala15, Sala16",
          "compañiaCinematografica": "Paramount Pictures"
        },
        {
          "codigo": "009",
          "nombre": "Forrest Gump",
          "director": "Robert Zemeckis",
          "fechaEstreno": "1994-07-06",
          "personajes": "Forrest Gump, Jenny",
          "salas": "Sala17, Sala18",
          "compañiaCinematografica": "Paramount Pictures"
        },
        {
          "codigo": "010",
          "nombre": "Toy Story 4",
          "director": "Josh Cooley",
          "fechaEstreno": "2019-06-11",
          "personajes": "Woody, Buzz Lightyear, Bo Peep",
          "salas": "Sala19, Sala20",
          "compañiaCinematografica": "Walt Disney Pictures"
        }
    
    '''
    


# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
