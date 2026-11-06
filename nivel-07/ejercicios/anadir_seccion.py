# Nivel 7 · Bloque A.2 — Añadir al final con "a" (no borra lo anterior)
with open("secciones.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Sanidad\n")

with open("secciones.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)
