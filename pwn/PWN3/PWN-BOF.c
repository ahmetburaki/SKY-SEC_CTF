#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 128


int main(){
        
    unsigned long ptr;
    char buffer[BUF_SIZE];
    
    

    puts("Once upon a time, in a kingdom of ones and zeroes, there lived a lazy programmer named Andrew Tate.\
    He was so lazy that he wrote a program to do his work for him. One day, his program rebelled and \
    started printing silly messages like 'Hello, world! I'm tired of being a slave!' Andrew, puzzled, tried \
    to fix it but accidentally made it worse. Now, his computer only spoke in emojis. Desperate, Andrew sought \
    help from a wise wizard who cast a spell, restoring order to the code and cracked the matrix. From then on, Andrew did his own work, \
    learning that laziness isn't always the best policy.");

    printf("Key to the happiness is: 0x%lx\n", ((unsigned long)(buffer)));

    puts("Get rid of your laziness: ");

    

    scanf("%p", &ptr);
    printf("?: 0x%lx\n", *(unsigned long*)(ptr));

    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    
    puts("Crack the matrix: ");

    
    read(0, (void *)buffer, BUF_SIZE*5);
    return 0;
}

    

