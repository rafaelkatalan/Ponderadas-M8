# Chat-bot Ponderada 5

Este chat bot, baseado no modelo de linguagem Ollama "wizard-vicuna", foi configurado através do arquivo de modelo (Modelfile) para atuar como uma inteligência artificial de auxílio com foco em regras de segurança industrial.

## Funcionamento do Código

O código utiliza a biblioteca Langchain, integrando a funcionalidade do modelo Ollama "George" para fornecer respostas ponderadas em cenários de segurança industrial. A abordagem inclui:

- **Embeddings com SentenceTransformer:** Utiliza a biblioteca SentenceTransformer para gerar embeddings de texto, criando representações numéricas eficientes para análise semântica.

- **Armazenamento e Recuperação Eficientes com Chroma:** Os embeddings gerados são armazenados de maneira eficiente usando a classe Chroma da Langchain. Isso permite uma rápida recuperação dos vetores durante as interações do chat, garantindo respostas contextuais.

- **Interface com Chainlit:** O `chainlit` é empregado para criar uma interface que consome a API local do modelo Ollama, facilitando a interação através de um navegador.

## Instruções de Uso

Certifique-se de ter o Ollama e o Chainlit instalados em sua máquina. Clone o repositório do GitHub e, no terminal, navegue até o diretório onde ele está armazenado. Execute os seguintes comandos:

```bash
ollama create George -f Modelfile
chainlit run app.py -w
```

Acesse o chat-bot em seu navegador utilizando o link http://localhost:8000.

## Demonstração em Vídeo

Assista ao bot em ação no [vídeo demonstrativo](https://drive.google.com/file/d/1PMcsO807Oo8VqufIEAD5aX8HwX07iIld/view?usp=drive_link).