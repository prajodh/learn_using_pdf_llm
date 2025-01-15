import streamlit as st
import os
import uuid
from ingestion import ingest_data_and_create_vector_store, clean_resources
from model import run_model_and_RAG

# Initialize session state variables
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

if "file_saved" not in st.session_state:
    st.session_state.file_saved = False

if "button" not in st.session_state:
    st.session_state.button = False

if "button1" not in st.session_state:
    st.session_state.button1 = False

if "question" not in st.session_state:
    st.session_state.question = ""

# Function to handle file ingestion
def ingest_file(file_path):
    try:
        ingest_data_and_create_vector_store(file_path)
        st.write("File has been successfully ingested!")
        st.balloons()
    except Exception as e:
        st.error(f"An error occurred during ingestion: {e}")

# Title
st.title("Upload a File")

# File Uploader
uploaded_file = st.file_uploader("Upload the PDF file(s) you want to learn from")

if uploaded_file and not st.session_state.file_saved:
    # Process uploaded files
    
        # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(os.getcwd(), "pdf_files", unique_filename)
    
    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    
    st.write(f"Uploaded file: {uploaded_file.name}")
    st.session_state.uploaded_file_name = unique_filename
    st.session_state.file_saved = True

# Ingest Button
if st.session_state.uploaded_file_name:
    if st.button("Ingest"):
        ingest_file(st.session_state.uploaded_file_name)
        st.session_state.button = True

# Question Input and Answering
if st.session_state.button:
    st.session_state.question = st.text_input("Enter the question you want to ask:")
    if st.session_state.question.strip():
        if st.button("Get Answer"):
            try:
                answer = run_model_and_RAG(st.session_state.uploaded_file_name, st.session_state.question)
                st.write(f"Answer: {answer}")
            except Exception as e:
                st.error(f"An error occurred while processing your question: {e}")

    
    if st.button("End Session"):
            clean_resources(st.session_state.uploaded_file_name)
            st.session_state.clear()  # Clear the session state
            st.write("Session ended and cleaned up!")