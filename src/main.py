import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pdf_loader import load_pdf_and_transform_to_chunks
from embeddings import transform_chunks_to_vectors
from chat import agentic_rag

load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai", temperature=0.7)

chunks = load_pdf_and_transform_to_chunks()

vector_store = transform_chunks_to_vectors(chunks=chunks)

question = "Qual a quantidade máxima de dias que posso tirar de férias?"

question_1 = "Posso dividir minhas férias?"

question_2 = "Posso pedir férias sem ter completado um ano na empresa?"

question_3 = "Preciso avisar com quantos dias de antecedência?"

answer = agentic_rag(llm=llm, vector_store=vector_store, question=question_2)

print("\n")
print(answer)
print("\n")