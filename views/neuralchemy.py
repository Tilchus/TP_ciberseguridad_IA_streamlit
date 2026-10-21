import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils.loader import cargar_datos_neuralchemy
from utils.ui import SEVERITY_COLOR_MAP, apply_global_theme, style_plotly_chart

# ==========================================
# 1. APLICAR TEMA GLOBAL Y FONDO CIBERNÉTICO
# ==========================================
apply_global_theme()

# ==========================================
# 1.1 ESTILOS CSS ADICIONALES PARA EL PANEL DE ENCABEZADO
# ==========================================
st.markdown(
    """
    <style>
    /* Estilo para el panel contenedor del encabezado (Estilo Home/Horizon) */
    .header-panel {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(5, 11, 24, 0.98));
        border: 2px solid rgba(0, 229, 255, 0.6);
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.2);
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 2. ENCABEZADO PRINCIPAL DE LA VISTA (PANEL CIBERNÉTICO)
# ==========================================
st.markdown(
    """
    <div class="header-panel">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
            <div style="background: rgba(0, 229, 255, 0.15); border: 1px solid #00E5FF; border-radius: 10px; padding: 10px 14px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 1.5rem;">🧠</span>
            </div>
            <div>
                <h2 style="color: #00E5FF; margin: 0; font-weight: 800; font-size: 1.6rem; letter-spacing: 0.5px;">
                    NeurAlchemy: Auditoría y Análisis Avanzado
                </h2>
                <p style="color: rgba(255, 255, 255, 0.6); margin: 0; font-size: 0.85rem;">
                    Ecosistema de Auditoría, Detección de Prompt Injection y Severidad de Riesgos
                </p>
            </div>
        </div>
        <hr style="border-color: rgba(0, 229, 255, 0.2); margin: 12px 0;">
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px;">
            <em>Esta fuente contiene un conjunto de datos diseñado para entrenar y evaluar modelos de aprendizaje automático capaces de detectar ataques de inyección de instrucciones (prompt injection) y otras técnicas que buscan manipular el comportamiento de una IA o evadir sus medidas de seguridad.</em>
        </p>
        <p style="color: rgba(255, 255, 255, 0.75); font-size: 0.9rem; line-height: 1.6; margin-bottom: 0;">
            <em>Incluye ejemplos de textos maliciosos y legítimos, clasificados mediante etiquetas, categorías de ataque y niveles de gravedad. Estos datos permiten desarrollar y evaluar clasificadores que distingan entre instrucciones potencialmente peligrosas y mensajes benignos.</em>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 3. CARGA DE DATOS MEDIANTE EL LOADER
# ==========================================
df_sev, df_cat, df_cruce, df_proc = cargar_datos_neuralchemy()

# ==========================================
# FILA 1: DISTRIBUCIÓN GLOBAL Y TOP CATEGORÍAS
# ==========================================
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("📊 Diagrama de Pareto: Severidad de Riesgo")
        if not df_sev.empty:
            cols = df_sev.columns.tolist()
            
            # Copia local y ordenamiento descendente por cantidad de casos para Pareto
            df_pareto = df_sev.copy()
            df_pareto[cols[1]] = pd.to_numeric(df_pareto[cols[1]], errors='coerce').fillna(0)
            df_pareto = df_pareto.sort_values(by=cols[1], ascending=False).reset_index(drop=True)
            
            # Cálculo del porcentaje acumulado
            total_casos = df_pareto[cols[1]].sum()
            df_pareto["acumulado"] = (df_pareto[cols[1]].cumsum() / total_casos) * 100 if total_casos > 0 else 0
            
            # Mapeo de colores por barra
            bar_colors = [SEVERITY_COLOR_MAP.get(sev, "#00E5FF") for sev in df_pareto[cols[0]]]

            # Construcción del gráfico combinado (Barras + Línea con doble eje Y)
            fig_pareto = go.Figure()

            # Barras de frecuencia
            fig_pareto.add_trace(
                go.Bar(
                    x=df_pareto[cols[0]],
                    y=df_pareto[cols[1]],
                    name="Cantidad de Casos",
                    marker=dict(color=bar_colors),
                    text=df_pareto[cols[1]],
                    textposition="auto",
                    hovertemplate="%{x}: %{y} casos<extra></extra>",
                )
            )

            # Línea de porcentaje acumulado (Eje Y2)
            fig_pareto.add_trace(
                go.Scatter(
                    x=df_pareto[cols[0]],
                    y=df_pareto["acumulado"],
                    name="% Acumulado",
                    mode="lines+markers",
                    line=dict(color="#00E5FF", width=3),
                    marker=dict(size=8, color="#00E5FF"),
                    yaxis="y2",
                    hovertemplate="%{x}: %{y:.1f}% acumulado<extra></extra>",
                )
            )

            # Estilizado base
            fig_pareto = style_plotly_chart(fig_pareto)

            # Configuración de los ejes y legenda
            fig_pareto.update_layout(
                xaxis=dict(title="Nivel de Severidad"),
                yaxis=dict(
                    title="Cantidad de Casos",
                    showgrid=True,
                    gridcolor="rgba(255,255,255,0.1)"
                ),
                yaxis2=dict(
                    title="% Acumulado",
                    overlaying="y",
                    side="right",
                    range=[0, 105],
                    showgrid=False,
                    ticksuffix="%"
                ),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                margin=dict(t=30, b=20, l=10, r=10)
            )

            st.plotly_chart(fig_pareto, use_container_width=True)
            st.markdown(
                "_Análisis de Pareto que clasifica los niveles de severidad en orden descendente junto con la curva de frecuencia acumulada, permitiendo identificar rápidamente los niveles de riesgo que concentran la mayor proporción de incidentes._",
                unsafe_allow_html=True,
            )
        else:
            st.warning("⚠️ No se encontró el archivo resumen_severidad.parquet")

with col2:
    with st.container(border=True):
        st.subheader("🍩 Top Categorías de Ataque")
        if not df_cat.empty:
            cols_cat = df_cat.columns.tolist()
            fig_cat = px.pie(
                df_cat,
                names=cols_cat[0],
                values=cols_cat[1],
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Prism,
            )
            fig_cat = style_plotly_chart(fig_cat)
            st.plotly_chart(fig_cat, use_container_width=True)
            st.markdown(
                "_Ilustra la proporción porcentual de los principales vectores de"
                " ataque detectados en el corpus._",
                unsafe_allow_html=True,
            )
        else:
            st.warning("⚠️ No se encontró el archivo top_categorias_ataque.parquet")

st.markdown("---")

# ==========================================
# FILA 2: ANÁLISIS PROFUNDO (TOP 10 VS SEVERIDAD)
# ==========================================
with st.container(border=True):
    st.subheader("🔥 Análisis Profundo: Top 10 Categorías vs. Severidad")
    if not df_cruce.empty:
        severity_cols = [c for c in df_cruce.columns if c != "category"]
        df_cruce["total"] = df_cruce[severity_cols].sum(axis=1)
        df_top10 = (
            df_cruce.sort_values(by="total", ascending=False)
            .head(10)
            .sort_values(by="total", ascending=True)
        )
        df_top10_clean = df_top10.drop(columns=["total"])

        fig_cruce = px.bar(
            df_top10_clean,
            y="category",
            x=severity_cols,
            color_discrete_map=SEVERITY_COLOR_MAP,
            barmode="stack",
            orientation="h",
            labels={
                "value": "Cantidad de Incidencias",
                "category": "Categoría de Ataque",
                "variable": "Nivel de Severidad",
            },
        )
        
        # Aplicar estilos y quitar el 'undefined'
        fig_cruce = style_plotly_chart(fig_cruce)
        
        # Ajustes de dimensiones y espacio de barras
        fig_cruce.update_layout(
            xaxis_type="linear",
            height=480,
            bargap=0.25,
            legend_title_text="Nivel de Severidad"
        )
        
        st.plotly_chart(fig_cruce, use_container_width=True)
        st.markdown(
            "_Desglose detallado de las 10 principales categorías de ataque"
            " cruzadas con sus respectivos niveles de severidad, facilitando la"
            " detección de vulnerabilidades críticas prioritarias._",
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "⚠️ No se encontró la tabla de cruce categoría-severidad.parquet"
        )

st.markdown("---")

# ==========================================
# FILA 3: TABLA CONSOLIDADA DE REGISTROS PROCESADOS CON PAGINACIÓN
# ==========================================
with st.container(border=True):
    st.subheader("📋 Muestra Consolidada de Registros Procesados")
    st.markdown(
        "_Exploración tabular interactiva de los vectores de auditoría y"
        " metadatos de inyección procesados._",
        unsafe_allow_html=True,
    )

    if not df_proc.empty:
        rows_per_page = 25
        total_rows = len(df_proc)
        total_pages = max(
            1,
            (total_rows // rows_per_page)
            + (1 if total_rows % rows_per_page > 0 else 0),
        )

        col_info, col_pag = st.columns([3, 1])
        with col_info:
            page_number = st.number_input(
                "Seleccionar Página",
                min_value=1,
                max_value=total_pages,
                value=1,
                step=1,
                key="pag_neuralchemy_proc",
            )
        with col_pag:
            st.markdown(f"**Total Páginas:** {total_pages}")
            st.markdown(f"**Registros Totales:** {total_rows}")

        start_idx = (page_number - 1) * rows_per_page
        end_idx = start_idx + rows_per_page
        df_page = df_proc.iloc[start_idx:end_idx]

        st.dataframe(df_page, use_container_width=True, height=420)
    else:
        st.warning("⚠️ No se encontró el archivo neurAlchemy_procesado.parquet")

# ==========================================
# 4. PIE DE PÁGINA (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: rgba(255, 255, 255, 0.6);"
    " font-size: 0.85em;'>Fuente: NeurAlchemy — Prompt Injection Dataset,"
    " publicada en Hugging Face.</div>",
    unsafe_allow_html=True,
)
