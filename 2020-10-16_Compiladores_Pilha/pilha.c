#include <stdio.h>

#include <stdlib.h>

#define MAX 5

typedef struct {
    int elemento[MAX];
    int topo;
}
TPilha;

int main() {
    TPilha pilha;
    int op, dado;
    pilha.topo = -1;

    do {
        system("cls");
        printf("* * * * *   M E N U     * * * * *\n\n\n");
        printf("\n1 - Push");
        printf("\n2 - Pop");
        printf("\n3 - Mostra");
        printf("\n9 - Sair\n\n");
        printf("\nDigite a sua opcao: ");
        scanf("%d", & op);

        switch (op) {
        case 1:
            system("cls");
            printf("* * * * *   P u s h   * * * * *\n");
            printf("\nDigite o dado a ser empilhado: ");
            scanf("%d", & dado);
            if (pilha.topo >= (MAX - 1))
                printf("\n\nImpossivel inserir...\nPilha cheia!\n\n");
            else {
                pilha.topo = pilha.topo + 1;
                pilha.elemento[pilha.topo] = dado;
                printf("\n\nElemento inserido com sucesso!!\n\n");
            }
            system("pause");
            break;

        case 2:
            system("cls");
            printf("* * * * *   P o p   * * * * *\n");
            if (pilha.topo < 0)
                printf("\n\nImpossivel remover...\nPilha vazia!\n\n");
            else {
                pilha.topo = pilha.topo - 1;
                printf("\n\nDado removido com sucesso!\n\n");
            }
            system("pause");
            break;

        case 3:
            system("cls");
            printf("* * * *   P I L H A   * * * *\n\n\n");
            if (pilha.topo < 0)
                printf("\n\n Pilha vazia \n\n");
            else
                for (int i = pilha.topo; i >= 0; i--)
                    printf("\n\t%d", pilha.elemento[i]);
            printf("\n\n");
            system("pause");
            break;
        }

    } while (op != 9);

    return 0;
}