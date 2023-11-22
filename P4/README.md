# Chat-bot Ponderada 4

Este chat bot foi desenvolvido a partir do modelo LLM "wizard-vicuna" do Ollama. El foi cconfigurado a partir do modelfile para se comportar como uma AI de auxilio com regras de seguranças em uma industria. Para a interface foi ultilizado o `chainlit`, que consome a API do modelo local.

# Como usar?

Certifique-se de que você tem o Ollama e o chainlit baixado em sua maquina.

Clone o repositorio do gitHub e vá pelo terminal até o caminho da pasta onde ele esta salvo. Digite no terminal:

`ollama create George -f Modelfile`

Em seguida, digite no terminal:

`chainlit run app.py -w`

Agora você pode acessar o chat-bot em um browser no http://localhost:8000