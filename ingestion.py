import os
import shutil
import dotenv
dotenv.load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS  
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



def ingest_data_and_create_vector_store(name):
    
    """
    load the file ;chunk it into smaller segements and store it in vectorstore
    """
    file_path = os.path.join(os.getcwd(),"pdf_files",name)
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()
    text_splitters = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 30, separator = "\n")
    split_documents = text_splitters.split_documents(documents)
    store_in_vector_store(split_documents, name)

def store_in_vector_store(split_documents, name):
    """
    load the embeddings model and store the data
    """
    embeddings_model  = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_documents(split_documents, embeddings_model)
    folder_name = name.split(".")[0]
    os.mkdir(os.path.join(os.getcwd(),f"local_document_index_{folder_name}"))
    vector_store.save_local(os.path.join(os.getcwd(),f"local_document_index_{folder_name}"))

def clean_resources(name):
    folder_name = name.split(".")[0]
    shutil.rmtree(os.path.join(os.getcwd(),f"local_document_index_{folder_name}"))
    os.remove(os.path.join(os.getcwd(),"pdf_files",name))    



