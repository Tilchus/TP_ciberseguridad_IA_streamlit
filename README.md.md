# 🛡️ EVALUACIÓN Y ANÁLISIS DE PROMPT INJECTION EN LLMs
### *Dashboard Interactivo de Ciberseguridad e Inteligencia Artificial*

---

## 📌 DESCRIPCIÓN DEL PROYECTO

Este proyecto consiste en una plataforma interactiva y analítica desarrollada en **Python** y **Streamlit** para la **evaluación, visualización y análisis cuantitativo de amenazas de Prompt Injection** (Inyección de Prompts) en Modelos de Lenguaje de Gran Escala (LLMs).

La herramienta consolida data sets en ciberseguridad para IA, ofreciendo una interfaz gráfica ágil que permite examinar tácticas adversarias, niveles de vulnerabilidad y métricas de seguridad para futura toma de desiciones

---

## 📊 Datasets Utilizados

El dashboard procesa e integra datos optimizados en formato `.parquet` provenientes de tres fuentes clave de ciberseguridad para IA:

1. **neuralchemy / Prompt-injection-dataset**
   * Dataset de Hugging Face especializado en clasificar ataques y comportamiento benigno.
   * Contiene categorías como `benign`, `direct_injection`, `indirect_injection`, `crescendo`, `jailbreak` y `encoding_obfuscation`.

2. **Horizon Prompt Injection Eval Suite**
   * Corpus exhaustivo enfocado en la evaluación e inyección de prompts en idioma español.

3. **Benchmark Dataset**
   * Dataset complementario de pruebas comparativas para el análisis cuantitativo de vulnerabilidades y desempeño de modelos.
---

## 📁 ESTRUCTURA DE LA ARQUITECTURA

```text
TP_ciberseguridad_IA_streamlit/
│
├── 📂 datos/                  # Datasets optimizados en formato binario (.parquet)
│   └── 📂 procesados/         # Subcarpetas organizadas por benchmark y fuente
│
├── 📂 views/                  # Módulos y pestañas de la interfaz de usuario
├── 📂 utils/                  # Funciones auxiliares para procesamiento y gráficos
├── 📂 Notebooks/              # Notebooks de Jupyter (.ipynb) de análisis exploratorio
│
├── 📄 app.py                  # Código ejecutable principal del Dashboard en Streamlit
├── 📄 .gitignore              # Filtro de exclusión de archivos temporales y entornos
└── 📄 README.md               # Documentación general del repositorio
```

---

## 💻 TECNOLOGÍAS UTILIZADAS

* **Lenguaje Principal:** `Python 3.10+`
* **Framework Web / Dashboard:** `Streamlit`
* **Procesamiento de Datos:** `Pandas`, `PyArrow`, `FastParquet`
* **Visualización Gráfica:** `Plotly Express`, `Plotly Graph Objects`
* **Control de Versiones:** `Git` & `GitHub`

---

## ⚙️ GUÍA DE INSTALACIÓN Y EJECUCIÓN

Seguí estos simples pasos en tu terminal para clonar, configurar y correr el proyecto en tu máquina local:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Tilchus/TP_ciberseguridad_IA_streamlit.git
cd TP_ciberseguridad_IA_streamlit
```

### 2️⃣ Crear y activar el entorno virtual (*Opcional pero recomendable*)
```bash
python -m venv .venv
```
* **En Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **En Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

### 3️⃣ Instalar todas las dependencias
Para instalar las librerías necesarias sin crear un archivo externo de requerimientos, ejecutá directamente este comando en la consola:

```bash
pip install streamlit pandas plotly pyarrow fastparquet
```

### 4️⃣ Iniciar la aplicación
Una vez instaladas las librerías, lanzá el dashboard ejecutando:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web predeterminado en la dirección `http://localhost:8501`.

---

## 👥 AUTORES Y CRÉDITOS

Proyecto desarrollado para la evaluación y estudio de la **Ciberseguridad aplicada a la Inteligencia Artificial Generativa**.

* **Repositorio oficial:** [GitHub - Tilchus/TP_ciberseguridad_IA_streamlit](https://github.com/Tilchus/TP_ciberseguridad_IA_streamlit)

---
