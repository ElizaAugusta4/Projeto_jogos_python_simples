import pygame
import sys

# Configurações do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Classe para o jogador (representado por um coração)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coracao.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Função principal do jogo
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jogo Labirinto")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualiza o jogador e os objetos do jogo
        all_sprites.update()

        # Verifica se o jogador alcançou o final do labirinto
        if player.rect.colliderect(final_rect):
            pygame.quit()
            sys.exit()

        # Desenha a tela
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.draw.rect(screen, RED, final_rect)  # Retângulo vermelho representa o final do labirinto

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    final_rect = pygame.Rect(700, 500, 50, 50)  # Retângulo que representa o final do labirinto
    main()
