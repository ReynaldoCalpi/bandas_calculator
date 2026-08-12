# src/calculator.py
from src.config import TAX_PARAMS, BANDS_REFERENCE

def calcular_precio_normalizado(precio_bruto_usd, pais, tasa_cambio):
    """
    1. Convierte el precio bruto USD a moneda local.
    2. Resta impuestos fijos, divide entre (1 + tasa_iva) y vuelve a sumar los impuestos fijos.
    3. Convierte el resultado neto final a USD para evaluar la banda.
    """
    if tasa_cambio <= 0:
        return 0.0
    
    # Llevar a moneda local
    precio_local = precio_bruto_usd * tasa_cambio
    
    # Obtener parámetros del país
    params = TAX_PARAMS.get(pais, {'iva_rate': 0.0, 'fijos': []})
    iva = params['iva_rate']
    total_fijos_local = sum(params['fijos'])
    
    # Aplicar la fórmula exacta mostrada en el ejemplo:
    # ((Bruto - Fijos) / (1 + IVA)) + Fijos
    if iva > 0:
        neto_local = ((precio_local - total_fijos_local) / (1 + iva)) + total_fijos_local
    else:
        neto_local = precio_local - total_fijos_local
        
    # Convertir a USD final
    neto_usd = neto_local / tasa_cambio
    return round(neto_usd, 2)

def obtener_banda(precio_usd):
    for id_banda, (min_val, max_val) in BANDS_REFERENCE.items():
        if min_val <= precio_usd <= max_val:
            return id_banda, f"De ${min_val:.2f} hasta ${max_val:.2f}"
    return 0, "Fuera de Rango"
