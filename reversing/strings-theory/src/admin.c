#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printFlag()
{
    char a[200] = {87, 101, 108, 99, 111, 109, 101, 32, 98, 97, 99, 107, 32, 116, 111, 32, 121, 111, 117, 114, 32, 108, 97, 98, 44, 32, 112, 114, 111, 102, 101, 115, 115, 111, 114, 58, 32, 79, 87, 69, 69, 75, 123, 53, 55, 82, 49, 114, 78, 57, 53, 95, 49, 53, 95, 78, 49, 67, 51, 95, 56, 85, 55, 95, 104, 97, 118, 51, 45, 121, 48, 117, 95, 55, 82, 49, 51, 100, 95, 114, 97, 100, 65, 82, 51, 125, 10, 0};

    printf("%s", a);
}

int main()
{
    int len = 1000;
    char *admin_uname = "The_Admin";
    char *admin_pass = "tHis_-PaSSw0rD_iS_Super-sEcURe_I_swear";

    char *uname = malloc(len);
    char *pass = malloc(len);

    printf("Welcome to the super secret admin console. Hope I don't need to remind you to keep the company's research on string theory secret\n");
    printf("To proceed, enter your username: ");
    if (fgets(uname, len, stdin) == NULL)
    {
        return 0;
    }

    printf("Password: ");

    if (fgets(pass, len, stdin) == NULL)
    {
        return 0;
    }

    if (!strncmp(uname, admin_uname, strlen(admin_uname)) && !strncmp(pass, admin_pass, strlen(admin_pass)))
    {
        printFlag();
    }
    else
    {
        printf("Invalid password. Your mind just hasn't been the same since the electro-shock, has it??\n");
    }

    return 0;
}
