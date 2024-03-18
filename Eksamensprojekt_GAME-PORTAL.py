#Vi skal have lavet et eksamens projekt som er rimeligt gennemført. Det er en spilportal som ligger lokalt på ens computer- 
#og hurtigt can starte nogle små spil


from tkinter import *
#import pygame

#klasse som styrer de forskellige frames
class Controller(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(sticky='nsew')
        self.grid_configure()
          
          
        #opstiller vores grid() layout. Det skulle gerne være et 10x10 grid
        for i in range(10):
            root.columnconfigure(i, weight=2,)
            root.rowconfigure(i, weight=2,)
        

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
        #
        self.menu = Start(self)
        self.menu.grid(row=0, column=0, sticky='nsew')
        self.menu.configure(background='#4a4a4a')
        self.menu.tkraise() #Gør at start-menuen vises først når man åbner applikationen "Class Start(Frame)"





#Første frame som er menuen
class Start(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.topButtons()
        

        self.joker = Label(self, text="Joker", bg='black', fg='white')
        self.joker.grid(row=0, column=0,sticky='nsew')
        self.joker1 = Label(self, text="Joker1", bg='black', fg='white')
        self.joker1.grid(row=0, column=1,sticky='nsew')
        self.joker2 = Label(self, text="Joker2", bg='black', fg='white')
        self.joker2.grid(row=0, column=5,sticky='nsew')
        self.joker3 = Label(self, text="Joker3", bg='black', fg='white')
        self.joker3.grid(row=0, column=6,sticky='nsew')
        


        #besked som er på hovedmenuen
        '''self.welcomeMessage = Label(self, text="Velkommen til Quickplay",font=('Terminal', 20), fg='white', bg='#4a4a4a', borderwidth=1, relief="solid")
        self.welcomeMessage.grid(row=0, column=0,columnspan=10, sticky='nsew')
        #self.welcomeMessage.configure(background='#4a4a4a')'''

#Knapper som navigere til de forskellige spil
    def topButtons(self):
        self.firstPage = Button(self, text="Aimlab", background="WHITE", command= self.master.pageOne.tkraise)
        self.firstPage.grid(row=1, column=1,  sticky='nsew')

        self.secondPage = Button(self, text="Pong", background="WHITE", command= self.master.pageTwo.tkraise)
        self.secondPage.grid(row=1, column=3, sticky='nsew')

        self.thirdPage = Button(self, text="Test", background="WHITE", command= self.master.pageThree.tkraise)
        self.thirdPage.grid(row=1, column=5, sticky='nsew')


#frame til spillet AimLab
class aim_Lab(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        self.Label1 = Label(self, text=" Aimlab ", height = 20, width = 52, background="Green")
        self.Label1.grid()
        
        #indfør spillet herunder


#Frame til spillet Pong
class pong(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        self.returnButton()

        self.gameScreen = Label(self, text="spillet vises her", background="cyan")
        self.gameScreen.grid(row=0,column=0, sticky='nsew')

#knap som navigere tilbage til hovedmenu - VIRKER IKKE, men kan vises
    def returnButton(self):
        

        self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=16, command=self.navReturn)
        self.menuReturn.grid(row=0, column=1, sticky='news')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()
        
        #indfør spillet herunder




#Frame til potentielt tredje spil
class TEST(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        self.returnButton()

        self.joker = Label(self, text="Joker", bg='black', fg='white')
        self.joker.grid(row=0, column=0,sticky='ew')
        self.joker1 = Label(self, text="Joker1", bg='black', fg='white')
        self.joker1.grid(row=0, column=1,sticky='nsew')
        self.joker2 = Label(self, text="Joker2", bg='black', fg='white')
        self.joker2.grid(row=0, column=5,sticky='ew')
        self.joker3 = Label(self, text="Joker3", bg='black', fg='white')
        self.joker3.grid(row=0, column=6,sticky='ew')


        self.skærm = Label(self, text=" SKÆRM til spil ", background="cyan", fg='black')
        self.skærm.grid(row=0,column=0, columnspan=10, rowspan=9, sticky='nsew')

        
    def returnButton(self):
            self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=10, command=self.navReturn)
            self.menuReturn.grid(row=9, column=0, sticky='news')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()





def main():
    root = Tk()
    root.title("GAME-PORTAL")
    root.geometry('625x475') 
    app = Controller(root)
    app.pack(expand=True, fill=BOTH)
    
    #kører vores Tkinter
    root.mainloop()
    

if __name__ == '__main__':
    main()


