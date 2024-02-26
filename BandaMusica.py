import random

class Musica:
    def __init__(self,ins):
        self.instrumento = ins

    def afinar_instrumento(self):
        self.instrumento.afinar()