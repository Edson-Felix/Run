from random import randint
from threading import Thread
from time import sleep

from gui import Jogo
from pontos.Ponto import Ponto


class Vermelho(Ponto, Thread):

    def __init__(self, posx, posy, preto):
        super().__init__(posx, posy)
        self.preto = preto

    def run(self):
        sleep(0.5)
        c = 0
        while Jogo.rodando:
            passo = 5
            vel = 0.035
            if abs(self.posy - self.preto.posy) < 10:
                if self.posx < self.preto.posx:
                    self.posx += passo
                    sleep(vel)
                if self.posx > self.preto.posx:
                    self.posx -= passo
                    sleep(vel)

            elif abs(self.posx - self.preto.posx) < 10:
                if self.posy < self.preto.posy:
                    self.posy += passo
                    sleep(vel)
                if self.posy > self.preto.posy:
                    self.posy -= passo
                    sleep(vel)

            else:
                sleep(0.06)
                if self.posx < 540 and self.posy == 50:
                    self.posx += passo

                elif self.posx == 540 and self.posy < 340:
                    self.posy += passo

                elif self.posx > 50 and self.posy == 340:
                    self.posx -= passo

                elif self.posx == 50 and self.posy > 50:
                    self.posy -= passo

                else:
                    if c % 6 == 0:
                        mv = randint(1, 4)
                    sleep(0.06)
                    if mv == 1 and self.posx < 590:
                        self.posx += passo

                    elif mv == 2 and self.posy < 390:
                        self.posy += passo

                    elif mv == 3 and self.posx > 0:
                        self.posx -= passo

                    elif mv == 4 and self.posy > 0:
                        self.posy -= passo

                    c += 1
