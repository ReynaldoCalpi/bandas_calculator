# app.py
import streamlit as st
import pandas as pd
from src.config import OFFICIAL_SOURCES
from src.calculator import calcular_precio_normalizado, obtener_banda

st.set_page_config(page_title="CAFFA - Central America Fuel & Freight", layout="wide")

st.title("🚛 CAFFA: Automatización de Bandas y Tarifas Centroamérica")
st.markdown("Plataforma analítica basada en consultas directas a fuentes oficiales de la región.")

# Sidebar de Parámetros
st.sidebar.header("Parámetros del Periodo")
fecha_inicio = st.sidebar.date_input("Fecha Inicial de Consulta")
fecha_final = st.sidebar.date_input("Fecha Final de Consulta")

st.markdown("---")
st.markdown("### 🌐 1. Enlaces a Fuentes Oficiales de Consulta")
st.markdown("Utiliza estos accesos directos institucionales para verificar los precios diarios y tasas de cambio antes de ingresarlos:")

cols_fuentes = st.columns(5)
paises = ['SV', 'GT', 'HN', 'NI', 'CR']

for i, p in enumerate(paises):
    with cols_fuentes[i]:
        st.markdown(f"**{OFFICIAL_SOURCES[p]['nombre']}**")
        st.markdown(f"[🔗 Ver Combustible]({OFFICIAL_SOURCES[p]['url_combustible']})")
        if p != 'SV':
            st.markdown(f"[💱 Ver Tasa Cambio]({OFFICIAL_SOURCES[p]['url_tasa']})")

st.markdown("---")
col_izq, col_der = st.columns(2)

with col_izq:
    st.markdown("### 📊 2. Registro de Precios Brutos y Tasas ($$$)")
    st.info("Ingresa los precios brutos promedio expresados en Dólares ($$$) tras consultar las fuentes oficiales.")
    
    precios_brutos = {}
    tasas_cambio = {}
    default_tasas = {'SV': 1.0, 'GT': 7.62, 'HN': 26.72, 'NI': 36.62, 'CR': 454.50}
    default_precios_usd = {'SV': 4.52, 'GT': 4.76, 'HN': 4.52, 'NI': 4.47, 'CR': 5.09}
    
    for p in paises:
        c1, c2 = st.columns(2)
        with c1:
            precios_brutos[p] = st.number_input(f"Bruto {p} ($)", value=default_precios_usd[p], format="%.2f", key=f"p_{p}")
        with c2:
            tasas_cambio[p] = st.number_input(f"Tasa {p}", value=default_tasas[p], format="%.4f", key=f"t_{p}")

with col_der:
    st.markdown("### 📥 3. Datos Compartidos por CMI ($$$)")
    st.info("Ingresa los valores en USD recibidos por correo de CMI para realizar el contraste.")
    
    cmi_valores = {}
    for p in paises:
        cmi_valores[p] = st.number_input(f"Valor CMI {p} ($)", value=4.00, format="%.2f", key=f"cmi_{p}")

st.markdown("---")
if st.button("🚀 Ejecutar Validación y Cruce de Bandas", type="primary"):
    resultados = []

    for p in paises:
        p_bruto = precios_brutos[p]
        t_cambio = tasas_cambio[p]
        
        # Normalización Calpi (Resta de impuestos convertidos a USD + Precio en USD)
        precio_norm = calcular_precio_normalizado(p_bruto, p, t_cambio)
        id_banda_calpi, desc_banda_calpi = obtener_banda(precio_norm)
        
        # Valor CMI
        cmi_val = cmi_valores[p]
        diferencia = round(precio_norm - cmi_val, 2)
        
        # Banda CMI
        id_banda_cmi, desc_banda_cmi = obtener_banda(cmi_val)

        resultados.append({
            "País": p,
            "Bruto Local ($)": p_bruto,
            "Tasa Cambio": t_cambio,
            "Calculado Calpi (USD)": precio_norm,
            "Valor CMI (USD)": cmi_val,
            "Diferencia": diferencia,
            "Banda Calpi Validada": desc_banda_calpi,
            "Banda Autorizada CMI": desc_banda_cmi,
            "Estado": "MATCH" if abs(diferencia) <= 0.01 else "REVISIÓN REQUERIDA"
        })

    df_resultados = pd.DataFrame(resultados)
    
    st.markdown("### 📋 Cuadro Resumen de Validación y Asignación de Bandas")
    st.dataframe(df_resultados, use_container_width=True)
    
    st.success("Proceso de validación completado con éxito.")
