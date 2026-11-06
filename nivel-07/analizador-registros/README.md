# Proyecto: analizador de registros de seguridad

**Proyecto final de la Fase 1.** Empezado en el curso de ChatGPT, continúa aquí.

## Qué hará al terminar

1. Leer `registros.txt` (formato `usuario|RESULTADO`, una línea por intento de acceso).
2. Validar cada línea y no fiarse de nada: estructura, usuario y resultado.
3. Contar los fallos por usuario.
4. Registrar los errores en `errores.log` con fecha y hora, **sin exponer datos sensibles**.
5. Avisar de los usuarios sospechosos (por ejemplo, 3 o más fallos).
6. No caerse nunca: si falta el archivo, mensaje claro.
7. Mostrar un resumen final legible.

## Versiones

| Versión | Qué añade | Estado |
|---|---|---|
| `analizador_v0.py` | Lista en el código, validación básica, `errores.log` con fecha | ✅ (curso ChatGPT) |
| `analizador_v1.py` | Leer de `registros.txt` + `try/except` si falta el archivo | ⏳ siguiente |
| `analizador_v2.py` | Validación completa con los casos trampa de `registros.txt` | ⏳ |
| `analizador_v3.py` | Organizado en funciones (patrones del Nivel 6) + alerta de usuarios sospechosos | ⏳ |
| `analizador_v4.py` | Resumen alineado y registro de errores sin datos sensibles | ⏳ |

> Cada versión es un archivo nuevo: las anteriores no se tocan. Así se ve tu evolución en GitHub.

## Sobre `registros.txt`

Contiene registros normales y **casos trampa** a propósito, como los que llegan en la vida real. Antes de programar nada, léelo y apunta:

- ¿Qué líneas crees que son válidas?
- ¿Cuáles deberían rechazarse y por qué?
- ¿Hay alguna que esté en una zona gris, donde tienes que **decidir** tú qué hacer?

Esas decisiones son parte del trabajo de seguridad: no hay una única respuesta correcta, pero sí hay que poder justificarla.

## Conexión con la ciberseguridad

- **Varios fallos seguidos del mismo usuario** pueden indicar un intento de adivinar contraseñas (fuerza bruta). Por sí solos no prueban un ataque.
- **Validar las entradas** es la primera defensa ante datos manipulados.
- **Los registros de errores** pueden filtrar información si guardan más de la cuenta.
- Este mismo razonamiento lo aplicarás en la Fase 3 para defender tu RAG.

## Regla ética

Este analizador trabaja solo con registros de ejemplo o de sistemas propios.
