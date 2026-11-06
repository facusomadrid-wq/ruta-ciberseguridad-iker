ANCHO = "=" * 40
SEPARADOR = "-" * 40

# Diccionario de afiliados
afiliados_facuso = {
    "001": {"nombre": "Ana García", "edad": 45, "seccion": "Central", "cuota_mensual": 25.50, "antiguedad": 8, "cargo": "afiliado"},
    "002": {"nombre": "Luis Martínez", "edad": 38, "seccion": "Territorial", "cuota_mensual": 25.50, "antiguedad": 3, "cargo": "delegado"},
    "003": {"nombre": "María López", "edad": 52, "seccion": "Central", "cuota_mensual": 30.00, "antiguedad": 15, "cargo": "delegada"},
    "004": {"nombre": "Pedro Sánchez", "edad": 41, "seccion": "Territorial", "cuota_mensual": 25.50, "antiguedad": 6, "cargo": "afiliado"},
    "005": {"nombre": "Carmen Ruiz", "edad": 33, "seccion": "Comunicación", "cuota_mensual": 25.50, "antiguedad": 2, "cargo": "afiliada"},
    "006": {"nombre": "Javier Torres", "edad": 47, "seccion": "Central", "cuota_mensual": 30.00, "antiguedad": 12, "cargo": "responsable"},
    "007": {"nombre": "Elena Vega", "edad": 29, "seccion": "Territorial", "cuota_mensual": 25.50, "antiguedad": 1, "cargo": "afiliada"},
    "008": {"nombre": "Miguel Ortiz", "edad": 55, "seccion": "Central", "cuota_mensual": 35.00, "antiguedad": 20, "cargo": "presidente"}
}

# FUNCIONES

# Calcular la edad promedio
def media(afiliados, campo):
    suma_edad = 0
    for afiliado in afiliados.values():
        suma_edad += afiliado[campo]
    promedio = suma_edad / len(afiliados)
    return promedio

# Calcular una suma
def suma(afiliados, campo):
    suma_cuota = 0
    for cuota in afiliados.values():
        suma_cuota += cuota[campo]
    return suma_cuota

# Calcular el más veterano y el más joven
def analizar_afiliados(afiliados):
    mas_veterano = None
    max_antiguedad = float("-inf")
    mas_joven = None
    min_edad = float("inf")
    for afiliado in afiliados.values():
        # Buscamos al más veterano
        if afiliado["antiguedad"] > max_antiguedad:
            max_antiguedad = afiliado["antiguedad"]
            mas_veterano = afiliado["nombre"]
        # Buscamos al más joven
        if afiliado["edad"] < min_edad:
            min_edad = afiliado["edad"]
            mas_joven = afiliado["nombre"]
    return mas_veterano, max_antiguedad, mas_joven, min_edad

# Contar veteranos
def contar_veteranos(afiliados, anios):
    contador = 0
    for afiliado in afiliados.values():
        if afiliado["antiguedad"] > anios:
            contador += 1
    return contador

# Contar afiliados por sección
def contar_por_seccion(afiliados):
    contador_secciones = {}
    for afiliado in afiliados.values():
        seccion = afiliado["seccion"]
        if seccion in contador_secciones:
            contador_secciones[seccion] += 1
        else:
            contador_secciones[seccion] = 1
    return contador_secciones

# Contar afiliados por cargo
def contar_por_cargo(afiliados):
    contador_cargos = {}
    for afiliado in afiliados.values():
        cargo = afiliado["cargo"]
        if cargo in contador_cargos:
            contador_cargos[cargo] += 1
        else:
            contador_cargos[cargo] = 1
    return contador_cargos

# Filtrar por cargo
def filtrar_por_cargo(afiliados, cargo):
    # 1. Necesito un diccionario vacío para los filtrados
    filtrados = {}    
    # 2. Recorro los afiliados con .items() (necesito el ID)
    for id_afiliado, datos in afiliados.items():        
        # 3. Si el cargo del afiliado empieza por lo invocado
        if datos["cargo"].startswith(cargo):
            # 4. Añado al diccionario filtrado el ID y los datos
            filtrados[id_afiliado] = datos                       
    # 5. Devuelvo el diccionario filtrado
    return filtrados

def realizar_informe(afiliados):

    # INVOCACIONES
    media_edad_afiliados = media(afiliados, "edad")
    cuota_mensual_total = suma(afiliados, "cuota_mensual")

    mas_veterano, antiguedad, mas_joven, edad = analizar_afiliados(afiliados)

    mas_10_anios = contar_veteranos(afiliados, 10)

    secciones = contar_por_seccion(afiliados)

    cargos = contar_por_cargo(afiliados)

    delegados = filtrar_por_cargo(afiliados, "delegad")

    # PRINTS
    
    print(ANCHO)
    print("INFORME FAC-USO")
    print(ANCHO)
    print("📊 ESTADÍSTICAS GENERALES")
    print(SEPARADOR)
    print(f"- Total afiliados: {len(afiliados)}")
    print(f"- Edad media: {media_edad_afiliados:.2f} años")
    print(f"- Total cuotas mensuales: {cuota_mensual_total:.2f} euros")
    print(SEPARADOR)
    print(f"El/la afiliado/a más veterano/a es: {mas_veterano} con {antiguedad} años de antigüedad.")
    print(f"El/la afiliado/a más joven es: {mas_joven} con {edad} años.")
    print(SEPARADOR)
    print("👑 CARGOS DE REPRESENTACIÓN")
    print(SEPARADOR)
    print(f"Veteranos (>10 años): {mas_10_anios} afiliados.")
    print(SEPARADOR)
    print("🏢 DISTRIBUCIÓN POR SECCIÓN")
    print(SEPARADOR)
    for seccion, cantidad in secciones.items():
        print(f"- {seccion}: {cantidad} afiliados")
    print(SEPARADOR)
    print("👤 DELEGADOS")
    print(SEPARADOR)
    for id_afiliado, datos in delegados.items():
        print(f"- {datos['nombre']} ({datos['cargo']})")
    print(SEPARADOR)

realizar_informe(afiliados_facuso)