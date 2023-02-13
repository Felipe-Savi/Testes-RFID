# Testes

## Componentes:
* Antena
* Arduino
* Cabo RS232M-RS232M
* Computador
* Conversor USB-RS232M
* Conversor RS232F-TTL

## Testes

### O.B.S.
Nos testes, foi considerado que todos os bytes da seção "INFO" são referentes ao cartão. Mas pelo que eu testei usando o programa "New Passive Demo", o primeiro byte talvez não faça parte do ID do cartão

### Antena-Arduino
* Componentes/Conexão: Antena + RS232M-RS232M + RS232F-TTL + Arduino
* Utilidade: Objetivo final
* Funcionamento: O Arduino indica qual cartão foi identificado pela antena

### Antena-Computador
* Componentes/Conexão: Antena + RS232M-USB + Computador
* Utilidade: Testar a antena
* Funcionamento: O computador indica qual cartão foi identificado pela antena
* O.B.S.: É possível escrever dados na antena, mas esse programa não faz isso

### Arduino-Computador
* Componentes/Conexão: Arduino + TTL-RS232F + RS232M-USB + Computador
* Utilidade: Testar comunicação com o Arduino
* Funcionamento: Computador envia ASCII, Arduino incrementa e retorna
* O.B.S.: Se remover o delay, o Arduino recebe bytes estranhos. O programa em Python não aceita frases longas, a não ser que for aumentado o delay do Arduino

### Computador-Computador
* Componentes/Conexão: Computador + USB-RS232M + RS232F-TTL (RX e TX em curto-circuito)
* Utilidade: Testar USB-RS232M e RS232F-TTL
* Funcionamento: Computador envia o input e dá print no retorno
* O.B.S.: Arduino está sendo utilizado para alimentar o RS232F-TTL

## calculate_checksum.c
Programa responsável por calcular o checksum. Para usá-lo, é só alterar o valor da variável `bytes`