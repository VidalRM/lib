# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calcular_mediana(valores):
    # Ordenar la lista de valores
    valores_ordenados = sorted(valores)

    # Calcular la cantidad de valores en la lista
    cantidad_valores = len(valores_ordenados)

    # Calcular el índice central
    indice_central = cantidad_valores // 2

    if cantidad_valores % 2 == 0:
        # Si la cantidad de valores es par, calcular la mediana como el promedio de los dos valores centrales
        mediana = (valores_ordenados[indice_central - 1] + valores_ordenados[indice_central]) / 2
    else:
        # Si la cantidad de valores es impar, la mediana es el valor central
        mediana = valores_ordenados[indice_central]

    return mediana


# Ejemplo de uso
valores = [5, 2, 9, 1, 7, 6, 3]
mediana = calcular_mediana(valores)
print("La mediana de la lista de valores es:", mediana)