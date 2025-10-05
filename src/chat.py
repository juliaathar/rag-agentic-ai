from langchain.chains import RetrievalQA

def agentic_rag(llm, vector_store, question):

    retriver = vector_store.as_retriever(
        search_kwargs={'k': 10}
    )

    chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever= retriver,
        return_source_documents=True
    )

    answer = chain.invoke({"query": question})

    return answer['result']