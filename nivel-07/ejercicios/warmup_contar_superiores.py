# Nivel 7 · Warm-up — Patrón CONTADOR (no FILTRAR: el enunciado pedía "cuántas")
ANCHO = "=" * 40
SEPARADOR = "-" * 40

cuotas = [25.50, 30.00, 25.50, 35.00, 25.50]

def contar_superiores(lista, limite):
    contador = 0                       # contador que empieza en 0
    for elemento in lista:             # recorro todos
        if elemento > limite:          # si es mayor...
            contador += 1              # sumo 1
    return contador                    # devuelvo el total

total_superiores = contar_superiores(cuotas, 26)

print(ANCHO)
print("CUOTAS MAYORES QUE EL LÍMITE")
print(ANCHO)
print(f"En esta lista hay {total_superiores} cuotas mayores que el límite.")
print(SEPARADOR)
