#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1"
#define SERVER_PORT 12345
#define BUFFER_SIZE 1024

int main() {
    int sock;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];

    // Création du socket UDP
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) {
        perror("Erreur lors de la création du socket");
        exit(EXIT_FAILURE);
    }

    // Configuration de l'adresse du serveur
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    printf("Client UDP prêt à envoyer des commandes au serveur %s:%d\n", SERVER_IP, SERVER_PORT);

    while (1) {
        // Demander une commande utilisateur
        printf("Entrez une commande (ex: mov v1 (10,5), ou 'exit' pour quitter) : ");
        fgets(buffer, BUFFER_SIZE, stdin);
        
        // Supprimer le retour à la ligne
        buffer[strcspn(buffer, "\n")] = 0;

        // Vérifier si l'utilisateur veut quitter
        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        // Envoyer la commande au serveur Python via UDP
        if (sendto(sock, buffer, strlen(buffer), 0, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
            perror("Erreur lors de l'envoi des données");
            break;
        }

        printf("Commande envoyée : %s\n", buffer);
    }

    // Fermer le socket
    close(sock);
    printf("Client terminé.\n");
    return 0;
}
