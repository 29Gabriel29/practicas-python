"""
from saludoModulo import hola, holas

print(hola("Gabriel"))

nombres = ["BenedettooooOOOOOaOAAAAAAAAAA", "GOOOOOOOOL", "bokle 1", "River 1111"]
saludos = holas(nombres)

for saludo in saludos.values():
    print(saludo)
"""    
# Esta seria una version, la otra posibilidad es importando el modulo saludos ejemplo:

import saludoModulo

print(saludoModulo.hola("Gabriel"))

nombres = ["Chadoca", "El Rey de VOxer", "Cayo el, el rey de Voxer", "un degenerado con todas las letras"]
saludos = saludoModulo.holas(nombres)

for saludo in saludos.values():
    print(saludo)
       

