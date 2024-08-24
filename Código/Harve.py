"""Ficheiro que contém a classe que é usada para trabalhar com o robô"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""


# classe que coordena diversas operações do robô
class Harve:

    def __init__(self, position):  # metodo que inicia a classe Harve
        self.xpos = position.getX()  # recupera a coordenada X no momento da criação do robô
        self.ypos = position.getY()  # recupera a coordenada Y no momento da criação do robô
        self.angle = 0  # inicia o robô virado para a direção de 0 radianos

    def getAngle(self):  # metodo que retorna o angulo para o qual o robô se encontra direcionado
        return self.angle

    def update(self, X, Y):  # metodo que atualiza a posição do robô
        self.xpos = X  # atualiza o X das coordenadas
        self.ypos = Y  # atualiza o Y das coordenadas

    def returnPosition(self):  # metodo que retorna a posição do robô
        return self.xpos, self.ypos  # retorna o X e depois o Y das coordenadas
