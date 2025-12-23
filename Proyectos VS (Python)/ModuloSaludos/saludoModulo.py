import random
from typing import List, Dict


def formato_aleatorio()->str:
    """
    Retorna un saludo aleatorio formateando con el nombre proporcionado

    Returns:
       str: Saludo aleatorio con el formato adecuado
    """
    formatos = [
        "!Hola, {}¡ !Bienvenido :)¡",
        "!Es Genial verte, {}¡",
        "¡Saludos, {}¡ !Me encanta tenerte aqui nuevamente¡",
    ]

    return random.choice(formatos)


def hola(nombre:str)->str:
    """
    Genera un saludo personalizado usando nombre.

    args: 
           nombre (str): Nombre del destinatario del saludo.

    Returns:
           str: saludo personalizado.
    """
    if nombre == "":
        return "Error: Nombre vacio :/"
    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres:List)->Dict:
    """
    Genera saludos personalizados para una lista de nombre.

    args: 
            nombres (List[str]): Lista de nombres para los cuales se generaran saludos

    Returns:
            dict[str, str]: Diccionario donde las claves son nombres y los valores son saludos personalizados
    """

    saludos = {}

    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos



