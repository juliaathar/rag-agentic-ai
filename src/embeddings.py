import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from pdf_loader import chunks
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]

embeddings = GoogleGenerativeAIEmbeddings(
    model='models/embedding-001',
    google_api_key= google_api_key
)

vector_store = Chroma.from_documents(
    documents= chunks,
    embedding= embeddings,
    persist_directory= './data/chroma_db'
)

print(vector_store._collection.count())