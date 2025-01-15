# PDF Research Paper Q&A with LLMs

This project enables users to upload PDF files, such as research papers, and ask questions to gain better insights into the document. Using Retrieval-Augmented Generation (RAG) with a local FAISS vector database, the system efficiently retrieves relevant content and provides concise answers. The frontend is built using Streamlit for an interactive user experience.

## Features

- **Upload PDF Documents**: Users can upload any PDF file (e.g., research papers).
- **Dynamic Summaries**: Generates embeddings for document text and provides contextual answers to user queries.
- **Question Answering**: Leverages a Retrieval-Augmented Generation (RAG) approach to answer questions based on the uploaded document.
- **Efficient Embedding Storage**: Uses a local FAISS vector database to store embeddings for fast and accurate retrieval.
- **Streamlit Interface**: Provides a clean and interactive frontend for users to interact with the system.

## Tech Stack

### Backend
- **model**: Google Gemini
- **Python**: Core programming language.
- **LangChain**: For prompt engineering and question-answering workflows.
- **FAISS**: Local vector database for storing and retrieving embeddings.
- **OpenAI / Hugging Face LLMs**: For generating embeddings and providing context-aware answers.

### Frontend
- **Streamlit**: Simple and interactive web-based interface for user interactions.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prajodh/learn_using_pdf_llm.git
   cd learn_using_pdf_llm
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required Python packages:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your API keys and configurations (e.g., OpenAI API key).
   ```env
    GOOGLE_API_KEY=value
    LANGCHAIN_API_KEY=value
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT = pdf project
   ```

4. **Run the Application**:
   Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

## Usage

1. **Upload PDF**: Drag and drop a PDF file or select one from your local system using the interface.
2. **Ask Questions**: Type your questions in the input box. The system will retrieve relevant sections from the PDF and generate an answer.
3. **Explore Summaries**: View the summarized content and explore detailed insights from the uploaded document.


## How It Works

1. **PDF Upload**:
   - Extracts text from the uploaded PDF using libraries like `PyPDF2` or `pdfminer`.
2. **Embedding Generation**:
   - Converts document text into embeddings using a pre-trained LLM (e.g., OpenAI or Hugging Face models).
   - Stores embeddings in a FAISS vector database for efficient retrieval.
3. **RAG Pipeline**:
   - Processes user queries by retrieving the most relevant chunks from the FAISS database.
   - Combines the retrieved content with a Retrieval-QA prompt from the LangChain hub.
   - Generates answers using the LLM.

## Future Improvements

- **Multi-File Support**: Allow users to upload and query multiple PDFs.
- **Enhanced Frontend**: Improve user experience with better design and additional features.
- **Cloud Deployment**: Deploy the application on platforms like AWS, Azure, or Google Cloud.
- **Support for More File Formats**: Extend support for Word documents and other text-based file formats.

## License

This project is licensed under the [MIT License](LICENSE).

Thank you for checking out this project! We hope it helps you better understand complex research papers and documents.
