#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");
    string name = get_string("What's your name: ");
    printf("Hello to you too, %s!!\n", name);
}