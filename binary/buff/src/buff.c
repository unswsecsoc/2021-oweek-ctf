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
        // `man gets` is probably the best man page ever :)
        printf("Nice to meet you %s, here's your flag: OWEEK{I_5W3Ar_7HI5-I5_a_900d_ID3A}\n", &buf);
    }
    else
    {
        printf("Nice to meet you, %s :)\n", &buf);
    }

    fflush(stdout);

    return 0;
}
