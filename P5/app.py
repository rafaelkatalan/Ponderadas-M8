from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough

import chainlit as cl

loader = TextLoader("./safety.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """As George, asnswer the question based only on the following context:
{context}

Question: {question}
"""

@cl.on_chat_start
async def on_chat_start():
    model = Ollama(base_url='http://localhost:11434', model="George")
    prompt = ChatPromptTemplate.from_template(template)
    
    chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    )
    
    cl.user_session.set("runnable", chain)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    for chunk in runnable.stream(message.content):
        await msg.stream_token(chunk)

    await msg.send()