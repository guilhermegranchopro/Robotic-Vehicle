"""Ficheiro que contém todas as funções destinadas a lidar diretamente com todas as implementações"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""

from mapMemory import *  # importa o ficheiro mapMemory para usar determinadas funções e metodos que permitem trabalahr com o mapa de obstaculos e objetivos criado
from graphics import *  # importa o modulo graphics para trabalhar na janela gráfica criada
from random import *  # importa o modulo random
from Tree import *  # importa o ficheiro Tree para criar os obstaculos do mapa
from time import *  # importa o modulo time para parar o funcionamento do programa durante um determinado tempo
from MenusFile import *  # importa o ficehiro MenusFile para criar e interagir com os menus gráficos
from Harve import *  # importa o ficheiro Harve para trabalhar com o robô
from bodyBotT import *  # importa o ficheiro bodyBotT para trbalhar com o layout gráfico do robô


# função para ver quantos obstaculos vai haver no mapa
def numberOfObstacules(Implementation):
    if Implementation == 1:  # se for a primeira implematação
        n = 3  # numero de obstaculos
    elif Implementation == 2:  # se for a segunda implematação
        n = 5  # numero de obstaculos
    else:  # se for a quarta implementação
        n = 7  # numero de obstaculos
    return n  # retorna o numero de obstaculos

# função para criar os obstaculos
def obstacules(win2, mapM, Implementation, xL, yL, r1, fourthImplementation1Boolean):
    a, n = 0, numberOfObstacules(Implementation)  # inicializa as variaveis usadas
    while a < n:  # loop que corre 3 vezes
        X, Y = randint(20, 100), randint(20, 80)  # gera as coordenadas que vão dar origem aos obstaculos de forma aleatoria
        C = Point(X, Y)  # cria o centro geometrico do obstaculo com as coordenadas geradas
        if (a == 0 and not fourthImplementation1Boolean) or validate(X, Y, xL, yL, r1):  # se for o primeiro obstaculo de todas as implementações exceto da versão um da quarta implementação(na versão um da quarta implementação é a unica que os objetivos são defenidos primeiro que os obstaculos como tal até o primeiro obstaculo tem a condição de não estar a chocar com os objetivos) ou se osbsctaculos estiverem corretamente espaçados
            obstacule = Tree(C, 3, win2, a, Point(0, 0), 0, 0)  # inicializa o obstaculo na classe Tree
            if Implementation == 1:  # se for a primeira implematação
                obstacule.draw1(mapM)  # metodo da classe Tree para desenhar os obstaculos
            else:  # se for a segunda ou quarta implematação
                obstacule.draw2(mapM)  # metodo da classe Tree para desenhar os obstaculos
            xL.append(X), yL.append(Y), r1.append(18**0.5)  # guarda o x do centro geometrico do obstaculo
            a = a + 1  # avança para o obstaculo seguinte
    return xL, yL, r1  # retorna o x e o y do centro geomtrico do obstaculo assim como o seu raio

# função para os objetivos
def objectives(win2, mapM, xL, yL, r1, x):
    a = 0  # inicializa as variaveis usadas
    listOfObjectives = []

    while True:  # loop permanente
        P1 = win2.getMouse()  # retira o ponto clicado pelo utilizador
        if ((P1.getX()-(x-7))**2+(P1.getY()-7)**2)**0.5 <= 3:  # se clicado em cima do robô
            break  # o loop de colocar os objetivos quebra
        if not((2 <= P1.getX() <= 12) and (88 <= P1.getY() <= 98)) and not((x-2 <= P1.getX() <= x-12) and (2 <= P1.getY() <= 12)) and (6 <= P1.getX() <= x-6) and (6 <= P1.getY() <= 94) and validate(P1.getX(), P1.getY(), xL, yL, r1):  # verifica se o ponto clicado está dentro dos limites impostos
            objective = Circle(P1, 2)  # cria o objetivo
            mapM.addObjectives(P1, 2)  # adiciona o objetivo `informação sobre o mapa
            objective.setFill('Red')  # cor do objetivo
            objective.draw(win2)  # desenha o objetivo
            listOfObjectives.append(objective)  # guarda a informação gráfica sobre o objetivo
            a = a + 1  # passa para o objetivo seguinte

    return listOfObjectives  # retorna a informação gráfica dos objetivos

# função para o robô da primeira implementação
def robot(win2, bot, listOfObjectives, mapM, body, x):
    end = 0  # inicializa as variaveis usadas
    exitBot = False
    a = 0

    while win2.checkKey() != 'e' and not exitBot:  # enquanto 'e' não for clicado nem o robô terminar as suas tarefas
        valid = False  # o robô ainda não andou
        if end == 0:  # se o robô ainda não coletou todos os objetivos
            Angle, end, a = goalFinder(mapM, bot, listOfObjectives, a)  # chama a função
        else:  # se o robô já apanhou todos os objetivos
            Angle, exitBot = baseFinder(bot, x)  # chama a função
        sleep(0.05)  # o programa para 0.05 segundos
        while not valid and not exitBot:  # enquato o robô não andar ou enquanto anida não tiver acabado as suas tarefas
            Angle, valid, steps = run(body, bot, mapM, Angle, x, 0, False)  # chama a função

# função para defenir o template da primeira implementação
def background():
    win2 = GraphWin("Mapa", 600, 500, autoflush=True)  # desenha a janela gráfica
    win2.setCoords(0.0, 0.0, 120.0, 100.0)  # impõem um referencial sobre a janela
    win2.setBackground('Grey')  # cor dos limites do mapa
    borderline = Rectangle(Point(2, 2), Point(118, 98))  # limite do mapa
    borderline.setFill('White')  # cor do mapa
    borderline.draw(win2)  # desenha os limites do mapa

    return win2  #devolve a janela da implementação

# funçao para a primeira implematação
def firstImplementation():
    win2 = background()  # chama a função que cria gráficamente o mapa

    mapM = mapMemory()  # inicia uma classe que permite trablhar com a informação do mapa

    xL, yL, r1 = [], [], []

    xL, yL, r1 = obstacules(win2, mapM, 1, xL, yL, r1, False)  # chama a função que cria os obstaculos

    bot = Harve(Point(113, 7))  # inicia uma classe que inicializa o robô
    body = bodyForTheBot(win2, 120)  # chama a função que atribui a parte gráfica ao robô

    listOfObjectives = objectives(win2, mapM, xL, yL, r1, 120)  # chama a função que cria os objetivos

    robot(win2, bot, listOfObjectives, mapM, body, 120)  # chama a função

    win2.close()  # fecha a janela

# função para trabalhar com a bateria do robô da segunda implementação
def bateryForTheSecondImplementation2(number, x, y, win2, batery, bot, body, mapM, exitBot, color, steps):
    while win2.checkKey() != 'e' and not exitBot:  # enquanto 'e' não for clicado nem o robô terminar as suas tarefas
        valid = False  # o robô ainda não andou
        Angle, exitBot = baseFinder(bot, 120)  # chama a função
        sleep(0.05)  # o programa para 0.05 segundos
        while not valid and not exitBot:  # enquato o robô não andar ou enquanto anida não tiver acabado as suas tarefas
            Angle, valid, steps = run(body, bot, mapM, Angle, 120, steps, True)  # chama a função
            x, y = bot.returnPosition()  # guarda aposição atual da bateria
            batery.undraw()  # apaga o desenho da batria anterior
            batery = setBotBatery(win2, x, y, number, color)  # chama a função
    return batery, x, y, Angle, valid  # retrona a parte grafica da bateria, as coordendas da posição do robô e se o robô andouou não

# função para trabalhar com a bateria do robô da segunda implementação
def bateryForTheSecondImplementation(number, x, y, win2, batery, bot, body, mapM, exitBot):
    steps, color = 0, 'Yellow'  # inicializa as variaveis da bateria
    number = str(int(number) - 1)  # diminui a bateria do robô
    batery.undraw()  # apaga o desenho anterior sa bateria do robô
    batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
    if number == '2':  # se a bateria tiver no 2
        color = 'Red'  # cor da bateria
        batery.undraw()  # apaga o desenho anterior sa bateria do robô
        batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
        exitBot = False  # o robô ainda não acabou as suas tarefas
        batery, x, y, Angle, valid = bateryForTheSecondImplementation2(number, x, y, win2, batery, bot, body, mapM, exitBot, color, steps)  # chama a função
        sleep(1.5)  # o programa para durante 1.5 segundos
        color, number = 'Yellow', '3'  # troca as caracteristicas da bateria
        batery.undraw()  # apaga o desenho anterior sa bateria do robô
        batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
        sleep(1.5)  # o programa para durante 1.5 segundos
        number, color = '4', 'Green'  # troca as caracteristicas da bateria
        batery.undraw()  # apaga o desenho anterior sa bateria do robô
        batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
        number, exitBot, steps = 4, False, 0  # reinicia as variaveis após o robô ter carregado
    return batery, number, exitBot, steps, color  # retorna a parte gráfica da bateria do robô, o numero da bateria, se o robô já acabou as suas tarefas ou não e o numero de passos que o robô já deu

# função para trabalhar com a bateria do robô da segunda implementação
def botForTheSecondImplementation(win2, bot, listOfObjectives, mapM, body):
    end, a, exitBot, steps, x, y, number, color = 0, 0, False, 0, 113, 7, '4', 'Green'  # inicializa as variaveis da bateria
    batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
    while win2.checkKey() != 'e' and not exitBot:  # enquanto 'e' não for clicado nem o robô terminar as suas tarefas
        valid = False  # ainda não andou
        if end == 0:  # há objetivos
            Angle, end, a = goalFinder(mapM, bot, listOfObjectives, a)  # chama a função que encontra objetivos
        else:  # já não há objetivos
            Angle, exitBot = baseFinder(bot, 120)  # chama a função que encontra as bases
        sleep(0.05)  # o programa para 0.05 segundos
        while not valid and not exitBot:  # enquanto o robô não tiver andado nem tiver acabado as suas tarefas
            Angle, valid, steps = run(body, bot, mapM, Angle, 120, steps, True)  # função que faz o robô andar
            x, y = bot.returnPosition()  # guarda a posição do robô
            batery.undraw()  # apaga o desenho anterior sa bateria do robô
            batery = setBotBatery(win2, x, y, number, color)  # redesenha a bateria do robô com as novas configurações
            if steps == 105:  # se tiver atingido os 105 passos
                batery, number, exitBot, steps, color = bateryForTheSecondImplementation(number, x, y, win2, batery, bot, body, mapM, exitBot)  # chama a função

# funçao para a segunda implematação
def secondImplementation():
    win2 = background()  # chama a função

    mapM = mapMemory()  # inicia uma classe

    xL, yL, r1 = [], [], []  # inicializa as variaveis

    xL, yL, r1 = obstacules(win2, mapM, 2, xL, yL, r1, False)  # chama a função

    bot = Harve(Point(113, 7))  # inicia uma classe
    body = bodyForTheBot(win2, 120)  # chama a função

    listOfObjectives = objectives(win2, mapM, xL, yL, r1, 120)  # chama a função

    botForTheSecondImplementation(win2, bot, listOfObjectives, mapM, body)  # chama a função

    win2.close()  # fecha a janela

# função que entende quando é necessário utilizar a palavra 'Point'
def doubleWord(i, q, importante, z):
    if q >= 0 and i == q + 3 and z == 1:
        importante.append('Point')  # adiciona a palavra 'Point' à informação
        i = i + 1
        z = 1
        q = -1

    return i, q, importante, z

# função que adiciona um espaço extra qundo deteta a palavra Circle
def virtualAdd(i, ie, importante, z):
    if ie >= 0 and (i == ie + 5 or i == ie + 3) and z == 1: # se esta é a posição correta para adicionar um espaço vazio
        importante.append('/')  # adiciona o espaço vazio
        i = i + 1  # volta à contagem de palvras
        z = 1 # e de espaços vazios colocados

    return i, ie, importante, z  # retorna o numero da palavra a ser analisada, se à salto ou não no espaço das palavras, quais as palvras importantes e

# função destinada a encontrar numeros no ficheiro Ambiente.txt
def readFileObstaculesSubfunction(a, word, z, importante, i, n):
    if word[n] == a:  # se for encontrado um determinado numero
        if z == 1:  # é tomado nota que já foi encontrado um numero
            importante.append(a)  # adiciona-se esse numero
            i = i + 1  # avança-se para o próximo
            z = 2  # desta forma vamos no segundo numero
        else:  # se não for encontrado um determinado numero
            importante[i] = importante[i] + a  # é poque ainda estamos a construir o mesmo numero então apenas é adicionado um algarismo

    return i, z, importante  # devolve as variaveis necessarias para continuar a analise e toda a informação importante do ficheiro

# função que identifica palavras chave no ficheiro ambiente.txt
def readFileObstaculesSubfunction4(information, ie, i, z, importante, a, TYPE):
    if information[a].casefold().find(TYPE.lower()) >= 0:  # se for identificado a palavra
        importante.append(TYPE)  # adiciona-se a palavra á informação retirada do ficheiro
        i = i + 1  # avança para a palavra importante seguinte
        if TYPE == 'Circle':  # a palvra circulo è guradada de forma um pouco diferente porque não necessita de dois pontos no modulo graphics para ser criada então quando a informação do ficheiro é devolvida ele cria um espaço sem informação para manter o padrão da informação retirada do ficheiro
            ie = i
        i, ie, importante, z = virtualAdd(i, ie, importante, z) # chama a função que organiza a informação como necessário
    return information, ie, i, z, importante, a  # retrona a informação, e todas as outras variaveis que dão continuidade à analise da informação

# funçaõ que deteta a palavra 'Point'
def readFileObstaculesSubfunction3(information, importante, a, i, ie, z):
    q = 0
    if information[a].casefold().find('point') >= 0:  # se for a palavra 'Point'
        if information[a].casefold().count('point') == 2:  # vão existir duas palvras 'Point' caso oobstaculo seja um retangulo
            q = i  # nota-se que já foi a palavra
        importante.append('Point')  # adiciona a palavra 'Point'
        i = i + 1  # avança para a próxima palavra
        i, ie, importante, z = virtualAdd(i, ie, importante, z)  # chama a função
    return i, ie, importante, z, q, information  # retorna a informação importante do ficheiro assim como todas as variaveis necessarias para dar sequencia à analise do ficheiro

# função que inicia as variaveis para ler o ficheiro Ambiente.txt
def readFileObstaculesDefiningVariables():
    importante, i, ie, q = [], -1, -1, -1  # inicia as variaveis
    file = open('Ambiente.txt', 'r')  # abre e lê o ficheiro
    return importante, i, ie, q, file  # devolve as vaiaveis e o ficheiro

# função que trabalha os algarismos decimais do ficheiro
def readFileObstaculesSubfunction2(word, importante, n, i):
    if word[n] == '.' and n + 1 <= len(word) - 1:  # se identificado um ponto
        if (word[n + 1] == '1' or word[n + 1] == '2' or word[n + 1] == '3' or word[n + 1] == '4' or word[
            n + 1] == '5' or word[n + 1] == '6' or word[n + 1] == '7' or word[n + 1] == '8' or word[
            n + 1] == '9' or word[n + 1] == '0'):  # e se esse ponto separar dois numeros
            importante[i] = importante[i] + '.'  # é adicionado um ponto que representa os algarismo inteiros dos decimais
    return importante  # devolve toda a informação importante do ficheiro

# principal função que lê o ficheiro Ambiente.txt
def readFileObstacules():
    importante, i, ie, q, file = readFileObstaculesDefiningVariables()  # inicia as variaveis e abre o ficheiro
    for line in file.readlines():  # loop por cada linha do ficheiro
        information = line.split(' ')  # separa as palvras no ficheiro
        for a in range(len(information)):  # loop que corre tantas vezes como o numero de palavras no ficheiro
            word = information[a]  # guarda a palavra do ficheiro a ser analisada
            z = 1
            typeOfWords = ['Bush', 'Stone', 'Grass', 'Rectangle', 'Circle']  # lista com o tipo possivel de obstaculos e de formatos de obstaculos
            for TYPE in typeOfWords:  # loop que corre por cada tipo e formato de obstaculo
                information, ie, i, z, importante, a = readFileObstaculesSubfunction4(information, ie, i, z, importante, a, TYPE)  # organiza e guarda a informação
            i, ie, importante, z, q, information = readFileObstaculesSubfunction3(information, importante, a, i, ie, z)  # verifica se foi encontrada a palvra 'Point'
            for n in range(len(word)):  # loop que corre o numero de vezes igual ao numero de palvras no ficheiro
                i, ie, importante, z = virtualAdd(i, ie, importante, z)  # chama a função
                i, q, importante, z = doubleWord(i, q, importante, z)  # chama a função
                if word[n] == ',' or word[n] == ')' or word[n] == '(':  # se existirem virgulas ou parenteses
                    z = 1  # é tomado nota
                for counter in range(10):  # loop que corre o numeor de vezes igual ao numero de possiveis numeros
                    i, z, importante = readFileObstaculesSubfunction(str(counter), word, z, importante, i, n)  # função que trata dos numeros no ficheiro
                importante = readFileObstaculesSubfunction2(word, importante, n, i)  # função que devolve os algarismos com casas decimais
    file.close()  # fecha o ficheiro Ambiente.txt
    return importante  # retorna uma lista periodicamente organizada com a informação importante do ficheiro

# função que cria os obstaculos da terceira implementação
def obstaculesForTheThirdImplementation(l, information, win2, mapM):
    xL, yL, r1 = [], [], []  # inicia as variaveis
    for a in range(int((l - 2) / 8)):  # loop que corre o numero de vezes igual ao numero de obstaculos
        q = int(8 * a + 2)  # equação para passar pela disposição periodica da lista que guarda a informação do ficheiro Ambiente.txt
        C = Point(float(information[q + 3]), float(information[q + 4]))  # centro do obstaculo
        if information[q + 1] == 'Rectangle':  # se o obstaculo for um retangulo
            C2 = Point(float(information[q + 6]), float(information[q + 7]))  # calculo do segundo ponto necessario para desenhar um retangulo usando o modulo graphics
            r = (((float(information[q + 6]) - float(information[q + 3])) ** 2 + (
                    float(information[q + 7]) - float(information[q + 4])) ** 2) ** 0.5)/2 # calculo do raio que circunescreve o retangulo
            r1.append(r)  # guarda a informação sobre o raio calculado anteriormente
            obstacule = Tree(C, r, win2, a, C2, information[q], information[q + 1])  # cria o obstaculo usando o metodo Tree
            obstacule.draw3(mapM)  # desenha o obstaculo no mapa
            xL.append((float(information[q + 3])+float(information[q + 6]))/2)  # guarda o x do centro geometrico do obstaculo
            yL.append((float(information[q + 4])+float(information[q + 7]))/2)  # guarda o y do centro geometrico do obstaculo
        else:  # se o obstaculo for um circulo
            obstacule = Tree(C, float(information[q + 6]), win2, a, Point(0, 0), information[q], information[q + 1])  # cria o obstaculo usando o metodo Tree
            obstacule.draw3(mapM)  # desenha o obstaculo no mapa
            r1.append(float(information[q + 6]))  # guarda a informação sobre o raio do obstaculo
            xL.append(C.getX())  # guarda o x do centro geometrico do obstaculo
            yL.append(C.getY())  # guarda o y do centro geometrico do obstaculo
    return xL, yL, r1  # retorna a informação sobre as coordenadas do centro geometrico do obstaculo, assim como o seu raio

# função que lê o ficheiro Ambiente.txt
def informationForTheThirdImplementation():
    information = readFileObstacules()  # informação importante do ficheiro
    x = ((float(information[0]) * 100) / float(information[1]))  # proporção da janela atraves do tamanho dado no ficheiro
    l = len(information)  # tamanho da informação retirada

    return information, x, l  # retorna a informação importante do ficheiro, a proporção da janela atraves do tamanho dado no ficheiro e o tamanho da informação retirada

# funçao para a terceira implematação
def thirdImplementation():
    information, x, l = informationForTheThirdImplementation()  # chama a função que lê o ficheiro Ambiente e retira a informação

    win2 = GraphWin("Mapa", float(information[0]), float(information[1]), autoflush=False)  # desenha a janela gráfica
    win2.setCoords(0.0, 0.0, x, 100.0)  # impõem um referencial sobre a janela
    win2.setBackground('Grey')  # cor dos limites do mapa
    borderline = Rectangle(Point(2, 2), Point(x - 2, 98))  # limite do mapa
    borderline.setFill('White')  # cor do mapa
    borderline.draw(win2)  # desenha os limites do mapa

    mapM = mapMemory()  # inicia uma classe para guardar informação sobre o mapa
    xL, yL, r1 = obstaculesForTheThirdImplementation(l, information, win2, mapM)  # chama a função que cria os obstaculos recorrendo ao ficheiro Ambiente.txt

    bot = Harve(Point(x - 7, 7))  # inicia uma classe para trabalhar com o robô
    body = bodyForTheBot(win2, x)  # chama a função que inicializa o corpo gráfico do robô

    listOfObjectives = objectives(win2, mapM, xL, yL, r1, x)  # chama a função que cria os objetivos
    robot(win2, bot, listOfObjectives, mapM, body, x)  # chama a função que faz o robô ir coletar os objetivos

    win2.close()  # fecha a janela

#  função que lê o ficheiro lixo.txt
def readFileObjectives():
    importante = []  # inicia a variavel

    file = open('Limpeza.txt', 'r')  # abre o ficheiro
    for line in file.readlines():  # loop que passa por cada linha do ficheiro
        information = line.split(' ')  # divide o que está escrito no ficheiro
        for a in range(len(information)):  # loop que corre numero de vezes igual ao numero de palavras no ficehiro
            word = information[a]  # vamos agora analisar cada palavra extraida
            for n in range(len(word)):  # loop por cada letra/numero na palavra a ser analisada
                if word[n] == '0' or word[n] == '1' or word[n] == '2' or word[n] == '3' or word[n] == '4' or word[
                    n] == '5' or word[n] == '6' or word[n] == '7' or word[n] == '8' or word[n] == '9':  # se a palavra tiver algum deste numeros adiciona a palavra à informação extraida do ficheiro
                    importante.append(information[a])  # adiciona a palavra à informação extraida do ficheiro
                    break  # quebra o loop
    file.close()  # fecha o ficheiro
    return importante  # retorna a informação importante extraida do ficheiro

# função para os objetivos da querta implementação
def objectivesForThefourthImplementation1(mapM, listOfObjectives, win2):
    xL, yL, r1, c = [], [], [], 0  # inicia as variaveis
    coordenates = readFileObjectives()  # chama a função que lê o ficheiro lixo.txt
    for a in range(int((len(coordenates)) / 2)):  # loop que corre igual ao numero de objetivos que existem
        if c + 1 <= len(coordenates):  # se ainda faltar objetvos que estão descritos no ficheiro
            center = Point(coordenates[c], coordenates[c + 1])  # retira o centro geometrico do objetivo da informação
            objective = Circle(center, 2)  # cria graficamente a variavel do objetivo
            objective.setFill('Red')  # cor do objetivo
            mapM.addObjectives(center, 2)  # adiciona o ojetivo à informação sobre o mapa
            listOfObjectives.append(objective)  # adiciona a variavel grafica do objetivo à lista de objetivos criados
            objective.draw(win2)  # desenha o objetivo
            r1.append(3.5)  # guarda informação sobre a posição e tamanho do objetivo
            xL.append(float(coordenates[c]))
            yL.append(float(coordenates[c + 1]))
            c = c + 2  # passa ao objetivo seguinte
    return xL, yL, r1  # retorna a informação sobre os objetivos

# funçao para a primeira versão da quarta implematação
def fourthImplementation1():
    win2 = background()  # chama a função

    mapM = mapMemory()  # inicia uma classe
    bot = Harve(Point(113, 7))  # inicia uma classe
    body = bodyForTheBot(win2, 120)  # chama a função
    listOfObjectives = []  # iniciação das variaveis

    xL, yL, r1 = objectivesForThefourthImplementation1(mapM, listOfObjectives, win2)  # chama a função que cria os objetivos
    xL, yL, r1 = obstacules(win2, mapM, 4, xL, yL, r1, True)  # chama a função que cria os obstaculos
    robot(win2, bot, listOfObjectives, mapM, body, 120)  # chama a função que inicia o robô

    win2.close()  # fecha a janela


# funçao para a segunda versão da quarta implematação
def fourthImplementation2():
    win2 = background()  # chama a função

    mapM = mapMemory()  # inicia uma classe

    xL, yL, r1 = [], [], []  # iniciação das variaveis

    xL, yL, r1 = obstacules(win2, mapM, 4, xL, yL, r1, False)  # chama a função

    bot = Harve(Point(113, 7))  # inicia uma classe
    body = bodyForTheBot(win2, 120)  # chama a função

    listOfObjectives = objectives(win2, mapM, xL, yL, r1, 120)  # chama a função
    robot(win2, bot, listOfObjectives, mapM, body, 120)  # chama a função

    win2.close()  # fecha a janela
