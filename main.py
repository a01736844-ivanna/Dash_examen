import streamlit as st

st.set_page_config(
    page_title= "Dashboard Examen",
    page_icon="📊",
    layout = "wide",
    initial_sidebar_state = "expanded" 
)

#definir paginas
home_page= st.Page(
    "pages/1_home.py",
    title="Dashboard Principal"
)

projects_page= st.Page(
    "pages/2_analisis.py",
    title="Análsis de Projectos"
)


#navegación
pg=st.navigation({
    "Inicio": [home_page],
    "Análsis":[projects_page],
    })

#ejectutar
pg.run()