#include <stdio.h>

int main()
{
    int leet = 1337;
    char buf[101];
    printf("Welcome to the CTF Gym. What's your name? (upto 100 characters only)\n");
    fflush(stdout);
    gets(&buf);

    if (leet != 1337)
    {
        printf("Nice to meet you %s, here's your flag: [REDACTED]\n", &buf);
    }
    else
    {
        printf("Nice to meet you, %s :)\n", &buf);
    }

    fflush(stdout);

    return 0;
}
