#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define MAX 10

using namespace std;


int main() {
  char palavra[MAX];
  char estado;
  int tamanho,i;

  printf("\nDigite uma palavra: ");
  scanf("%s",&palavra);
  
  printf("\nVoce digitou a palavra: %s\n",palavra);
  tamanho=strlen(palavra);
  
  printf("\nA palavra digitada tem %d caracteres",tamanho);
  estado = '0';

  i=0;
  while ((i < tamanho) && (estado != 'e')) {
      switch(estado) {
        case '0' :
            if (palavra[i] == 'a')
                    estado = '1';
                else
                    estado = 'e';
                break;

         case '1' :
            if (palavra[i]=='b')
                       estado = '2';
                 else
                       estado = 'e';
                 break;

        case '2' :
            if (palavra[i] == 'c')
                estado = '3';
            else
                estado ='e';
            break;

        case '3' :
            if (palavra[i] == 'c')
                estado = '4';
            else
                if (palavra[i] == 'd')
                    estado = '5';
                else
                    estado = 'e';
                break;

        case '4' :
            if (palavra[i] == 'c')
                estado = '3';
            else
                estado = 'e';
            break;

        case '5' : 
            if (palavra[i] == 'e')
                estado = '6';
            else
                estado = 'e';
            break;

        case '6' : 
            if (i < tamanho)
                estado = 'e';
            break;
        }
        i++;
    }

    if (estado=='6')
        printf("\n\n\nPalavra reconhecida!\n\n\n");
    else
        printf("\n\n\nPalavra nao reconhecida\n\n\n");

    return 0;
}