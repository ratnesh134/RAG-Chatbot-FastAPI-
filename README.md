# RAG PDF Chatbot with FastAPI, ChromaDB & Streamlit

## Project Structure

~~~
RAG-Chatbot/
├── client/         # Streamlit Frontend
│   |──components/
|   |  |──chatUI.py
|   |  |──history_download.py
|   |  |──upload.py
|   |──utils/
|   |  |──api.py
|   |──app.py
|   |──config.py
├── server/         # FastAPI Backend
│   ├── chroma_store/ ....after run
|   |──modules/
│      ├── load_vectorestore.py
│      ├── llm.py
│      ├── pdf_handler.py
│      ├── query_handlers.py
|   |──uploaded_pdfs/ ....after run
│   ├── logger.py
│   └── main.py
└── README.md
|___ requirements.txt
~~~

## ✨ Features
📄 Upload and parse PDFs

🧠 Embed document chunks with HuggingFace embeddings

💂️ Store embeddings in ChromaDB

💬 Query documents using LLaMA3 via Groq

🌍 Microservice architecture (Streamlit client + FastAPI server)

## 🌟 Credits

LangChain

ChromaDB

Groq

Streamlit
