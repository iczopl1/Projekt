import random
zag1 = ["N","N","N"]
zag2 = ["N","N","N"]
zag3 = ["N","N","N"]
lista=[zag1,zag2,zag3]
win = 0

def spaw():
    if(lista[0][0]==lista[0][1] and  lista[0][0]==lista[0][2] and lista[0][0] !="N" or lista[1][0]==lista[1][1] and  lista[1][0]==lista[1][2] and lista[1][0] !="N" or lista[2][0]==lista[2][1] and  lista[2][0]==lista[2][2] and lista[2][0] !="N"):
        winko()
    if(lista[0][0]==lista[1][1] and  lista[0][0]==lista[2][2] and lista[0][0] !="N" or lista[0][2]==lista[1][1] and lista[0][2] !="N" and  lista[1][1]==lista[2][0]):
        winko()
    if(lista[0][0]==lista[1][0] and  lista[0][0]==lista[2][0] and lista[0][0] !="N" or lista[0][1]==lista[1][1] and  lista[0][1]==lista[2][1] and lista[0][1] !="N" or lista[0][2]==lista[1][2] and  lista[0][2]==lista[2][2] and lista[0][2] !="N"):
        winko()
    if 'N' in lista == False:
        input("Koniec rundy nikt nie wygrał")


def winko():
    wypis()
    global win
    win =1
    print("Koniec gry ktoś wygrał")

def wypis():
    print("Stan stołu")
    print(lista[0][0]+"|"+lista[0][1]+"|"+lista[0][2]+"\n")
    print(lista[1][0]+"|"+lista[1][1]+"|"+lista[1][2]+"\n")
    print(lista[2][0]+"|"+lista[2][1]+"|"+lista[2][2]+"\n")


def gracz():
    x = int(input("Wybierz pozycje x dla kółka"))
    y = int(input("Wybierz pozycje y dla kółka"))
    if(x < 0 or x > 3 and y < 0 or y > 3 ):
        print("Nieprawidłowy zakres")
        gracz()
    if lista[x-1][y-1] =="N":
        lista[x-1][y-1] = "O"
        spaw()
    else:
        print("Wybrane pola są zajente")
        gracz()


def komp():
    x = random.randint(1,3)
    y = random.randint(1,3)
    if lista[x-1][y-1] =="N":
        lista[x-1][y-1] = "X"
        spaw()
    else:
        komp()


if __name__ == "__main__":
    print("Kółko i krzyżyk gra")
    los = random.randint(0,1)
    if los == 1:
        print("Grasz kółkiem jako 2 gracz")
        while(win == 0):
            komp()
            wypis()
            gracz()
    print("Grasz kółkiem i zaczynasz grę")
    while(win == 0):
        gracz()
        komp()
        wypis()