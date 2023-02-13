#include <SoftwareSerial.h>

uint8_t rx_pin = 7;
uint8_t tx_pin = 6;

SoftwareSerial computador(rx_pin, tx_pin, false);

void setup() {
    Serial.begin(9600);
    computador.begin(9600);
}

void loop() {
    if (computador.available()) {
        int valor = computador.read();
        
        // Sem esse delay da ruim nao sei por que
        // Acho que eh porque nao da para escrever e ler ao mesmo tempo
        delay(10);
        
        computador.write(valor+1);
    }
}
