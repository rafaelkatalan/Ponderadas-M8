# Pacote Ponderada 2

Este pacote do ROS 2 foi desenvolvido para facilitar a execução do ROS Navigation 2 (nav2) para mapeamento, juntamente com a simulação no Webots. Além disso, o pacote inclui um script Python que abre um novo terminal, permitindo o controle do robô utilizando o teleop.

## Como Usar

Para utilizar este pacote, siga as instruções abaixo:

1. Clone este repositório em sua máquina.

2. Abra um terminal na pasta do repositório clonado.

3. Execute os seguintes comandos para compilar o pacote:

    ```bash
    colcon build
    ```

4. Execute o lançamento (launch) com o seguinte comando:

    ```bash
    ros2 launch my_package launch.py
    ```

Isso iniciará a execução do ROS Navigation 2 para mapeamento e abrirá a simulação no Webots. Além disso, um novo terminal será aberto para controle do robô usando o pacote teleop.

## Controle do Robô com Teleop

Após a execução do lançamento, um novo terminal será aberto para controle do robô. Utilize o teleop para mover o robô de forma interativa.

Lembre-se de encerrar todas as execuções quando necessário.

## Requisitos

Certifique-se de ter o ROS 2, NAV2 e o Webots instalados em sua máquina antes de utilizar este pacote.
