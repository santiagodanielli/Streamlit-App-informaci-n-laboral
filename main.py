"""
Hacer comentarios aquí
"""

import streamlit as st
from PIL import Image

# Crear aplicación
st.set_page_config(page_title="Santiago Danielli",
                   layout="centered")

# Variables de Texto

descripcion_personal = """
Soy analista de datos con orientación en investigación social, de mercados, opinión pública y segmentación demográfica. 
Me dedico a combinar mi formación y experiencia en estadística descriptiva e inferencial con herramientas como Power BI y Python para 
analizar datos que aporten a la toma de decisiones.
"""

concepto_ad = """
El análisis de datos es un proceso integral que implica examinar, limpiar y modelar datos con el objetivo de 
descubrir patrones, tendencias y obtener información significativa. Este enfoque se utiliza en diversas 
disciplinas, desde la investigación científica hasta la toma de decisiones empresariales. En primer lugar, 
implica la recopilación y organización de datos brutos provenientes de diversas fuentes, como encuestas, 
sensores o bases de datos. Posteriormente, se aplican técnicas estadísticas y algoritmos de aprendizaje 
automático para identificar relaciones, correlaciones y generar insights valiosos. El análisis de datos 
se ha convertido en una herramienta esencial para la toma de decisiones informadas, ya que proporciona una 
comprensión profunda de los fenómenos estudiados y facilita la anticipación de tendencias futuras.
"""

# Variables de imagenes

image1 = Image.open("image1.png")

# Encabezado y primera parte
st.write("Santiago Danielli")
colum1, colum2 = st.columns(2)
with colum1:
    st.header("Analista de datos - Transformando datos en conocimiento")
    st.markdown(descripcion_personal)
with colum2:
    st.image(image1)

st.markdown("------")

# Experiencia
st.subheader('EXPERIENCIA LABORAL')
st.write('*Abril 2023 - Actualidad*')
st.write('Analista de datos en Latam Research')
st.write("")
st.write('*Octubre 2019 - Marzo 2023*')
st.write('Asistente en equipo de datos y luego Analista de datos en CNPT-AR')
st.write("")

st.markdown("------")

# Segunda parte
st.header("Análisis de datos: parte fundamental de cualquier organización")
st.markdown(concepto_ad)


st.markdown("------")


columna1, columna2 = st.columns(2)
with columna1:
    st.subheader("Podes encontrarme en:")
    st.link_button(":briefcase: Perfil de Linkedin", "https://www.linkedin.com/in/santiago-danielli-3a6859b2/")
    st.link_button(":computer: Github", "https://github.com/santiagodanielli")

st.markdown("------")

# Formulario para mails
formulario_contacto = """
<form action="https://formsubmit.co/santiagodanielli0@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu correo electrónico" required>
     <textarea name="message" placeholder="Escribe tu mensaje a continuación"></textarea>
     <button type="submit">Enviar</button>
</form>
"""
st.subheader("También podes enviarme un correo electrónico:")
st.markdown(formulario_contacto, unsafe_allow_html=True)

# Usar css file
def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")



