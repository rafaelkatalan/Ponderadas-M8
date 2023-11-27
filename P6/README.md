# Atividade Ponderada 6

O código implementa um Perceptron, um modelo simples de rede neural, para realizar a operação lógica AND. O Perceptron é treinado iterativamente com entradas (X) e saídas desejadas (y), ajustando seus pesos e bias com base nos erros de previsão. A função de ativação é uma função degrau simples, e o treinamento é realizado por um número definido de iterações. O exemplo de uso fornece dados para a porta AND, onde o Perceptron é treinado para produzir saídas corretas para diferentes combinações de entradas. Após o treinamento, o Perceptron é testado com todas as combinações possíveis de entradas da porta AND, e as saídas são impressas para verificar a eficácia do modelo treinado.

Para treinalo com as saidas das outras portas, a linha com a saida da porta AND é comentada e a saida da porta desejada descomentada.

## Não funciona para o XOR

A porta lógica XOR não é linearmente separável, o que impede que o Perceptron simples resolva corretamente essa operação. O Perceptron pode aprender operações lógicas como AND, NAND e OR, que são linearmente separáveis, mas não XOR, que requer uma separação não linear para ser representada adequadamente. Para resolver a XOR, seria necessário utilizar arquiteturas mais complexas, como redes neurais multicamadas.

