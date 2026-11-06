# Importamos de la caja de herramientas de python la herramienta Counter
from collections import Counter

ANCHO = "=" * 40
SEPARADOR = "-" * 40
afiliados = {
    "AF-001": {
        "nombre_completo": "María López García",
        "edad": 42,
        "provincia": "Madrid",
        "cuota_mensual": 12.50,
        "tipo_cuota": "COMPLETA",
        "sector": "Educación"
    },
    "AF-002": {
        "nombre_completo": "Pedro Ruiz Torres",
        "edad": 35,
        "provincia": "Barcelona",
        "cuota_mensual": 10.00,
        "tipo_cuota": "REDUCIDA",
        "sector": "Sanidad"
    },
    "AF-003": {
        "nombre_completo": "Ana Martín Sánchez",
        "edad": 51,
        "provincia": "Madrid",
        "cuota_mensual": 12.50,
        "tipo_cuota": "COMPLETA",
        "sector": "Administración"
    },
    "AF-004": {
        "nombre_completo": "Luis García Pérez",
        "edad": 28,
        "provincia": "Valencia",
        "cuota_mensual": 8.00,
        "tipo_cuota": "REDUCIDA",
        "sector": "Educación"
    },
    "AF-005": {
        "nombre_completo": "Carmen Ortiz Vidal",
        "edad": 47,
        "provincia": "Madrid",
        "cuota_mensual": 15.00,
        "tipo_cuota": "VOLUNTARIA",
        "sector": "Sanidad"
    },
    "AF-006": {
        "nombre_completo": "Jorge Blanco Ríos",
        "edad": 39,
        "provincia": "Barcelona",
        "cuota_mensual": 12.50,
        "tipo_cuota": "COMPLETA",
        "sector": "Educación"
    },
    "AF-007": {
        "nombre_completo": "Elena Torres Ruiz",
        "edad": 33,
        "provincia": "Valencia",
        "cuota_mensual": 10.00,
        "tipo_cuota": "REDUCIDA",
        "sector": "Administración"
    },
    "AF-008": {
        "nombre_completo": "Antonio Núñez Vera",
        "edad": 56,
        "provincia": "Madrid",
        "cuota_mensual": 12.50,
        "tipo_cuota": "COMPLETA",
        "sector": "Sanidad"
    }
}

# Para la fase 1 necesito declarar variables: total afiliados, sum_edades, edad media,  cuota media y recaudación mensual
total_afiliados = len(afiliados)
sum_edades = sum(afiliado["edad"] for afiliado in afiliados.values())
edad_media = sum_edades / total_afiliados
sum_cuota = sum(afiliado["cuota_mensual"] 
for afiliado in afiliados.values())
cuota_media = sum_cuota / total_afiliados


# Sacamos con counter todas las provincias y las cuenta automáticamente
por_provincia = Counter(datos["provincia"] for datos in afiliados.values())

# Ahora recopilamos datos sobre recaudación por provincia 
por_provincia_recaudacion = {}
for datos in afiliados.values():
    provincia = datos["provincia"]
    cuota = datos["cuota_mensual"]
    if provincia in por_provincia_recaudacion:
        por_provincia_recaudacion[provincia] += cuota
    else:
        por_provincia_recaudacion[provincia] = cuota



por_sector = {}
for datos in afiliados.values():
    sector = datos["sector"]
    nombre = datos["nombre_completo"]
    if sector in por_sector:
        por_sector[sector].append(nombre)
    else:
        por_sector[sector] = [nombre]

print(ANCHO)
print("INFORME COMPLETO FAC-USO".center(40))
print(ANCHO)

# Alineamos el concepto a la izquierda (25 espacios) y el valor a la derecha (15 espacios)
print("Total afiliados:".ljust(25) + str(total_afiliados).rjust(15))
print("Edad media:".ljust(25) + f"{edad_media:.2f} años".rjust(15))
print("Cuota media:".ljust(25) + f"{cuota_media:.2f} €".rjust(15))
print("Recaudación mensual:".ljust(25) + f"{sum_cuota:.2f} €".rjust(15))
print(ANCHO)
print("AFILIADOS POR PROVINCIA".center(40))
print(ANCHO)
for provincia, cantidad in por_provincia.items(): 
    # Se imprime el nombre de la provincia y su cantidad
    print(provincia.ljust(25) + f" {str(cantidad).rjust(3)} afiliados.")
# Ahora Imprimimos afiliados por tipo de cuota
print(ANCHO)
por_tipo = Counter(datos["tipo_cuota"] for datos in afiliados.values())
print("AFILIADOS POR TIPO DE CUOTA".center(40))
print(ANCHO)
for tipo, cantidad in por_tipo.items(): 
    print(tipo.ljust(25) + f" {str(cantidad).rjust(3)} afiliados.")
print(ANCHO)
print("RECAUDACION POR PROVINCIA".center(40))
print(ANCHO)
for provincia, importe in por_provincia_recaudacion.items():
    print(provincia.ljust(25) + f"{importe:.2f} €".rjust(15))
print(ANCHO)
print("AFILIADOS POR SECTOR".center(40))
print(ANCHO)

for sector, lista_nombres in por_sector.items():
    print(f"\nSector: {sector} ({len(lista_nombres)} afiliados)")
    print(SEPARADOR)
    for nombre in lista_nombres:
        print(f"  • {nombre}")