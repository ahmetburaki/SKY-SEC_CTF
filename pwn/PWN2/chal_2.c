#include <stdio.h>
#include <string.h>

void notflaglol(){
    printf("What is this string for?\n"); 
    FILE* ptr;
    ptr = fopen("notaflag.txt","r");
    char flag[64];
    if(fgets(flag,sizeof(flag),ptr)){
        puts(flag);
    }
    fclose(ptr);
}

void flag(){
    FILE* ptr;
    ptr = fopen("notaflag.txt","r");
    char password[64];
    char userPassword[64];
    if(fgets(password,17,ptr)){}
    fclose(ptr);   
    printf("What is the password?\n");
    //fflush(stdout);
    scanf("%s",userPassword);
    if(!strcmp(password,userPassword)){
        printf("Well done! Here's your flag:\n"); 
        //fflush(stdout);
        ptr = fopen("flag.txt","r");
        char flag[64];
        if(fgets(flag,sizeof(flag),ptr)){
            puts(flag);
        }
        fclose(ptr);
    }
}

void vuln(){
    char buffer[128];
    puts("Let's see could you pwn this challenge :D");
    //fflush(stdout);
    gets(buffer);
    printf(buffer);
    puts("\nIf I were you I wouldn't go further lol");
    //fflush(stdout);
    gets(buffer);
}

int main(){
    setvbuf(stdout,NULL,_IONBF,0);
    vuln();
    return 0;
}