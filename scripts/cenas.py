import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto
from scripts.interfaces import Botao


class Partida:

    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"

    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()
        self.cano.desenhar()

        return self.estado
    
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela,"FlappyBird",100,20,(255,255,255),50)
        self.estado = "menu"
        self.botao_jogar = Botao(tela,"jogar",100,100,50(200,0,0),(255,255,255))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado