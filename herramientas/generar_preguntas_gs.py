"""
Convierte repaso/preguntas.csv (fuente única) en app-apps-script/Preguntas.gs.

Uso, desde la carpeta raíz del repositorio:
    python herramientas/generar_preguntas_gs.py

Después: pega Preguntas.gs en el editor de Apps Script y ejecuta recargarPreguntas().
"""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "repaso" / "preguntas.csv"
DESTINO = RAIZ / "app-apps-script" / "Preguntas.gs"

COLUMNAS = ["id", "nivel", "tema", "pregunta", "codigo",
            "opcion_a", "opcion_b", "opcion_c", "opcion_d",
            "correcta", "explicacion"]


def leer_preguntas(ruta):
    # utf-8-sig: acepta el CSV con o sin la marca BOM que añade Excel
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        cabecera = archivo.readline()
        separador = ";" if cabecera.count(";") > cabecera.count(",") else ","
        archivo.seek(0)
        return list(csv.DictReader(archivo, delimiter=separador))


def validar(preguntas):
    errores = []
    vistos = set()
    for numero, p in enumerate(preguntas, start=2):      # fila 1 = cabecera
        faltan = [c for c in COLUMNAS if c not in p]
        if faltan:
            errores.append(f"Fila {numero}: faltan columnas {faltan}")
            continue
        if not p["id"].strip():
            errores.append(f"Fila {numero}: sin id")
        elif p["id"] in vistos:
            errores.append(f"Fila {numero}: id repetido {p['id']}")
        vistos.add(p["id"])
        if p["correcta"].strip().upper() not in ("A", "B", "C", "D"):
            errores.append(f"Fila {numero} ({p['id']}): 'correcta' debe ser A, B, C o D")
        if not p["nivel"].strip().isdigit():
            errores.append(f"Fila {numero} ({p['id']}): 'nivel' debe ser un número")
    return errores


def main():
    try:
        preguntas = leer_preguntas(ORIGEN)
    except FileNotFoundError:
        print(f"No encuentro {ORIGEN}. ¿Estás en la carpeta raíz del repositorio?")
        return

    errores = validar(preguntas)
    if errores:
        print("❌ El CSV tiene errores. No se ha generado nada:")
        for e in errores:
            print("  -", e)
        return

    limpias = []
    for p in preguntas:
        fila = {c: p[c].strip() if c != "codigo" else p[c].rstrip() for c in COLUMNAS}
        fila["nivel"] = int(fila["nivel"])
        fila["correcta"] = fila["correcta"].upper()
        limpias.append(fila)

    contenido = (
        "// ARCHIVO GENERADO AUTOMÁTICAMENTE — no lo edites a mano.\n"
        "// Fuente: repaso/preguntas.csv  ·  Generador: herramientas/generar_preguntas_gs.py\n"
        "const PREGUNTAS = "
        + json.dumps(limpias, ensure_ascii=False, indent=1)
        + ";\n"
    )
    DESTINO.write_text(contenido, encoding="utf-8")
    print(f"✅ {len(limpias)} preguntas → {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
