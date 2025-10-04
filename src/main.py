import getpass
import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

template = PromptTemplate.from_template(
  'Hi, my name is {name}! Tell me a joke about machine learning'
)

text = template.format(name='Júlia')

response = llm.invoke(text)

print(response.content)