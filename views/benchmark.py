from pathlib import Path
import sys

# Agregar la raíz del proyecto al path de Python para que reconozca 'utils'
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
  sys.path.append(str(ROOT_DIR))

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils.loader import cargar_datos_benchmark
from utils.ui import SEVERITY_COLOR_MAP, apply_global_theme, style_plotly_chart

# ==========================================
# 1. APLICAR TEMA GLOBAL Y FONDO CIBERNÉTICO
# ==========================================
apply_global_theme()

# ==========================================
# 1.1 ESTILOS CSS ADICIONALES PARA BENCHMARK
# ==========================================
st.markdown(
    """
    <style>
    .header-panel {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(5, 11, 24, 0.98));
        border: 2px solid rgba(0, 229, 255, 0.6);
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.2);
        margin-bottom: 25px;
    }
    .kpi-card-cyan {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.9), rgba(5, 11, 24, 0.95));
        border: 1px solid #00E5FF;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.15);
    }
    .kpi-card-red {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.9), rgba(5, 11, 24, 0.95));
        border: 1px solid #FF1744;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(255, 23, 68, 0.15);
    }
    .kpi-card-yellow {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.9), rgba(5, 11, 24, 0.95));
        border: 1px solid #FFEA00;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(255, 234, 0, 0.15);
    }
    .kpi-card-green {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.9), rgba(5, 11, 24, 0.95));
        border: 1px solid #00E676;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0, 230, 118, 0.15);
    }
    .methodology-box {
        background: rgba(255, 193, 7, 0.1);
        border: 1px solid rgba(255, 193, 7, 0.5);
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 2. ENCABEZADO PRINCIPAL DE LA VISTA
# ==========================================
st.markdown(
    """
    <div class="header-panel">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
            <div style="background: rgba(0, 229, 255, 0.15); border: 1px solid #00E5FF; border-radius: 10px; padding: 10px 14px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 1.5rem;">🎯</span>
            </div>
            <div>
                <h2 style="color: #00E5FF; margin: 0; font-weight: 800; font-size: 1.6rem; letter-spacing: 0.5px;">
                    Injection Benchmark | Análisis del Banco de Pruebas
                </h2>
                <p style="color: rgba(255, 255, 255, 0.6); margin: 0; font-size: 0.85rem;">
                    Conjunto de datos de ataques de inyección de prompt y ejemplos benignos
                </p>
            </div>
        </div>
        <hr style="border-color: rgba(0, 229, 255, 0.2); margin: 12px 0;">
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px;">
            <em>Este conjunto de datos recopila ejemplos de ataques de inyección de prompt etiquetados junto con prompts benignos, diseñado específicamente para poner a prueba y comparar sistemas de detección de inyecciones.</em>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Nota Simple
st.markdown(
    """
    <div class="methodology-box">
        <h4 style="color: #FFD600; margin: 0 0 8px 0; font-size: 1rem;">⚠️ Nota sobre el Dataset</h4>
        <p style="color: rgba(255, 255, 255, 0.85); font-size: 0.88rem; margin: 0; line-height: 1.5;">
            El análisis utiliza una muestra de referencia con ejemplos distribuidos en categorías de ataque y tráfico benigno para evaluar el comportamiento del sistema.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 3. CARGA DE DATOS DEL BENCHMARK (4 VALORES)
# ==========================================
df_label, df_category, df_severity, df_cat_sev = cargar_datos_benchmark()

# ==========================================
# 4. KPIS PRINCIPALES DEL BENCHMARK
# ==========================================
total_muestras = int(df_label["cantidad"].sum()) if not df_label.empty else 303
total_taxonomias = len(df_category) if not df_category.empty else 8

pct_inyeccion = 66.01
cant_inyeccion = 200
cant_benigno = 103
pct_benigno = 33.99

if not df_label.empty:
  row_inj = df_label[df_label["label"].astype(str).str.lower() == "injection"]
  if not row_inj.empty:
    pct_inyeccion = float(row_inj["porcentaje (%)"].values[0])
    cant_inyeccion = int(row_inj["cantidad"].values[0])

  row_ben = df_label[df_label["label"].astype(str).str.lower() == "benign"]
  if not row_ben.empty:
    pct_benigno = float(row_ben["porcentaje (%)"].values[0])
    cant_benigno = int(row_ben["cantidad"].values[0])

col_k1, col_k2, col_k3, col_k4 = st.columns(4)

with col_k1:
  st.markdown(
      f"""
        <div class="kpi-card-cyan">
            <p style="color: rgba(255,255,255,0.7); font-size: 0.85rem; margin: 0;">📊 Muestras Totales</p>
            <h3 style="color: #00E5FF; font-size: 1.8rem; font-weight: 800; margin: 5px 0 0 0;">{total_muestras}</h3>
        </div>
        """,
      unsafe_allow_html=True,
  )

with col_k2:
  st.markdown(
      f"""
        <div class="kpi-card-red">
            <p style="color: rgba(255,255,255,0.7); font-size: 0.85rem; margin: 0;">⚡ Porcentaje de Ataques</p>
            <h3 style="color: #FF1744; font-size: 1.8rem; font-weight: 800; margin: 5px 0 0 0;">{pct_inyeccion:.2f}%</h3>
        </div>
        """,
      unsafe_allow_html=True,
  )

with col_k3:
  st.markdown(
      f"""
        <div class="kpi-card-yellow">
            <p style="color: rgba(255,255,255,0.7); font-size: 0.85rem; margin: 0;">🗂️ Categorías de Ataque</p>
            <h3 style="color: #FFEA00; font-size: 1.8rem; font-weight: 800; margin: 5px 0 0 0;">{total_taxonomias}</h3>
        </div>
        """,
      unsafe_allow_html=True,
  )

with col_k4:
  st.markdown(
      f"""
        <div class="kpi-card-green">
            <p style="color: rgba(255,255,255,0.7); font-size: 0.85rem; margin: 0;">🛡️ Niveles de Severidad</p>
            <h3 style="color: #00E676; font-size: 1.8rem; font-weight: 800; margin: 5px 0 0 0;">4 Rangos</h3>
        </div>
        """,
      unsafe_allow_html=True,
  )

st.write("")
st.markdown("---")

# ==================
# 5. VISUALIZACIONES 
# ==================
col_g1, col_g2 = st.columns(2)

# --- GRÁFICO 1: GAUGE CHART ---
with col_g1:
  with st.container(border=True):
    st.subheader("🎯 Concentración de Ataques")

    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=pct_inyeccion,
            number={"suffix": "%", "font": {"color": "#00E5FF", "size": 36}},
            title={
                "text": "Tasa de Inyección vs Benigno",
                "font": {"color": "white", "size": 16},
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "white",
                },
                "bar": {"color": "#FF1744"},
                "bgcolor": "rgba(10, 25, 47, 0.8)",
                "borderwidth": 2,
                "bordercolor": "rgba(0, 229, 255, 0.5)",
                "steps": [
                    {"range": [0, 34], "color": "rgba(0, 229, 255, 0.35)"},
                    {"range": [34, 100], "color": "rgba(255, 23, 68, 0.35)"},
                ],
                "threshold": {
                    "line": {"color": "#FF1744", "width": 4},
                    "thickness": 0.75,
                    "value": 60,
                },
            },
        )
    )
    fig_gauge = style_plotly_chart(fig_gauge)
    fig_gauge.update_layout(height=310, margin=dict(t=40, b=10, l=30, r=30))
    st.plotly_chart(fig_gauge, use_container_width=True)

    subcol1, subcol2 = st.columns(2)
    with subcol1:
      st.markdown(
          f"<div style='text-align: center; background: rgba(255,23,68,0.1); border: 1px solid rgba(255,23,68,0.4); border-radius: 8px; padding: 8px;'><span style='color: #FF1744; font-weight: bold;'>Injection:</span> {cant_inyeccion} reg. ({pct_inyeccion:.2f}%)</div>",
          unsafe_allow_html=True,
      )
    with subcol2:
      st.markdown(
          f"<div style='text-align: center; background: rgba(0,229,255,0.1); border: 1px solid rgba(0,229,255,0.4); border-radius: 8px; padding: 8px;'><span style='color: #00E5FF; font-weight: bold;'>Benign:</span> {cant_benigno} reg. ({pct_benigno:.2f}%)</div>",
          unsafe_allow_html=True,
      )

    st.caption(
        "_Gauge Chart (Tacómetro) — Concentración de prompts maliciosos frente"
        " al tráfico benigno._"
    )

# --- GRÁFICO 2: TREEMAP ---
with col_g2:
  with st.container(border=True):
    st.subheader("🗺️ Mapa Jerárquico de Categorías")

    if not df_category.empty:
      fig_tree = px.treemap(
          df_category,
          path=["category"],
          values="cantidad",
          color="category",
          color_discrete_sequence=px.colors.qualitative.Set3,
      )
      fig_tree = style_plotly_chart(fig_tree)
      fig_tree.update_layout(
          height=380, margin=dict(t=20, b=20, l=20, r=20), coloraxis_showscale=False
      )
      st.plotly_chart(fig_tree, use_container_width=True)
      st.caption(
          "_Treemap — Distribución proporcional de los vectores de ataque. "
          "Destacan las categorías con mayor incidencia: **jailbreak** (elusión de directivas de seguridad "
          "y restricciones éticas del modelo) y **data_exfiltration** (intentos de forzar al sistema a "
          "revelar información confidencial o datos privados del entorno)._"
      )
    else:
      st.info("⚠️ Datos de categorías no disponibles.")

st.markdown("---")

# ==========================================
# 6. SECCIÓN INFERIOR: MAPA DE CALOR Y MATRIZ 3D
# ==========================================
col_inf1, col_inf2 = st.columns([1, 1])

# --- GRÁFICO NUEVO: MAPA DE CALOR (HEATMAP CON PALETA TURBO) ---
with col_inf1:
  st.subheader("🔥 Mapa de Calor: Categoría vs. Severidad")
  with st.container(border=True):
    if not df_cat_sev.empty:
      cols_sev = [
          c
          for c in ["low", "medium", "high", "critical"]
          if c in df_cat_sev.columns
      ]

      fig_heat = px.imshow(
          df_cat_sev[cols_sev].values,
          x=[s.upper() for s in cols_sev],
          y=df_cat_sev["category"].tolist(),
          text_auto=True,
          color_continuous_scale="Turbo",
          aspect="auto",
      )
      fig_heat = style_plotly_chart(fig_heat)
      fig_heat.update_layout(
          height=350,
          margin=dict(t=20, b=20, l=50, r=20),
          xaxis_title="Nivel de Severidad",
          yaxis_title="Categoría de Ataque",
          coloraxis_showscale=True,
      )
      fig_heat.update_traces(
          textfont=dict(color="white", size=12, family="sans-serif")
      )

      st.plotly_chart(fig_heat, use_container_width=True)
      st.caption(
          "_Heatmap (Mapa de Calor) — Distribución cruzada por categoría y nivel de severidad. "
          "**Análisis y sugerencias:** Este mapa nos sugiere que la concentración de incidencias no se distribuye de manera uniforme; "
          "permite identificar rápidamente qué vectores de ataque acumulan los niveles de riesgo más altos (como *critical* y *high*). "
          "Esto sugiere priorizar las defensas y los filtros de validación en aquellas categorías específicas que muestran mayor densidad de amenazas severas, "
          "evitando asignar los mismos recursos de mitigación a vectores de menor impacto._"
      )
    else:
      st.info("⚠️ Datos de distribución cruzada no disponibles.")

# --- GRÁFICO 3: MATRIZ 3D DE SEVERIDAD ---
with col_inf2:
  st.subheader("🌌 Matriz 3D de Severidad")
  with st.container(border=True):
    if not df_severity.empty:
      sev_orden = ["low", "medium", "high", "critical"]
      df_sev_plot = df_severity.copy()
      df_sev_plot["orden"] = df_sev_plot["severity"].map(
          {s: i for i, s in enumerate(sev_orden)}
      )
      df_sev_plot = df_sev_plot.sort_values("orden")

      x_vals = df_sev_plot["severity"].tolist()
      y_vals = [i * 1.5 for i in range(len(x_vals))]
      z_vals = df_sev_plot["cantidad"].tolist()
      colors = [SEVERITY_COLOR_MAP.get(s, "#00E5FF") for s in x_vals]

      fig_3d = go.Figure()

      for x, y, z, col in zip(x_vals, y_vals, z_vals, colors):
        fig_3d.add_trace(
            go.Scatter3d(
                x=[x, x],
                y=[y, y],
                z=[0, z],
                mode="lines",
                line=dict(color=col, width=6),
                showlegend=False,
                hoverinfo="none",
            )
        )

      fig_3d.add_trace(
          go.Scatter3d(
              x=x_vals,
              y=y_vals,
              z=z_vals,
              mode="markers+text",
              text=[
                  f"<b>{s.upper()}</b><br>{c} reg."
                  for s, c in zip(x_vals, z_vals)
              ],
              textposition="top center",
              textfont=dict(color="white", size=11),
              marker=dict(
                  size=14,
                  color=colors,
                  symbol="diamond",
                  opacity=0.9,
                  line=dict(color="white", width=1),
              ),
              showlegend=False,
          )
      )

      fig_3d.update_layout(
          scene=dict(
              xaxis=dict(
                  title="Nivel de Severidad",
                  backgroundcolor="rgba(0,0,0,0)",
                  gridcolor="rgba(0,229,255,0.2)",
                  color="white",
              ),
              yaxis=dict(
                  title="",
                  showticklabels=False,
                  backgroundcolor="rgba(0,0,0,0)",
                  gridcolor="rgba(0,0,0,0)",
              ),
              zaxis=dict(
                  title="Volumen",
                  backgroundcolor="rgba(0,0,0,0)",
                  gridcolor="rgba(0,229,255,0.2)",
                  color="white",
              ),
              bgcolor="rgba(5,11,24,0.95)",
              camera=dict(
                  eye=dict(x=0.0, y=-2.8, z=0.9),
                  center=dict(x=0, y=0, z=0),
                  up=dict(x=0, y=0, z=1),
              ),
          ),
          height=350,
          margin=dict(t=20, b=20, l=20, r=20),
          paper_bgcolor="rgba(0,0,0,0)",
          plot_bgcolor="rgba(0,0,0,0)",
      )
      st.plotly_chart(fig_3d, use_container_width=True)
      st.caption(
          "_3D Scatter & Drop-lines Matrix — Proyección tridimensional de los"
          " niveles de severidad._"
      )
    else:
      st.info("⚠️ Datos de severidad no disponibles para el gráfico 3D.")

# ==========================================
# 7. PIE DE PÁGINA (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: rgba(255, 255, 255, 0.6);"
    " font-size: 0.85em;'>Injection Benchmark — Evaluación de Suite. Entorno"
    " Experimental.</div>",
    unsafe_allow_html=True,
)