def calcular_media(valores):
    suma = sum(valores)
    cantidad_valores = len(valores)
    media = suma / cantidad_valores
    return media

# Ejemplo de uso
valores = [5, 2, 9, 1, 7, 6, 3]
media = calcular_media(valores)
print("La media de la lista de valores es:", media)
