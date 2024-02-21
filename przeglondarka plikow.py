import PySimpleGUI as sg
import os
import dodatki


class lokalizacja:
    def __init__(self):
        # pobranie lokalizacji pliku
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.pliki = []
        self.foldery = []
        self.plik = './pustyplik.png'
        self.folder_img = dodatki.tobase64('./dir.png')
        self.initgui()
    def wypispliku(self):
        # pobranie wszystkich folderów
        self.pliki = []
        self.foldery = []
        dir_path = self.path
        self.foldery.append('../')
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                self.pliki.append(os.path.join(path))
            else:
                self.foldery.append(path)
    def go(self,gofolder:str):
        if gofolder =='../':
            self.path = os.path.dirname(os.path.dirname(self.path))
        else:
            self.path = os.path.join(self.path, gofolder)
        self.initgui()

    def listaplikow(self):
        self.wypispliku()
        dirlayout = []
        filelayout = []
        for foldery in self.foldery:
            dirlayout.append([sg.Image(source=self.folder_img), sg.Button(foldery)])
        for pliki in self.pliki:
            if dodatki.isimg(pliki):
                filelayout.append([sg.Text(os.path.join('./', pliki))])
            else:
                filelayout.append([sg.Image(source=dodatki.tobase64(self.plik)), sg.Button(pliki)])
        return [dirlayout]

    def initgui(self):
        self.initlayout = [sg.Text("Przeglondarka plików Ireneusz")]
        self.locationlayout = [sg.Text('Lokalizacja: '+self.path)]
        self.endlayout = [sg.Button("OK")]
        element = [self.listaplikow()]
        pliki = sg.Frame("Dostempne pliki",element)
        gitlayout = (self.initlayout, self.locationlayout, pliki, self.endlayout, sg.List())
        self.layout = gitlayout


def mainloop():
    okno = lokalizacja()
    while True:
        window = sg.Window('Przeglondarka plików', okno.layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        gofolder = event
        if gofolder in okno.foldery:
            okno.go(gofolder)
            dirandfilelayout = okno.listaplikow()
            #brak punktu do odwołania
            window['-TOUPDATE-'].Update([dirandfilelayout])
    window.close()


def main():
    if '__main__' == __name__:
        mainloop()

    else:
        print('To plik main')




main()