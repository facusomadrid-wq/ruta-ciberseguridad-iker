# Nivel 7 — Archivos, errores y validación de datos

## Plan del nivel

| Bloque | Contenido | Estado |
|---|---|---|
| A | Escribir y leer archivos de texto | ✅ |
| B.1–B.2 | `try / except` con `FileNotFoundError` | ✅ |
| B.3 | Validar datos: `split("|")`, `continue`, valores permitidos, `ValueError` | ⏳ siguiente |
| B.4 | Registrar errores con fecha (`datetime`) sin exponer datos sensibles | ⏳ |
| C | Archivos CSV | ⏳ |
| **Proyecto** | [`analizador-registros/`](analizador-registros/) | 🔄 v0 hecha |

También: [`resumen-curso-chatgpt.md`](resumen-curso-chatgpt.md), lo aprendido en paralelo e integrado aquí.

## Bloque A — lo aprendido

```python
with open("secciones.txt", "w", encoding="utf-8") as archivo:   # w: borra y escribe
with open("secciones.txt", "a", encoding="utf-8") as archivo:   # a: añade al final
with open("secciones.txt", "r", encoding="utf-8") as archivo:   # r: solo lee
```

- `with` cierra el archivo solo al salir del bloque.
- `encoding="utf-8"` para tildes y ñ.
- `\n` = salto de línea. Se guarda en el archivo y vuelve pegado al leer.
- `print` añade su propio salto → doble salto. Se arregla con `.strip()` **al leer**.
- `for linea in archivo:` recorre el archivo renglón a renglón.
- Windows oculta las extensiones: actívalas en *Ver → Mostrar → Extensiones de nombre de archivo*.

> "Hay que tener cuidado de no pisar con write lo que ya tengas en el archivo; eso en un RAG de verdad te lo cargas."

## Bloque B — lo aprendido

```python
try:
    with open("secciones.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            ...
    print(f"Total: {contador} secciones")      # dentro del try: solo si se leyó bien
except FileNotFoundError:
    print("No encuentro el archivo de secciones. Revisa el nombre.")
```

- Cuando Python encuentra un error, **se para en seco**: lo que venía después no se ejecuta.
- Leer el mensaje rojo: la **línea** y el **nombre del error** (la palabra antes de los dos puntos).
- Si falla algo dentro del `try`, Python salta al `except` y **se salta el resto del `try`**.
- Un programa que falla **no debe decir nada falso** ("Total: 0" cuando no sabe cuántas hay).
- Siempre **dos pruebas**: la que debe salir bien y la que debe fallar bien.

## Ejercicios

- `warmup_contar_superiores.py` — CONTADOR (no FILTRAR)
- `secciones.py` — escribir con `"w"`
- `anadir_seccion.py` — añadir con `"a"`
- `leer_lineas.py` — leer, limpiar, numerar y contar
