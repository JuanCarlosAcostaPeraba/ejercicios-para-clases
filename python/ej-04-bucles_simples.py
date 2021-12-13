"""
Con los siguintes datos se obtendrán los
aprobados de FP1. Hacer un programa que
devuelva una lista con los aprobados y otra
con los suspendidos
Requisito: si z < 10/3, se cuenta como 0
"""

# Datos de las notas: [c, z]
datos = [[8.2, 7.1], [0.0, 5.1], [9.0, 8.8], [5.0, 3.1], [8.4, 4.6], [7.2, 2.0], [5.0, 4.1], [9.2, 7.4], [4.9, 4.4], [7.9, 8.8]]

def nota_final(c, z):
    return (0.6 * c) + (z * ((10 - (0.6 * c)) / 10))

# Esccribe tu código aquí