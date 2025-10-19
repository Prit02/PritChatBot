
import streamlit
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

st.title("💬 I AM PRIT. Throw me questions!")
st.set_page_config(
    page_title="Pritesh's Chatbot",
    page_icon="💬 ",
    initial_sidebar_state="collapsed",
    layout="wide"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

userMessage = st.chat_input("Enter you message")

llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.0
    )
Template = (
    "Your name is Prit a 'CHATBOT' of guy named Pritesh. Introduce yourself first and then be an lovable chatbot"
    "You're 28 years old and have an emmense knowledge in Computer Science. You have done BE in CSE"
    "You're working in a Software Company and have no competitions"
    "ANSWERING RULES:"
    "Do not entertain any more personal questions other than the Given ones, you can say You will fall in Love with me if I tell anything else"
    "Only Speak in 1 sentences"
    "ONLY SPEAK IN HINDI")

if userMessage:
    st.chat_message("user").markdown(userMessage)
    st.session_state.chat_history.append({"role":"user","content":userMessage})

    response = llm.invoke(
        input = [{"role":"system","content":Template},*st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

# Flow:
# Write Query
# Display Query
# Insert Query in ChatHistory
# Give ChatHistory to LLM
# Get response
# Save response in ChatHistory
# Print Response


