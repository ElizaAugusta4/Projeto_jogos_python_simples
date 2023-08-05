def fazer_perguntas_jogador(nome_jogador):
    perguntas = [
        "Qual é o protagonista do anime 'Naruto'?",
        "Em que mundo o anime 'Attack on Titan' se passa?",
        "Qual é o nome do Death Note?",
        "Qual é o personagem principal do anime 'One Piece'?",
        "Em qual jogo o anime 'Sword Art Online' se passa?",
    ]

    respostas_corretas = [
        "Naruto Uzumaki",
        "Mundo dos Titãs",
        "Ryuk",
        "Monkey D. Luffy",
        "Sword Art Online"
    ]

    pontuacao = 0

    print(f"{nome_jogador}, é a sua vez de responder às perguntas!")

    for i in range(len(perguntas)):
        resposta = input(perguntas[i] + "\nSua resposta: ")
        if resposta.lower() == respostas_corretas[i].lower():
            print("Resposta correta!")
            pontuacao += 1
        else:
            print("Resposta incorreta!")

    print(f"\n{nome_jogador}, sua pontuação final é: {pontuacao} ponto(s).\n")
    return pontuacao

def quiz_animes():
    print("Bem-vindos ao Quiz de Animes!")
    nome_jogador1 = input("Jogador 1, digite o seu nome: ")
    nome_jogador2 = input("Jogador 2, digite o seu nome: ")

    pontuacao_jogador1 = fazer_perguntas_jogador(nome_jogador1)
    pontuacao_jogador2 = fazer_perguntas_jogador(nome_jogador2)

    if pontuacao_jogador1 > pontuacao_jogador2:
        print(f"Parabéns, {nome_jogador1}! Você ganhou o Quiz de Animes!")
    elif pontuacao_jogador1 < pontuacao_jogador2:
        print(f"Parabéns, {nome_jogador2}! Você ganhou o Quiz de Animes!")
    else:
        print("Empate! Vocês dois são verdadeiros fãs de animes!")

quiz_animes()
