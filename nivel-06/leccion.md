# Nivel 6 — Funciones

## Qué se vio

- `def`, parámetros, `return`, invocación.
- Familia **MAX/MIN sobre strings** (F.14–F.19): frase con más/menos palabras, caracteres, vocales, mayúsculas, palabras que empiezan o terminan en vocal.
- Funciones que llaman a funciones (`contar_palabras` dentro de `frase_mas_larga`).
- **Funciones universales** con parámetro `campo` (DRY).
- `float("inf")` y `float("-inf")`.
- Devolver varios valores (tupla) y **desempaquetar**: `a, b, c, d = analizar_afiliados(...)`.
- Devolver diccionarios: agrupar contando y filtrar.
- `.startswith()` para coincidencias por raíz (delegado/delegada).
- **Función principal** que coordina a las demás.

## Proyecto grande: informe FAC-USO con funciones

`ejercicios/proyecto_nivel6_final.py`

| Función | Patrón |
|---|---|
| `media(afiliados, campo)` | MEDIA universal |
| `suma(afiliados, campo)` | ACUMULADOR universal |
| `analizar_afiliados(afiliados)` | MAX + MIN en un solo recorrido (decisión consciente) |
| `contar_veteranos(afiliados, anios)` | CONTADOR |
| `contar_por_seccion(afiliados)` | AGRUPAR CONTANDO |
| `contar_por_cargo(afiliados)` | AGRUPAR CONTANDO |
| `filtrar_por_cargo(afiliados, cargo)` | FILTRAR (con `.startswith`) |
| `realizar_informe(afiliados)` | Coordinador: invoca a todas e imprime |

## Bugs cazados (y cómo)

1. `afiliados_facuso` global dentro de `media`/`suma` → test con otro diccionario.
2. `10` fijo en `contar_veteranos` → test con umbrales 5 y 15.
3. `contar_por_cargo` usaba la global → test con un diccionario de "tesoreros".
4. `filtrar_por_cargo` con `"delegad"` fijo → test con "presidente".
5. `NameError` en la línea 117 → la sangría dejaba los prints fuera de la función.
6. Confusión CONTAR/FILTRAR → analogía del archivador (mueble, cajón, carpeta).

## Concepto clave: el archivador

```
diccionario = mueble · clave = etiqueta del cajón · valor = contenido
mueble[etiqueta] = contenido
```
