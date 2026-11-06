# Despliegue de la app de repaso (Apps Script)

Tiempo: unos 10 minutos. Coste: 0 €. Acceso: **solo tú**.

## 1. Crear el proyecto

1. Ve a [script.google.com](https://script.google.com) → **Nuevo proyecto**.
2. Ponle nombre: `Repaso Python Iker`.
3. Crea estos archivos y pega su contenido desde esta carpeta:

| En el editor | Archivo del repositorio | Cómo crearlo |
|---|---|---|
| `Código.gs` | `Code.gs` | Ya existe: borra lo que trae y pega |
| `Preguntas.gs` | `Preguntas.gs` | **+** → Secuencia de comandos → `Preguntas` |
| `index.html` | `index.html` | **+** → HTML → `index` |
| `appsscript.json` | `appsscript.json` | ⚙️ Configuración del proyecto → ✔ *Mostrar el archivo de manifiesto "appsscript.json"* |

4. Guarda (Ctrl + S).

## 2. Instalar

1. En el desplegable de funciones elige **`instalar`** → **Ejecutar**.
2. Autoriza los permisos: la app solo pide acceso a Hojas de cálculo (para crear y usar su propia hoja).
3. En el registro verás: `✅ Instalación completa. Hoja de cálculo: https://…`
   En tu Drive aparecerá **"Curso Python Iker — Repaso"** con las pestañas `Preguntas` y `Progreso`.

> `instalar()` se puede repetir sin miedo: reutiliza la hoja y **no borra tu progreso**.

## 3. Probar ANTES de producción (entorno de pruebas)

1. **Implementar → Probar implementaciones** → copia la URL que acaba en `/dev`.
2. Ábrela en el PC y en el móvil (con tu cuenta de Google) y comprueba:

- [ ] Carga la pantalla de inicio con **44 preguntas**
- [ ] Los botones Nivel 5 / 6 / 7 cambian el número de preguntas
- [ ] Haz un **test**: las opciones salen barajadas y al responder aparece la explicación
- [ ] Termina el test y mira el **resultado**
- [ ] En la hoja `Progreso` aparecen tus respuestas con fecha
- [ ] **Fichas**: "Ver respuesta" → "Sí / No" → pasa a la siguiente
- [ ] **Progreso**: porcentajes por nivel y temas que más fallas
- [ ] En el móvil se lee bien, sin scroll horizontal

La URL `/dev` siempre ejecuta el código guardado más reciente: úsala para probar cambios.

## 4. Producción

Solo cuando todo el checklist esté en verde:

1. **Implementar → Nueva implementación** → tipo **Aplicación web**.
2. Descripción: `v1 — primera versión`.
3. **Ejecutar como:** Yo · **Quién tiene acceso:** **Solo yo**.
4. **Implementar** → copia la URL que acaba en `/exec`.
5. En el móvil: abre la URL en Chrome → menú ⋮ → **Añadir a pantalla de inicio**.

## Actualizar sin romper nada

- **Cambiar el código:** edita, guarda, prueba con `/dev`. Cuando esté bien: **Implementar → Gestionar implementaciones → ✏️ → Versión: Nueva versión**. La URL `/exec` no cambia.
- **Volver atrás:** en *Gestionar implementaciones* elige una versión anterior. Tu progreso está en la hoja y no se pierde.
- **Añadir preguntas:**
  1. Edita `repaso/preguntas.csv`.
  2. `python herramientas/generar_preguntas_gs.py` (valida el CSV y avisa si hay errores).
  3. Pega el nuevo `Preguntas.gs` en el editor y ejecuta **`recargarPreguntas()`**. Tu progreso no se toca.

## Seguridad

- Acceso **"Solo yo"**: nadie más puede abrirla aunque tenga la URL. No lo cambies.
- Todo lo que llega del navegador se valida en el servidor (id, resultado y modo).
- Sin APIs externas ni claves: nada que pueda filtrarse.

## Opcional: trabajar con clasp y Claude Code

```
npm install -g @google/clasp
clasp login
cd app-apps-script
clasp create --type standalone --title "Repaso Python Iker"
clasp push
```

Activa antes la API en [script.google.com/home/usersettings](https://script.google.com/home/usersettings). No subas `.clasprc.json` a GitHub (ya está en `.gitignore`).

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| "La app no está instalada" | No se ejecutó `instalar()` | Ejecútalo desde el editor |
| "Falta Preguntas.gs" | No se creó el archivo | Créalo y pega el contenido |
| Pantalla en blanco | El archivo HTML no se llama `index` | Renómbralo a `index` |
| "No se pudo guardar la última respuesta" | Conexión o permisos | Recarga; si sigue, ejecuta `instalar()` |
| Al abrir pide elegir cuenta | Varias cuentas de Google abiertas | Usa la misma cuenta con la que desplegaste |
