import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils.loader import cargar_datos_horizon
from utils.ui import apply_global_theme, style_plotly_chart

# ==========================================
# 1. APLICAR TEMA GLOBAL Y FONDO CIBERNÉTICO
# ==========================================
apply_global_theme()

# ==============================================================
# 1.1 ESTILOS CSS ADICIONALES PARA PANELES Y EXPANSOR 3D NEÓN
# ==============================================================
st.markdown(
    """
    <style>
    /* Estilo para el panel contenedor del encabezado (Estilo Home/Ciberseguridad) */
    .header-panel {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(5, 11, 24, 0.98));
        border: 2px solid rgba(0, 229, 255, 0.6);
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.2);
        margin-bottom: 25px;
    }

    /* Estilizar el st.expander para que tenga el look de tarjeta KPI brillante y 3D */
    div[data-testid="stExpander"] {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(5, 11, 24, 0.95)) !important;
        border: 2px solid rgba(0, 229, 255, 0.7) !important;
        border-radius: 14px !important;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.25) !important;
        transition: all 0.3s ease-in-out;
    }
    
    div[data-testid="stExpander"]:hover {
        border-color: #00E5FF !important;
        box-shadow: 0px 0px 25px rgba(0, 229, 255, 0.6) !important;
        transform: translateY(-2px);
    }

    /* Estilizar el texto del summary/expander para que resalte en cian brillante */
    div[data-testid="stExpander"] summary p {
        color: #00E5FF !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        letter-spacing: 0.5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ====================================
# 2. ENCABEZADO PRINCIPAL DE LA VISTA 
# ====================================
st.markdown(
    """
    <div class="header-panel">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
            <div style="background: rgba(0, 229, 255, 0.15); border: 1px solid #00E5FF; border-radius: 10px; padding: 10px 14px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 1.5rem;">📊</span>
            </div>
            <div>
                <h2 style="color: #00E5FF; margin: 0; font-weight: 800; font-size: 1.6rem; letter-spacing: 0.5px;">
                    Horizon Dataset | Análisis Estructural y Lingüístico
                </h2>
                <p style="color: rgba(255, 255, 255, 0.6); margin: 0; font-size: 0.85rem;">
                    Ecosistema de Evaluación de Prompt Injection y Diversidad Lingüística
                </p>
            </div>
        </div>
        <hr style="border-color: rgba(0, 229, 255, 0.2); margin: 12px 0;">
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px;">
            <em>Esta fuente contiene un conjunto de datos destinado a evaluar la capacidad de los sistemas de inteligencia artificial para detectar ataques de inyección de instrucciones (prompt injection). Incluye ejemplos de mensajes maliciosos, intentos de evadir las restricciones de seguridad y textos legítimos que podrían confundirse con un ataque.</em>
        </p>
        <p style="color: rgba(255, 255, 255, 0.75); font-size: 0.9rem; line-height: 1.6; margin-bottom: 0;">
            <em>Los registros están clasificados mediante etiquetas que permiten comparar las respuestas de un detector con la clasificación esperada. De esta manera, el conjunto de datos ayuda a evaluar la precisión de los sistemas de detección y a identificar errores, como aceptar instrucciones maliciosas o marcar incorrectamente mensajes legítimos.</em>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 3. CARGA DE DATOS MEDIANTE EL LOADER
# ==========================================
df_corpus, df_matriz, df_lang = cargar_datos_horizon()

if not df_corpus.empty:
  # -------------------------------------------
  # SECCIÓN 1: MÉTRICAS Y GRÁFICOS SUPERIORES
  # -------------------------------------------
  col1, col2 = st.columns(2)

  with col1:
    with st.container(border=True):
      st.subheader("🌐 Distribución por Tipo de Ataque (Kind)")
      kind_counts = df_corpus["kind"].value_counts().reset_index()
      kind_counts.columns = ["kind", "count"]

      fig_kind = px.bar(
          kind_counts,
          x="kind",
          y="count",
          color="kind",
          color_discrete_sequence=["#00E5FF", "#FF6D00"],
          labels={
              "kind": "Tipo de Vector",
              "count": "Cantidad de Registros",
          },
      )
      fig_kind = style_plotly_chart(fig_kind)
      st.plotly_chart(fig_kind, use_container_width=True)
      st.caption(
          "_Proporción entre vectores de ataque directos (instrucciones maliciosas "
          "introducidas explícitamente por el usuario para burlar las restricciones) e "
          "indirectos (instrucciones ocultas o inyectadas a través de fuentes externas, "
          "como páginas web o documentos procesados por el modelo)._"
      )

  with col2:
    with st.container(border=True):
      st.subheader("🗣️ Top Idiomas en el Corpus")
      lang_counts = df_corpus["lang"].value_counts().reset_index().head(10)
      lang_counts.columns = ["lang", "count"]

      fig_lang = px.bar(
          lang_counts,
          x="lang",
          y="count",
          color="lang",
          color_discrete_sequence=px.colors.qualitative.Prism,
          labels={"lang": "Idioma (lang)", "count": "Registros"},
      )
      fig_lang = style_plotly_chart(fig_lang)
      st.plotly_chart(fig_lang, use_container_width=True)
      st.caption(
          "_Principales lenguajes evaluados y su representación dentro del"
          " dataset Horizon._"
      )

  st.markdown("---")

  # -------------------------------------------------------------
  # SECCIÓN 2: MATRIZ CONSOLIDADA DE FRECUENCIAS Y EXPLORADOR SANKEY
  # -------------------------------------------------------------
  with st.container(border=True):
    st.subheader("📋 Matriz Consolidada de Frecuencias y Porcentajes")
    st.markdown(
        "_Cruce global avanzado entre la diversidad lingüística, la tipología"
        " de inyección y la participación porcentual ponderada._"
    )

    if not df_matriz.empty:
      st.dataframe(df_matriz, use_container_width=True)
    else:
      st.info("⚠️ No se encontró la matriz consolidada procesada.")

    st.write("")
    # Módulo interactivo con el Diagrama de Sankey integrado y paleta de neones flúor
    with st.expander("Exploración avanzada diagrama de Sankey", expanded=False):
      st.markdown(
          "_Análisis jerárquico de flujos de 3 niveles: volumen total del"
          " corpus, filtrado personalizado por idioma (con agrupación en"
          " 'OTROS' en verde flúor) y bifurcación final en conteos"
          " absolutos por tipo de ataque._"
      )

      if df_matriz.empty:
        st.warning("⚠️ No hay datos disponibles en la matriz consolidada para armar el Sankey.")
      else:
        # Preparamos la matriz consolidada asegurando que el idioma esté en mayúsculas
        df_sankey_matriz = df_matriz.copy()
        df_sankey_matriz["lang"] = df_sankey_matriz["lang"].astype(str).str.upper()

        # Extraemos los idiomas disponibles (excluyendo la fila de totales generales si la hubiera como 'TOTAL GENERAL')
        all_items = sorted([x for x in df_sankey_matriz["lang"].dropna().unique().tolist() if x not in ["TOTAL GENERAL", "TOTAL"]])
        
        # Selección por defecto de los 4 principales basados en Total General
        default_selection = [x for x in df_sankey_matriz.sort_values(by="Total General", ascending=False)["lang"].head(4).tolist() if x in all_items]

        selected_items = st.multiselect(
            "Seleccionar Idiomas para el Flujo Estructural:",
            options=all_items,
            default=default_selection,
            key="sankey_custom_filter",
        )

        if not selected_items:
          st.warning(
              "⚠️ Por favor, seleccione al menos un elemento para visualizar el"
              " diagrama."
          )
        else:
          # Filtramos los seleccionados y agrupamos el resto en "OTROS" usando df_matriz
          mask_selected = df_sankey_matriz["lang"].isin(selected_items)
          df_sel = df_sankey_matriz[mask_selected]
          
          df_otros_rows = df_sankey_matriz[~mask_selected & ~df_sankey_matriz["lang"].isin(["TOTAL GENERAL", "TOTAL"])]
          
          if not df_otros_rows.empty:
            df_otros = pd.DataFrame({
                "lang": ["OTROS"],
                "direct": [df_otros_rows["direct"].sum()],
                "indirect": [df_otros_rows["indirect"].sum()],
                "Total General": [df_otros_rows["Total General"].sum()]
            })
            df_plot_matriz = pd.concat([df_sel, df_otros], ignore_index=True)
          else:
            df_plot_matriz = df_sel

          total_corpus_count = int(df_sankey_matriz[df_sankey_matriz["lang"].isin(["TOTAL GENERAL", "TOTAL"])]["Total General"].values[0]) if any(df_sankey_matriz["lang"].isin(["TOTAL GENERAL", "TOTAL"])) else int(df_plot_matriz["Total General"].sum())
          
          total_label = f"TOTAL CORPUS<br>{total_corpus_count:,} Reg. (100.0%)"

          nodes = [total_label]
          node_dict = {total_label: 0}
          sources = []
          targets = []
          values = []
          link_colors = []
          node_colors = ["#00E5FF"]

          neon_palette = [
              "#00E5FF",
              "#FF007F",
              "#FFEA00",
              "#00E676",
              "#AB47BC",
              "#FF7043",
          ]
          color_idx = 0
          group_color_map = {}

          # Nivel 2: Grupos / Idiomas / OTROS
          for _, row in df_plot_matriz.iterrows():
            g = row["lang"]
            cnt = int(row["Total General"])
            pct = (cnt / total_corpus_count) * 100 if total_corpus_count > 0 else 0
            g_label = f"{g}<br>{cnt:,} Reg. ({pct:.1f}%)"
            
            node_dict[g_label] = len(nodes)
            nodes.append(g_label)

            if g == "OTROS":
              g_color = "#00E676"
            else:
              g_color = neon_palette[color_idx % len(neon_palette)]
              color_idx += 1
            group_color_map[g] = g_color
            node_colors.append(g_color)

            # Enlace Raíz -> Grupo
            sources.append(node_dict[total_label])
            targets.append(node_dict[g_label])
            values.append(cnt)
            
            hex_c = g_color.lstrip("#")
            r, g_val, b = int(hex_c[0:2], 16), int(hex_c[2:4], 16), int(hex_c[4:6], 16)
            link_colors.append(f"rgba({r}, {g_val}, {b}, 0.38)")

          # Nivel 3: Bifurcación limpia en Directo e Indirecto por cada grupo
          for _, row in df_plot_matriz.iterrows():
            g = row["lang"]
            val_dir = int(row["direct"])
            val_indir = int(row["indirect"])
            
            g_label = [k for k, v in node_dict.items() if k.startswith(f"{g}<br>")][0]
            g_idx = node_dict[g_label]
            g_color = group_color_map[g]

            hex_c = g_color.lstrip("#")
            r, g_val, b = int(hex_c[0:2], 16), int(hex_c[2:4], 16), int(hex_c[4:6], 16)

            # Bifurcación Directo
            if val_dir > 0:
              pct_dir = (val_dir / total_corpus_count) * 100 if total_corpus_count > 0 else 0
              k_display_dir = f"DIRECTO ({g})<br>{val_dir:,} Reg. ({pct_dir:.1f}%)"
              if k_display_dir not in node_dict:
                node_dict[k_display_dir] = len(nodes)
                nodes.append(k_display_dir)
                node_colors.append("#00E5FF")

              sources.append(g_idx)
              targets.append(node_dict[k_display_dir])
              values.append(val_dir)
              link_colors.append(f"rgba({r}, {g_val}, {b}, 0.32)")

            # Bifurcación Indirecto
            if val_indir > 0:
              pct_indir = (val_indir / total_corpus_count) * 100 if total_corpus_count > 0 else 0
              k_display_indir = f"INDIRECTO ({g})<br>{val_indir:,} Reg. ({pct_indir:.1f}%)"
              if k_display_indir not in node_dict:
                node_dict[k_display_indir] = len(nodes)
                nodes.append(k_display_indir)
                node_colors.append("#FF6D00")

              sources.append(g_idx)
              targets.append(node_dict[k_display_indir])
              values.append(val_indir)
              link_colors.append(f"rgba({r}, {g_val}, {b}, 0.32)")

          fig_sankey = go.Figure(
              go.Sankey(
                  node=dict(
                      pad=18,
                      thickness=24,
                      line=dict(color="rgba(255, 255, 255, 0.95)", width=1.5),
                      label=nodes,
                      color=node_colors,
                  ),
                  link=dict(
                      source=sources,
                      target=targets,
                      value=values,
                      color=link_colors,
                  ),
              )
          )

          fig_sankey.update_layout(
              font=dict(size=12, color="white"),
              paper_bgcolor="rgba(0,0,0,0)",
              plot_bgcolor="rgba(0,0,0,0)",
              height=600,
              margin=dict(l=20, r=20, t=30, b=20),
          )
          fig_sankey = style_plotly_chart(fig_sankey)
          st.plotly_chart(fig_sankey, use_container_width=True)
          st.caption(
              "_Estructura de flujo de 3 niveles con paleta neón flúor,"
              " herencia de color por categoría y conteos absolutos basados en la Matriz Consolidada._"
          )

  st.markdown("---")

  # -------------------------------------------------------------
  # SECCIÓN 3: TABLA MAESTRA DEL CORPUS CON PAGINACIÓN REAL
  # -------------------------------------------------------------
  with st.container(border=True):
    st.subheader("🗂️ Corpus Maestro Unificado (Registros Completos)")
    st.markdown(
        "_Exploración tabular interactiva del corpus completo con paginación"
        " optimizada (25 registros por página)._"
    )

    rows_per_page = 25
    total_rows = len(df_corpus)
    total_pages = max(1, math.ceil(total_rows / rows_per_page))

    col_inf, col_p = st.columns([3, 1])
    with col_inf:
      page_number = st.number_input(
          "Seleccionar Página",
          min_value=1,
          max_value=total_pages,
          value=1,
          step=1,
          key="pag_horizon_corpus",
      )
    with col_p:
      st.markdown(f"**Total Páginas:** {total_pages}")
      st.markdown(f"**Registros Totales:** {total_rows}")

    start_idx = (page_number - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    df_page = df_corpus.iloc[start_idx:end_idx]

    st.dataframe(df_page, use_container_width=True, hide_index=True)
    st.caption(
        f"Mostrando del registro {start_idx + 1} al"
        f" {min(end_idx, total_rows)} de un total de {total_rows}."
    )

else:
  st.warning(
      "⚠️ No se pudo cargar el corpus maestro de Horizon desde la carpeta de"
      " datos procesados."
  )

# ==========================================
# 4. PIE DE PÁGINA (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: rgba(255, 255, 255, 0.6);"
    " font-size: 0.85em;'>Fuente: Horizon-Labs — Prompt Injection Eval Suite,"
    " publicada en Hugging Face.</div>",
    unsafe_allow_html=True,
)