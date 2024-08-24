"""Ficheiro para lidar com todos os obstaculos incluindo a classe Tree"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""

from random import *  # importa o modulo random
from graphics import *  # importa o modulo graphics para trabalhar na janela gráfica criada
from mapMemory import *  # importa o ficheiro mapMemory para usar determinadas funções e metodos que permitem trabalahr com o mapa de obstaculos e objetivos criado

# função que valida se um obstaculo não é criado em cima de outro ou um objetivo não é colocado em cima de umo bstaculo
def validate(X1, Y1, xL, yL, r1):
    validate = True  # boolean inicializado como se os obstaculos não estivesse uns em cima dos outros ou nem o objetivo em cima do obstaculo

    for a in range(len(xL)):  # loop que corre o numero de vezes igual ao numero de obstaculos já criados
        distance = (((X1 - xL[a]) ** 2 + (Y1 - yL[a]) ** 2) ** 0.5)  # calcula a distancia entre o ponto onde se està a tentar colocar o objetivo/obstaculo e todos os obstaculos já criados
        if distance <= r1[a] + 3.4:  # se a distancia calculada for menor ou igual que 2 vezes o raio do obstaculo já existente (os obstaculos encontram-se padronizados para terem raio 3 ou estarem circunscritos num circulo de raio 3 e os objetivos têm raio 2 o que deixa 1 de espaço pra o robô se movimentar, visto que o robô tem raio 3)
            validate = False  # o boolean mostar que o objetivo/obstaculo que se está a tentar criar está em cima de um obstaculo já criado
            break  # quebra o loop

    return validate  # retorna o boolean que indica se o obstaculo/objetivo que se está a tenatr criar está em cima ou não de um obstaculo já criado

# classe usada para criar os obstaculos
class Tree:

    def __init__(self, center, radius, win, N, center2, typee, formate):  # metodo que inicializa a classe Tree
        self.Tree = None  # variavel que apenas será usada nos metodos seguintes
        self.radius = radius  # raio do obstaculo
        self.N = N  # numero do obstaculo
        self.type = typee  # tipo do obstaculo usado na terceira implementação bush/stone/grass
        self.format = formate  # formato do obstaculo usado na terceira implementação Circle/Rectangle
        self.win = win  # janela a qual os obstaculos pertencem
        self.center = center  # ponto importante para o desenho geometrico dos obstaculos
        self.center2 = center2  # caso seja um rectangulo o segundo ponto que define essa figura geometrica tendo em conta o graphics
        self.virtualRadius = (((center.getX() - center2.getX()) ** 2 + (center.getY() - center2.getY()) ** 2) ** 0.5) / 2  # raio da circunferencia que circunescreve os obstaculos retangulares
        self.objective = 'objective'  # variavel que apenas será usada nos metodos seguintes

    def draw1(self, mapM):  # metodo que desenha os obsatculos da primeira implemetação
        self.objective = Circle(self.center, self.radius)  # usa-se o metodo Circle do modulo graphics para desenhar os obstaculos
        mapM.addWalls(self.center, self.radius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
        self.objective.setFill('Green')  # cor dos obtaculos
        self.objective.draw(self.win)  # desenha os obstaculos

    def draw2(self, mapM):  # metodo que desenha os obsatculos da segunda implemetação
        if self.N != 0 and self.N != 1 and self.N != 2:  # se já foram desenhados os três tipos diferentes de obstaculos
            self.N = randint(0, 2)  # o estilo dos próximos obstaculos será aleatorio
        if self.N == 0:  # caso este seja o primeiro obstaculo
            self.Tree = Circle(self.center, self.radius)  # usa-se o metodo Circle do modulo graphics para desenhar os obstaculos
            mapM.addWalls(self.center, self.radius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            self.Tree.setFill('Green')  # cor dos obtaculos
        elif self.N == 1:  # caso este seja o segundo obstaculo
            self.Tree = Circle(self.center, 2)  # usa-se o metodo Circle do modulo graphics para desenhar os obstaculos
            mapM.addWalls(self.center, 2)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            self.Tree.setFill('Grey')  # cor dos obtaculos
        elif self.N == 2:  # caso este seja o terceiro obstaculo
            x1 = self.center.getX() + 3  # calculos necessarios para criar dois pontos para usar o metodo Rectangle do graphics apartir de apenas um ponto dado que funciona como centro do retangulo
            y1 = self.center.getY() + 3
            x2 = self.center.getX() - 3
            y2 = self.center.getY() - 3
            self.Tree = Rectangle(Point(x1, y1), Point(x2, y2))  # desenha os obstaculos usando o metodo Rectangle do graphics
            mapM.addWalls(self.center, 3)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            self.Tree.setFill('Green')  # cor dos obtaculos
        self.Tree.draw(self.win)  # desenha os obstaculos

    def draw3(self, mapM):  # metodo que desenha os obstaculos da terceira implemetação
        if self.type == 'Bush' or self.type == 'Grass':  # se a o typo de obstaculo for Grass/Bush
            if self.format == 'Rectangle':  # se a o formato de obstaculo for Rectangle
                self.Tree = Rectangle(self.center, self.center2)  # desenha os obstaculos usando o metodo Rectangle do graphics
                virtualCenter = Point((self.center.getX()+self.center2.getX())/2, (self.center.getY()+self.center2.getY())/2)  # calcula o centro geometrico do retângulo
                mapM.addWalls(virtualCenter, self.virtualRadius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            else:  # caso seja Circle
                self.Tree = Circle(self.center, self.radius)  # usa-se o metodo Circle do modulo graphics para desenhar os obstaculos
                mapM.addWalls(self.center, self.radius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            self.Tree.setFill('Green')  # cor dos obtaculos
        else:  # caso seja Stone
            if self.format == 'Rectangle':  # se a o formato de obstaculo for Rectangle
                virtualCenter = Point((self.center.getX() + self.center2.getX()) / 2, (self.center.getY() + self.center2.getY()) / 2)  # calcula o centro geometrico do retângulo
                self.Tree = Rectangle(self.center, self.center2)  # desenha os obstaculos usando o metodo Rectangle do graphics
                mapM.addWalls(virtualCenter, self.virtualRadius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            else:  # caso seja Circle
                self.Tree = Circle(self.center, self.radius)  # usa-se o metodo Circle do modulo graphics para desenhar os obstaculos
                mapM.addWalls(self.center, self.radius)  # adiciona os obstaculos à informação sobre o mapa regida pela classe mapMemory
            self.Tree.setFill('Gray')  # cor dos obtaculos
        self.Tree.draw(self.win)  # desenha os obstaculos
