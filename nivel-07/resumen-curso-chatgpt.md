# Resumen del curso de ChatGPT: Python aplicado a la ciberseguridad

Curso hecho en paralelo en octubre de 2026 e integrado en esta ruta. El proyecto continúa en [`analizador-registros/`](analizador-registros/).

## 1. Qué es un log

Un registro de eventos de un sistema: inicios de sesión, errores, accesos.
Un intento fallido de inicio de sesión es un **evento que se analiza**, no un error del programa. Varios fallos seguidos pueden ser sospechosos, pero por sí solos no demuestran un ataque.

## 2. Contadores y condiciones

```python
fallos = 0
if resultado == "FALLO":
    fallos += 1
```

→ En esta ruta: patrón **CONTADOR** (Nivel 6).

## 3. Bucles y `continue`

```python
for resultado in resultados:
    print(resultado)
```

`continue` salta el resto de la vuelta actual y pasa a la siguiente.

## 4. Separar los campos con `split("|")`

```python
campos = linea.split("|")
usuario = campos[0]
resultado = campos[1]
```

Los índices empiezan en 0.

## 5. Contadores por usuario

```python
if usuario not in fallos_por_usuario:
    fallos_por_usuario[usuario] = 0
fallos_por_usuario[usuario] += 1
```

→ En esta ruta: patrón **AGRUPAR CONTANDO** (`contar_por_seccion`, Nivel 6).

## 6. Validación de datos: no confiar en lo que llega

```python
if len(campos) != 2:
    print("Registro incorrecto")
    continue

if resultado not in ["OK", "FALLO"]:
    print("Resultado no reconocido")
    continue
```

Una línea incompleta y un resultado desconocido son problemas distintos. En ambos casos se marca el error y se sigue analizando.

## 7. Registrar errores en un archivo

```python
with open("errores.log", "a", encoding="utf-8") as archivo:
    archivo.write("ERROR detectado\n")
```

`"a"` añade y conserva; `"w"` puede borrar lo anterior; `"r"` lee.
→ En esta ruta: Bloque A del Nivel 7.

## 8. Fecha y hora con `datetime`

```python
from datetime import datetime
ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Si `ahora` se calcula **antes** del bucle, todos los errores tienen la misma hora; **dentro**, cada uno la suya.

## 9. Leer archivos línea a línea

```python
with open("registros.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        print(linea)
```

→ En esta ruta: ejercicio A.3 (`leer_lineas.py`).

## Pendiente al unificar

- Integrar la lectura de `registros.txt` en el analizador → **`analizador_v1.py`**
- Probar con registros válidos, incompletos y resultados desconocidos
- `try/except` si falta el archivo o no hay permisos → Bloque B
- Detectar usuarios vacíos y no exponer información sensible en los registros
- Redes, IP, puertos y DNS → Fase 2

## Consejo final del curso (sigue vigente)

> Consolidar la capacidad de leer un programa, **predecir** qué hará y **explicar** por qué, antes que aprender muchas instrucciones nuevas.
