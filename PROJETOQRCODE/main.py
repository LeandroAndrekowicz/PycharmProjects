from tkinter import *
from tkinter import messagebox
import pyqrcode

janela = Tk()
janela.title("Conversor de QRCODE")
janela.config(bg='#4682B4')


def gerador():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showwarning('', 'Digite algo na caixa de texto')
    try:
        imagem()
    except:
        pass


def imagem():
    img_lbl.config(image=img)
    output.config(text="Link Convertido: " + user_input.get())


lbl = Label(janela, text="Digite o link que deseja converter", bg='#4682B4')
lbl.pack()

user_input = StringVar()
entry = Entry(janela, textvariable=user_input)
entry.pack(padx=10)

button = Button(janela, text="Converter", width=15, command=gerador)
button.pack(pady=10)

img_lbl = Label(janela, bg='#4682B4')
img_lbl.pack()
output = Label(janela, text="", bg='#4682B4')
output.pack()

janela.mainloop()