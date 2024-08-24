"""Ficheiro com todas as funções que permitem o funcionamento dos menus gráficos"""
"""Guilherme Fernandes - 103847 & Gonçalo Drago - 103332"""

from implementations import *  # carrega o ficheiro implementations para utilizar as funções que correm as implemtações

# função encarregue pela janela Help
def Help():
    winHelp = GraphWin("Help", 500, 500, autoflush=False)  # cria a janela Help, usando o modulo graphics usando o metodo GraphWin
    winHelp.setCoords(0.0, 0.0, 100.0, 100.0)  # impõem um referencial para o eixo dos X e dos Y
    texto1 = Text(Point(50, 60), "Trabalho realizado por:")  # cria o texto usando o metodo Text do modulo graphics
    texto1.draw(winHelp)  # desenha o texto
    texto2 = Text(Point(48, 50), "Guilherme Fernandes & Gonçalo Drago")  # cria o texto usando o metodo Text do modulo graphics
    texto2.draw(winHelp)  # desenha o texto
    texto3 = Text(Point(48, 40), "Projeto de Fundamentos da Programação")  # cria o texto usando o metodo Text do modulo graphics
    texto3.draw(winHelp)  # desenha o texto
    buttonBack = Text(Point(91, 5), "Return")  # cria o texto usando o metodo Text do modulo graphics
    buttonBack.draw(winHelp)  # desenha o texto
    Rectangle(Point(85, 3), Point(97, 7)).draw(winHelp)  # cria um um retangulo à volta do texto 'return'

    valid = False  # boolean que garante um loop permante
    while not valid: # loop que mantem o programa na janela Help
        p = winHelp.getMouse()  # metodo que retira onde o utilizador carregou na janela
        if 85 <= p.getX() <= 97 and 3 <= p.getY() <= 7:  # se o utilizador carregar no botão return
            winHelp.close()  # fecha a janela help
            mainMenu()  # chama a função mainMenu()
            valid = True  # o programa sai do loop

# função para os botões do primeiro menu grafico
def buttonsForTheMainMenu(win):
    valid = False  # boolean que garante um loop permante
    while not valid:  # loop que mantem o programa na janela do primeiro menu gráfico
        P = win.getMouse()  # metodo que retira onde o utilizador carregou na janela
        if 30 <= P.getX() <= 65 and 65 <= P.getY() <= 75:  # se o utilizador carregar no botão play
            win.close()  # fecha a janela do menu gráfico principal
            valid = True  # o programa sai do loop
            mainMenu2()  # chama a função mainMenu2()
        elif 30 <= P.getX() <= 65 and 50 <= P.getY() <= 60:  # se o utilizador carregar no botão help
            win.close()  # fecha a janela do menu gráfico principal
            valid = True  # o programa sai do loop
            Help()    # chama a função Help()
        elif 30 <= P.getX() <= 65 and 35 <= P.getY() <= 45:  # se o utilizador carregar no botão exit
            win.close()  # fecha a janela do menu gráfico principal
            valid = True  # o programa sai do loop

# função encarregue pela janela do menu gráfico principal
def mainMenu():
    win = GraphWin("Main Menu", 500, 500, autoflush=True)  # cria a janela Main Menu, usando o modulo graphics usando o metodo GraphWin
    win.setCoords(0.0, 0.0, 100.0, 100.0)  # impõem um referencial para o eixo dos X e dos Y
    buttonPlay = Text(Point(48, 70), "Play")  # cria o texto usando o metodo Text do modulo graphics
    buttonPlay.draw(win)  # desenha o texto
    Rectangle(Point(30, 65), Point(65, 75)).draw(win)  # cria um um retangulo à volta do texto 'Play'
    buttonHelp = Text(Point(48, 55), "Help")  # cria o texto usando o metodo Text do modulo graphics
    buttonHelp.draw(win)  # desenha o texto
    Rectangle(Point(30, 50), Point(65, 60)).draw(win)  # cria um um retangulo à volta do texto 'Help'
    buttonExit = Text(Point(48, 40), "Exit")  # cria o texto usando o metodo Text do modulo graphics
    buttonExit.draw(win)  # desenha o texto
    Rectangle(Point(30, 35), Point(65, 45)).draw(win)  # cria um um retangulo à volta do texto 'Exit'

    buttonsForTheMainMenu(win)  # chama a função buttonsForTheMainMenu()

# função para os botões do segundo menu grafico
def buttonsForTheMainMenu2(winMainMenu2):
    valid = False  # boolean que garante um loop permante
    while not valid:  # loop que mantem o programa na janela do primeiro menu gráfico
        P = winMainMenu2.getMouse()  # metodo que retira onde o utilizador carregou na janela
        if 30 <= P.getX() <= 65 and 65 <= P.getY() <= 75:  # se o utilizador carregar no botão first Implementation
            winMainMenu2.close()  # fecha a janela do menu gráfico secundário
            firstImplementation()  # chama a função firstImplementation()
            mainMenu2()  # chama a função mainMenu2()
        elif 30 <= P.getX() <= 65 and 50 <= P.getY() <= 60:  # se o utilizador carregar no botão second Implementation
            winMainMenu2.close()  # fecha a janela do menu gráfico secundário
            secondImplementation()  # chama a função secondImplementation()
            mainMenu2()  # chama a função mainMenu2()
        elif 30 <= P.getX() <= 65 and 35 <= P.getY() <= 45:  # se o utilizador carregar no botão third Implementation
            winMainMenu2.close()  # fecha a janela do menu gráfico secundário
            thirdImplementation()  # chama a função thirdImplementation()
            mainMenu2()  # chama a função mainMenu2()
        elif 30 <= P.getX() <= 65 and 20 <= P.getY() <= 30:  # se o utilizador carregar no botão fourth Implementation
            winMainMenu2.close()  # fecha a janela do menu gráfico secundário
            mainMenu3()  # chama a função mainMenu3()
        elif 85 <= P.getX() <= 97 and 3 <= P.getY() <= 7:  # se o utilizador carregar no botão return
            winMainMenu2.close()  # fecha a janela do menu gráfico secundário
            mainMenu()  # chama a função mainMenu()
            valid = True  # o programa sai do loop

# função encarregue pela janela do menu gráfico secundário
def mainMenu2():
    winMainMenu2 = GraphWin("Main Menu 2", 500, 500, autoflush=False)  # cria a janela Main Menu 2, usando o modulo graphics usando o metodo GraphWin
    winMainMenu2.setCoords(0.0, 0.0, 100.0, 100.0)  # impõem um referencial para o eixo dos X e dos Y
    Text(Point(48, 70), "First Implementation").draw(winMainMenu2)   # cria o texto usando o metodo Text do modulo graphics
    Rectangle(Point(30, 65), Point(65, 75)).draw(winMainMenu2)  # cria um um retangulo à volta do texto
    Text(Point(48, 55), "Second Implementation").draw(winMainMenu2)  # cria o texto usando o metodo Text do modulo graphics
    Rectangle(Point(30, 50), Point(65, 60)).draw(winMainMenu2)  # cria um um retangulo à volta do texto
    Text(Point(48, 40), "Third Implementation").draw(winMainMenu2)  # cria o texto usando o metodo Text do modulo graphics
    Rectangle(Point(30, 35), Point(65, 45)).draw(winMainMenu2)  # cria um um retangulo à volta do texto
    Text(Point(48, 25), "Fourth Implementation").draw(winMainMenu2)   # cria o texto usando o metodo Text do modulo graphics
    Rectangle(Point(30, 20), Point(65, 30)).draw(winMainMenu2)  # cria um um retangulo à volta do texto
    Text(Point(91, 5), "Return").draw(winMainMenu2)  # cria o texto usando o metodo Text do modulo graphics
    Rectangle(Point(85, 3), Point(97, 7)).draw(winMainMenu2)  # cria um um retangulo à volta do texto
    Text(Point(48, 90), "To stop creating goals and start the robot click on it").draw(winMainMenu2)  # desenha texto com instruções
    Text(Point(48, 85), "To stop the robot while the program is running press 'e'").draw(winMainMenu2)  # desenha texto com instruções

    buttonsForTheMainMenu2(winMainMenu2)  # chama a função buttonsForTheMainMenu2()

# função para os botões do terceiro menu grafico
def buttonsForTheMainMenu3(winMainMenu2):
    valid = False  # boolean que garante um loop permante

    while not valid:  # loop que mantem o programa na janela do primeiro menu gráfico
        P = winMainMenu2.getMouse() # metodo que retira onde o utilizador carregou na janela
        if 30 <= P.getX() <= 65 and 65 <= P.getY() <= 75:
            winMainMenu2.close()  # fecha a janela do menu gráfico terciario
            fourthImplementation1()  # chama a função fourthImplementation1()
            mainMenu3()  # chama a função  mainMenu3()
        elif 30 <= P.getX() <= 65 and 50 <= P.getY() <= 60:
            winMainMenu2.close()  # fecha a janela do menu gráfico terciario
            fourthImplementation2()  # chama a função  fourthImplementation2()
            mainMenu3()  # chama a função  mainMenu3()
        elif 85 <= P.getX() <= 97 and 3 <= P.getY() <= 7:
            winMainMenu2.close()  # fecha a janela do menu gráfico terciario
            mainMenu2()  # chama a função  mainMenu2()
            valid = True  # o programa sai do loop

# função encarregue pela janela do menu gráfico terciario
def mainMenu3():
    winMainMenu2 = GraphWin("Main Menu 3", 500, 500, autoflush=False)  # cria a janela Main Menu 3, usando o modulo graphics usando o metodo GraphWin
    winMainMenu2.setCoords(0.0, 0.0, 100.0, 100.0)  # impõem um referencial para o eixo dos X e dos Y

    Text(Point(48, 90), "The collection points should be set by a:").draw(winMainMenu2)  # desenha o texto

    buttonLevel1 = Text(Point(48, 70), "file")  # cria o texto usando o metodo Text do modulo graphics
    buttonLevel1.draw(winMainMenu2)  # desenha o texto
    Rectangle(Point(30, 65), Point(65, 75)).draw(winMainMenu2)  # cria um um retangulo à volta do texto

    buttonLevel2 = Text(Point(48, 55), "mouse click")  # cria o texto usando o metodo Text do modulo graphics
    buttonLevel2.draw(winMainMenu2)  # desenha o texto
    Rectangle(Point(30, 50), Point(65, 60)).draw(winMainMenu2)  # cria um um retangulo à volta do texto

    buttonBack = Text(Point(91, 5), "Return")  # cria o texto usando o metodo Text do modulo graphics
    buttonBack.draw(winMainMenu2)  # desenha o texto
    Rectangle(Point(85, 3), Point(97, 7)).draw(winMainMenu2)  # cria um um retangulo à volta do texto

    buttonsForTheMainMenu3(winMainMenu2)  # chama a função buttonsForTheMainMenu3()
