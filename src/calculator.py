# src/calculator.py
from src.config import TAX_PARAMS, BANDS_REFERENCE

def calcular_precio_normalizado(precio_bruto_usd, pais, tasa_cambio):
    """
    1. Si es SV, aplica la fórmula directamente en USD.
    2. Si es GT (u otro), lleva el precio bruto USD a moneda local, aplica la fórmula de impuestos 
       y convierte el resultado neto final a USD.
    """
    if tasa_cambio <= 0:
        return 0.0
    
    params = TAX_PARAMS.get(pais, {'iva_rate': 0.0, 'fijos': []})
    iva = params['iva_rate']
    total_fijos = sum(params['fijos'])
    
    # Caso El Salvador (Moneda base USD)
    if pais == 'SV':
        if iva > 0:
            neto_usd = ((precio_bruto_usd - total_fijos) / (1 + iva)) + total_fijos
        else:
            neto_usd = precio_bruto_usd - total_fijos
        return round(neto_usd, 2)
    
    # Caso Guatemala y otros (Moneda local)
    precio_local = precio_bruto_usd * tasa_cambio
    
    if iva > 0:
        neto_local = ((precio_local - total_fijos) / (1 + iva)) + total_fijos
    else:
        neto_local = precio_local - total_fijos
        
    # Convertir el neto local final a USD
    neto_usd = neto_local / tasa_cambio
    return round(neto_usd, 2)

def obtener_banda(precio_usd):
    for id_banda, (min_val, max_val) in BANDS_REFERENCE.items():
        if min_val <= precio_usd <= max_val:
            return id_banda, f"De ${min_val:.2f} hasta ${max_val:.2f}"
    return 0, "Fuera de Rango"
