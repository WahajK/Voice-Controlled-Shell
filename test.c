#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <wchar.h>
#include <stdlib.h>

// cc -fPIC -shared -o test.so test.c
//g++ -c -o test.o test.c
//gcc -shared -o libfoo.so test.o

char* multipurpose(char *arr)
{
    system(arr);
    sleep(3);
    // FILE *cmd=popen(arr, "r");
    // char result[24]={0x0};
    // while (fgets(result, sizeof(result), cmd) !=NULL)
    //     printf("%s\n", result);
    // pclose(cmd);
    // sleep(3);
    // return result;
}

void current_directory()
{
    system("pwd");
    sleep(3);
}

void show_date()
{
    system("date");
    sleep(3);
}

void show_day()
{
    system("date +%A");
    sleep(3);
}

void show_time()
{
    system("date +%T");
    sleep(3);
}

void show_cal()
{
    system("cal");
    sleep(3);
}

void show_user()
{
    system("whoami");
    sleep(3);
}

void snapshot()
{
    system("import -window root screenshot.png");
    sleep(3);
}

void network()
{
    system("ifconfig");
    sleep(3);
}

void shutdown()
{
    printf("Shutting down in 3...\n");
    sleep(1);
    printf("Shutting down in 2...\n");
    sleep(1);
    printf("Shutting down in 1...\n");
    sleep(1);
    system("shutdown now");
}

// void list_file(char *arr)
// {
//     system(arr);
//     sleep(3);
// }

// void list_file_perms(char *arr)
// {
//     system(arr);
// }

// void list_file_hidden(char *arr)
// {
//     system(arr);
// }

// void cd_home()
// {
//     system("cd ~");
// }

// void cd_root()
// {
//     system("cd /");
// }

// void touch(char *arr)
// {
//     system(arr);
// }

// void gedit(char *arr)
// {
//     system(arr);
// }

// void nano(char *arr)
// {
//     system(arr);
// }

// void code(char *arr)
// {
//     system(arr);
// }