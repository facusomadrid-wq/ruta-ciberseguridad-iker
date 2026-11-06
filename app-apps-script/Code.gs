/**
 * REPASO DEL CURSO DE PYTHON — App web (Google Apps Script)
 *
 * Archivos del proyecto:
 *   Code.gs        → este archivo (servidor)
 *   Preguntas.gs   → generado desde repaso/preguntas.csv (no editar a mano)
 *   index.html     → interfaz
 *
 * Primera vez:  ejecuta instalar()  → crea la hoja de cálculo y carga las preguntas.
 * Tras cambiar el CSV: pega el nuevo Preguntas.gs y ejecuta recargarPreguntas().
 */

const NOMBRE_HOJA_CALCULO = 'Curso Python Iker — Repaso';
const HOJA_PREGUNTAS = 'Preguntas';
const HOJA_PROGRESO = 'Progreso';
const PROP_ID_HOJA = 'ID_HOJA_REPASO';

const COLUMNAS_PREGUNTAS = ['id', 'nivel', 'tema', 'pregunta', 'codigo',
  'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d', 'correcta', 'explicacion'];
const COLUMNAS_PROGRESO = ['fecha', 'id', 'resultado', 'modo'];
const MODOS_VALIDOS = ['test', 'fichas'];


// ─────────────────────────────── Web app ───────────────────────────────

function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('Repaso Python')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}


// ─────────────────────────── Instalación ───────────────────────────────

/** Ejecutar UNA vez desde el editor. Es seguro repetirlo: no duplica nada. */
function instalar() {
  const libro = obtenerOCrearLibro_();
  prepararHoja_(libro, HOJA_PROGRESO, COLUMNAS_PROGRESO);
  cargarPreguntasEnHoja_(libro);
  Logger.log('✅ Instalación completa. Hoja de cálculo: ' + libro.getUrl());
}

/** Vuelve a cargar las preguntas desde Preguntas.gs. NO toca tu progreso. */
function recargarPreguntas() {
  const libro = abrirLibro_();
  cargarPreguntasEnHoja_(libro);
  Logger.log('✅ Preguntas recargadas: ' + PREGUNTAS.length);
}


// ──────────────────────── Funciones para la interfaz ───────────────────

/** Devuelve preguntas y estadísticas de cada una. */
function getDatos() {
  const libro = abrirLibro_();
  const preguntas = leerTabla_(libro.getSheetByName(HOJA_PREGUNTAS), COLUMNAS_PREGUNTAS)
    .filter(function (p) { return p.id; })
    .map(function (p) {
      p.nivel = Number(p.nivel);
      p.correcta = String(p.correcta).trim().toUpperCase();
      return p;
    });

  const estadisticas = {};
  leerTabla_(libro.getSheetByName(HOJA_PROGRESO), COLUMNAS_PROGRESO).forEach(function (fila) {
    const id = fila.id;
    if (!id) return;
    if (!estadisticas[id]) estadisticas[id] = { aciertos: 0, fallos: 0 };
    if (fila.resultado === 'acierto') estadisticas[id].aciertos++;
    else if (fila.resultado === 'fallo') estadisticas[id].fallos++;
  });

  return { preguntas: preguntas, estadisticas: estadisticas };
}

/** Guarda una respuesta. Valida todo lo que llega del navegador. */
function registrarRespuesta(id, acierto, modo) {
  if (typeof id !== 'string' || !/^[A-Za-z0-9_-]{1,20}$/.test(id)) {
    throw new Error('Identificador de pregunta no válido.');
  }
  if (typeof acierto !== 'boolean') throw new Error('Resultado no válido.');
  if (MODOS_VALIDOS.indexOf(modo) === -1) throw new Error('Modo no válido.');

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    abrirLibro_().getSheetByName(HOJA_PROGRESO)
      .appendRow([new Date(), id, acierto ? 'acierto' : 'fallo', modo]);
  } finally {
    lock.releaseLock();
  }
  return true;
}


// ───────────────────────────── Internas ────────────────────────────────

function obtenerOCrearLibro_() {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty(PROP_ID_HOJA);
  if (id) {
    try {
      return SpreadsheetApp.openById(id);
    } catch (e) {
      Logger.log('La hoja guardada ya no existe o no es accesible. Se crea una nueva.');
    }
  }
  const libro = SpreadsheetApp.create(NOMBRE_HOJA_CALCULO);
  libro.getSheets()[0].setName(HOJA_PREGUNTAS);
  props.setProperty(PROP_ID_HOJA, libro.getId());
  return libro;
}

function abrirLibro_() {
  const id = PropertiesService.getScriptProperties().getProperty(PROP_ID_HOJA);
  if (!id) throw new Error('La app no está instalada: ejecuta instalar() desde el editor.');
  return SpreadsheetApp.openById(id);
}

function prepararHoja_(libro, nombre, columnas) {
  let hoja = libro.getSheetByName(nombre);
  if (!hoja) hoja = libro.insertSheet(nombre);
  if (hoja.getLastRow() === 0) {
    hoja.appendRow(columnas);
    hoja.getRange(1, 1, 1, columnas.length).setFontWeight('bold');
    hoja.setFrozenRows(1);
  }
  return hoja;
}

function cargarPreguntasEnHoja_(libro) {
  if (typeof PREGUNTAS === 'undefined' || !PREGUNTAS.length) {
    throw new Error('Falta Preguntas.gs o está vacío.');
  }
  const hoja = prepararHoja_(libro, HOJA_PREGUNTAS, COLUMNAS_PREGUNTAS);
  if (hoja.getLastRow() > 1) {
    hoja.getRange(2, 1, hoja.getLastRow() - 1, COLUMNAS_PREGUNTAS.length).clearContent();
  }
  const filas = PREGUNTAS.map(function (p) {
    return COLUMNAS_PREGUNTAS.map(function (c) { return p[c] === undefined ? '' : p[c]; });
  });
  const rango = hoja.getRange(2, 1, filas.length, COLUMNAS_PREGUNTAS.length);
  rango.setNumberFormat('@');       // todo como texto: evita que "1.75" o fórmulas se transformen
  rango.setValues(filas);
}

function leerTabla_(hoja, columnas) {
  if (!hoja || hoja.getLastRow() < 2) return [];
  const valores = hoja.getRange(2, 1, hoja.getLastRow() - 1, columnas.length).getDisplayValues();
  return valores.map(function (fila) {
    const obj = {};
    columnas.forEach(function (c, i) { obj[c] = fila[i]; });
    return obj;
  });
}
