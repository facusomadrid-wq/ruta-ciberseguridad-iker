# Plantillas de Python — patrones dominados

> Consultar plantillas **no es trampa**: es infraestructura profesional.
> Regla de oro: **adapta, no copies a ciegas.** Después de pegar, relee nombres, comentarios y mensajes.

## Antes de escribir código: protocolo de 3 capas

1. **Verbaliza:** ¿qué recibe? ¿qué devuelve? ¿qué patrón es?
2. **Pseudocódigo:** escribe los pasos como comentarios en español.
3. **Traduce:** convierte cada comentario en una línea de Python.

## ¿Qué patrón necesito?

| El enunciado dice… | Patrón | Devuelve |
|---|---|---|
| "el mayor", "el más…" | MAX | un elemento |
| "el menor", "el menos…" | MIN | un elemento |
| "total", "suma" | ACUMULADOR | un número |
| "media", "promedio" | MEDIA | un número |
| "**cuántos** cumplen…" | CONTADOR | un número |
| "**los que** cumplen…" | FILTRAR | una lista o diccionario |
| "cuántos hay **de cada**…" | AGRUPAR CONTANDO | un diccionario |

---

## 1. MAX — encontrar el mayor

```python
def encontrar_mayor(lista):
    mayor = lista[0]              # empiezo con el primero (nunca un número inventado)
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor
```

Sobre un diccionario, guardando el nombre:

```python
def mas_veterano(afiliados):
    nombre = None
    max_antiguedad = float("-inf")     # menos infinito: cualquier número es mayor
    for afiliado in afiliados.values():
        if afiliado["antiguedad"] > max_antiguedad:
            max_antiguedad = afiliado["antiguedad"]
            nombre = afiliado["nombre"]
    return nombre
```

⚠️ Nada de `mayor = 0` o `menor = 1000` (números mágicos). Usa `lista[0]` o `float("-inf")` / `float("inf")`.

## 2. MIN — encontrar el menor

Igual que MAX cambiando **un carácter**: `>` por `<` (e inicializando con `lista[0]` o `float("inf")`).

## 3. ACUMULADOR — suma total

```python
def suma(afiliados, campo):
    total = 0                          # aquí sí se empieza en 0
    for afiliado in afiliados.values():
        total += afiliado[campo]       # suma EL VALOR
    return total
```

## 4. MEDIA — promedio

```python
def media(afiliados, campo):
    total = 0
    for afiliado in afiliados.values():
        total += afiliado[campo]
    return total / len(afiliados)      # la división, FUERA del bucle
```

## 5. CONTADOR CON CONDICIÓN — cuántos cumplen

```python
def contar_veteranos(afiliados, anios):
    contador = 0
    for afiliado in afiliados.values():
        if afiliado["antiguedad"] > anios:   # ¡usa el parámetro, no un 10 fijo!
            contador += 1                    # suma UNO, no el valor
    return contador
```

## 6. FILTRAR — los que cumplen

Sobre una lista:

```python
def filtrar_aprobados(notas):
    aprobados = []
    for nota in notas:
        if nota >= 5:
            aprobados.append(nota)
    return aprobados
```

Sobre un diccionario (necesitas el ID → `.items()`):

```python
def filtrar_por_cargo(afiliados, cargo):
    filtrados = {}
    for id_afiliado, datos in afiliados.items():
        if datos["cargo"].startswith(cargo):     # "delegad" → delegado y delegada
            filtrados[id_afiliado] = datos       # cajón con el ID, dentro la ficha entera
    return filtrados
```

⚠️ `.startswith("")` deja pasar **a todos** (todo texto empieza por "nada").

## 7. AGRUPAR CONTANDO — cuántos de cada

```python
def contar_por_seccion(afiliados):
    contador_secciones = {}
    for afiliado in afiliados.values():
        seccion = afiliado["seccion"]
        if seccion in contador_secciones:
            contador_secciones[seccion] += 1
        else:
            contador_secciones[seccion] = 1
    return contador_secciones
```

### CONTAR frente a FILTRAR (la analogía del archivador)

```
CONTAR   →  mueble[etiqueta] = número          {"Central": 4}
FILTRAR  →  mueble[ID] = ficha completa        {"002": {"nombre": "Luis", ...}}
```

---

## Bonus: función universal con parámetro (DRY)

En vez de `media_edad()`, `media_cuota()`, `media_antiguedad()`… una sola:

```python
media(afiliados, "edad")
media(afiliados, "cuota_mensual")
```

## Bonus: función principal (el coordinador)

```python
def realizar_informe(afiliados):
    media_edad = media(afiliados, "edad")      # invoca a las demás…
    print(f"Edad media: {media_edad:.2f}")     # …e imprime
# al final del archivo, UNA línea:
realizar_informe(afiliados_facuso)
```

## Archivos (Nivel 7)

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:   # w = borra y escribe
    archivo.write("Línea\n")

with open("notas.txt", "a", encoding="utf-8") as archivo:   # a = añade al final
    archivo.write("Otra línea\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:   # r = solo leer
    for linea in archivo:
        print(linea.strip())     # strip() quita el \n (si no, print pone otro)
```

⚠️ Antes de ejecutar algo que toca un archivo, **mira la letra del `open`**.

---

## Glosario rápido

```python
for clave in d:                  # solo claves
for valor in d.values():         # solo valores
for clave, valor in d.items():   # ambos

texto.split()  texto.lower()  texto.upper()  texto.strip()  texto.startswith("x")
palabra[0]     palabra[-1]     len(texto)

f"{valor:.2f}"   f"{texto:<20}"   f"{texto:>20}"   f"{texto:^20}"
```

La versión Word original está en `Plantillas_Python_Iker.docx`.
