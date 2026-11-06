# Nivel 7 · Bloque A.1 — Escribir un archivo con "w" (borra y empieza de cero)
with open("secciones.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Central\n")
    archivo.write("Territorial\n")
    archivo.write("Comunicación\n")

with open("secciones.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)
