import tkinter as tk

# Funções
def jogar(linha, coluna):
    global jogo_ativo, turno, vencedor

    if jogo_ativo and tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = turno
        jogadas.append((linha, coluna))

        # Verificar vencedor
        vencedor = verificar_vencedor()

        # Atualizar interface
        desenhar_tabuleiro()

        if vencedor or len(jogadas) == 9:
            jogo_ativo = False
            mensagem_fim_jogo()

        # Trocar turno
        turno = "X" if turno == "O" else "O"

def verificar_vencedor():
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != " ":
            return tabuleiro[linha][0]
        if tabuleiro[0][linha] == tabuleiro[1][linha] == tabuleiro[2][linha] != " ":
            return tabuleiro[0][linha]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    return None

def desenhar_tabuleiro():
    for linha in range(3):
        for coluna in range(3):
            cor = 'white'  # Cor padrão para espaços em branco
            if tabuleiro[linha][coluna] == "X":
                cor = 'blue'
            elif tabuleiro[linha][coluna] == "O":
                cor = 'red'
                
            canvas.create_rectangle(
                coluna * 100 + 10,
                linha * 100 + 10,
                (coluna + 1) * 100 - 10,
                (linha + 1) * 100 - 10,
                fill=cor,
            )

def mensagem_fim_jogo():
    mensagem = "Empate!" if not vencedor else f"Vencedor: {vencedor}"
    label_fim_jogo.config(text=mensagem)

# Variáveis
jogo_ativo = True
turno = "X"
vencedor = None
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
jogadas = []

# Janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")

# Canvas
canvas = tk.Canvas(janela, width=300, height=300)
canvas.grid(row=0, column=0, columnspan=3)

# Botões
for linha in range(3):
    for coluna in range(3):
        botao = tk.Button(
            janela,
            text=" ",
            width=3,
            height=2,
            command=lambda linha=linha, coluna=coluna: jogar(linha, coluna),
        )
        botao.grid(row=linha+1, column=coluna, padx=5, pady=5)

# Label para mensagem de fim de jogo
label_fim_jogo = tk.Label(janela, text="")
label_fim_jogo.grid(row=4, column=0, columnspan=3)

# Desenhar tabuleiro inicial
desenhar_tabuleiro()

# Iniciar loop principal
janela.mainloop()
