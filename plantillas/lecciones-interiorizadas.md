# Lecciones interiorizadas

Cada una salió de un error real. Por eso se recuerdan.

| # | Lección | De dónde salió |
|---|---|---|
| 1 | **Inicialización correcta:** `lista[0]` o `float("inf")` / `float("-inf")` en MAX/MIN; `0` en acumuladores y contadores. Nunca números mágicos. | F.14: `min_palabras = 1000` |
| 2 | **Lectura activa del enunciado:** "cuántos" = CONTAR; "los que" = FILTRAR; "más" = MAX; "menos" = MIN. | F.16 (comprensión invertida) y warm-up del Nivel 7 (devolví una lista en vez de un número) |
| 3 | **Copy-paste-modify:** al adaptar código, relee TODO: nombres, comentarios, mensajes y operadores. | F.19: cuatro restos de F.18 |
| 4 | **Ámbito:** dentro de una función se usa el parámetro, nunca la variable global. Y lo de dentro no se ve desde fuera. | `media`, `suma`, `contar_por_cargo` (global dentro) y `NameError` línea 117 (local fuera) |
| 5 | **Parámetro ignorado:** si recibes `anios` o `cargo`, úsalo; no escribas `10` ni `"delegad"` dentro. | `contar_veteranos` y `filtrar_por_cargo` |
| 6 | **Probar con OTRO diccionario** destapa los bugs silenciosos. | Cuatro veces en el proyecto del Nivel 6 |
| 7 | **La máquina es la verdad:** ejecuta en vez de contar de cabeza. | Conteos mentales erróneos (también los de Claude) |
| 8 | **Responsabilidad única:** cada función hace una cosa. Excepción consciente: `analizar_afiliados`. | Fase 2 del Nivel 6 |
| 9 | **DRY:** si tres funciones solo cambian el campo, haz una con parámetro. | `media(afiliados, campo)`, descubierta "de chiripa" |
| 10 | **Primero funciona, después bonito.** | F.15 |
| 11 | **Protocolo 3 capas** cuando estás en frío: verbalizar → pseudocódigo → traducir. | Bloqueo de 20 minutos en la Fase 3 |
| 12 | **Deshielo progresivo:** los días de pausa enfrían, no borran. El primer ejercicio cuesta; el tercero fluye. | Vueltas tras varios días |
| 13 | **Sangría = pertenencia:** 4 espacios dentro, 0 espacios fuera. | Mudanza a la función principal |
| 14 | **Nombres distintos dentro y fuera** (parámetro `afiliados`, global `afiliados_facuso`) para que el bug de ámbito salte a la vista. | `realizar_informe(afiliados_facuso)` |
| 15 | **El archivo no se toca, se aprende a leer:** el problema del doble salto se arregla al leer (`.strip()`), no quitando los `\n` al escribir. | Ejercicio A.3 |
| 16 | **Mirar la letra del `open`** antes de ejecutar: `"w"` borra, `"a"` añade, `"r"` solo lee. | Predicciones del Bloque A |
| 17 | **Contar líneas, no palabras:** `split()` cuenta palabras ("Recursos Humanos" = 2). | Ejercicio A.3 |
| 18 | **Un programa que falla no debe decir nada falso:** el resultado va dentro del `try`, no después. | B.2: "Total: 0 secciones" sin haber leído el archivo |
| 19 | **Dos pruebas siempre:** la que debe salir bien y la que debe fallar bien. | B.2 |
| 20 | **No confiar en los datos que llegan:** validar estructura y valores antes de usarlos. | Analizador de registros (curso ChatGPT) |
| 21 | **Pedir ayuda con precisión:** "ayúdame sin decirme qué poner". | Fase 3 del Nivel 6 |

## Manifiesto

> "Sin culpa y sin prisa, para ser un buen profesional."
> "Hasta que hacerlo sea automático."
> "No pienso rendirme y voy a conseguir aprender a programar bien."
