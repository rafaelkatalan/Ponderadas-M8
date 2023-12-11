# Ponderada 8

## Visão Geral
Este script Python cria um aplicativo simples de conversão de fala para texto e tradução, utilizando várias bibliotecas. Certifique-se de ter as versões específicas das bibliotecas instaladas executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Este comando instalará automaticamente as versões corretas das dependências necessárias.

## Uso

1. Execute o script em um ambiente Python.
2. Quando aparecer no terminal "capturando áudio", você deve falar o que deseja que seja traduzido.
3. Quando a fala for detectada, ela será convertida em texto usando a API Google Web Speech.
4. O script traduzirá então o texto para o Hebraico usando a API Google Translator.
5. O texto traduzido será lido em voz alta usando a síntese de texto para fala.

## Dependências e APIs

- **Reconhecimento de Fala:** Utiliza a biblioteca `speech_recognition` para capturar áudio do microfone e convertê-lo em texto usando a API Google Web Speech.
- **Texto para Fala:** Utiliza a biblioteca `pyttsx3` para síntese de texto para fala e a biblioteca `gtts` para gerar um arquivo MP3 a partir do texto traduzido.
- **Reprodução de Áudio:** Implementa a reprodução de áudio usando a biblioteca `pygame`.
- **Tradução:** Utiliza a biblioteca `deep_translator` para traduzir texto de um idioma para outro usando a API Google Translator.

### [Vídeo](https://drive.google.com/file/d/1WKLEu3VAg97Jt8vxiaqlzhwfHmh3lrjb/view?usp=sharing)