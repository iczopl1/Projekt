import random
import time
def startup():
    print("Gra w Papier kamień nożyce")
    print("Zaczynasz grę Wybierz\n1 - Papier\n2 - Kamień\n3 - Nożyce")
    wybur = int(input("Wybierz a gra się rozpocznie!"))
    print("Potyczka/n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    komputer_los =random.randint(1,3)
    if(komputer_los ==1):
        print("Komputer wylosował Papier")
    if(komputer_los ==2):
        print("Komputer wylosował Kamień")
    if(komputer_los ==3):
        print("Komputer wylosował Nożyce")
    if(wybur == komputer_los):
        print("Remis")
        startup()
    elif(wybur ==1 and komputer_los ==2 or wybur ==2 and komputer_los ==3 or wybur ==3 and komputer_los ==1):
        print("Wygrałeś")
        startup()
    else:
        print("You lose")
if __name__ == "__main__":
    startup()