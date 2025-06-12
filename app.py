import streamlit as st
import yt_dlp
import os
import uuid

# Configuración de la app
st.set_page_config(page_title="Descarga YouTube/TikTok/X", page_icon="🎬")
st.title("🎬 Descarga tu video o audio")
st.markdown("Pega el enlace de YouTube, TikTok o X y descarga el video en formato MP4:")

# Entrada
url = st.text_input("🔗 Enlace del video", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Descargar"):
    if not url:
        st.error("❌ Por favor, ingresa un enlace válido.")
    else:
        try:
            carpeta_salida = "descargas"
            os.makedirs(carpeta_salida, exist_ok=True)
            nombre_archivo = str(uuid.uuid4())

            opciones = {
                'format': 'mp4',
                'outtmpl': f'{carpeta_salida}/{nombre_archivo}.mp4'
            }

            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])

            ruta_archivo = f"{carpeta_salida}/{nombre_archivo}.mp4"
            with open(ruta_archivo, "rb") as f:
                st.success("✅ Descarga completada.")
                st.download_button(
                    label="⬇️ Descargar video (MP4)",
                    data=f,
                    file_name="video.mp4",
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Ocurrió un error: {e}")
