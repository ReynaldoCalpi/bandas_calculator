# src/calculator.py
from src.config import TAX_DEDUCTIONS, BANDS_REFERENCE

def calcular_precio_normalizado(precio_bruto_usd, pais, tasa_cambio):
    """
    1. Recibe el precio bruto en USD.
    2. Convierte las deducciones de impuestos locales a USD dividiéndolas por la tasa de cambio.
    3. Resta los impuestos para obtener el precio neto en USD.
    """
    if tasa_cambio <= 0:
        return 0.0
    
    # Sumar deducciones de impuestos en moneda local
    deducciones_locales = sum(TAX_DEDUCTIONS.get(pais, {}).values())
    
    # Convertir las deducciones locales a USD
    deducciones_usd = deducciones_locales / tasa_cambio
    
    # Restar para obtener el precio neto en USD
    precio_neto_usd = precio_bruto_usd - deducciones_usd
    return round(precio_neto_usd, 2)

def obtener_banda(precio_usd):
    """
    Busca a qué ID de banda y rango pertenece el precio USD calculado.
    """
    for id_banda, (min_val, max_val) in BANDS_REFERENCE.items():
        if min_val <= precio_usd <= max_val:
            return id_banda, f"De ${min_val:.2f} hasta ${max_val:.2f}"
    return 0, "Fuera de Rango"
