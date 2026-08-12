# src/calculator.py
from src.config import TAX_PARAMS, BANDS_REFERENCE

def calcular_precio_normalizado(precio_bruto_usd, pais, tasa_cambio):
    """
    1. Multiplica el precio bruto USD por la tasa de cambio para llevarlo a moneda local.
    2. Aplica la fórmula: ((PrecioLocal - FijosLocales) / (1 + IVA)) + FijosLocales
    3. Convierte el resultado neto final a USD para evaluar la banda.
    """
    if tasa_cambio <= 0:
        return 0.0
    
    # Obtener parámetros del país
    params = TAX_PARAMS.get(pais, {'iva_rate': 0.0, 'fijos': []})
    iva = params['iva_rate']
    total_fijos_local = sum(params['fijos'])
    
    # Para El Salvador (SV), trabajamos directamente en USD porque su moneda oficial es el dólar
    if pais == 'SV':
        if iva > 0:
            neto_usd = ((precio_bruto_usd - total_fijos_local) / (1 + iva)) + total_fijos_local
        else:
            neto_usd = precio_bruto_usd - total_fijos_local
        return round(neto_usd, 2)
    
    # Para el resto de países (GT, CR, HN, NI), operamos en moneda local
    precio_local = precio_bruto_usd * tasa_cambio
    
    if iva > 0:
        neto_local = ((precio_local - total_fijos_local) / (1 + iva)) + total_fijos_local
    else:
        neto_local = precio_local - total_fijos_local
        
    # Convertir el precio neto final a USD
    neto_usd = neto_local / tasa_cambio
    return round(neto_usd, 2)

def obtener_banda(precio_usd):
    for id_banda, (min_val, max_val) in BANDS_REFERENCE.items():
        if min_val <= precio_usd <= max_val:
            return id_banda, f"De ${min_val:.2f} hasta ${max_val:.2f}"
    return 0, "Fuera de Rango"
