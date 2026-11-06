# Informe para Claude Code — App de aprendizaje a medida de Iker

> **Para Claude Code:** este documento es tu punto de partida. Léelo entero junto con `CLAUDE.md` y `ROADMAP.md` antes de proponer nada. **No escribas código hasta presentar un plan y recibir la aprobación de Iker.**
>
> **Para Iker:** aquí está todo lo hecho, lo que viene y lo que tiene que construir la app. Si algo no te cuadra, se cambia antes de empezar.

Fecha: 1 de noviembre de 2026

---

## Índice

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Quién es el alumno](#2-quién-es-el-alumno)
3. [Cómo se trabaja: el método](#3-cómo-se-trabaja-el-método)
4. [Todo lo hecho hasta hoy](#4-todo-lo-hecho-hasta-hoy)
5. [Lecciones interiorizadas y errores recurrentes](#5-lecciones-interiorizadas-y-errores-recurrentes)
6. [El programa que vamos a seguir](#6-el-programa-que-vamos-a-seguir)
7. [Estado exacto donde lo dejamos](#7-estado-exacto-donde-lo-dejamos)
8. [Lo que ya existe en el repositorio](#8-lo-que-ya-existe-en-el-repositorio)
9. [La app a medida: especificación](#9-la-app-a-medida-especificación)
10. [Arquitectura técnica propuesta](#10-arquitectura-técnica-propuesta)
11. [Fases de implementación](#11-fases-de-implementación)
12. [Seguridad y privacidad](#12-seguridad-y-privacidad)
13. [Plan de pruebas y despliegue](#13-plan-de-pruebas-y-despliegue)
14. [Decisiones abiertas para Iker](#14-decisiones-abiertas-para-iker)
15. [Instrucciones operativas para Claude Code](#15-instrucciones-operativas-para-claude-code)

---

## 1. Resumen ejecutivo

> **Actualización 04/11/2026:** el objetivo profesional es **trabajar en remoto en Anthropic** (seguridad de la IA), con horizonte de 2 años. Se añade la pista paralela **Inglés + Portafolio** (ver `ROADMAP.md`) y el módulo **M11**. Todo el código nuevo de Iker va en inglés.

- **Objetivo profesional de Iker:** dedicarse a la **ciberseguridad**. El curso de Python y el curso RAG ya no son proyectos separados: forman **una sola ruta** de 4 fases (Python base → fundamentos de sistemas → RAG seguro → ciberseguridad profesional).
- **Dónde está:** Fase 1, **Nivel 7** (archivos, errores y validación de datos). Bloques A y B.1–B.2 terminados; está a mitad de **B.3**, decidiendo las reglas de validación del **analizador de registros de seguridad**, el proyecto final de la Fase 1.
- **Qué hay construido:** un repositorio (`ruta-ciberseguridad-iker`) con plantillas, lecciones, ejercicios reales, un banco de 56 preguntas, `repaso.py` con 4 huecos de calentamiento y una app de repaso en Apps Script (test, fichas y progreso).
- **Qué se pide ahora:** una **app a medida** que sea el centro de su aprendizaje: le dice qué toca hoy, le permite estudiar y practicar desde el móvil y el PC, repasa con repetición espaciada, registra su progreso y su diario de sesiones, y crece con la ruta hasta la ciberseguridad.
- **Recomendación técnica:** evolucionar la app de Apps Script existente (gratis, la domina, móvil primero, acceso "Solo yo") y añadir ejecución de Python **dentro del navegador** con Pyodide para practicar sin instalar nada.

---

## 2. Quién es el alumno

| Aspecto | Detalle |
|---|---|
| Nombre | Iker González |
| Edad | 47 años |
| Trabajo | FAC-USO Madrid (Administración General del Estado): comunicación, coordinación de información y automatización |
| Experiencia técnica | Mucha en **Google Apps Script** (más de 20 proyectos), automatizaciones con IA. **Python: aprendiendo desde cero** |
| Ritmo | Sesiones de 20–30 minutos, normalmente a primera hora (5:30–8:00). Pausas de días o semanas por trabajo |
| Equipos | PC Windows con VS Code (terminal `cmd`; PowerShell bloquea scripts) y a veces python.codeutility.io. Móvil Android; tiene **presbicia** → letra grande |
| Idioma | Español siempre |

### Cómo aprende (importante para diseñar la app)

- **Le cuesta la sintaxis y lo dice abiertamente.** Reconoce el código cuando lo ve, pero le cuesta escribirlo de memoria (*recognition vs recall*). La app debe entrenar el **recordar**, no solo el reconocer.
- **Llega "en frío"** tras días sin programar. El primer ejercicio cuesta, el segundo menos y el tercero fluye (deshielo progresivo). La app debe empezar siempre con un **calentamiento corto**.
- **Algunos días está "espeso".** Necesita poder pedir una versión más guiada sin sentirse mal.
- **Aprende mucho con analogías:** el archivador con cajones (diccionarios), el despacho y el pasillo (ámbito), la oficina y el coordinador (función principal), la caja llena o vacía (`return []`).
- **Puntos fuertes:** honestidad total sobre sus errores, desconfía de los resultados que "parecen" bien, prueba casos raros, detecta *code smells* por intuición ("la colocación no me convence"), investiga por su cuenta y toma decisiones híbridas propias.
- **Es organizado a su manera**, pero se describe como "un desastre organizativo". La app debe **decirle qué toca hoy** sin que tenga que pensarlo.

### Manifiesto (sus palabras)

> "Sin culpa y sin prisa, para ser un buen profesional."
> "Hasta que hacerlo sea automático."
> "No pienso rendirme y voy a conseguir aprender a programar bien."

---

## 3. Cómo se trabaja: el método

1. **Socrático estricto:** no se le dan soluciones. Se pregunta, se dan pistas y se señala la línea sospechosa sin escribir el arreglo.
2. **Protocolo de 3 capas** cuando se bloquea: verbalizar (qué recibe, qué devuelve, qué patrón es) → pseudocódigo en comentarios → traducir línea a línea. Si sigue atascado: pseudocódigo **con huecos**.
3. **Predecir antes de ejecutar:** "¿qué crees que saldrá?". Luego se ejecuta: **la máquina es la verdad**.
4. **Dos pruebas siempre:** la que debe salir bien y la que debe fallar bien. Y probar con **otros datos** (otro diccionario, valores raros) para cazar bugs silenciosos.
5. **Celebrar lo que hace bien antes de corregir**, sin exagerar.
6. **Conectar cada concepto con la ciberseguridad** y con su futuro RAG.
7. **Proponer cerrar** cuando hay cansancio o bloqueo. Cerrar con victoria.
8. **Plan antes de código** (también para Claude Code) y **plan de pruebas antes de desplegar**.
9. **Regla ética:** todo lo ofensivo, solo en sistemas propios o laboratorios preparados. Nunca sistemas ajenos.

---

## 4. Todo lo hecho hasta hoy

### Niveles 1–4 — Fundamentos ✅
Variables, tipos (`int`, `float`, `str`, `bool`), conversión (`int()`), f-strings, métodos de strings (`upper`, `lower`, `capitalize`, `title`, `replace`, `strip`, `in`, índices `[0]` y `[-1]`), decisiones (`if/elif/else`), bucles, listas (`append`, `insert`, `remove`, `index`), primeras funciones. Entorno: Python 3.14, VS Code, venv, Git instalados.

### Nivel 5 — Diccionarios e informes ✅
- Diccionarios anidados, `.values()`, `.items()`, `Counter`, agrupar contando y agrupar en listas.
- Formato de informes: `ljust`, `rjust`, `center`, `:.2f`, constantes `ANCHO` y `SEPARADOR`.
- **Proyecto:** informe completo de afiliados FAC-USO (totales, medias, por provincia, por tipo de cuota, recaudación, por sector).

### Nivel 6 — Funciones ✅
- Familia MAX/MIN sobre strings (F.14–F.19): más/menos palabras, caracteres, vocales, mayúsculas, palabras que empiezan o terminan en vocal (con tildes y `.lower()`).
- Funciones universales con parámetro `campo` (DRY), `float("inf")` y `float("-inf")`, devolver tuplas y desempaquetar, devolver diccionarios, `.startswith()`, función principal que coordina a las demás.
- **Proyecto grande:** informe FAC-USO con 8 funciones (`media`, `suma`, `analizar_afiliados`, `contar_veteranos`, `contar_por_seccion`, `contar_por_cargo`, `filtrar_por_cargo`, `realizar_informe`). Pasa el test con otros diccionarios.
- **Bugs cazados:** variable global dentro de la función (4 veces), parámetro ignorado (`10` y `"delegad"` fijos), `NameError` por sangría, confusión CONTAR/FILTRAR.

### Nivel 7 — Archivos, errores y validación 🔄
- **Bloque A ✅:** modos `"w"` (borra), `"a"` (añade) y `"r"` (lee); `with`, `encoding="utf-8"`, `\n` y el doble salto con `print`, `.strip()` al leer, recorrer un archivo línea a línea, contar líneas y no palabras. Reflexión propia: *"un `w` en el sitio equivocado se carga un RAG de verdad"*.
- **Bloque B.1–B.2 ✅:** leer el mensaje de error (línea y nombre), `try/except FileNotFoundError`, el `print` del resultado **dentro** del `try` para no decir nada falso, dos pruebas.
- **Hueco 1 de `repaso.py` ✅:** `try/except` + `return []`. Duda resuelta: **una función puede tener dos `return`** porque cada camino tiene su salida ("llena o vacía, pero siempre con caja").
- **Bloque B.3 🔄:** clasificó las 14 líneas de `registros.txt` (ver sección 7).

### Curso paralelo con ChatGPT (integrado) ✅
Logs, contadores por usuario, `split("|")`, `continue`, validación (número de campos y valores permitidos), `errores.log` en modo `"a"`, `datetime` (fuera o dentro del bucle). Resultado: **`analizador_v0.py`**, ya en el repositorio. Decisión: la ruta sigue **solo** en el repositorio; ChatGPT u otras IA, como segunda explicación.

### Infraestructura creada ✅
Repositorio `ruta-ciberseguridad-iker`, plantillas (Word y Markdown), 21 lecciones interiorizadas, banco de 56 preguntas, `repaso.py`, generador CSV → Apps Script y app de repaso en Apps Script (test, fichas y progreso, acceso "Solo yo"). Ver sección 8.

---

## 5. Lecciones interiorizadas y errores recurrentes

| # | Lección | Origen |
|---|---|---|
| 1 | Inicializar con `lista[0]` o `float("±inf")` en MAX/MIN; `0` en contadores. Nunca números mágicos | F.14 |
| 2 | Lectura activa: "cuántos" = CONTAR, "los que" = FILTRAR | F.16 y warm-up Nivel 7 |
| 3 | Copy-paste-modify: releer nombres, comentarios, mensajes y operadores | F.19 |
| 4 | Ámbito: dentro, el parámetro; lo de dentro no se ve desde fuera | Nivel 6 |
| 5 | Parámetro ignorado: si lo recibes, úsalo | `contar_veteranos`, `filtrar_por_cargo` |
| 6 | Probar con OTROS datos destapa bugs silenciosos | Nivel 6 |
| 7 | La máquina es la verdad | Varias |
| 8 | Responsabilidad única (excepción consciente: `analizar_afiliados`) | Nivel 6 |
| 9 | DRY: una función con parámetro en vez de tres | `media(afiliados, campo)` |
| 10 | Primero funciona, después bonito | F.15 |
| 11 | Protocolo de 3 capas cuando estás en frío | Nivel 6 |
| 12 | Deshielo progresivo: las pausas enfrían, no borran | Vueltas tras pausas |
| 13 | Sangría = pertenencia | Función principal |
| 14 | Nombres distintos para parámetro y global | `realizar_informe` |
| 15 | El archivo no se toca: se aprende a leer | A.3 |
| 16 | Mirar la letra del `open` antes de ejecutar | Bloque A |
| 17 | Contar líneas, no palabras | A.3 |
| 18 | Un programa que falla no debe decir nada falso | B.2 |
| 19 | Dos pruebas: la que sale bien y la que falla bien | B.2 |
| 20 | No confiar en los datos que llegan: validar estructura y valores | Analizador |
| 21 | Pedir ayuda con precisión ("sin decirme qué poner") | Nivel 6 |
| 22 | Una función puede tener varios `return`: uno por camino, y siempre devuelve lo prometido (`[]`, no `None`) | Hueco 1 |
| 23 | Normalizar la forma (espacios, mayúsculas) sí; interpretar la intención (sinónimos) no | B.3 |

**Errores que más se repiten** (la app debe reforzarlos con más frecuencia):
1. Usar la variable global en vez del parámetro.
2. Confundir CONTAR y FILTRAR (devolver lista cuando se pide número).
3. Restos de copy-paste (comentarios y nombres sin actualizar).
4. Sangría que deja código fuera de donde debería.
5. Paréntesis innecesarios (`contador = (0)`) y sangrías de 11 espacios.

---

## 6. El programa que vamos a seguir

### Fase 1 — Python base (2–3 meses) · en curso

| Nivel | Bloques | Proyecto |
|---|---|---|
| 7 | B.3 validación (`split`, `continue`, valores permitidos, `ValueError`) · B.4 `datetime` y registros sin datos sensibles · C CSV | **Analizador de registros** v1→v4 |
| 8 | Módulos e `import` propios, JSON, expresiones regulares básicas, `argparse` sencillo | Analizador v5: configurable y con salida JSON |

**Plan de versiones del analizador:**

| Versión | Añade |
|---|---|
| v0 ✅ | Lista en el código, validación básica, `errores.log` con fecha |
| v1 | Leer `registros.txt` + `try/except` si falta |
| v2 | Validación completa con las reglas decididas en B.3 |
| v3 | Organizado en funciones + alerta de usuarios con 3 o más fallos |
| v4 | Resumen alineado y registro de errores sin datos sensibles |

**Calentamientos pendientes** (`repaso.py`): hueco 2 (filtrar por nivel), hueco 3 (guardar progreso con `"a"`), hueco 4 (contar aciertos).

### Fase 2 — Fundamentos de sistemas (3–4 meses)
Terminal Linux (navegación, permisos, procesos, registros del sistema), redes (IP, puertos, protocolos, DNS), la web por dentro (HTTP, cabeceras, cookies), Python para el laboratorio propio (`requests`, herramientas sencillas).

### Fase 3 — RAG seguro (4–5 meses)
Curso RAG ya diseñado (Google Drive API, extracción de documentos, *chunking*, embeddings, base vectorial, Claude API, interfaz web, despliegue en Cloud Run) con la seguridad como pilar: **construir**, **atacar** (inyección de prompts directa e indirecta, documentos maliciosos, fuga de contexto, envenenamiento) y **defender**, documentando cada ataque y su mitigación.

### Fase 4 — Ciberseguridad profesional (continuo)
Blue team (análisis de registros, detección, SOC), normativa (ENS, RGPD), laboratorios legales, certificación de entrada (a elegir comprobando la oferta del momento) y portafolio en GitHub.

---

## 7. Estado exacto donde lo dejamos

**Sesión B.3, 28/10/2026.** Iker clasificó `registros.txt`:

| Línea | Contenido | Su decisión | Estado |
|---|---|---|---|
| 1–7 | registros correctos | ✅ Acepta | Correcto |
| 8 | `ana|FALLIDO` | Zona gris: aceptar sinónimos | **Pendiente** de que decida (propuesta: rechazar y registrar, por lista blanca) |
| 9 | `registro_incompleto` | ❌ Rechaza (un solo campo) | Correcto |
| 10 | `|FALLO` | ❌ Rechaza "por un solo campo" | **Pendiente:** motivo equivocado. `split` da 2 campos (`["", "FALLO"]`); hay que rechazarla por **usuario vacío**. Pregunta abierta para él |
| 11 | `admin|FALLO|extra` | ❌ Rechaza (3 campos) | Correcto |
| 12 | línea vacía | ❌ Rechaza como error | **Pendiente:** ¿error o se ignora en silencio? |
| 13 | `  maria|FALLO  ` | Zona gris | Propuesta: normalizar con `.strip()` y aceptar |
| 14 | `admin|fallo` | Zona gris | Propuesta: normalizar con `.upper()` y aceptar |

**Siguiente sesión:** responder las 3 preguntas pendientes (líneas 10, 12 y 8), fijar las reglas de `analizador_v2.py` y escribir `analizador_v1.py`.

---

## 8. Lo que ya existe en el repositorio

```
ruta-ciberseguridad-iker/
├── README.md · CLAUDE.md · ROADMAP.md · .gitignore
├── plantillas/
│   ├── patrones.md                    7 patrones + archivos + glosario
│   ├── lecciones-interiorizadas.md
│   └── Plantillas_Python_Iker.docx
├── nivel-05/  leccion.md · ejercicios/informe_facuso_nivel5.py
├── nivel-06/  leccion.md · ejercicios/proyecto_nivel6_final.py
├── nivel-07/
│   ├── leccion.md · resumen-curso-chatgpt.md
│   ├── ejercicios/  warmup_contar_superiores.py · secciones.py · anadir_seccion.py · leer_lineas.py
│   └── analizador-registros/  README.md · analizador_v0.py · registros.txt
├── repaso/  preguntas.csv (56, FUENTE ÚNICA) · repaso.py (huecos 2–4 pendientes)
├── herramientas/  generar_preguntas_gs.py (valida el CSV y genera Preguntas.gs)
└── app-apps-script/
    ├── Code.gs        instalar(), recargarPreguntas(), getDatos(), registrarRespuesta()
    ├── Preguntas.gs   generado
    ├── index.html     Inicio · Test · Fichas · Progreso (móvil, modo oscuro)
    ├── appsscript.json  webapp USER_DEPLOYING / MYSELF
    └── DESPLIEGUE.md
```

**Formato de `preguntas.csv`:** `id, nivel, tema, pregunta, codigo, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion`. Las opciones se barajan al mostrarlas (había un sesgo: la B era la correcta en más de la mitad).

**App actual (Apps Script):** Google Sheet con hojas `Preguntas` y `Progreso` (fecha, id, resultado, modo); prioriza las preguntas falladas; valida todo lo que llega del navegador; `LockService` al escribir.

> **Nota:** confirmar con Iker si ya subió el repositorio a GitHub y si la app está desplegada. Si no, ese es el paso 0.

---

## 9. La app a medida: especificación

### Visión

**"Mi ruta"**: la app que Iker abre cada mañana y le dice **qué toca hoy**, le deja **practicar** y **repasar** en el tiempo que tenga, y le muestra **cuánto ha avanzado**. Funciona igual de bien en el móvil (repaso, lectura) que en el PC (ejercicios).

### Principios de diseño

1. **Cero decisiones al abrirla:** una pantalla "Hoy" con un plan según los minutos disponibles.
2. **Recordar, no solo reconocer:** además del test de opciones, ejercicios de escribir código, predecir la salida y encontrar el bug.
3. **Sin culpa:** nada de rachas que castiguen las pausas. Tras una pausa larga, la app propone automáticamente un **calentamiento suave** ("deshielo").
4. **Modo espeso:** un botón que hace la sesión más guiada (más pistas, pseudocódigo con huecos, menos tareas).
5. **Socrática:** las pistas se revelan por niveles; la solución nunca se muestra de entrada.
6. **Accesible:** letra grande (base 19 px o más), alto contraste, modo oscuro, botones de al menos 48 px, sin scroll horizontal en móvil.
7. **Una sola fuente de contenido:** el repositorio (CSV y Markdown). La app no duplica contenido a mano.

### Módulos funcionales

| # | Módulo | Qué hace | Prioridad |
|---|---|---|---|
| M1 | **Hoy** | Pregunta "¿cuánto tiempo tienes?" (10 / 20 / 30 min) y genera la sesión: calentamiento → tarea principal → repaso. Detecta pausas largas y propone deshielo. Botón "modo espeso" | Alta |
| M2 | **Ruta y progreso** | Fases → niveles → bloques con estado (pendiente, en curso, hecho). Barra de progreso. Fuente: `ROADMAP.md` o una hoja `Ruta` | Alta |
| M3 | **Repaso espaciado** | Evoluciona el test y las fichas actuales con repetición espaciada (tipo Leitner o SM-2 simplificado): cada pregunta tiene una próxima fecha; las falladas vuelven antes. Etiqueta de "error recurrente" para los 5 errores de la sección 5 | Alta |
| M4 | **Ejercicios de código** | Tipos: **predecir la salida**, **encontrar el bug**, **completar huecos**, **escribir la función**. Ejecución de Python en el navegador (Pyodide) con tests ocultos que comprueban el resultado, incluidas las "dos pruebas" (caso normal y caso que debe fallar bien). Pistas en 3 niveles | Media-alta |
| M5 | **Biblioteca** | Plantillas, lecciones, glosario y analogías, con buscador. Lectura cómoda en el móvil. Fuente: los `.md` del repositorio | Media |
| M6 | **Diario de sesiones** | Al cerrar: qué hice, qué me costó, cómo me sentí (fresco / normal / espeso), siguiente paso. Sirve para retomar tras pausas ("la última vez lo dejaste en…") | Media |
| M7 | **Mis errores** | Registro de los errores cometidos (tipo, ejemplo, lección relacionada). Alimenta el repaso espaciado | Media |
| M8 | **Proyectos** | Seguimiento del analizador de registros por versiones (v0–v5) y, más adelante, del RAG y del laboratorio de seguridad. Checklist por versión | Media |
| M9 | **Exportar para Claude** | Botón que genera un resumen de estado (nivel, bloque, últimos errores, diario reciente) para pegar al empezar una sesión con Claude. Evita repetir contexto | Alta (muy barato) |
| M10 | **Laboratorio de seguridad** | Fase 2 en adelante: retos guiados y legales (decodificar, analizar registros, validar entradas, simular inyección de prompts sobre su propio RAG). Siempre con la regla ética visible | Baja (más adelante) |
| M11 | **Inglés técnico** | Vocabulario técnico (Python, seguridad, IA) con repaso espaciado; registro diario de las frases de cierre en inglés y sus correcciones; contador de racha "código todos los días" | Media |

### Modelo de datos (Google Sheets)

| Hoja | Columnas principales |
|---|---|
| `Preguntas` | las del CSV + `tipo` (test / predecir / bug / huecos / escribir), `error_recurrente` (opcional) |
| `Repaso` | `id`, `caja` o `intervalo`, `proxima_fecha`, `aciertos`, `fallos`, `ultima_vez` |
| `Progreso` | `fecha`, `id`, `resultado`, `modo` (ya existe) |
| `Ejercicios` | `id`, `nivel`, `tipo`, `enunciado`, `codigo_inicial`, `tests` (JSON), `pistas` (JSON, 3 niveles), `explicacion` |
| `Ruta` | `fase`, `nivel`, `bloque`, `titulo`, `estado`, `fecha_inicio`, `fecha_fin` |
| `Diario` | `fecha`, `minutos`, `estado_animo`, `hecho`, `costo`, `siguiente` |
| `Errores` | `fecha`, `tipo`, `descripcion`, `codigo`, `leccion_id` |
| `Config` | ajustes (tamaño de letra, minutos por defecto, umbral de pausa larga en días) |

---

## 10. Arquitectura técnica propuesta

### Recomendada: evolucionar la app de Apps Script

| Pieza | Tecnología | Motivo |
|---|---|---|
| Servidor | Google Apps Script (V8) | Gratis, Iker lo domina, ya hay una base que funciona |
| Datos | Google Sheets | Visible y editable por Iker; copia de seguridad trivial |
| Interfaz | HtmlService + HTML/CSS/JS sin frameworks | Ligera, móvil primero, coherente con lo existente |
| Python en el navegador | **Pyodide** (desde cdn.jsdelivr.net) cargado bajo demanda solo en el módulo de ejercicios | Ejecutar Python sin instalar nada, también en el móvil |
| Contenido | Repositorio GitHub → herramienta `herramientas/` genera los `.gs` de datos | Una sola fuente de verdad |
| Despliegue | `clasp` + GitHub, acceso "Solo yo" | Versionado y vuelta atrás |

**Comprobaciones obligatorias antes de comprometerse con Pyodide** (Claude Code debe hacerlas y reportarlas):
- Que Pyodide carga y ejecuta dentro del iframe de HtmlService (sandbox `IFRAME`) en Chrome de escritorio y Chrome Android.
- Tiempo de carga real en el móvil de Iker (el paquete pesa varios MB). Si es inaceptable, alternativa: ejecutar ejercicios solo en el PC, o una ruta sin ejecución (predecir y huecos, corregidos por comparación).
- `input()` no funciona igual en el navegador: los ejercicios deben diseñarse con funciones y tests, no con entrada interactiva.

### Alternativas (solo si Iker las prefiere)

| Opción | Ventajas | Inconvenientes |
|---|---|---|
| App local en Python (Flask o FastAPI) | Practica Python también construyéndola | Solo en el PC; Iker tendría que mantener código que aún no domina |
| Web estática en GitHub Pages + Pyodide | Gratis, rápida | Hay que resolver dónde guardar el progreso de forma privada |

---

## 11. Fases de implementación

Cada fase termina con algo usable, probado y desplegado.

| Fase | Contenido | Entregable |
|---|---|---|
| **0. Puesta a punto** | Confirmar estado de GitHub y de la app actual. Configurar `clasp`. Copia de seguridad de la Sheet | Repositorio y app al día |
| **1. Base y Hoy** | Migración de datos (hojas nuevas sin perder `Progreso`), módulo Hoy (M1), Ruta (M2) y Exportar para Claude (M9) | Abre la app y sabe qué toca hoy |
| **2. Repaso espaciado** | M3 sobre las 56 preguntas + etiquetas de error recurrente + M7 Mis errores | Repasa lo que toca, cuando toca |
| **3. Diario y biblioteca** | M6 y M5 (Markdown → HTML seguro) | Retoma tras pausas y consulta plantillas desde el móvil |
| **4. Ejercicios con Python** | Prueba de concepto de Pyodide → M4 con 10 ejercicios iniciales de los niveles 6–7 | Practica escribiendo código y con tests |
| **5. Proyectos** | M8 con el analizador de registros por versiones | Ve el avance de su proyecto |
| **6. Laboratorio** | M10, cuando empiece la Fase 2 de la ruta | Retos de seguridad legales |

### Contenido inicial a preparar

- **10 ejercicios** (fase 4), basados en sus errores reales: CONTAR frente a FILTRAR, parámetro ignorado, global dentro de función, `return []` frente a `None`, modos de archivo, `.strip()`, `split("|")` con usuario vacío, `try/except`, sangría, inicialización con infinito.
- **Ampliar el banco de preguntas** a medida que avance el Nivel 7 (B.3, B.4, C).
- Cada ejercicio con: enunciado, código inicial, tests (caso normal **y** caso que debe fallar bien), 3 pistas progresivas y explicación.

---

## 12. Seguridad y privacidad

La app es también un ejercicio de lo que Iker quiere aprender: debe ser **ejemplar**.

- **Acceso "Solo yo"** y `executeAs: USER_DEPLOYING`. Nunca acceso público.
- **Validar en el servidor** todo lo que llega del navegador (ids con expresión regular, tipos, listas blancas de valores), como ya hace `registrarRespuesta`.
- **Sin `innerHTML` con contenido de datos:** usar `textContent`. Al convertir Markdown a HTML, sanear (lista blanca de etiquetas) para evitar XSS.
- **Código de Python del usuario:** solo se ejecuta en su navegador (Pyodide, aislado); nunca se envía al servidor para ejecutarse.
- **Sin claves de API** en esta fase. Si en el futuro se integra Claude API, usar `PropertiesService` (nunca en el código ni en GitHub) y un límite de gasto.
- **Diario y errores:** pueden contener notas personales. No guardar datos de terceros ni de FAC-USO en la app.
- **`LockService`** en todas las escrituras; copia de seguridad semanal de la Sheet (activador de tiempo que duplica el archivo).
- **`.gitignore`:** `.clasprc.json`, credenciales y datos personales exportados.
- Documentar en `SEGURIDAD.md` qué amenazas se han considerado y cómo se mitigan: servirá como primera pieza del portafolio de Iker.

---

## 13. Plan de pruebas y despliegue

Iker teme romper lo que ya funciona. Por eso:

1. **Copia de seguridad** de la Sheet antes de cualquier migración.
2. **Pruebas automáticas fuera de Apps Script:** lógica del servidor probada en Node con un simulador de Sheets (ya existe uno de referencia en una sesión anterior: reconstruirlo si hace falta); lógica de repaso espaciado con casos límite (primera vez, muchos fallos, pausa de 30 días).
3. **Pruebas de interfaz** con Playwright a 390 × 844 (móvil) en modo claro y oscuro: sin errores en consola y sin scroll horizontal.
4. **Entorno de pruebas:** URL `/dev` con el checklist de cada fase antes de producción.
5. **Producción:** nueva versión de la implementación existente (la URL `/exec` no cambia). Vuelta atrás desde "Gestionar implementaciones".
6. **Checklist por fase** en `DESPLIEGUE.md`, con casillas que Iker marque en el móvil.

---

## 14. Decisiones abiertas para Iker

Claude Code debe **preguntarlas antes de empezar** (con `AskUserQuestion` si está disponible):

1. **Plataforma:** ¿evolucionar la app de Apps Script (recomendado) o alguna alternativa?
2. **Nombre de la app:** ¿"Mi ruta", "Ruta Ciber" u otro?
3. **Ejecutar Python en el móvil:** ¿imprescindible, o basta con hacerlo en el PC?
4. **Repaso espaciado:** ¿sistema sencillo por cajas (Leitner) o uno más fino?
5. **Diario:** ¿quiere registrar cómo se siente en cada sesión, o solo lo hecho?
6. **Avisos:** ¿quiere un recordatorio diario (por ejemplo, por su bot de Telegram "FAC-USO") o prefiere que la app no le avise?
7. **Orden de las fases de implementación:** ¿le encaja el propuesto?

---

## 15. Instrucciones operativas para Claude Code

1. Lee `CLAUDE.md`, `ROADMAP.md` y este informe. Revisa `app-apps-script/` y `repaso/`.
2. Pregunta las decisiones de la sección 14.
3. Presenta el **plan de la Fase 0 y la Fase 1** con archivos a crear o modificar, migración de datos y plan de pruebas. **Espera aprobación.**
4. Implementa por fases pequeñas. Al final de cada una: pruebas automáticas, capturas en móvil, checklist `/dev` para Iker y resumen corto de qué ha cambiado.
5. **En la app, escribe código completo** (es una herramienta, no un ejercicio). **En `nivel-*`, `repaso/repaso.py` y `analizador-registros/`, nunca resuelvas nada:** son de Iker.
6. Explica a Iker lo que haces **en lenguaje sencillo**, con analogías cuando ayuden. Relaciónalo con la ciberseguridad (por ejemplo: "esta validación es lo mismo que haces en el analizador").
7. Commits pequeños, en español, con mensajes claros. Nada de datos personales ni credenciales en el repositorio.
8. Si una decisión es irreversible (borrar hojas, cambiar el acceso de la app), **para y pregunta**.

---

*"Sin culpa y sin prisa, para ser un buen profesional."*
