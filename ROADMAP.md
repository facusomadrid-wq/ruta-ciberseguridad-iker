# Ruta hacia Anthropic

**Objetivo profesional:** trabajar en remoto en **Anthropic**, en el área de seguridad de la IA.
**Camino:** Python → fundamentos de sistemas → un RAG propio construido, atacado y defendido → ciberseguridad profesional.
**En paralelo, desde el primer día:** inglés técnico + portafolio público en GitHub.

> *Sin culpa y sin prisa, para ser un buen profesional.*

## Compromiso y ritmo

- **Curso con Claude:** lunes a viernes, sesiones de **30 minutos** en VS Code.
- **Compromiso de Iker:** tocar algo de código **todos los días**, también el fin de semana (aunque sean 10 minutos).
- **Horizonte:** 2 años (revisión: **noviembre de 2028**). Revisión intermedia cada 6 meses.
- Los plazos de cada fase son orientativos.

---

## Fase 1 — Python base (2–3 meses) · 🔄 en curso

| Nivel | Contenido | Estado |
|---|---|---|
| 1–4 | Variables, tipos, strings, decisiones, bucles, listas | ✅ |
| 5 | Diccionarios e informes | ✅ |
| 6 | Funciones (proyecto: informe FAC-USO) | ✅ |
| 7 | Archivos, errores, validación de datos | 🔄 |
| 8 | Módulos, JSON, expresiones regulares básicas | ⏳ |

**Proyecto de la fase:** [`nivel-07/analizador-registros/`](nivel-07/analizador-registros/). Lee un archivo de registros, valida cada línea, cuenta los fallos por usuario y guarda los errores con fecha.

## Fase 2 — Fundamentos de sistemas (3–4 meses) · ⏳

- Terminal de Linux: moverse, permisos, procesos, ver registros del sistema.
- Redes: IP, puertos, protocolos, DNS.
- La web por dentro: HTTP, peticiones, cabeceras, cookies.
- Python para tu laboratorio: peticiones web y herramientas propias.

## Fase 3 — RAG seguro (4–5 meses) · ⏳

El curso RAG ya diseñado (Google Drive, embeddings, base vectorial, Claude API, interfaz web, despliegue) con la seguridad como pilar:

1. **Construir** el RAG.
2. **Atacarlo** tú mismo: inyección de prompts, documentos maliciosos, fuga de información.
3. **Defenderlo** y documentar cada ataque y su mitigación.

Es tu primer proyecto de **seguridad de la IA**, una especialidad con poca gente formada.

## Fase 4 — Ciberseguridad profesional · ⏳

- **Defensa (blue team):** análisis de registros, detección, funcionamiento de un SOC.
- **Normativa:** Esquema Nacional de Seguridad, RGPD y la que aplique en ese momento.
- **Laboratorios legales** de práctica.
- **Certificación de entrada** (elegirla cuando lleguemos, comprobando la oferta del momento).
- **Portafolio en GitHub** con tus proyectos documentados.

## Pista paralela — Inglés + Portafolio · 🔄 desde el 04/11/2026

| Paso | Qué | Cuándo |
|---|---|---|
| 0 | Prueba de nivel de inglés (punto de partida) | 04/11/2026 |
| 1 | Código **en inglés**: variables, funciones y comentarios | Desde Nivel 7 · B.3 |
| 2 | **Cierre en inglés:** 3–5 frases propias explicando lo aprendido; Claude corrige | Cada sesión |
| 3 | Lectura de **documentación oficial en inglés** (Python docs, OWASP, docs de la API de Claude) | Desde Nivel 8 |
| 4 | Sesiones progresivamente en inglés | Fase 2 en adelante |
| 5 | **Repositorio público** con README en inglés: analizador, RAG seguro, app de repaso | Al cerrar cada fase |
| 6 | Proyecto de seguridad de la IA propio (p. ej., detector de inyección de prompts en documentos) | Fase 3 |
| 7 | Práctica de entrevistas en inglés (técnicas y de conducta) | Último semestre |

**Git y GitHub:** se aprenden usándolos. Cada sesión termina con un `commit` hecho por Iker.

---

## Regla ética (no negociable)

Todo lo ofensivo se practica **solo** sobre sistemas propios o en laboratorios preparados para ello. Acceder a sistemas ajenos sin permiso es delito, aunque sea "para aprender".

## Método

- Una sola ruta, en este repositorio. ChatGPT u otras IA, solo como segunda explicación.
- Método socrático: pistas, no soluciones.
- Cada sesión empieza con un calentamiento de 5 minutos (los huecos de `repaso/repaso.py` y la app de repaso).
- Cada ejercicio de Python tiene su lectura en clave de seguridad.
