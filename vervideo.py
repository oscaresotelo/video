

import streamlit as st
from pytube import YouTube
import requests
from st_pages import Page, show_pages, add_page_title
# Inyectar CSS personalizado
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Configurar título y descripción de la aplicación
st.markdown('<h1 class="title">Descargador de videos de YouTube</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">¡Bienvenido! Con esta aplicación puedes descargar videos de YouTube. Simplemente ingresa el enlace del video y selecciona la calidad de descarga.</p>', unsafe_allow_html=True)
show_pages([
        Page("vervideo.py", "Inicio"),
        Page("busqueda.py", "Buscar", ":notebook:"),
    ])
# Crear un campo de entrada de texto para el enlace de YouTube
video_url = st.text_input("Enlace del video")

# Verificar si se ha ingresado un enlace válido
if video_url:
    try:
        # Crear una instancia de objeto YouTube
        yt = YouTube(video_url)

        # Mostrar detalles del video
        st.markdown('<h2 class="subtitle">Detalles del video:</h2>', unsafe_allow_html=True)
        st.markdown(f'<p class="details">Título: {yt.title}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="details">Duración: {yt.length} segundos</p>', unsafe_allow_html=True)
        st.video(video_url, format='video/mp4')

        # Obtener las resoluciones disponibles
        available_resolutions = [stream.resolution for stream in yt.streams.filter(file_extension="mp4")]

        # Crear un campo de selección para la calidad del video
        selected_resolution = st.selectbox("Seleccionar calidad:", available_resolutions, key='quality', help='Seleccione la calidad de descarga')

        # Obtener el objeto Stream correspondiente a la calidad seleccionada
        stream = None
        for s in yt.streams.filter(file_extension="mp4"):
            if s.resolution == selected_resolution:
                stream = s
                break

        # Verificar si se encontró el objeto Stream
        if stream is not None:

            # Agregar un botón para generar el enlace de descarga
            if st.button("Generar enlace de descarga", key='download', help='Haga clic para generar el enlace de descarga'):
                st.markdown('<p class="success-message">Generando enlace de descarga...</p>', unsafe_allow_html=True)
                response = requests.head(stream.url)
                content_type = response.headers.get('content-type')
                if 'video' in content_type:
                    content_extension = content_type.split('/')[1]
                    file_name = f'{yt.title}.{content_extension}'
                    st.markdown(f'<p class="success-message">Enlace de descarga: <a href="{stream.url}" download="{file_name}">Descargar</a></p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p class="warning-message">No se puede generar el enlace de descarga.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="warning-message">La calidad seleccionada no está disponible para este video.</p>', unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f'<p class="error-message">Ocurrió un error: {str(e)}</p>', unsafe_allow_html=True)
