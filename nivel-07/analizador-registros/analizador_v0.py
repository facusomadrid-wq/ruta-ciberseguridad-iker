# Analizador de registros de seguridad — versión 0
# Escrita por Iker en el curso de ChatGPT (octubre 2026), antes de unificar la ruta.
# Los registros están escritos dentro del código. El siguiente paso es leerlos de registros.txt.
from datetime import datetime

registros = [
    "ana|FALLO",
    "ana|OK",
    "ana|FALLIDO",
    "admin|FALLO",
    "registro_incompleto"
]

fallos_por_usuario = {}
errores = 0

for linea in registros:
    campos = linea.split("|")

    if len(campos) != 2:
        mensaje = f"Registro incorrecto: {linea}"
        errores += 1

    else:
        usuario = campos[0]
        resultado = campos[1]

        if resultado not in ["OK", "FALLO"]:
            mensaje = f"Resultado no reconocido: {resultado}"
            errores += 1

        else:
            mensaje = ""

            if resultado == "FALLO":
                if usuario not in fallos_por_usuario:
                    fallos_por_usuario[usuario] = 0

                fallos_por_usuario[usuario] += 1

    if mensaje:
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("errores.log", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{ahora}] ERROR: {mensaje}\n")

        print(f"ERROR: {mensaje}")

print("Fallos por usuario:", fallos_por_usuario)
print("Registros incorrectos:", errores)
