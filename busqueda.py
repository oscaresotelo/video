
import streamlit as st
from pytube import Search, YouTube
import re
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("BUSCAR VIDEOS")

busqueda = st.text_input("Ingresar Nombre Video")
buscar = Search(busqueda)
bt_buscar = st.button("Buscar")

if bt_buscar:
    st.write(len(buscar.results))
    results_text = str(buscar.results) # Convertir la lista de resultados a texto
    matches = re.findall(r'=(.*?)>', results_text) # Buscar texto entre "=" y ">"
    for match in matches:
        video_link = "https://www.youtube.com/watch?v=" + match.strip() # Agregar cadena al texto extraído
        st.video(video_link) # Mostrar el enlace del video
        video = YouTube(video_link)
        video_title = video.title # Obtener el título del video
        st.info("Título: " + video_title) # Mostrar el título del video
        video_stream = video.streams.get_by_itag(22) # Obtener la corriente de video con calidad MP4 y resolución 720p
        video_duration = video.length # Obtener duración del video en segundos
        video_duration = video_duration / 60
        st.info("Duración:  " + str(video_duration) + "  minutos") # Mostrar la duración del video
        if video_stream:
            file_name = video.title + ".mp4"

            # Generar el enlace de descarga con JavaScript para descargar automáticamente
            download_link = f'<a href="{video_stream.url}" download="{file_name}" onclick="setTimeout(function() {{ window.location.href = \'{video_stream.url}\'; }}, 100);">Descargar video en formato MP4</a>'
            # Mostrar el enlace de descarga como HTML con el JavaScript inyectado
            st.write(download_link, unsafe_allow_html=True)
