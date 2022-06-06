import tkinter
from tkinter import *
import pyqrcode


def gerador():
    site = input("Digite o site que deseja criar um QRCode: ")
    url = pyqrcode.create(site)
    url.png("myqr.png", scale= 6)
    
def digiteSite():
    result = textExample.get(1.0, tk.END+"-1c")
    print(result)

janela = Tk()
janela.title("Gerador de QRCODE")

texto = Label(janela, text="Digite o site que deseja converter para QRCODE")
texto.grid(column=0, row=0)

botao = Button(janela, text="Converter", command=gerador)
botao = botao.grid(column=0, row=1)

textExample = tkinter.Text(janela, height=10)
textExample.pack()
btnRead = tkinter.Button(janela, height=1, width=10, text="Read", command=digiteSite)
btnRead.pack()

janela.mainloop()