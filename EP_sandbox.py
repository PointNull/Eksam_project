#Vi skal have lavet et eksamens projekt som er rimeligt gennemført. Det er en spilportal som ligger lokalt på ens computer- 
#og hurtigt can starte nogle små spil


from tkinter import *
#import pygame


def main():
    root = Tk()
    root.title("GAME-PORTAL")
    root.geometry('600x500') 
    app = Controller(root)
    app.grid(sticky='nsew')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
   
    #kører vores Tkinter
    root.mainloop()

#klasse som styrer de forskellige frames. Er også "Parent-frame" som alle andre frames ligges ovenpå
class Controller(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

        #
        self.pageOne = aim_Lab(self)
        self.pageOne.grid(row=0, column=0, sticky='nsew')
        #
        self.pageTwo = pong(self)
        self.pageTwo.grid(row=0, column=0, sticky='nsew')
        #
        self.pageThree = TEST(self)
        self.pageThree.configure(background='#4a4a4a')
        self.pageThree.grid(row=0, column=0, sticky='nsew')
        #først vindue man ser når man åbner applikationen
        self.menu = Start(self)
        self.menu.grid(row=0, column=0, sticky='nsew')
        self.menu.configure(background='#4a4a4a')
        self.menu.tkraise() #Gør at start-menuen vises først når man åbner applikationen "Class Start(Frame)"





#Første frame som er menuen
class Start(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.topButtons()
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        

#Knapper som navigere til de forskellige spil
    def topButtons(self):
        self.firstPage = Button(self, text="Aimlab", background="WHITE", command= self.master.pageOne.tkraise)
        self.firstPage.grid(row=3, column=1, sticky='new')

        self.secondPage = Button(self, text="Pong", background="WHITE", command= self.master.pageTwo.tkraise)
        self.secondPage.grid(row=3, column=2, sticky='new')

        self.thirdPage = Button(self, text="Test", background="WHITE", command= self.master.pageThree.tkraise)
        self.thirdPage.grid(row=3, column=3, sticky='new')  


#frame til spillet AimLab
class aim_Lab(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        
        
        #indfør spillet herunder


#Frame til spillet Pong
class pong(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller



#Frame til potentielt tredje spil
class TEST(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        self.returnButton()
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        

        self.skærm = Label(self, text=" SKÆRM til spil ", background="cyan", fg='black')
        self.skærm.grid(column=0, row=0, columnspan=5, rowspan=4, sticky='nsew')

        

    def returnButton(self):
        self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=10, command=self.navReturn)
        self.menuReturn.grid(column=0, row=4, columnspan=1, rowspan=2,  sticky='sw')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()






    
    
    

if __name__ == '__main__':
    main()


