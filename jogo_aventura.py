def fase1():
    print("Vocês estão em uma floresta misteriosa. À sua frente, há dois caminhos.")
    print("Vocês podem escolher entre 'caminho da direita' ou 'caminho da esquerda'.")
    escolha = input("Qual caminho vocês vão escolher? (digite 'direita' ou 'esquerda'): ")
    
    if escolha.lower() == "direita":
        print("Vocês encontraram uma clareira com uma fada amigável.")
        fase2()
    elif escolha.lower() == "esquerda":
        print("Vocês caíram em um pântano e ficaram presos. Fim de jogo.")
    else:
        print("Opção inválida. Tente novamente.")
        fase1()

def fase2():
    print("A fada agradece por terem encontrado e pergunta se desejam um desejo.")
    desejo = input("Qual é o desejo de vocês? (digite o desejo): ")
    print(f"A fada concedeu o desejo de vocês: '{desejo}'.")
    print("A fada os guia para a próxima fase.")
    fase3()

def fase3():
    print("Vocês chegaram a um castelo assustador.")
    print("Na porta do castelo, há um enigma para resolver.")
    print("O enigma é: 'O que tem um buraco no topo, dois buracos embaixo e faz as pessoas chorarem?'")
    resposta = input("Qual é a resposta? ")
    
    if resposta.lower() == "olhos":
        print("Resposta correta! A porta se abre e vocês encontram um tesouro.")
        print("Parabéns! Vocês concluíram a jornada juntos!")
    else:
        print("Resposta incorreta. A porta permanece trancada. Fim de jogo.")

def jogo_aventura():
    print("Bem-vindo ao jogo de aventura!")
    print("Vocês são um casal corajoso e estão prontos para enfrentar desafios juntos.")
    print("Vamos começar!")
    fase1()

jogo_aventura()
