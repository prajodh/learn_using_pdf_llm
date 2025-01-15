import os
import dotenv
dotenv.load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS  
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

def run_model_and_RAG(name, question):
    folder_name = name.split(".")[0]
    embeddings_model = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    new_vector_store = FAISS.load_local(f"local_document_index_{folder_name}", embeddings_model, allow_dangerous_deserialization=True)
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")
    retrieval_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    chain_docs = create_stuff_documents_chain(llm, retrieval_prompt)
    retrival_chain = create_retrieval_chain(new_vector_store.as_retriever(), chain_docs)
    res = retrival_chain.invoke(input = {"input": question})
    return res["answer"]