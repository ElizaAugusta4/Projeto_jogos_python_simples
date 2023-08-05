import tkinter as tk
from tkinter import messagebox
import pygame

jogo_ativo = True

def fazer_pergunta(pergunta):
    global jogo_ativo
    root = tk.Tk()
    root.title("Pergunta")
    root.geometry("300x150")
    root.configure(bg="pink")

    def on_close():
        global jogo_ativo
        jogo_ativo = False
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    label = tk.Label(root, text=pergunta, fg="white", bg="pink", font=("Helvetica", 12))
    label.pack(pady=20)

    resposta = tk.StringVar()
    entry = tk.Entry(root, textvariable=resposta, bg="white")
    entry.pack()

    def on_submit():
        resposta_usuario = resposta.get()
        root.destroy()
        validar_resposta(pergunta, resposta_usuario)

    btn = tk.Button(root, text="Enviar", bg="white", command=on_submit)
    btn.pack(pady=10)

    root.mainloop()

def validar_resposta(pergunta, resposta_usuario):
    respostas_corretas = {
        "Qual é o prato favorito da Eliza?": "Creme de galinha",
        "Em que cidade a Eliza nasceu?": "Piancó",
        "Qual é a cor favorita da Eliza?": "Vermelho",
        "Qual é o filme favorito da Eliza?": "Todo mundo em Pânico",
        "Em que data comemoramos o nosso primeiro beijo?": "Dia 29 de julho de 2022",
        "Qual é a música favorita da Eliza?": "Nuvole Bianchi",
        "Qual é o destino dos sonhos da Eliza?": "Viagem para o Japão",
        "Qual é o hobby favorito da Eliza?": "Assistir animes"
    }

    if resposta_usuario.lower() == respostas_corretas[pergunta].lower():
        return True
    else:
        return False

def jogo_de_perguntas():
    global jogo_ativo
    perguntas = [
        "Qual é o prato favorito da Eliza?",
        "Em que cidade a Eliza nasceu?",
        "Qual é a cor favorita da Eliza?",
        "Qual é o filme favorito da Eliza?",
        "Em que data comemoramos o nosso primeiro beijo?",
        "Qual é a música favorita da Eliza?",
        "Qual é o destino dos sonhos da Eliza?",
        "Qual é o hobby favorito da Eliza?"
    ]
    
    pontuacao = 0
    
    for pergunta in perguntas:
        if jogo_ativo:
            resposta = fazer_pergunta(pergunta)
            if resposta:
                pontuacao += 1
        else:
            break
    
    if pontuacao == len(perguntas) and jogo_ativo:
        messagebox.showinfo("Resultado", "Parabéns! Você acertou todas as perguntas e conseguiu se casar com a Eliza!")
    elif jogo_ativo:
        messagebox.showinfo("Resultado", "Infelizmente, você não respondeu a todas as perguntas, tente novamente para conseguir se casar com a Eliza!")

jogo_de_perguntas()
