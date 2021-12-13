"""
Con una lista con 10 números enteros con valores
distintos y arbitrarios de 0 a 100. Programar una
función que encuentre el mayor de ellos y que de
su posición en la lista
"""

import random

lista = []

while len(lista) < 10:
    r = random.randint(1, 100)
    if r not in lista:
        lista.append(r)

# Esccribe tu código aquí