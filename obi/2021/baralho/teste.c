// import stdio.h 
#include <stdio.h>

int main()
{
    char input[500];
    scanf("%s", input);
    for(int i = 0; i < sizeof(input); i += 3){
        printf("%c", input[i]);
    }

    return 0;
}
