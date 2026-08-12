# src/config.py

# Enlaces oficiales extraídos de tus fuentes de consulta
OFFICIAL_SOURCES = {
    'GT': {
        'nombre': 'Guatemala (MEM / Banguat)',
        'url_combustible': 'https://mem.gob.gt/que-hacemos/hidrocarburos/comercializacion-downstream/precios-combustible-nacionales/',
        'url_tasa': 'https://www.banguat.gob.gt/tipo_cambio'
    },
    'CR': {
        'nombre': 'Costa Rica (Recope / BCCR)',
        'url_combustible': 'https://www.recope.go.cr/productos/precios-nacionales/historicos/',
        'url_tasa': 'https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%20400'
    },
    'SV': {
        'nombre': 'El Salvador (DGEHM / BCR)',
        'url_combustible': 'https://sinapp.dgehm.gob.sv/drhm/estadisticas.aspx?uid=3',
        'url_tasa': 'Moneda Oficial (USD)'
    },
    'HN': {
        'nombre': 'Honduras (SEN / BCH)',
        'url_combustible': 'https://sen.hn/',
        'url_tasa': 'https://www.bch.hn/politica-institucional/politica-cambiaria/tipo-de-cambio-de-referencia'
    },
    'NI': {
        'nombre': 'Nicaragua (INE / BCN)',
        'url_combustible': 'https://www.ine.gob.ni/',
        'url_tasa': 'https://www.bcn.gob.ni/IRR/tipo_cambio_mensual/index.php'
    }
}

# Impuestos fijos por galón en MONEDA LOCAL a deducir antes de convertir a USD
TAX_DEDUCTIONS = {
    'SV': {'FOVIAL': 0.20, 'COTRANS': 0.10, 'FEFE': 0.16, 'IEC': 0.00},
    'GT': {'IVA': 1.12, 'IDP': 1.30},
    'HN': {'IMPUESTOS': 0.00},
    'NI': {'IMPUESTOS': 0.00},
    'CR': {'IVA_ESTIMADO': 1.66}
}

# Estructura de las 15 Bandas (Factor en USD)
BANDS_REFERENCE = {
    1: (2.11, 2.36), 2: (2.37, 2.62), 3: (2.63, 2.88), 4: (2.89, 3.14),
    5: (3.15, 3.40), 6: (3.41, 3.66), 7: (3.67, 3.92), 8: (3.93, 4.18),
    9: (4.19, 4.44), 10: (4.45, 4.70), 11: (4.71, 4.96), 12: (4.97, 5.22),
    13: (5.23, 5.48), 14: (5.49, 5.74), 15: (5.75, 6.00)
}
