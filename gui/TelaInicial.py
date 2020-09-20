import tkinter as tk

from gui.Janela import Janela
from gui.Jogo import Jogo


class TelaInicial(tk.Frame):

    def __init__(self, master=Janela("Run!", 600, 400).janela):
        super().__init__(master)
        self.master = master
        self.criar_widgets()
        self.place(width=self.master["width"], height=self.master["height"])
        self.mainloop()

    def criar_widgets(self):
        self.ctn_geral = tk.Frame(master=self, bg='grey', width=self.master["width"], height=self.master["height"])
        self.ctn_central = tk.Frame(master=self.ctn_geral)

        tamx_bts, tamy_bts = 200, 60
        self.bt_jogar = tk.Button(master=self.ctn_central, text="JOGAR", command=self.go_telajogo, width=tamx_bts, height=tamy_bts)
        self.bt_sair = tk.Button(master=self.ctn_central, text="SAIR", command=self.master.destroy, width=tamx_bts, height=tamy_bts)

        self.bt_jogar.place(bordermode=tk.OUTSIDE, width=self.bt_jogar["width"], height=self.bt_jogar["height"], x=0, y=0*tamy_bts)
        self.bt_sair.place(bordermode=tk.OUTSIDE, width=self.bt_sair["width"], height=self.bt_sair["height"], x=0, y=1*tamy_bts)

        #                                                     *#bts                                                                                                   *#bts
        self.ctn_central.place(width=tamx_bts, height=tamy_bts*2, x=self.ctn_central.master["width"]/2 - tamx_bts/2, y=self.ctn_central.master["height"]/2 - (tamy_bts*2)/2)
        self.ctn_geral.place(width=self.ctn_geral["width"], height=self.ctn_geral["height"])

    def go_telajogo(self):
        self.destroy()
        Jogo(self.master)
