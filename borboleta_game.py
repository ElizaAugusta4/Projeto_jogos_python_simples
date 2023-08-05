import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo das Borboletas")

# Carregar imagem de fundo
fundo_imagem = pygame.image.load("fundo.png").convert()

# Classe da borboleta
class Borboleta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("borboleta.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(0, altura_tela - self.rect.height)
        self.velocidade_x = random.randint(-3, 3)
        self.velocidade_y = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Verificar colisão com as bordas da tela
        if self.rect.left < 0 or self.rect.right > largura_tela:
            self.velocidade_x = -self.velocidade_x
        if self.rect.top < 0 or self.rect.bottom > altura_tela:
            self.velocidade_y = -self.velocidade_y

# Classe da borboleta animada
class BorboletaAnimada(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagens = [pygame.image.load("borboleta_asa_aberta.png").convert_alpha(),
                        pygame.image.load("borboleta_asa_fechada.png").convert_alpha()]
        self.image = self.imagens[0]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(0, altura_tela - self.rect.height)
        self.velocidade_x = random.randint(-3, 3)
        self.velocidade_y = random.randint(-3, 3)
        self.frame = 0
        self.animacao_delay = 10
        self.tempo_animacao = self.animacao_delay

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Verificar colisão com as bordas da tela
        if self.rect.left < 0 or self.rect.right > largura_tela:
            self.velocidade_x = -self.velocidade_x
        if self.rect.top < 0 or self.rect.bottom > altura_tela:
            self.velocidade_y = -self.velocidade_y

        # Animação das asas
        self.tempo_animacao -= 1
        if self.tempo_animacao == 0:
            self.frame = (self.frame + 1) % len(self.imagens)
            self.image = self.imagens[self.frame]
            self.tempo_animacao = self.animacao_delay

# Classe da segunda borboleta animada
class BorboletaAnimada2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagens = [pygame.image.load("borboleta-asa-aberta-2.png").convert_alpha(),
                        pygame.image.load("borboleta-asa-fechada-2.png").convert_alpha()]
        self.image = self.imagens[0]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(0, altura_tela - self.rect.height)
        self.velocidade_x = random.randint(-3, 3)
        self.velocidade_y = random.randint(-3, 3)
        self.frame = 0
        self.animacao_delay = 10
        self.tempo_animacao = self.animacao_delay

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Verificar colisão com as bordas da tela
        if self.rect.left < 0 or self.rect.right > largura_tela:
            self.velocidade_x = -self.velocidade_x
        if self.rect.top < 0 or self.rect.bottom > altura_tela:
            self.velocidade_y = -self.velocidade_y

        # Animação das asas
        self.tempo_animacao -= 1
        if self.tempo_animacao == 0:
            self.frame = (self.frame + 1) % len(self.imagens)
            self.image = self.imagens[self.frame]
            self.tempo_animacao = self.animacao_delay

# Lista de todas as borboletas
borboletas = pygame.sprite.Group()
# for _ in range(5):
#     # Crie 5 borboletas normais
#     borboleta = Borboleta()
#     borboletas.add(borboleta)

for _ in range(5):
    # Crie 5 borboletas animadas (que batem as asas)
    borboleta_animada = BorboletaAnimada()
    borboletas.add(borboleta_animada)

for _ in range(5):
    # Crie 5 borboletas animadas (que batem as asas)
    borboleta_animada2 = BorboletaAnimada2()
    borboletas.add(borboleta_animada2)

# Loop principal do jogo
jogo_ativo = True
relogio = pygame.time.Clock()

while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Atualizar a posição de todas as borboletas
    borboletas.update()

    # Desenhar o fundo na tela
    tela.blit(fundo_imagem, (0, 0))

    # Desenhar todas as borboletas na tela
    borboletas.draw(tela)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    relogio.tick(60)

# Finalizar o Pygame
pygame.quit()
