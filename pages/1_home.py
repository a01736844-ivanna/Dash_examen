import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.functions import filter_main_dashboard, get_kpis

st.markdown("<h1 style='text-align: center;'>Dashboard principal de proyectos</h1>", unsafe_allow_html=True)


# Cargar datos
df = load_data()

#  ==================== SIDEBAR  ====================
with st.sidebar:
    st.markdown("### Filtros")

    estados = df["State"].dropna().unique().tolist()
    estado_filtro = st.selectbox("Estado", ["Todos"] + estados)

    categorias = df["Category"].dropna().unique().tolist()
    categoria_filtro = st.selectbox("Categoría", ["Todas"] + categorias)

    avance_min = st.slider("Avance mínimo (%)", 0, 100, 0)

    managers = df["Manager"].dropna().unique().tolist()
    manager_filtro = st.selectbox("Manager", ["Todos"] + managers)


#  ==================== FILTRO  ====================
df_filtrado = filter_main_dashboard(df, estado_filtro, categoria_filtro, manager_filtro, avance_min)


# ==================== KPIs ====================
total_proyectos, prom_avance, managers_unicos, presupuesto_medio = get_kpis(df_filtrado)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Proyectos", total_proyectos)

with col2:
    st.metric("Promedio avance (%)", f"{prom_avance:.1f}")

with col3:
    st.metric("Managers únicos", managers_unicos)

with col4:
    st.metric("Presupuesto medio", f"{presupuesto_medio:.1f}K")

st.markdown("---")

st.dataframe(df_filtrado.head(15))