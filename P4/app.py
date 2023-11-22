import chainlit as cl
from langchain.llms import Ollama

ollama = Ollama(base_url='http://localhost:11434',
model="George")


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=(ollama(message.content)),
    ).send()