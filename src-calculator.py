# src/calculator.py
from src.config import TAX_DEDUCTIONS, BANDS_REFERENCE

def calcular_precio_normalizado(precio_promedio_local, pais, tasa_cambio):
    """
    1. Resta los impuestos locales fijos en moneda local.
    2. Convierte el resultado a USD usando la tasa de cambio del día.
    """
    if tasa_cambio <= 0:
        return 0.0
    
    # Sumar deducciones de impuestos para el país
    deducciones = sum(TAX_DEDUCTIONS.get(pais, {}).values())
    
    # Restar impuestos en moneda local
    precio_neto_local = precio_promedio_local - deducciones
    
    # Convertir a USD
    precio_usd = precio_neto_local / tasa_cambio
    return round(precio_usd, 2)

def obtener_banda(precio_usd):
    """
    Busca a qué ID de banda y rango pertenece el precio USD calculado.
    """
    for id_banda, (min_val, max_val) in BANDS_REFERENCE.items():
        if min_val <= precio_usd <= max_val:
            return id_banda, f"De ${min_val:.2f} hasta ${max_val:.2f}"
    return 0, "Fuera de Rango"