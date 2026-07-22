# Análisis y minería de datos

Repositorio con notebooks y scripts para aprender análisis de datos desde cero utilizando **Python** y **Jupyter / Google Colab**.

Este repositorio está pensado con un enfoque **didáctico**: el objetivo principal es aprender análisis de datos, no herramientas avanzadas de gestión de paquetes.  
Por ello, se proponen **dos formas de uso**, según el perfil del usuario.

---

## Requisitos

- **Python >= 3.12**
- Jupyter Notebook o JupyterLab

> Google Colab utiliza actualmente Python 3.12.x, por lo que este repositorio es totalmente compatible.

---

## Estructura del repositorio

- `data/`: archivos CSV, Excel, etc.
- `notebooks/`: Notebooks principales del curso
- `practicas/`: ejercicios por tema
- `recursos/`: material complementario
- `utils/`: funciones auxiliares en Python
- `setup_colab.ipynb`: preparación del entorno en Colab
- `README.md`: este archivo
- `pyproject.toml`: configuración moderna del proyecto (uso del profesor / mantenimiento)
- `requirements.txt`: lista de paquetes **legacy** (uso recomendado para alumnos)

---

## Opción A — Instalación recomendada para alumnos (pip)

Esta es la **forma más sencilla y recomendada** para estudiantes, ya que utiliza herramientas estándar de Python que podrán reutilizar en futuros proyectos.

### 1. Crear un entorno virtual

```bash
python -m venv venv
```

Activar el entorno:

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Iniciar Jupyter

```bash
jupyter lab
```

O bien:

```bash
jupyter notebook
```

---

## Uso en Google Colab

En un notebook de Colab ejecuta:

```python
!pip install -r requirements.txt
```

Luego reinicia el runtime si Colab lo solicita.

---

## Opción B — Uso avanzado / mantenimiento del proyecto (uv)

Esta opción está pensada para el **profesor o mantenedor del repositorio**, no es necesaria para los alumnos.

Se utiliza [uv](https://github.com/astral-sh/uv), un gestor moderno de dependencias para Python.

### 1. Instalar `uv`

```bash
# macOS y Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 2. Crear entorno virtual y sincronizar dependencias

```bash
uv venv
source .venv/bin/activate
uv sync --group dev --no-install-project
```

> En este repositorio **no se instala el proyecto como paquete**, `uv` se usa únicamente para gestionar dependencias.

---

## Notas pedagógicas importantes

- El uso de `pip install -r requirements.txt` **no es una mala práctica**: es el estándar más común en cursos, tutoriales y muchos entornos profesionales.
- Herramientas como `uv`, `poetry` o `pip-tools` existen y son útiles, pero se consideran **un nivel posterior**.
- El enfoque del curso prioriza el aprendizaje de **análisis de datos**, no la complejidad del tooling.

---

## Autor

Desarrollado por **Adán Reyes S.** para fines educativos  
© 2025. Todos los derechos reservados.
