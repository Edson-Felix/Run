from random import randint
from threading import Thread
from time import sleep

from gui import Jogo
from pontos.Ponto import Ponto


class Amarelo(Ponto, Thread):
    def __init__(self, posx, posy, preto):
        super().__init__(posx, posy)
        self.preto = preto
        self.rodando = True

    def run(self):
        sleep(0.5)
        c = 0
        while Jogo.rodando and self.rodando:
            passo = 5
            vel = 0.07
            if abs(self.posy - self.preto.posy) < 11:
                sleep(vel)
                if self.preto.posx > self.posx > 0:
                    self.posx -= passo

                if self.preto.posx < self.posx < 590:
                    self.posx += passo

            elif abs(self.posx - self.preto.posx) < 11:
                sleep(vel)
                if self.preto.posy > self.posy > 0:
                    self.posy -= passo
                if self.preto.posy < self.posy < 390:
                    self.posy += passo

            else:
                sleep(vel)
                if self.posx > 50 and self.posy == 50:
                    self.posx -= passo

                elif self.posy < 340 and self.posx == 50:
                    self.posy += passo

                elif self.posx < 540 and self.posy == 340:
                    self.posx += passo

                elif self.posy > 50 and self.posx == 540:
                    self.posy -= passo

                else:
                    if c % 6 == 0:
                        mv = randint(1, 4)
                    sleep(vel)
                    if mv == 1 and self.posx < 590:
                        self.posx += passo

                    elif mv == 2 and self.posy < 390:
                        self.posy += passo

                    elif mv == 3 and self.posx > 0:
                        self.posx -= passo

                    elif mv == 4 and self.posy > 0:
                        self.posy -= passo

                    c += 1

    def parar(self):
        self.rodando = False
