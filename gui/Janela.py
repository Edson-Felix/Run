import tkinter as tk


class Janela:
    def __init__(self, titulo, largura, altura):
        self.janela = tk.Tk()
        self.janela.title(titulo)
        self.janela["width"] = largura
        self.janela["height"] = altura
        self.janela.resizable(width=False, height=False)
        # centralizando
        ws = self.janela.winfo_screenwidth()
        hs = self.janela.winfo_screenheight()
        posx = (ws / 2) - (largura / 2)
        posy = (hs / 2) - (altura / 2)
        self.janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
