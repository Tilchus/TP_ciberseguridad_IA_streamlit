import base64
from pathlib import Path
import streamlit as st


def apply_global_theme():
  img_path = Path("imagenes/fondo.png")

  if img_path.exists():
    with open(img_path, "rb") as f:
      encoded = base64.b64encode(f.read()).decode()

    bg_style = f"""
            <style>
            /* 1. Fondo principal de la app */
            .stApp {{
                background-image: linear-gradient(rgba(5, 11, 24, 0.65), rgba(5, 11, 24, 0.65)), url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            
            /* 2. Ocultar el panel/encabezado blanco superior de Streamlit */
            [data-testid="stHeader"] {{
                background-color: rgba(0, 0, 0, 0) !important;
            }}
            
            /* 3. Panel lateral (Sidebar) en tono azul oscuro con borde celeste */
            [data-testid="stSidebar"] {{
                background-color: rgba(5, 11, 24, 0.95) !important;
                border-right: 1px solid rgba(0, 229, 255, 0.3) !important;
            }}
            
            /* 4. Tipografía blanca para todo el documento */
            h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown, div[data-testid="stCaptionContainer"] {{
                color: #FFFFFF !important;
            }}
            
            /* 5. Contenedores de tarjetas con fondo azul cibernético translúcido */
            div[data-testid="stVerticalBlock"] > div[data-testid="stContainer"] {{
                background-color: rgba(10, 25, 47, 0.85) !important;
                border: 1px solid rgba(0, 229, 255, 0.4) !important;
                border-radius: 12px;
                padding: 15px;
            }}
            
            /* 6. Botones estilizados */
            div[data-testid="stButton"] > button {{
                background-color: rgba(10, 25, 47, 0.9) !important;
                color: #FFFFFF !important;
                border: 1px solid #00E5FF !important;
                border-radius: 8px;
                transition: all 0.3s ease;
            }}
            
            div[data-testid="stButton"] > button:hover {{
                background-color: rgba(0, 229, 255, 0.25) !important;
                border-color: #00E5FF !important;
                box-shadow: 0px 0px 12px rgba(0, 229, 255, 0.6);
                color: #FFFFFF !important;
            }}
            </style>
            """
    st.markdown(bg_style, unsafe_allow_html=True)
  else:
    st.error(
        "⚠️ Error de UI: No se encontró la imagen en la ruta:"
        f" {img_path.resolve()}"
    )


# Paleta semántica estricta e intensa reutilizable
SEVERITY_COLOR_MAP = {
    "critical": "#FF1744",
    "Critical": "#FF1744",
    "high": "#FF6D00",
    "High": "#FF6D00",
    "medium": "#FFD600",
    "Medium": "#FFD600",
    "low": "#00E676",
    "Low": "#00E676",
}


def style_plotly_chart(fig):
  """Aplica tema transparente y letras blancas a los gráficos Plotly."""
  fig.update_layout(
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font=dict(color="#FFFFFF"),
      title_font=dict(color="#FFFFFF"),
      legend=dict(font=dict(color="#FFFFFF")),
      xaxis=dict(
          gridcolor="rgba(255,255,255,0.1)",
          title_font=dict(color="#FFFFFF"),
          tickfont=dict(color="#FFFFFF"),
      ),
      yaxis=dict(
          gridcolor="rgba(255,255,255,0.1)",
          title_font=dict(color="#FFFFFF"),
          tickfont=dict(color="#FFFFFF"),
      ),
  )
  return fig