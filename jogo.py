import os
import time
import keyboard
import pygame

# Função para reproduzir a música em segundo plano
def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/Pichau/Documents/Git-Github/Eliza/Projeto_Lelist/Projeto_Lelist/Projeto_jogos_python_simples/audio.mp3')
    pygame.mixer.music.play(-1)  # -1 significa tocar a música em loop

# Função para exibir as instruções do jogo
def show_instructions():
    print("Bem-vindo ao Jogo Simples em Python com Música!")
    print("Pressione as teclas 'A', 'S', 'D' e 'F' para interagir.")
    print("Pressione 'Q' para sair.")
    print()

# Função principal do jogo
def main():
    # Inicialização das variáveis do jogo
    score = 0
    game_over = False

    # Reproduzir música em segundo plano
    play_background_music()

    # Mostrar instruções
    show_instructions()

    # Loop principal do jogo
    while not game_over:
        # Verificar se o jogador quer sair (pressionou 'Q')
        if keyboard.is_pressed('q'):
            game_over = True
            break

        # Obter entrada do jogador
        if keyboard.is_pressed('a'):
            score += 1
        elif keyboard.is_pressed('s'):
            score += 2
        elif keyboard.is_pressed('d'):
            score += 3
        elif keyboard.is_pressed('f'):
            score += 4

        # Atualizar a tela do jogo
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela do console
        print(f"Pontuação: {score}")
        time.sleep(0.1)  # Aguardar um curto intervalo para evitar taxa de atualização rápida

    # Finalizar o jogo
    pygame.mixer.music.stop()
    print("Fim do Jogo. Obrigado por jogar!")

if __name__ == "__main__":
    main()
