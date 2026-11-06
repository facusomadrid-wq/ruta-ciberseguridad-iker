# Ruta hacia Anthropic — Iker González

De Python desde cero hasta la seguridad de la IA, pasando por un sistema **RAG** propio construido, atacado y defendido. En paralelo: inglés técnico y portafolio en GitHub.

> *Sin culpa y sin prisa, para ser un buen profesional.*

📍 **Plan completo y progreso:** [`ROADMAP.md`](ROADMAP.md)

## Dónde estoy

| Fase | Estado |
|---|---|
| 1. Python base | 🔄 Nivel 7: archivos, errores y validación |
| 2. Fundamentos de sistemas | ⏳ |
| 3. RAG seguro | ⏳ |
| 4. Ciberseguridad profesional | ⏳ |
| ➕ Inglés + portafolio | 🔄 prueba de nivel hecha |

**Proyecto actual:** [`nivel-07/analizador-registros/`](nivel-07/analizador-registros/)

## Qué hay aquí

| Carpeta | Contenido |
|---|---|
| [`plantillas/`](plantillas/) | Patrones (MAX, MIN, ACUMULADOR, MEDIA, CONTADOR, FILTRAR, AGRUPAR) y lecciones aprendidas |
| [`nivel-05/`](nivel-05/) [`nivel-06/`](nivel-06/) [`nivel-07/`](nivel-07/) | Resumen de cada nivel y mis ejercicios |
| [`repaso/`](repaso/) | Banco de preguntas (`preguntas.csv`) y la herramienta de repaso en Python |
| [`app-apps-script/`](app-apps-script/) | App web de repaso para el móvil |
| [`ingles/`](ingles/) | Nivel de inglés y progreso |
| [`herramientas/`](herramientas/) | Utilidades (pasar las preguntas a la app) |

## Cómo repasar

**En el móvil:** la app web (ver [`app-apps-script/DESPLIEGUE.md`](app-apps-script/DESPLIEGUE.md)).

**En el PC:**

```
cd repaso
python repaso.py
```

> `repaso.py` tiene **4 huecos** que uso como calentamiento de 5 minutos al empezar las sesiones.

## Añadir preguntas

1. Edita `repaso/preguntas.csv` (VS Code o Google Sheets). Es la **única** fuente de preguntas.
2. Ejecuta `python herramientas/generar_preguntas_gs.py`.
3. Pega el nuevo `app-apps-script/Preguntas.gs` en el editor de Apps Script y ejecuta `recargarPreguntas()`.

Columnas: `id`, `nivel`, `tema`, `pregunta`, `codigo` (opcional, admite varias líneas), `opcion_a`…`opcion_d`, `correcta` (A/B/C/D) y `explicacion`.

## Trabajar con Claude Code

[`CLAUDE.md`](CLAUDE.md) recoge las reglas: método socrático, plan antes de código, plan de pruebas antes de desplegar y regla ética (solo sistemas propios o laboratorios).

## GitHub

**Si todavía no lo has subido:**

1. github.com → **New repository** → `ruta-ciberseguridad-iker` → **Private** → sin README.
2. En la carpeta del proyecto:

```
git init
git add .
git commit -m "Ruta de ciberseguridad: Python niveles 5-7, repaso y app"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/ruta-ciberseguridad-iker.git
git push -u origin main
```

**Si ya lo subiste como `curso-python-iker`:** en GitHub → Settings → Repository name → `ruta-ciberseguridad-iker` → Rename. Después, en tu carpeta:

```
git remote set-url origin https://github.com/TU_USUARIO/ruta-ciberseguridad-iker.git
```
