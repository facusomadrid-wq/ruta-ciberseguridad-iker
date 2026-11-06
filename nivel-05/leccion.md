# Nivel 5 — Diccionarios e informes

## Qué se vio

- **Diccionarios anidados:** un diccionario cuyos valores son otros diccionarios (`afiliados["AF-001"]["edad"]`).
- Recorrer con `.values()` (solo fichas) y `.items()` (ID + ficha).
- **Agrupar contando** con `if clave in diccionario` y con `Counter` de `collections`.
- **Agrupar en listas:** `por_sector[sector].append(nombre)`.
- `sum(... for ... in ...)` para totales en una línea.
- Formato de informes: `.ljust()`, `.rjust()`, `.center()`, `f"{valor:.2f}"`, constantes `ANCHO` y `SEPARADOR`.

## Proyecto final

`ejercicios/informe_facuso_nivel5.py`: informe completo de afiliados con totales, medias, distribución por provincia, por tipo de cuota, recaudación por provincia y afiliados por sector.

## Lo que aprendí a base de errores

- Construir el diccionario agrupado **una vez** y luego imprimir, en vez de volver a filtrar dentro de los prints.
- Alinear columnas hace el informe legible: concepto a la izquierda, valor a la derecha.
