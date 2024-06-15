from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama  # Import Ollama class directly
import streamlit as st

# Title and input field
st.title('Langchain Demo with Ollama')
input_text = st.text_input("Search the topic you want")

# Create Ollama instance
llm = Ollama(model="llama2:latest")  # Access Ollama class and instantiate

# Define prompt and output parser
prompt = ChatPromptTemplate.from_messages(
    [
        ("system,you are a helpful assistant. Please respond to the user."),
        ("user", "question:{question}")
    ]
)
output_parser = StrOutputParser()

# Build the chain
chain = prompt | llm | output_parser

# Run the chain if there's input
if input_text:
    st.write(chain.invoke({"question": input_text}))
