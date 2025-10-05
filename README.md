# Assistente de PDF com RAG (LangChain)

Projeto de aprendizado para implementar um sistema RAG (Retrieval Augmented Generation) que responde perguntas sobre documentos PDF usando LangChain.

## Arquitetura

![Diagrama RAG](https://github.com/user-attachments/assets/fab43c72-574a-4f9f-91ac-f7ab059857cb)

## Tecnologias Utilizadas

- **LangChain**: Framework para aplicações com LLMs
- **Google Gemini**: Modelo de linguagem para geração de respostas
- **HuggingFace Embeddings**: Geração de embeddings locais
- **ChromaDB**: Banco de dados vetorial
- **PyPDF**: Extração de texto de PDFs

## Como Funciona

1. **Preparação dos Dados**:
   - Carrega o PDF
   - Divide em chunks menores
   - Gera embeddings (vetores) de cada chunk
   - Armazena no ChromaDB

2. **Consulta**:
   - Usuário faz uma pergunta
   - Sistema busca chunks mais relevantes semanticamente
   - Monta um prompt com os chunks + pergunta
   - LLM gera resposta baseada no contexto
