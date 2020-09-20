from threading import Thread


class Ponto(Thread):
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        Thread.__init__(self)
        self.start()
