import streamlit as st

st.set_page_config(
    page_title="Panel de Ciberseguridad LLM - NEXO GRIDS",
    page_icon="🛡️",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* Ocultar la barra de desplazamiento en la barra lateral */
    [data-testid="stSidebar"]::-webkit-scrollbar {
        display: none;
    }
    [data-testid="stSidebar"] {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }
    
    /* Forzar diseño flexible en el sidebar para anclar contenido al fondo sin scroll */
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        overflow: hidden !important;
    }
    
    /* Asegurar que no queden bordes o líneas blancas sobrantes */
    [data-testid="stSidebar"] hr {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navegación: las vistas del ecosistema
pg = st.navigation([
    st.Page("views/home.py", title="Inicio / Home", icon="🏠"),
    st.Page(
        "views/neuralchemy.py", title="NeurAlchemy (Base Principal)", icon="🧠"
    ),
    st.Page("views/horizon.py", title="Horizon Dataset", icon="📊"),
    st.Page("views/benchmark.py", title="Injection Benchmark", icon="🎯"),
])

pg.run()

# Logo institucional 
with st.sidebar:
  st.image("imagenes/logo.png", use_container_width=True)