import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.functions import filter_scatter

st.markdown("<h1 style='text-align: center;'>Visualizaciones y comparación</h1>", unsafe_allow_html=True)


# ==================== CARGA DE DATOS ====================
df = load_data()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### Filtros")

    managers = df["Manager"].dropna().unique().tolist()
    managers_filtro = st.multiselect(
        "Selecciona Manager",
        managers,
        default=managers,
    )

    categorias = df["Category"].dropna().unique().tolist()
    categorias_filtro = st.multiselect(
        "Filtra por categoría",
        categorias,
        default=categorias,
    )

# ==================== FILTROS ====================
df_filtrado = filter_scatter(df, managers_filtro, categorias_filtro)


# ==================== GRÁFICA ====================
fig = px.scatter(
    df_filtrado,
    x="BudgetThousands",
    y="PercentComplete",
    color="State",
    hover_data=["ProjectName", "Manager", "PercentComplete", "BudgetThousands"],
    title = "Avance vs Presupuesto (k$)"
)

st.plotly_chart(fig, use_container_width=True)
