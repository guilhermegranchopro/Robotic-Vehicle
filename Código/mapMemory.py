"""Ficheiro que contém a classe que é usada para trabalhar com o robô"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""

from math import *  # importa o modulo math para fazer calculos usando funções matematicas
from time import *  # importa o modulo time para parar o funcionamento do programa durante um determinado tempo

# função que calcula se o robô chocou contra alguma barreira ou não
def freeToPass(x, y, mapM, minX, maxX, minY, maxY):
    valid = True  # boolean inicializado como se o robô não estivesse a chocar em nada
    n = mapM.numberOfWalls()  # o numero de obstaculos no mapa é guaradado na variavel 'n'
    information = mapM.wallsReturn()  # a informação do raio e do centro geometrico é guardado num formato de lista na variavel 'information'

    if not (minX + 3.5 < x < maxX - 3.5 and minY + 3.5 < y < maxY - 3.5):  # se o robô atingiu os limites do mapa
        valid = False  # o boolean mostra que o robô não pode continuar nessa direção/sentido
    else:  # se o robô não atingiu os limites do mapa
        for a in range(n):  # loop que corre o numero de vezes igual ao numero de obstaculos no mapa
            center = information[a][0]  # a variavel 'center' guarda a o centro geometrico de um obstaculo
            centerX = center.getX()  # retira o X das coordenadas do centro geometrico
            centerY = center.getY()  # retira o Y das coordenadas do centro geometrico
            ray = information[a][1]  # a variavel 'ray' guarda a o raio geometrico de um obstaculo
            distance = ((centerX - x) ** 2 + (centerY - y) ** 2) ** 0.5  # calcula a distância do centro do robô ao centro geometrico do obstaculo
            if distance <= ray + 3.5:  # se a distancia for menor ou igual ao raio geometrico do obstaculo mais 3.5 (3 é o raio do robô)
                valid = False  # o boolean mostra que o robô não pode continuar nessa direção/sentido

    return valid  # devolve o boolen que indica que se o robô chocou ou não com um obstaculo

# função para saber o ângulo da direção e sentido que o robô deve seguir
def angleFinder(X,Y,x,y):
    if X - x == 0:  # se o robô estiver perfeitamente alinhado com o caminho que deve de seguir no eixo dos X
        Angle = pi/2  # angulo igual a pi/2
    else:  # se o robô não estiver perfeitamente alinhado com o caminho que deve de seguir no eixo dos X
        Angle = atan((Y - y) / (X - x))  # angulo para o qual o robô tem de se direcionar para encontrar o objetivo

    if ((Y - y) > 0 and (X - x) < 0) or ((Y - y) < 0 and (X - x) < 0) or (Y - y == 0 and X - x < 0) or (X - x == 0 and Y - y < 0):  # ajuste no angulo calculado anteriormente de forma ao robô saber o sentido que tem de seguir já que a direção já foi estabelecida anteriormente (estes ajustes são necessarios devido ás proprias caracteristicas da função arcotangente)
            Angle = Angle + pi  # muda o sentido inicial

    return Angle  # retorna o angulo que o robô deve seguir

# função para o robô encontarar os objetivos no mapa
def goalFinder(mapM, bot, listOfObjectives, a):
    if mapM.objectivesReturn():  # se existirem objetivos no mapa
        end = 0  # ainda existem objetivos no mapa
        information = mapM.objectivesReturn()  # variavel que guarda a informação sobre os objetivos no mapa
        x, y = bot.returnPosition()  # as variaveis guardam as coordenadas da posição do robô
        center = information[0][0]  # variavel que guarda o centro geometrico do objetivo
        X, Y = center.getX(), center.getY()  # coordenadas x e y do centro geometrico do objetivo
        if abs(X - x) <= 0.4 and abs(Y - y) <= 0.4:  # se o robô já estiver aproximadamente no centro do objetivo
            sleep(3)  # o programa para durante 3 segundos
            del information[0]  # apaga a informação sobre o objetivo já apanhado
            mapM.redefineObjectives(information)  # atualiza a informação sobre os objetivos ainda existentes
            listOfObjectives[a].undraw()  # apaga o objetivo do mapa
            a = a + 1  # passa para o próximo objetivo
            goalAngle = 0  #
        else:  # se o robô ainda não estiver no objetivo
            goalAngle = angleFinder(X, Y, x, y)  # retorna o angulo que o robô deve seguir
    else:  # se não existirem objetivos no mapa
        end = 1  # já não existem objetivos no mapa
        goalAngle = 0  # o angulo para que o robô tem de se virar para encontrar objetivos agora é irrelevante
    return goalAngle, end, a  # retorna o angulo que o robô tem de se virar para encontar, se ainda existem objetivos e qual o proximo objetivo do robô

# função para encontarar as bases do robô
def baseFinder(bot, proportion):
    exitBot = False  # boolean que registar se o robô já encontrou a base ou não
    x, y = bot.returnPosition()  # guarda a posição do robô em coordenadas x e y
    distance1 = (((x - proportion - 7) ** 2 + (y - 7) ** 2) ** 0.5)  # distância à base 1 do robô
    distance2 = (((x - 8) ** 2 + (y - 93) ** 2) ** 0.5)  # distância à base 2 do robô

    if (abs(proportion - 7 - x) <= 0.4 and abs(7 - y) <= 0.4) or (abs(8 - x) <= 0.4 and abs(93 - y) <= 0.4):  # se o robô já estiver aproximadamente no centro da base
        exitBot = True  # o robô já chegou à base
        baseAngle = 0  # retorna o angulo que o robô deve seguir
    else:  # se o robô ainda não estiver numa das bases
        if distance1 > distance2:  # se a distancia à base 1 do robô for maior que a de á base 2
            baseAngle = angleFinder(8, 93, x, y)  # retorna o angulo que o robô deve seguir
        else:  # se a distancia à base 1 do robô não for maior que a de á base 2
            baseAngle = angleFinder(proportion - 7, 7, x, y)  # retorna o angulo que o robô deve seguir

    return baseAngle, exitBot  # retorna o angulo que o robô tem de seguir para chegar à base e se ele já chegou à base ou não

# classe que tem diversos metodos para trabalhar com o mapa de objetivos e obstaculos criado
class mapMemory:

    def __init__(self):  # metodo que inicializa a classe
        self.walls = []  # inicializa a variavel que vai registrar a posição dos obstaculos
        self.objectives = []  # inicializa a variavel que vai registrar a posição dos objetivos

    def wallsReturn(self):  # retorna a informação sobre os obstaculos do mapa
        return self.walls

    def objectivesReturn(self):  # retorna a informação sobre os objetivos do mapa
        return self.objectives

    def addWalls(self, center, ray):  # adiciona obstaculos ao mapa
        information = [center, ray]  # adiciona a informação em formato de uma varivael lista com o centro geometrico e o raio do obstaculo
        self.walls.append(information)

    def addObjectives(self, center, ray):  # adiciona objetivos ao mapa
        information = [center, ray]  # adiciona a informação em formato de uma varivael lista com o centro geometrico e o raio do objetivos
        self.objectives.append(information)

    def redefineObjectives(self, information):  # redefine a informação sobre os objetivos do mapa
        self.objectives = information

    def cleanObjectives(self):  # limpa a informação sobre os objetivos do mapa
        self.objectives = []

    def numberOfWalls(self):  # retorna o numero de obstaculos do mapa
        return len(self.walls)

    def numberOfObjectives(self):  # retorna o numero de objetivos do mapa
        return len(self.objectives)
