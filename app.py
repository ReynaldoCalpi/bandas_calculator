# app.py
import streamlit as st
import pandas as pd
from src.calculator import calcular_precio_normalizado, obtener_banda
from src.config import BANDS_REFERENCE

st.set_page_config(page_title="CAFFA - Central America Fuel & Freight", layout="wide")

st.title("🚛 CAFFA: Automatización de Bandas y Tarifas Centroamérica")
st.markdown("Plataforma analítica para el cálculo, normalización y validación de bandas de fletes por país.")

# Sidebar para parámetros generales
st.sidebar.header("Parámetros de Cálculo")
fecha_inicio = st.sidebar.date_input("Fecha Inicial Cálculo")
fecha_final = st.sidebar.date_input("Fecha Final Cálculo")

st.markdown("### 📊 Ingesta de Precios Promedio y Tasas de Cambio")
st.info("Ingrese los valores promedio y las tasas de cambio de referencia para cada país.")

paises = ['SV', 'GT', 'HN', 'NI', 'CR']
monedas = {'SV': '$', 'GT': 'Q', 'HN': 'L', 'NI': 'C$', 'CR': '₡'}

# Creación de inputs dinámicos para los usuarios
datos_ingresados = {}

col1, col2 = st.columns(2)

with col1:
    st.subheader("Precios Promedio Locales (C/IVA o Brutos)")
    precios_brutos = {}
    for p in paises:
        precios_brutos[p] = st.number_input(f"Precio Promedio {p} ({monedas[p]})", value=0.0, format="%.2f")

with col2:
    st.subheader("Tasas de Cambio a USD")
    tasas_cambio = {}
    # Valores por defecto lógicos para arranque
    default_tasas = {'SV': 1.0, 'GT': 7.62, 'HN': 26.72, 'NI': 36.62, 'CR': 454.50}
    for p in paises:
        tasas_cambio[p] = st.number_input(f"Tasa Cambio {p}", value=default_tasas[p], format="%.4f")

if st.button("Ejecutar Cálculo y Normalización", type="primary"):
    resultados = []
    
    # Simulación de datos recibidos por correo de CMI para la comparativa
    # (Puedes ajustar estos valores mock según tu caso de prueba real)
    cmi_mock = {'GT': 4.18, 'CR': 5.59, 'SV': 4.18, 'HN': 4.57, 'NI': 4.45}

    for p in paises:
        p_bruto = precios_brutos[p]
        t_cambio = tasas_cambio[p]
        
        # Cálculo interno
        precio_norm = calcular_precio_normalizado(p_bruto, p, t_cambio)
        id_banda, desc_banda = obtener_banda(precio_norm)
        
        # Comparativa con CMI
        cmi_val = cmi_mock.get(p, precio_norm)
        diferencia = round(precio_norm - cmi_val, 2)
        
        # Banda CMI simulada
        cmi_banda_id, cmi_banda_desc = obtener_banda(cmi_val)

        resultados.append({
            "País": p,
            "Precio Normalizado (USD)": precio_norm,
            "Precio CMI (USD)": cmi_val,
            "Diferencia": diferencia,
            "Banda Calpi Validada": desc_banda,
            "Banda Autorizada CMI": cmi_banda_desc,
            "Estado": "MATCH" if diferencia == 0 else "REVISIÓN REQUERIDA"
        })

    df_resultados = pd.DataFrame(resultados)
    
    st.markdown("---")
    st.markdown("### 📋 Cuadro Resumen de Validación de Bandas")
    st.dataframe(df_resultados, use_container_width=True)
    
    st.success("Cálculos completados con éxito de acuerdo con los parámetros configurados.")