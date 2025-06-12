import streamlit as st
import yt_dlp
import os
import uuid

# Configurar la app
st.set_page_config(page_title="Descarga YouTube/TikTok/X", page_icon="🎬")
st.title("🎬 Descarga tu video o audio")
st.markdown("Pega el enlace de YouTube, TikTok o X y elige qué deseas descargar:")

# Entrada de usuario
url = st.text_input("🔗 Enlace del video", placeholder="https://www.youtube.com/watch?v=...")

opcion = st.radio("¿Qué deseas descargar?", ["🎧 Solo el audio (MP3)", "🎥 Video completo (MP4)"])

if st.button("Descargar"):
    if not url:
        st.warning("Por favor, pega un enlace válido.")
    else:
        try:
            # Crear carpeta temporal
            carpeta_salida = "descargas"
            os.makedirs(carpeta_salida, exist_ok=True)

            # Nombre aleatorio temporal
            nombre_archivo = str(uuid.uuid4())

            if opcion == "🎧 Solo el audio (MP3)":
                formato = {
                    'format': 'bestaudio/best',
                    'outtmpl': f'{carpeta_salida}/{nombre_archivo}.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                }
                extension = "mp3"
            else:
                formato = {
                    'format': 'bestvideo+bestaudio/best',
                    'outtmpl': f'{carpeta_salida}/{nombre_archivo}.%(ext)s',
                    'merge_output_format': 'mp4'
                }
                extension = "mp4"

            # Descargar
            with yt_dlp.YoutubeDL(formato) as ydl:
                info = ydl.download([url])

            # Buscar el archivo descargado
            archivo_generado = f"{carpeta_salida}/{nombre_archivo}.{extension}"
            with open(archivo_generado, "rb") as f:
                st.success("✅ ¡Descarga lista!")
                st.download_button(
                    label=f"⬇️ Descargar archivo ({extension})",
                    data=f,
                    file_name=f"descarga.{extension}",
                    mime=f"audio/mpeg" if extension == "mp3" else "video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Ocurrió un error: {e}")
