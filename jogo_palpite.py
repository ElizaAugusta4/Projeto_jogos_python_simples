import random
import tkinter as tk
from tkinter import messagebox
import pygame
from time import sleep

def gerar_numero(intervalo_min, intervalo_max):
    return random.randint(intervalo_min, intervalo_max)

def resultado(resultado):
    label_resultado = tk.Label(app,text=f"{resultado}",font=("Arial",15),bg='pink', fg='red')
    label_resultado.pack()
   

def verificar_tentativa():
    tentativa = int(entrada_tentativa.get())
    if tentativa == numero_aleatorio:
        pygame.mixer.music.stop()  # Para a música de fundo ao acertar
        # messagebox.showinfo("Resultado", f"Parabéns! Você adivinhou o número em {tentativas + 1} tentativas!")
        resultado(f"Parabéns! Você adivinhou o número em {tentativas + 1} tentativas!")
    elif tentativa < numero_aleatorio:
        # messagebox.showinfo("Dica", "O número é maior. Tente novamente.")
        resultado("O número é maior. Tente novamente.")
        
    else:
        # messagebox.showinfo("Dica", "O número é menor. Tente novamente.")
        resultado("O número é menor. Tente novamente.")

    entrada_tentativa.delete(0, tk.END)

def iniciar_jogo():
    global numero_aleatorio, tentativas
    numero_aleatorio = gerar_numero(intervalo_min, intervalo_max)
    tentativas = 0
    btn_adivinhar['state'] = tk.NORMAL
    messagebox.showinfo("Bem-vindo", f"Tente adivinhar o número entre {intervalo_min} e {intervalo_max}.")
    pygame.mixer.music.load("C:/Users/Pichau/Documents/Git-Github/Eliza/Projeto_Lelist/Projeto_Lelist/Projeto_jogos_python_simples/audio.mp3")  # Carrega a música de fundo
    pygame.mixer.music.play(-1)  # Reproduz a música em loop infinito

def jogo_adivinhacao():
    global tentativas
    tentativas += 1

    if tentativas <= tentativas_maximas:
        verificar_tentativa()
    else:
        pygame.mixer.music.stop()  # Para a música de fundo ao exceder as tentativas
        messagebox.showinfo("Fim de Jogo", f"Suas {tentativas_maximas} tentativas acabaram. O número era {numero_aleatorio}. Tente novamente.")
        iniciar_jogo()

# Configuração inicial
intervalo_min = 1
intervalo_max = 100
tentativas_maximas = 7
tentativas = 0

app = tk.Tk()
app.title("Jogo de Adivinhação")
app.configure(bg='pink')
app.geometry("400x400")
app.resizable(False,False)



label_instrucao = tk.Label(app, text="Digite seu palpite:", bg='pink', fg='black',font=("Arial",20))
label_instrucao.pack()

entrada_tentativa = tk.Entry(app,font=("Arial",20))
entrada_tentativa.pack()

btn_adivinhar = tk.Button(app, text="Adivinhar", command=jogo_adivinhacao, state=tk.DISABLED, bg='pink', fg='white',font=("Arial",20))
btn_adivinhar.pack()

btn_iniciar = tk.Button(app, text="Iniciar Jogo", command=iniciar_jogo, bg='pink', fg='white',font=("Arial",20))
btn_iniciar.pack()

#resultado()

pygame.mixer.init()  # Inicializa o mixer do pygame para reproduzir áudio

app.mainloop()