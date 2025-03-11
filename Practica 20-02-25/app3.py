import streamlit as st
import ollama

#configurar la interfaz de streamlit
st.title("Chat con DeepSeek-R1 en Streamlit")

#Cuadro de texto para entrada del usuario
user_input = st.text_area("Escribe tu consulta...", "")

if st.button("Enviar"):
    if user_input.strip():
        with st.empty():
            full_response = ""
            for chunk in ollama.chat(model="deepseek-r1:1.5b", messages=[{"role":"user", "content": user_input}], stream=True):
                if "message" in chunk:
                    full_response += chunk["message"]["content"]
                    st.write(full_response) #mostrar en streaming
    else:
        st.warning("Por favor, ingresa una consulta antes de enviar.")