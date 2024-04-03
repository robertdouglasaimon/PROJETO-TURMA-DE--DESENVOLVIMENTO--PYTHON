from  tkinter import *
from datetime import datetime

cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

janela = Tk()
janela.title("")
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

def atualizar_relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l2.config(text=f"{dia_semana}\u00a0 {dia}/{mes}/{ano}")

    l1.after(200, atualizar_relogio)

l1 = Label(janela, text="11:50:05", font=('Arial', 80), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=(5, 10))

l2 = Label (janela, font=('Arial', 20), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=(5,  10))

atualizar_relogio()

janela.mainloop()







'''
Explicando o código linha por linha:

PARTE 1 - 

from tkinter import *
from datetime import datetime

Nesta parte, estamos importando dois módulos: tkinter e datetime. O tkinter é uma biblioteca gráfica para Python que nos permite criar interfaces gráficas de usuário (GUI), enquanto datetime é usado para trabalhar com objetos de data e hora em Python.


PARTE 2 -

cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

Essas linhas definem algumas variáveis para cores. Isso é útil para garantir que a interface gráfica tenha uma aparência consistente e agradável. É tipo o root:: do JS, só que mais simples e menos burocrático KKKKK'



PARTE 3 -

janela = Tk()
janela.title("")
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

Aqui, estamos criando uma instância da classe Tk, que representa a janela principal da nossa aplicação GUI. Em seguida, estamos configurando algumas propriedades da janela, como título, tamanho e cor de fundo.



PARTE 4 -

def atualizar_relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l2.config(text=f"{dia_semana}\u00a0 {dia}/{mes}/{ano}")

    l1.after(200, atualizar_relogio)

Essa é uma função chamada atualizar_relogio(), que atualiza o relógio na interface gráfica. Ela obtém a hora atual usando datetime.now() e formata-a em uma string com o formato de hora desejado. Em seguida, atualiza o texto dos Labels l1 e l2 com a hora e a data formatadas. A função é chamada novamente após 200 milissegundos usando l1.after() para manter o relógio atualizado periodicamente.



PARTE 5 -

l1 = Label(janela, text="11:50:05", font=('Arial', 80), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, font=('Arial', 20), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)
Aqui, estamos criando dois Labels (l1 e l2) para exibir a hora e a data na interface gráfica. l1 exibe a hora atual com um tamanho de fonte grande, enquanto l2 exibe o dia da semana, dia, mês e ano com uma fonte menor. Eles são colocados na janela usando o método grid() para organizá-los em uma grade.



PARTE 6 - 

atualizar_relogio()
Chamamos a função atualizar_relogio() uma vez para iniciar o relógio.


PARTE 7 - FIM

janela.mainloop()

Finalmente, chamamos o método mainloop() para iniciar o loop principal da interface gráfica, que mantém a janela aberta e responde às interações do usuário até que a janela seja fechada.

'''
