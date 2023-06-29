
import streamlit as st
import fitz

st.title("Extracción de texto de archivos PDF")

# Subir archivo PDF
uploaded_file = st.file_uploader("Selecciona un archivo PDF", type="pdf")

if uploaded_file is not None:
    # Leer archivo PDF y extraer texto
    pdf_data = uploaded_file.read()
    doc = fitz.open(stream=pdf_data, filetype="pdf")

    all_text = ""
    previous_line = ""
    for page in doc:
        text = page.get_text()
        lines = text.split("\n")
        for line in lines:
            if line.strip() and line.strip() != "$" and not line.startswith("*") and "COD" not in line:
                if "$" in line.strip():
                    all_text += previous_line.strip() + line.strip() + "\n"
                    previous_line = ""
                else:
                    all_text += line.strip() + " "
                    previous_line = line.strip()

    # Mostrar texto extraído sin las líneas que contienen "COD" y las líneas que comienzan con "*"
    st.header("Texto extraído:")
    st.text_area("", all_text)
