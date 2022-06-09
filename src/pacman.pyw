import pygame
from abc import ABCMeta, abstractmethod
import random
import time
import Highscore
import login

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("Pacman")
font = pygame.font.SysFont("arial", 20, True, False)


AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
LARANJA = (255, 140, 0)
ROSA = (255, 15, 192)
CIANO = (0, 255, 255)
VELOCIDADE = 1
ACIMA = 1
ABAIXO = 2
DIREITA = 3
ESQUERDA = 4

nomeUsuario = ''

global matrizMapa
matrizMapa = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass

    @abstractmethod
    def esquina(self, direcoes):
        pass


class Cenario(ElementoJogo):
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.moviveis = []
        self.pontos = 0
        # Estados possiveis 0-Jogando 1-Pausado 2-GameOver  3-Vitoria
        self.estado = 0
        self.tamanho = tamanho
        self.vidas = 5
        self.matriz = matrizMapa

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)

    def pintar_score(self, tela):
        pontos_x = self.tamanho * 30
        pontos_img = font.render("Score {}".format(self.pontos), True, AMARELO)
        vidas_img = font.render("Vidas {}".format(self.vidas), True, AMARELO)
        highscore_img = font.render("Highscore".format(self.vidas), True, AMARELO)
        listaTop10 = []
        cont = 0
        for score in Highscore.top10("Pacman"):
            tela.blit(font.render(score[0] + " " + score[1] + " " + score[2], True, AMARELO), (pontos_x, 150 + 25 * cont))
            cont += 1

        scoreUsuario = Highscore.buscaScore("Pacman", nomeUsuario)
        if scoreUsuario != []:
            tela.blit(font.render(scoreUsuario[0] + " " + scoreUsuario[1] + " " + scoreUsuario[2], True, AMARELO), (pontos_x, 430))
        tela.blit(highscore_img, (pontos_x, 120))
        tela.blit(pontos_img, (pontos_x, 50))
        tela.blit(vidas_img, (pontos_x, 74))

    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + half, y + half),
                                   self.tamanho // 10, 0)

    def pintar(self, tela):
        if self.estado == 0:
            self.pintar_jogando(tela)
        elif self.estado == 1:
            self.pintar_jogando(tela)
            self.pintar_pausado(tela)
        elif self.estado == 2:
            self.pintar_jogando(tela)
            self.pintar_gameover(tela)
        elif self.estado == 3:
            self.pintar_jogando(tela)
            self.pintar_vitoria(tela)

    def pintar_texto_centro(self, tela, texto):
        texto_img = font.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))

    def pintar_vitoria(self, tela):
        self.pintar_texto_centro(tela, "P A R A B E N S  V O C E  V E N C E U  ! ! !")

    def pintar_gameover(self, tela):
        self.pintar_texto_centro(tela, "G A M E   O V E R")

    def pintar_pausado(self, tela):
        self.pintar_texto_centro(tela, "P A U S A D Os")

    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_score(tela)

    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(ACIMA)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(ABAIXO)
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)
        return direcoes

    def calcular_regras(self):
        if self.estado == 0:
            self.calcular_regras_jogando()
        elif self.estado == 1:
            self.calcular_regras_pausado()
        elif self.estado == 2:
            self.calcular_regras_gameover()

    def calcular_regras_gameover(self):
        pass

    def calcular_regras_pausado(self):
        pass

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao)
            direcoes = self.get_direcoes(lin, col)
            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and movivel.linha == self.pacman.linha and \
                    movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <= 0:
                    Highscore.insereScore("Pacman", nomeUsuario, str(self.pontos))
                    self.estado = 2
                else:
                    self.pacman.linha = 1
                    self.pacman.coluna = 1
            else:
                if 0 <= col_intencao < 28 and 0 <= lin_intencao < 29 and \
                        self.matriz[lin_intencao][col_intencao] != 2:
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                        self.pontos += 1
                        self.matriz[lin][col] = 0
                        if self.pontos >= 306:
                            Highscore.insereScore("Pacman", nomeUsuario, str(self.pontos + 100 * self.vidas))
                            self.estado = 3
                else:
                    movivel.recusar_movimento(direcoes)

    def processar_eventos(self, evts):
        for e in evts:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == 0:
                        self.estado = 1
                    elif self.estado == 1:
                        self.estado = 0
                    elif self.estado == 2 or self.estado == 3:
                        
                        self.pacman.linha = 1
                        self.pacman.coluna = 1
                        self.vidas = 5
                        self.pontos = 0
                        self.estado = 0
                        self.matriz = [
                                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                                        [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
                                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                                    ]
                        
                        
                        self.moviveis.pop(4)
                        self.moviveis.pop(3)
                        self.moviveis.pop(2)
                        self.moviveis.pop(1)
                        gameLoop()

                        
                        



class Pacman(ElementoJogo, Movivel):
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho // 2
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.abertura = 0
        self.velocidade_abertura = 1

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def pintar(self, tela):
        # Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        self.abertura += self.velocidade_abertura
        if self.abertura > self.raio:
            self.velocidade_abertura = -1
        if self.abertura <= 0:
            self.velocidade_abertura = 1

        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.abertura)
        labio_inferior = (self.centro_x + self.raio, self.centro_y + self.abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna

    def esquina(self, direcoes):
        pass


class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 13.0
        self.linha = 15.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = ABAIXO
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x = int(px + fatia * 2.5)
        olho_e_y = int(py + fatia * 2.5)

        olho_d_x = int(px + fatia * 5.5)
        olho_d_y = int(py + fatia * 2.5)

        pygame.draw.circle(tela, BRANCO, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y), olho_raio_int, 0)
        pygame.draw.circle(tela, BRANCO, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y), olho_raio_int, 0)

    def calcular_regras(self):
        if self.direcao == ACIMA:
            self.linha_intencao -= self.velocidade
        elif self.direcao == ABAIXO:
            self.linha_intencao += self.velocidade
        elif self.direcao == ESQUERDA:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == DIREITA:
            self.coluna_intencao += self.velocidade

    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)

    def processar_eventos(self, evts):
        pass


def digitandoLogin(coord_x, coord_y, listaRender, modo):
    stringDigitada = ''
    clock = pygame.time.Clock()
    listaRender.append([])
    if modo == "senha":
        modoAsterisco = True
    else:
        modoAsterisco = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                break
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE and modo == "senha":
                    modoAsterisco = not modoAsterisco
                if evento.key == pygame.K_BACKSPACE:
                    stringDigitada = stringDigitada[:-1]
                digUnicode = str(evento.unicode)
                if ' '<=digUnicode<='~' and digUnicode != " ":
                    stringDigitada += digUnicode

                if not modoAsterisco:
                    Digitacao_img = font.render(stringDigitada, True, BRANCO)
                else:
                    Digitacao_img = font.render(len(stringDigitada) * "*", True, BRANCO)
                listaRender[-1] = [Digitacao_img, (coord_x, coord_y)]
                if evento.key == pygame.K_RETURN:
                    return stringDigitada

        screen.fill(PRETO)
        for elementoRender in listaRender:
            if elementoRender != []:
                screen.blit(elementoRender[0], elementoRender[1])
        
        pygame.display.flip()
        clock.tick(30)

def telaLogin():
    clock = pygame.time.Clock()
    coord_x = 20
    loginInicio_img = font.render("Voce ja possui login? Pressione Y/N", True, BRANCO)
    listaRender = [[loginInicio_img, (coord_x, 20)]]
    done = False
    tipoLogin = 0
    digitandoCoords = -1
    loginEnter = 0
    flagLoginInicial = False
    listaLogin = []
    while not done:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True
                pygame.quit()
                break
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_y:
                    flagLoginInicial = True
                    tipoLogin = 1
                    login_img = font.render("LOGIN:", True, BRANCO)
                    listaRender.append([login_img, (coord_x, 20)])
                    digitandoCoords = [coord_x, 45, "login"]
                elif evento.key == pygame.K_n:
                    flagLoginInicial = True
                    tipoLogin = 2
                    loginNovo_img = font.render("LOGIN NOVO:", True, BRANCO)
                    listaRender.append([loginNovo_img, (coord_x, 20)])
                    digitandoCoords = [coord_x, 45, "login"]

        if loginEnter == 1:
            if tipoLogin == 1:
                login_img = font.render("SENHA: (ESC para exibir)", True, BRANCO)
                listaRender.append([login_img, (coord_x, 90)])
                digitandoCoords = [coord_x, 115, "senha"]
            if tipoLogin == 2:
                login_img = font.render("SENHA NOVA: (ESC para exibir)", True, BRANCO)
                listaRender.append([login_img, (coord_x, 90)])
                digitandoCoords = [coord_x, 115, "senha"]
                
        screen.fill(PRETO)
        if flagLoginInicial == True:
            listaRender.pop(0)
            flagLoginInicial = False

        for elementoRender in listaRender:
            screen.blit(elementoRender[0], elementoRender[1])

        if digitandoCoords != -1:
            listaLogin.append(digitandoLogin(digitandoCoords[0], digitandoCoords[1] ,listaRender, digitandoCoords[2]))
            if len(listaLogin) == 2:
                if tipoLogin == 1:
                    ##VERIFICAR LOGIN E RETORNAR listaLogin[0]
                    if login.check_user(listaLogin[0], listaLogin[1]):
                        return listaLogin[0]
                    else:
                        return telaLogin()
                elif tipoLogin == 2:
                    ##REGISTRAR LOGIN E RETORNAR listaLogin[0]
                    if not login.check_username_duplicity(listaLogin[0]):
                        login.save_user(listaLogin[0], listaLogin[1])
                        return listaLogin[0]
                    else:
                        login_img = font.render("Nome de usuario ja em uso", True, VERMELHO)
                        screen.blit(login_img, (coord_x, 160))
                        pygame.display.flip()
                        time.sleep(3)
                        return telaLogin()

            loginEnter = 1
            digitandoCoords = -1

        pygame.display.flip()
        clock.tick(30)
            

def gameLoop():
    blinky = Fantasma(VERMELHO, size)
    inky = Fantasma(CIANO, size)
    clyde = Fantasma(LARANJA, size)
    pinky = Fantasma(ROSA, size)
                        
    cenario.moviveis.append(blinky)
    cenario.moviveis.append(inky)
    cenario.moviveis.append(clyde)
    cenario.moviveis.append(pinky)
                        
    while True:

        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

                                # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        blinky.pintar(screen)
        inky.pintar(screen)
        clyde.pintar(screen)
        pinky.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

                                # Captura os eventos
        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)




if __name__ == "__main__":
    size = 600 // 30

    nomeUsuario = telaLogin()
    
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)
    cenario.adicionar_movivel(pacman)

    gameLoop()
