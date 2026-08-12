# src/config.py

# Impuestos fijos por galón en MONEDA LOCAL a deducir antes de convertir a USD
TAX_DEDUCTIONS = {
    'SV': {'FOVIAL': 0.20, 'COTRANS': 0.10, 'FEFE': 0.00, 'IEC': 0.00}, # En USD
    'GT': {'IDP': 1.30},                                                # En Quetzales
    'HN': {'EXENTO': 0.00},                                             # En Lempiras
    'NI': {'EXENTO': 0.00},                                             # En Córdobas
    'CR': {'EXENTO': 0.00}                                              # En Colones
}

# Estructura de las 15 Bandas (Factor en USD) basadas en el estándar Calpi
BANDS_REFERENCE = {
    1: (2.11, 2.36), 2: (2.37, 2.62), 3: (2.63, 2.88), 4: (2.89, 3.14),
    5: (3.15, 3.40), 6: (3.41, 3.66), 7: (3.67, 3.92), 8: (3.93, 4.18),
    9: (4.19, 4.44), 10: (4.45, 4.70), 11: (4.71, 4.96), 12: (4.97, 5.22),
    13: (5.23, 5.48), 14: (5.49, 5.74), 15: (5.75, 6.00)
}