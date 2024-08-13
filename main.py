import os
import streamlit as st
import google.generativeai as gen_ai
from api import *

st.set_page_config(page_title="Chat with Gemini-Pro!",page_icon=":brain:",  layout="centered", )

gen_ai.configure(api_key=API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')
594812
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "ai"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 Welcome Back Bilal!")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    
    except gen_ai.generation_types.StopCandidateException as e:
        st.error("An error occurred while processing your request.")
        st.error(f"Reason: {e.finish_reason}")

