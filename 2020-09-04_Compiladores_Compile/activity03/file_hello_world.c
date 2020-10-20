#include <stdio.h>
#include <stdlib.h>


char output;

main() {
    FILE *pontfil;
    
    if((pontfil = fopen("file.txt","r")) == NULL) {
        printf("\nErro ao abrir o arquivo!\n");
        system("pause");
        exit(0);
    }
   
    while((output = getc(pontfil)) != EOF) {
        printf("%c", output);
    }
    printf("\n\n");
    
    system("pause");
    fclose(pontfil);
}
