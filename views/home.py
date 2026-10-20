import streamlit as st
from utils.ui import apply_global_theme

# Aplicar estilo unificado
apply_global_theme()

# ==========================================
# ESTILOS CSS AVANZADOS: SIMETRÍA Y BLOQUEO DE ALTURA EN KPIS
# ==========================================
st.markdown(
    """
    <style>
    /* Forzar que el contenedor principal aproveche mejor el ancho */
    .block-container {
        max-width: 95% !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Forzar simetría estricta y altura idéntica en las 3 tarjetas de KPIs */
    .kpi-red-card {
        background-color: rgba(239, 68, 68, 0.08) !important;
        border: 2px solid #ef4444 !important;
        border-radius: 14px !important;
        padding: 22px 18px !important;
        text-align: center !important;
        box-shadow: 0px 0px 15px rgba(239, 68, 68, 0.25) !important;
        height: 250px !important; /* Altura fija idéntica para los tres contenedores */
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important; /* Distribuye elementos de arriba a abajo de forma uniforme */
        box-sizing: border-box !important;
    }

    /* Estilizado estricto para los accesos directos a módulos de auditoría */
    div[data-testid="stHorizontalBlock"] > div {
        display: flex;
        flex-direction: column;
    }
    
    div[data-testid="stHorizontalBlock"] > div > div[data-testid="stContainer"] {
        flex: 1 !important;
        height: 360px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        background-color: rgba(10, 25, 47, 0.9) !important;
        border: 1px solid rgba(0, 229, 255, 0.5) !important;
        border-radius: 14px !important;
        padding: 24px !important;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
    }

    div[data-testid="stButton"] {
        width: 100% !important;
        margin-top: auto !important;
    }

    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, rgba(0, 229, 255, 0.15), rgba(10, 25, 47, 0.95)) !important;
        color: #00E5FF !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        border: 2px solid #00E5FF !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        letter-spacing: 0.5px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 0px 12px rgba(0, 229, 255, 0.25);
        display: block !important;
        margin: 0 auto !important;
    }

    div[data-testid="stButton"] > button:hover {
        background: rgba(0, 229, 255, 0.3) !important;
        color: #FFFFFF !important;
        border-color: #FFFFFF !important;
        box-shadow: 0px 0px 20px rgba(0, 229, 255, 0.8);
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# SECCIÓN HERO / BANNER PRINCIPAL
# ==========================================
st.markdown(
    """
    <div style="background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(5, 11, 24, 0.95)); border: 2px solid rgba(0, 229, 255, 0.6); border-radius: 16px; padding: 35px 30px; text-align: center; box-shadow: 0px 0px 30px rgba(0, 229, 255, 0.25); margin-bottom: 25px;">
        <div style="font-size: 3rem; margin-bottom: 10px;">🛡️</div>
        <h1 style="font-size: 3.2rem; font-weight: 900; background: linear-gradient(90deg, #00E5FF, #ffffff, #00E5FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0px 0px 25px rgba(0, 229, 255, 0.5); letter-spacing: 1px; margin-bottom: 10px;">
            RIESGO CRÍTICO EN CHATBOTS DE IA
        </h1>
        <p style="font-size: 1.4rem; font-weight: 600; color: #cbd5e1; letter-spacing: 0.5px; margin: 0;">
            Impacto Financiero y Exposición a Vulnerabilidades
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================
# LAS 3 KPIS FINANCIERAS 
# ==========================
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown(
        """
        <div class="kpi-red-card">
            <h4 style="color: #f87171; font-weight: 700; margin: 0; font-size: 1.15rem; line-height: 1.3;">💸 Pérdidas Directas e Interrupción</h4>
            <h2 style="color: #ffffff; font-weight: 900; font-size: 1.85rem; margin: 0; text-shadow: 0 0 10px rgba(239, 68, 68, 0.5);">$100k - $500k USD</h2>
            <p style="color: #cbd5e1; font-size: 0.85rem; margin: 0; line-height: 1.3;">Por incidente o evento critico, inactividad, auditoría forense y remediación de emergencia.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        """
        <div class="kpi-red-card">
            <h4 style="color: #f87171; font-weight: 700; margin: 0; font-size: 1.15rem; line-height: 1.3;">🔒 Fuga de Datos y Sanciones</h4>
            <h2 style="color: #ffffff; font-weight: 900; font-size: 1.85rem; margin: 0; text-shadow: 0 0 10px rgba(239, 68, 68, 0.5);">Hasta 4%</h2>
            <p style="color: #cbd5e1; font-size: 0.85rem; margin: 0; line-height: 1.3;">De facturación global anual en multas regulatorias por exfiltración.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        """
        <div class="kpi-red-card">
            <h4 style="color: #f87171; font-weight: 700; margin: 0; font-size: 1.15rem; line-height: 1.3;">📉 Impacto Reputacional</h4>
            <h2 style="color: #ffffff; font-weight: 900; font-size: 1.85rem; margin: 0; text-shadow: 0 0 10px rgba(239, 68, 68, 0.5);">Pérdida de Confianza</h2>
            <p style="color: #cbd5e1; font-size: 0.85rem; margin: 0; line-height: 1.3;">Degradación inmediata de la credibilidad de marca.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# PREGUNTA EJECUTIVA Y SÍNTESIS
# ==========================================
with st.container(border=True):
    st.markdown(
        """
        <h2 style="background: linear-gradient(90deg, #00E5FF, #ffffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.7rem; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
            ¿Sabías el riesgo real y el costo financiero que corre tu empresa si su chatbot es vulnerado?
        </h2>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #f1f5f9; margin-bottom: 10px;">
            El despliegue de asistentes virtuales expone a la organización a <b>inyecciones de instrucciones</b> (<i>Prompt Injection</i>). 
            No es un simple fallo técnico, sino un evento que <b>impacta fuertemente en lo económico y en lo operativo</b>.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.5; color: #cbd5e1; margin-bottom: 0;">
            📊 <b>Este reporte y centro de control analítico</b> visibiliza los vectores de ataque y su severidad para <b>tomar las decisiones correctas y blindar la inteligencia artificial de tu empresa.</b>
        </p>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ==========================================
# MARCO TEÓRICO: PROMPT INJECTION
# ==========================================
with st.container(border=True):
  st.subheader("📖¿Qué es el Prompt Injection?")
  st.markdown(
      "El **Prompt Injection** (Inyección de Instrucciones) representa una de"
      " las vulnerabilidades críticas más desafiantes en la seguridad de los"
      " Modelos de Lenguaje Grande (LLMs). Ocurre cuando un actor malicioso o"
      " una fuente de datos externa manipula las entradas de texto (*prompts*)"
      " con comandos diseñados para subvertir las restricciones de diseño,"
      " directrices éticas o directivas del sistema (*System Prompts*).",
      unsafe_allow_html=True,
  )
  st.markdown(
      "**Objetivos de esta plataforma:** Detectar, clasificar y auditar estos"
      " vectores de ataque para mitigar riesgos de filtración de datos,"
      " ejecución de comandos no autorizados y desalineación del comportamiento"
      " del modelo.",
      unsafe_allow_html=True,
  )

st.markdown("---")

# ==========================================
# ACCESOS DIRECTOS A LOS MÓDULOS
# ==========================================
st.subheader("🧭 Accesos Directos a los Módulos de Auditoría")
st.markdown(
    "_Seleccione cualquiera de los siguientes componentes para iniciar el"
    " análisis interactivo de los datasets procesados._",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
  with st.container(border=True):
    st.markdown("### 🧠 NeurAlchemy")
    st.markdown(
        "_Base principal de auditoría, distribución global de severidad,"
        " categorías de ataque y análisis cruzado._"
    )
    st.write("")
    if st.button("⚡ EXPLORAR NEURALCHEMY", key="btn_neur"):
      st.switch_page("views/neuralchemy.py")

with c2:
  with st.container(border=True):
    st.markdown("### 📊 Horizon")
    st.markdown(
        "_Análisis estructural del corpus, matrices de frecuencia absoluta y"
        " radiografía lingüística._"
    )
    st.write("")
    if st.button("🚀 EXPLORAR HORIZON", key="btn_horiz"):
      st.switch_page("views/horizon.py")

with c3:
  with st.container(border=True):
    st.markdown("### 🎯Benchmark")
    st.markdown(
        "_Evaluación estandarizada de distribuciones de etiquetas,"
        " categorías y severidades para benchmarks._"
    )
    st.write("")
    if st.button("🔥 EXPLORAR BENCHMARK", key="btn_bench"):
      st.switch_page("views/benchmark.py")