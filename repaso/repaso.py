"""
REPASO DEL CURSO — calentamientos de la ruta
=============================================

Este programa YA FUNCIONA: te hace 5 preguntas al azar de preguntas.csv.
Tiene 4 HUECOS: úsalos como calentamiento de 5 minutos al empezar las sesiones.
Mientras no los rellenes:
  - si falta preguntas.csv, el programa se rompe con un error rojo   (HUECO 1)
  - no filtra por nivel: pregunta de todos                         (HUECO 2)
  - no guarda tu progreso en progreso.txt                          (HUECO 3)
  - dice siempre "0 aciertos"                                      (HUECO 4)

Cómo ejecutarlo (desde la carpeta repaso):
    python repaso.py

Reglas del juego:
  - Rellena UN hueco cada vez, ejecuta y comprueba.
  - Usa el protocolo de 3 capas: verbaliza → pseudocódigo → traduce.
  - Mira tus plantillas (carpeta plantillas/) antes de pedir ayuda.
"""
import csv
import random

ARCHIVO_PREGUNTAS = "preguntas.csv"
ARCHIVO_PROGRESO = "progreso.txt"
PREGUNTAS_POR_RONDA = 5
ANCHO = "=" * 50
SEPARADOR = "-" * 50


# ---------------------------------------------------------------------------
# HUECO 1 — Bloque B (try / except)
# Ahora mismo, si preguntas.csv no existe, Python se para con FileNotFoundError.
# Objetivo: que muestre un mensaje claro en español y devuelva una lista vacía [].
# Pista: envuelve el "with open(...)" en un try, y captura FileNotFoundError.
# ---------------------------------------------------------------------------
def cargar_preguntas(ruta):
    # csv.DictReader convierte cada fila del CSV en un diccionario:
    #   {"id": "N6-01", "nivel": "6", "pregunta": "...", "correcta": "B", ...}
    # (lo verás a fondo en el Bloque C; de momento úsalo tal cual)
    try:
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        print("No encuentro el archivo preguntas.csv. Comprueba el nombre y que esté en la carpeta.")
        return []


# ---------------------------------------------------------------------------
# HUECO 2 — Patrón FILTRAR (Nivel 6)
# Objetivo: devolver SOLO las preguntas cuyo "nivel" sea igual al pedido.
# Si nivel es "" (el usuario pulsó Intro sin escribir), devolver todas.
# Ojo: en el CSV el nivel es TEXTO ("6"), y lo que escribe el usuario también.
# Pista: lista vacía al principio, for, if, append. Y… ¿usas el parámetro? 😉
# ---------------------------------------------------------------------------
def filtrar_por_nivel(preguntas, nivel):
    return preguntas  # ← sustituye esta línea por tu filtro


# ---------------------------------------------------------------------------
# (Ya hecho) Muestra una pregunta y devuelve True si aciertas, False si fallas
# ---------------------------------------------------------------------------
def hacer_pregunta(numero, pregunta):
    print(SEPARADOR)
    print(f"{numero}. [{pregunta['tema']}] {pregunta['pregunta']}")
    if pregunta["codigo"].strip():
        print()
        for linea in pregunta["codigo"].splitlines():
            print("    " + linea)
        print()
    # Barajamos las opciones para que la correcta no esté siempre en la misma letra
    correcta_original = pregunta["correcta"].strip().upper()
    opciones = []
    for letra in ("A", "B", "C", "D"):
        opciones.append((pregunta["opcion_" + letra.lower()], letra == correcta_original))
    random.shuffle(opciones)

    letra_correcta = ""
    for letra, (texto, es_correcta) in zip("ABCD", opciones):
        print(f"   {letra}) {texto}")
        if es_correcta:
            letra_correcta = letra

    respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
    acierto = respuesta == letra_correcta

    if acierto:
        print("✅ ¡Correcto!")
    else:
        print(f"❌ La correcta era la {letra_correcta}.")
    print(f"💡 {pregunta['explicacion']}")
    return acierto


# ---------------------------------------------------------------------------
# HUECO 3 — Bloque A (escribir en archivo)
# Objetivo: AÑADIR una línea al final de progreso.txt, SIN borrar lo anterior.
# Formato de la línea:  N6-01;acierto   o   N6-01;fallo
# Pista: ¿qué letra del open añade sin borrar? No olvides el \n final.
# ---------------------------------------------------------------------------
def guardar_resultado(ruta, id_pregunta, acierto):
    pass  # ← sustituye esta línea


def main():
    print(ANCHO)
    print("REPASO DEL CURSO DE PYTHON".center(50))
    print(ANCHO)

    preguntas = cargar_preguntas(ARCHIVO_PREGUNTAS)
    if not preguntas:
        print("No hay preguntas para repasar. Fin.")
        return

    nivel = input("¿Qué nivel quieres repasar? (5, 6, 7 o Intro para todos): ").strip()
    seleccion = filtrar_por_nivel(preguntas, nivel)
    if not seleccion:
        print(f"No hay preguntas del nivel {nivel}.")
        return

    random.shuffle(seleccion)
    ronda = seleccion[:PREGUNTAS_POR_RONDA]

    aciertos = 0
    for numero, pregunta in enumerate(ronda, start=1):
        acierto = hacer_pregunta(numero, pregunta)
        # -------------------------------------------------------------------
        # HUECO 4 — Patrón CONTADOR (Nivel 6)
        # Objetivo: si acierto es True, sumar 1 a aciertos.
        # -------------------------------------------------------------------
        guardar_resultado(ARCHIVO_PROGRESO, pregunta["id"], acierto)

    print(ANCHO)
    print(f"Resultado: {aciertos} de {len(ronda)} aciertos")
    print(ANCHO)


main()
