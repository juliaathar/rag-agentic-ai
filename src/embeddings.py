from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import shutil
import os

def transform_chunks_to_vectors(chunks):
    
    db_path = "./data/chroma_db"
    if os.path.exists(db_path):
        shutil.rmtree(db_path)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2" 
    )

    vector_store = Chroma.from_documents(
        documents= chunks,
        embedding= embeddings,
        persist_directory= './data/chroma_db'
    )

    return vector_store