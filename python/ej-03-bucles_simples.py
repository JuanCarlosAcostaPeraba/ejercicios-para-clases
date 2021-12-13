"""
Utilizando una lista de 10 números aleatorios,
crear una lista nueva que incluya
sólo los numeros pares y otra
que incluya sus índices
"""

import random

lista = []

while len(lista) < 10:
    r = random.randint(1, 100)
    if r not in lista:
        lista.append(r)

# Esccribe tu código aquí