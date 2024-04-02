#include <stdio.h>

void database(long first, long second, long third)
{
    if (first == 0xdeadbeefdeadbeef && second == 0xc0debabec0debabe && third == 0xcacadadacacadada){
        printf("Well done! Here's your flag:\n"); 
        FILE* ptr;
        ptr = fopen("flag.txt","r");
        char flag[64];
        if(fgets(flag,sizeof(flag),ptr)){
            puts(flag);
        }
        fclose(ptr);
    }else{
        printf("Nope, that's not how you're supposed to solve this challenge :D\n");
    }
}

void vuln()
{
    char buffer[16];

    printf("Welcome to the system. What is your name:\n");
    scanf("%s", buffer);
    printf("Hi there, %s\n", buffer);    
}

int gadgets(){
    asm("pop %rsi;ret");
    asm("pop %rdx;ret");
    asm("pop %rdi;ret");
}

int main()
{
    vuln();

    return 0;
}
