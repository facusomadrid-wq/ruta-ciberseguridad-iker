# Nivel 7 · Bloques A.3 y B.2 — Leer línea a línea y protegerse si falta el archivo
contador = 0                                        # empieza en 0

try:
    with open("secciones.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            limpia = linea.strip()                  # quita el \n que viene pegado
            contador += 1                           # suma uno por cada línea
            print(f"{contador}. {limpia}")          # número y sección
    print(f"Total: {contador} secciones")           # dentro del try: solo si se leyó bien
except FileNotFoundError:
    print("No encuentro el archivo de secciones. Revisa el nombre.")
