#include <string.h>
#include <stdio.h>

unsigned char getChecksum(unsigned char* buffer, unsigned char buffer_size) {
    unsigned char i, sum = 0;
    
    for(i = 0; i < buffer_size; i++) {
        sum = sum + buffer[i];
    }
    sum = (~sum) + 1;
    return sum;
}

int main() {
    unsigned char* bytes = "\x7c\xff\x10\x32\x00";
    
    unsigned char checksum = getChecksum(bytes, strlen(bytes));
    
    printf("%x", (unsigned int)checksum);
}