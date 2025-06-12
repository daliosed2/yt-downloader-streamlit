import streamlit as st
import yt_dlp
import os
import uuid

# Configuración inicial
st.set_page_config(page_title="Descarga YouTube/TikTok/X", page_icon="🎬")
st.title("🎬 Descarga tu video o audio")
st.markdown("Pega el enlace de YouTube, TikTok o X y elige qué deseas descargar:")

# Entrada de usuario
url = st.text_input("🔗 Enlace del video", placeholder="https://www.youtube.com/watch?v=...")
st.warning("⚠️ Por ahora solo está disponible la descarga de video completo (MP4) por compatibilidad.")

if st.button("Descargar"):
    if not url:
        st.error("❌ Por favor, ingresa un enlace válido.")
    else:
        try:
            # Carpeta temporal
            carpeta_salida = "descargas"
            os.makedirs(carpeta_salida, exist_ok=True)

            # Nombre aleatorio para evitar conflictos
            nombre_archivo = str(uuid.uuid4())

            # Configuración para video MP4
            opciones = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{carpeta_salida}/{nombre_archivo}.%(ext)s',
                'merge_output_format': 'mp4'
            }

            # Descargar video
            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])

            # Buscar archivo descargado
            ruta_archivo = f"{carpeta_salida}/{nombre_archivo}.mp4"
            with open(ruta_archivo, "rb") as f:
                st.success("✅ Video descargado con éxito.")
                st.download_button(
                    label="⬇️ Descargar video (MP4)",
                    data=f,
                    file_name="video_descargado.mp4",
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Ocurrió un error: {e}")
