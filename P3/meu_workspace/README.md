# Pacote Ponderada 3

Este pacote do ROS 2 foi desenvolvido para simplificar a execução do ROS Navigation 2 (nav2) para navegação, juntamente com a simulação no Gazebo. Ele permite o envio de comandos de locomoção para o turtlebot por meio de um chat-bot.

## Como Utilizar

Para empregar este pacote, siga as instruções abaixo:

1. Clone este repositório em sua máquina.

2. Abra um terminal na pasta do repositório clonado.

3. Execute os seguintes comandos para compilar o pacote:

    ```bash
    colcon build
    ```

4. Inicie o lançamento (launch) com o seguinte comando:

    ```bash
    ros2 launch my_package launch.py
    ```

Isso iniciará o ROS Navigation 2 para navegação, abrirá a simulação no Gazebo e abrirá automaticamente um novo terminal para o controle do robô por meio do chatbot.

## Chatbot

Quando o pacote é executado, um script python chamado subscriber.py é iniciado. Esse script é responsável por ouvir e interpretar os comandos do chat-bot, utilizando-os para movimentar o robô. Além disso, automaticamente abrirá em um terminal separado o publisher.py, um script responsável por publicar os inputs do chatbot no tópico "chat", que será escutado pelo subscriber.

## Requisitos

Certifique-se de ter o ROS 2, NAV2 e o Gazebo instalados em sua máquina antes de utilizar este pacote.