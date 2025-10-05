from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf_and_transform_to_chunks ():
    
    loader = PyPDFLoader(
        file_path='./data/politica_de_ferias.pdf',
        mode='single'
    )
    
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = text_splitter.split_documents(docs)

    return chunks