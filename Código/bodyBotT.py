"""Ficheiro que contém as funções que inicião as diversas caracteristicas do robô"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""

from math import *  # importa o modulo math para utilizar algumas funções para calculos matematicos
from graphics import *  # importa o modulo graphics para trabalhar na janela gráfica criada
from mapMemory import *  # importa o ficheiro mapMemory para usar determinadas funções e metodos que permitem trabalahr com o mapa de obstaculos e objetivos criado


# função que desenha inicialmente a parte gráfica para a bateria do robô para a segunda implementação
def setBotBatery(win, x, y, number, color):
    batery = Text(Point(x, y),
                  number)  # utiliza o metodo do graphics, Text para desenhar graficamente o indicador de bateria
    batery.setStyle('bold')  # estilo de letra da bateria
    batery.setSize(18)  # tamanho de letra da bateria
    batery.setTextColor(color)  # cor de letra da bateria
    batery.draw(win)  # desenha o texto que indica a bateria com as especificações referidas

    return batery  # devolve a variavel grafica onde está o texto da bateria


# função que desenha inicialmente a parte gráfica do robô e das suas bases
def bodyForTheBot(win, x):
    base = Rectangle(Point(x - 2, 2), Point(x - 12,
                                            12))  # utiliza o metodo do graphics, Rectangle para desenhar graficamente a base do canto inferior direito
    base.setFill('Purple')  # cor da base
    base.draw(win)  # desenha a base com as especificações referidas

    base2 = Rectangle(Point(2, 98), Point(12, 88))  # utiliza o metodo do graphics, Rectangle para desenhar graficamente a base do canto superior esquerdo
    base2.setFill('Purple')  # cor da base
    base2.draw(win)  # desenha a base com as especificações referidas

    body = Circle(Point(x - 7, 7),
                  3)  # utiliza o metodo do graphics, Circle para desenhar graficamente o robô numa fase inicial
    body.setFill('Blue')  # cor do robô
    body.draw(win)  # desenha o robô com as especificações referidas

    return body  # devolve a variavel grafica onde está o corpo gráfico do robô


# função que faz o robô andar e girar para uma determinada direção direção
def run(body, bot, mapM, Angle, x, steps, secondImpmentation):
    stepX = 0.5 * cos(Angle)  # calcula a direção e a distância do proximo passo do robô no eixo do X
    stepY = 0.5 * sin(Angle)  # calcula a direção e a distância do proximo passo do robô no eixo do Y
    X, Y = bot.returnPosition()  # com o metodo returnPosition da classe Harve guardamos a posição do robô nas variaveis X e Y
    if freeToPass(X + stepX, Y + stepY, mapM, 2, x - 2, 2, 98):  # se for possivel dar o passo pretendido
        if secondImpmentation:  # se estivermos na segunda implemantação
            steps = steps + 1  # contar e atualizar o numero de passos que o robô já deu
        body.move(stepX, stepY)  # move-se o corpo gráfico do robô usando o modulo graphics
        bot.update(X + stepX, Y + stepY)  # a posição do robô atualiza-se tendo em conta o ultimo passo, usando a classe Harve
        valid = True  # variavel que guarda no formato de um boolean se o robô ando mesmo ou não
    else:  # se não for possivel dar o passo pretendido
        Angle = Angle + pi / 50  # o robô roda pi/50 para a esquerda
        valid = False  # variavel que guarda no formato de um boolean se o robô ando mesmo ou não

    return Angle, valid, steps  # a função devolve o angulo a que o robô se encontra apontado em radianos, se ele andou ou apenas rodou e o numero de passos que o robô já deu
