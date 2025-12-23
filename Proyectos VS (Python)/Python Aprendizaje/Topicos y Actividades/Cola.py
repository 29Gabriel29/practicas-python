cola = []
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

print(cola)
cola.pop(0)
print(cola)
# simulo el efecto cola

from collections import deque
# importo una funcion de collections para usar colas

cola1 = deque()
print(cola1)
cola1.append(4)
cola1.append(5)
cola1.append(6)
cola1.append(8)
print(cola1)

cola1.popleft()
# retira elemnto de la izquierda por lo que respeta la teoria de la cola (First in first out)
