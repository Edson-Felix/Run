from threading import Thread
from time import sleep

from gui import Jogo
from pontos.Ponto import Ponto
import keyboard


class Preto(Ponto, Thread):
    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        
    def run(self):
        passo = 5
        intervalo = 0.04
        while Jogo.rodando:
            sleep(0.001)
            if keyboard.is_pressed('w') and not keyboard.is_pressed('s'):
                if self.posy > 0:
                    self.posy -= passo
                    sleep(intervalo)

            elif keyboard.is_pressed('s') and not keyboard.is_pressed('w'):
                if self.posy < 390:
                    self.posy += passo
                    sleep(intervalo)

            if keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
                if self.posx > 0:
                    self.posx -= passo
                    sleep(intervalo)

            elif keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
                if self.posx < 590:
                    self.posx += passo
                    sleep(intervalo)
