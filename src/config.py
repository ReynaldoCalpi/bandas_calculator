# src/config.py

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

# Parámetros de Impuestos por País
# SV: IVA 13% ($), Impuestos fijos: FOVIAL $0.20 + COTRANS $0.10
# GT: IVA 12% (Q), Impuesto fijo: IDP Q1.30
TAX_PARAMS = {
    'SV': {'iva_rate': 0.13, 'fijos': [0.20, 0.10]},
    'GT': {'iva_rate': 0.12, 'fijos': [1.30]},
    'CR': {'iva_rate': 0.00, 'fijos': []},
    'HN': {'iva_rate': 0.00, 'fijos': []},
    'NI': {'iva_rate': 0.00, 'fijos': []}
}

# Las 15 Bandas Oficiales Calpi
BANDS_REFERENCE = {
    1: (2.11, 2.36), 2: (2.37, 2.62), 3: (2.63, 2.88), 4: (2.89, 3.14),
    5: (3.15, 3.40), 6: (3.41, 3.66), 7: (3.67, 3.92), 8: (3.93, 4.18),
    9: (4.19, 4.44), 10: (4.45, 4.70), 11: (4.71, 4.96), 12: (4.97, 5.22),
    13: (5.23, 5.48), 14: (5.49, 5.74), 15: (5.75, 6.00)
}
