
# import streamlit as st
# from pytube import YouTube

# # Configurar título y descripción de la aplicación
# st.title("Descargador de videos de YouTube")
# st.write("Ingrese el enlace del video de YouTube:")

# # Crear un campo de entrada de texto para el enlace de YouTube
# video_url = st.text_input("Enlace del video")

# # Verificar si se ha ingresado un enlace válido
# if video_url:
#     try:
#         # Crear una instancia de objeto YouTube
#         yt = YouTube(video_url)

#         # Mostrar detalles del video
#         st.write("Título:", yt.title)
#         st.write("Duración:", yt.length, "segundos")
#         st.video(video_url)
#         # Obtener las resoluciones disponibles
#         available_resolutions = [stream.resolution for stream in yt.streams.filter(file_extension="mp4")]

#         # Crear un campo de selección para la calidad del video
#         selected_resolution = st.selectbox("Seleccionar calidad:", available_resolutions)

#         # Obtener el objeto Stream correspondiente a la calidad seleccionada
#         stream = None
#         for s in yt.streams.filter(file_extension="mp4"):
#             if s.resolution == selected_resolution:
#                 stream = s
#                 break

#         # Verificar si se encontró el objeto Stream
#         if stream is not None:

#             # Agregar un botón para iniciar la descarga
#             if st.button("Descargar"):
#                 st.write("Descargando...")
#                 stream.download()
#                 st.write("Descarga completada!")
#         else:
#             st.write("La calidad seleccionada no está disponible para este video.")

#     except Exception as e:
#         st.write("Ocurrió un error:", str(e))
import streamlit as st
from pytube import YouTube

# Inyectar CSS personalizado
st.markdown(
    """
    <style>
    .title {
        color: #336699;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    .subtitle {
        font-size: 24px;
        margin-bottom: 10px;
    }

    .details {
        margin-top: 20px;
    }

    .video {
        margin-top: 20px;
    }

    .selectbox {
        width: 300px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .button {
        background-color: #336699 !important;
        color: #ffffff !important;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
    }

    .button:hover {
        background-color: #214466 !important;
    }

    .success-message {
        color: #009933;
        font-weight: bold;
        margin-top: 20px;
    }

    .warning-message {
        color: #ff9900;
        font-weight: bold;
        margin-top: 20px;
    }

    .error-message {
        color: #ff0000;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Configurar título y descripción de la aplicación
st.markdown('<h1 class="title">Descargador de videos de YouTube</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">¡Bienvenido! Con esta aplicación puedes descargar videos de YouTube. Simplemente ingresa el enlace del video y selecciona la calidad de descarga.</p>', unsafe_allow_html=True)

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

            # Agregar un botón para iniciar la descarga
            if st.button("Descargar", key='download', help='Haga clic para iniciar la descarga'):
                st.markdown('<p class="success-message">Descargando...</p>', unsafe_allow_html=True)
                stream.download()
                st.markdown('<p class="success-message">¡Descarga completada!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="warning-message">La calidad seleccionada no está disponible para este video.</p>', unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f'<p class="error-message">Ocurrió un error: {str(e)}</p>', unsafe_allow_html=True)
