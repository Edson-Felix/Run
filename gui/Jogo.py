import tkinter as tk
from random import randint
from tkinter import messagebox
from threading import Thread
from time import sleep

import gui
from pontos.Amarelo import Amarelo
from pontos.Preto import Preto
from pontos.Vermelho import Vermelho

'''TO DO:
 - Transformar pontos vermelhos em lista
 - Mudar qnt inicial de pts vermelhos para 2
 - A cada 5 pts add um pnt vermelho
 '''


rodando = True


class Jogo(tk.Frame, Thread):

    def __init__(self, master):
        super().__init__(master)
        Thread.__init__(self)
        self.master = master
        self.criar_widgets()
        self.place(width=self.master["width"], height=self.master["height"])
        self.start()

    def criar_widgets(self):
        self.ctn_geral = tk.Frame(master=self, bg='grey', width=self.master["width"], height=self.master["height"])
        self.ctn_bts = tk.Frame(master=self.ctn_geral, bg='grey')

        self.lbl_ponto_preto = tk.Label(master=self.ctn_geral, bg='black', width=10, height=10)
        self.ponto_preto = Preto(self.lbl_ponto_preto.master["width"]/2, self.lbl_ponto_preto.master["height"]/2)
        self.lbl_ponto_preto.place(width=self.lbl_ponto_preto["width"], height=self.lbl_ponto_preto["height"], x=self.ponto_preto.posx, y=self.ponto_preto.posy)

        self.lbl_ponto_vermelho1 = tk.Label(master=self.ctn_geral, bg='red', width=10, height=10)
        self.ponto_vermelho1 = Vermelho(50, 50, self.ponto_preto)
        self.lbl_ponto_vermelho1.place(width=self.lbl_ponto_vermelho1["width"], height=self.lbl_ponto_vermelho1["height"], x=self.ponto_vermelho1.posx, y=self.ponto_vermelho1.posy)

        self.lbl_ponto_vermelho2 = tk.Label(master=self.ctn_geral, bg='red', width=10, height=10)
        self.ponto_vermelho2 = Vermelho(540, 50, self.ponto_preto)
        self.lbl_ponto_vermelho2.place(width=self.lbl_ponto_vermelho2["width"], height=self.lbl_ponto_vermelho2["height"], x=self.ponto_vermelho2.posx, y=self.ponto_vermelho2.posy)

        self.lbl_ponto_vermelho3 = tk.Label(master=self.ctn_geral, bg='red', width=10, height=10)
        self.ponto_vermelho3 = Vermelho(540, 340, self.ponto_preto)
        self.lbl_ponto_vermelho3.place(width=self.lbl_ponto_vermelho3["width"], height=self.lbl_ponto_vermelho3["height"], x=self.ponto_vermelho3.posx, y=self.ponto_vermelho3.posy)

        self.lbl_ponto_vermelho4 = tk.Label(master=self.ctn_geral, bg='red', width=10, height=10)
        self.ponto_vermelho4 = Vermelho(50, 340, self.ponto_preto)
        self.lbl_ponto_vermelho4.place(width=self.lbl_ponto_vermelho4["width"], height=self.lbl_ponto_vermelho4["height"], x=self.ponto_vermelho4.posx, y=self.ponto_vermelho4.posy)

        self.lbl_ponto_amarelo = tk.Label(master=self.ctn_geral, bg='yellow', width=10, height=10)
        self.ponto_amarelo = Amarelo(290, 50, self.ponto_preto)
        self.lbl_ponto_amarelo.place(width=self.lbl_ponto_amarelo["width"], height=self.lbl_ponto_amarelo["height"], x=self.ponto_amarelo.posx, y=self.ponto_amarelo.posy)

        self.score = 0
        self.lbl_score = tk.Label(master=self.ctn_geral, text="Score: " + str(self.score))
        self.lbl_score.place(x=0, y=0)

        tamx_bts, tamy_bts = 40, 40
        self.bt_cima     = tk.Button(master=self.ctn_bts, text='W '+u'\u2191', command=lambda : self.mover('c'), width=tamx_bts, height=tamy_bts)
        self.bt_baixo    = tk.Button(master=self.ctn_bts, text='S\n'+u'\u2193', command=lambda : self.mover('b'), width=tamx_bts, height=tamy_bts)
        self.bt_esquerda = tk.Button(master=self.ctn_bts, text='A\n'+u'\u2190', command=lambda : self.mover('e'), width=tamx_bts, height=tamy_bts)
        self.bt_direita  = tk.Button(master=self.ctn_bts, text='D\n'+u'\u2192', command=lambda : self.mover('d'), width=tamx_bts, height=tamy_bts)

        self.bt_cima.place(width=self.bt_cima["width"], height=self.bt_cima["height"], x=3*tamx_bts/2-tamx_bts/2, y=0)
        self.bt_baixo.place(width=self.bt_baixo["width"], height=self.bt_baixo["height"], x=tamx_bts, y=tamy_bts)
        self.bt_esquerda.place(width=self.bt_esquerda["width"], height=self.bt_esquerda["height"], x=0, y=tamy_bts)
        self.bt_direita.place(width=self.bt_direita["width"], height=self.bt_direita["height"], x=2*tamx_bts, y=tamy_bts)

        self.ctn_bts.place(width=3*tamx_bts, height=2*tamy_bts, x=self.ctn_bts.master["width"]-3*tamx_bts, y=self.ctn_bts.master["height"]-2*tamy_bts)
        self.ctn_geral.place(width=self.ctn_geral["width"], height=self.ctn_geral["height"])

    def mover(self, op):
        if Jogo.rodando:
            if op == 'c':
                self.ponto_preto.posy -= 10
            elif op == 'b':
                self.ponto_preto.posy += 10
            elif op == 'e':
                self.ponto_preto.posx -= 10
            elif op == 'd':
                self.ponto_preto.posx += 10

            self.lbl_ponto_preto.place(width=self.lbl_ponto_preto["width"], height=self.lbl_ponto_preto["height"],
                                       x=self.ponto_preto.posx, y=self.ponto_preto.posy)

    def run(self):
        nao_perdeu = True
        while nao_perdeu and rodando:
            sleep(0.00001)
            try:
                self.lbl_ponto_preto.place(width=self.lbl_ponto_preto["width"], height=self.lbl_ponto_preto["height"],
                                           x=self.ponto_preto.posx, y=self.ponto_preto.posy)

                self.lbl_ponto_vermelho1.place(width=self.lbl_ponto_vermelho1["width"],
                                               height=self.lbl_ponto_vermelho1["height"], x=self.ponto_vermelho1.posx,
                                               y=self.ponto_vermelho1.posy)

                self.lbl_ponto_vermelho2.place(width=self.lbl_ponto_vermelho2["width"],
                                               height=self.lbl_ponto_vermelho2["height"], x=self.ponto_vermelho2.posx,
                                               y=self.ponto_vermelho2.posy)

                self.lbl_ponto_vermelho3.place(width=self.lbl_ponto_vermelho3["width"],
                                               height=self.lbl_ponto_vermelho3["height"], x=self.ponto_vermelho3.posx,
                                               y=self.ponto_vermelho3.posy)

                self.lbl_ponto_vermelho4.place(width=self.lbl_ponto_vermelho4["width"],
                                               height=self.lbl_ponto_vermelho4["height"], x=self.ponto_vermelho4.posx,
                                               y=self.ponto_vermelho4.posy)
                if self.lbl_ponto_amarelo:
                    self.lbl_ponto_amarelo.place(width=self.lbl_ponto_amarelo["width"],
                                                 height=self.lbl_ponto_amarelo["height"], x=self.ponto_amarelo.posx,
                                                 y=self.ponto_amarelo.posy)

                if (abs(self.ponto_preto.posx-self.ponto_vermelho1.posx) < 10 and abs(self.ponto_preto.posy-self.ponto_vermelho1.posy) < 10) or \
                   (abs(self.ponto_preto.posx-self.ponto_vermelho2.posx) < 10 and abs(self.ponto_preto.posy-self.ponto_vermelho2.posy) < 10) or \
                   (abs(self.ponto_preto.posx-self.ponto_vermelho3.posx) < 10 and abs(self.ponto_preto.posy-self.ponto_vermelho3.posy) < 10) or \
                   (abs(self.ponto_preto.posx-self.ponto_vermelho4.posx) < 10 and abs(self.ponto_preto.posy-self.ponto_vermelho4.posy) < 10):
                    Jogo.rodando = False
                    if nao_perdeu:
                        nao_perdeu = tk.messagebox.askyesno("Run!", "Perdeu!\nScore: " + str(self.score) + "\n\nJogar Novamente?")
                        Jogo.rodando = nao_perdeu
                        if nao_perdeu:
                            self.criar_widgets()
                        else:
                            Jogo.rodando = False

                if abs(self.ponto_preto.posx - self.ponto_amarelo.posx) < 10 and abs(self.ponto_preto.posy - self.ponto_amarelo.posy) < 10:
                    self.score += 1
                    self.lbl_score = tk.Label(master=self.ctn_geral, text="Score: " + str(self.score))
                    self.lbl_score.place(x=0, y=0)
                    self.lbl_ponto_amarelo["bg"] = 'gray'
                    self.ponto_amarelo.parar()
                    self.ponto_amarelo = None
                    self.ponto_amarelo = Amarelo(randint(50, 540), randint(50, 340), self.ponto_preto)
                    self.lbl_ponto_amarelo["bg"] = 'yellow'
            except Exception as e:
                Jogo.rodando = False
                print(e)
                break
