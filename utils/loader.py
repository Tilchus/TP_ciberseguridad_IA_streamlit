from pathlib import Path
import pandas as pd
import streamlit as st
# Directorio raíz del proyecto paralelo apuntando a datos/procesados/
BASE_DIR = Path(__file__).resolve().parent.parent
DIR_PROCESADOS = BASE_DIR / "datos" / "procesados"

def cargar_datos_benchmark():
  dir_b = DIR_PROCESADOS / "injection-benchmark"

  try:
    df_label = pd.read_parquet(dir_b / "distribucion_label.parquet")
  except Exception as e:
    st.error(f"[DEBUG Benchmark] Error en distribucion_label: {e}")
    df_label = pd.DataFrame()

  try:
    df_category = pd.read_parquet(dir_b / "distribucion_category.parquet")
  except Exception as e:
    st.error(f"[DEBUG Benchmark] Error en distribucion_category: {e}")
    df_category = pd.DataFrame()

  try:
    df_severity = pd.read_parquet(dir_b / "distribucion_severity.parquet")
  except Exception as e:
    st.error(f"[DEBUG Benchmark] Error en distribucion_severity: {e}")
    df_severity = pd.DataFrame()

  try:
    df_cat_sev = pd.read_parquet(
        dir_b / "distribucion_categoria_severidad.parquet"
    )
  except Exception as e:
    st.error(f"[DEBUG Benchmark] Error en distribucion_categoria_severidad: {e}")
    df_cat_sev = pd.DataFrame()

  return df_label, df_category, df_severity, df_cat_sev


def cargar_datos_neuralchemy():
  dir_n = DIR_PROCESADOS / "neurAlchemy"

  # 1. Resumen de Severidad
  try:
    df_sev = pd.read_parquet(dir_n / "resumen_severidad.parquet")
  except Exception as e:
    st.error(f"[DEBUG NeurAlchemy] Error en resumen_severidad: {e}")
    df_sev = pd.DataFrame()

  # 2. Top Categorías de Ataque
  try:
    df_cat = pd.read_parquet(dir_n / "top_categorias_ataque.parquet")
  except Exception as e:
    st.error(f"[DEBUG NeurAlchemy] Error en top_categorias_ataque: {e}")
    df_cat = pd.DataFrame()

  # 3. Tabla de Cruce Categoría vs Severidad
  try:
    cruce_files = list(dir_n.glob("*cruce*.parquet"))
    df_cruce = pd.read_parquet(cruce_files[0]) if cruce_files else pd.DataFrame()
  except Exception as e:
    st.error(f"[DEBUG NeurAlchemy] Error en cruce: {e}")
    df_cruce = pd.DataFrame()

  # 4. Dataset Procesado Completo
  try:
    df_proc = pd.read_parquet(dir_n / "neurAlchemy_procesado.parquet")
  except Exception as e:
    st.error(f"[DEBUG NeurAlchemy] Error en procesado: {e}")
    df_proc = pd.DataFrame()

  return df_sev, df_cat, df_cruce, df_proc


def cargar_datos_horizon():
  dir_h = DIR_PROCESADOS / "Horizon"

  # 1. Corpus Maestro Unificado
  try:
    df_corpus = pd.read_parquet(dir_h / "horizon_corpus_maestro.parquet")
  except Exception as e:
    st.error(f"[DEBUG Horizon] Error en corpus maestro ({dir_h}): {e}")
    df_corpus = pd.DataFrame()

  # 2. Matriz Consolidada de Frecuencias
  try:
    df_matriz = pd.read_parquet(
        dir_h / "horizon_matriz_consolidada_total.parquet"
    )
  except Exception as e:
    st.error(f"[DEBUG Horizon] Error en matriz consolidada: {e}")
    df_matriz = pd.DataFrame()

  # 3. Resumen de Idiomas (Df 1)
  try:
    df_lang = pd.read_parquet(dir_h / "horizon_resumen_lang_df1.parquet")
  except Exception as e:
    st.error(f"[DEBUG Horizon] Error en resumen lang: {e}")
    df_lang = pd.DataFrame()

  return df_corpus, df_matriz, df_lang