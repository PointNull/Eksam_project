#Vi skal have lavet et eksamens projekt som er rimeligt gennemført. Det er en spilportal som ligger lokalt på ens computer- 
#og hurtigt can starte nogle små spil


from tkinter import *
import pygame
import sys
import random
import math

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
        self.pageOne.configure(background='#4a4a4a')
        self.pageOne.grid(row=0, column=0, sticky='nsew')
        #
        self.pageTwo = pong(self)
        self.pageTwo.configure(background='#4a4a4a')
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


        self.title = Label(self, text='Velkommen til QuickPlay')
        self.title.grid(column=2, row=1, sticky='nsew')

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
        self.returnButton()
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        
        self.button = Button(self, text="aimlab", command=self.start_aimlab)
        self.button.grid(column=2, row=2, sticky='nsew')

    def returnButton(self):
        self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=10, command=self.navReturn)
        self.menuReturn.grid(column=0, row=5, columnspan=1, rowspan=2,  sticky='swen')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()

    def start_aimlab(self):
        AimLabGame().run_game()

#indfør spillet herunder
class AimLabGame:
    def __init__(self):
        self.running = False

    def run_game(self):
        self.running = True
        # Initialize Pygame
        pygame.init()

        # Set up display
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Circle class
        class Circle:
            def __init__(self, radius):
                self.radius = radius
                self.circleX, self.circleY = self.generate_random_position()
                self.circleHits = 0
                self.circleMisses = 0

            def generate_random_position(self):
                circleX = random.randint(self.radius, width - self.radius)
                circleY = random.randint(self.radius, height - self.radius)
                return circleX, circleY

            def draw(self):
                pygame.draw.circle(screen, BLACK, (self.circleX, self.circleY), self.radius)

            def respawn(self):
                self.circleX, self.circleY = self.generate_random_position()

        # Player class
        class Player:
            def __init__(self):
                self.mousePosition = (0,0)

            def update(self):
                self.mousePosition = pygame.mouse.get_pos()

        # Topbar class
        class Topbar:
            def __init__(self):
                self.hits = 0
                self.misses = 0
                self.font = pygame.font.Font(None, 36)
                self.startTime = pygame.time.get_ticks()

            def updateHits(self, hits):
                self.hits = hits

            def updateMisses(self, misses):
                self.misses = misses

            def draw(self):
                textSurfaceHits = self.font.render("Hits: " + str(self.hits), True, BLACK)
                textSurfaceMisses = self.font.render("Misses: " + str(self.misses), True, BLACK)
                screen.blit(textSurfaceHits, (10, 10))
                screen.blit(textSurfaceMisses, (width - 200, 10))

        # Main function
        def main():
            clock = pygame.time.Clock()

            # Create a circle object
            circle = Circle(28)

            # Create a player object
            player = Player()

            # Create a topbar object
            topbar = Topbar()

            # Main loop
            while self.running:
                screen.fill(WHITE)

                # Draw the circle
                circle.draw()

                # Update player's position
                player.update()

                # Draw the topbar
                topbar.draw()

                # Check for events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            distance = math.sqrt((player.mousePosition[0] - circle.circleX) ** 2 + (player.mousePosition[1] - circle.circleY) ** 2)
                            if distance <= circle.radius:
                                circle.respawn()
                                circle.circleHits += 1
                                topbar.updateHits(circle.circleHits)
                            else:
                                circle.circleMisses += 1
                                topbar.updateMisses(circle.circleMisses)

                # Update the display
                pygame.display.flip()
                clock.tick(60)

            pygame.quit()

        # Run the game
        main()

#Frame til spillet Pong
class pong(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
        self.Controller = Controller
        self.returnButton()
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        
            self.button = Button(self, text="Pong", command=self.start_Pong)
            self.button.grid(column=2, row=2, sticky='nsew')

    def returnButton(self):
        self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=10, command=self.navReturn)
        self.menuReturn.grid(column=0, row=5, columnspan=1, rowspan=2,  sticky='swen')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()

    def start_Pong(self):
        PongGame().run_game()

#indfør spillet herunder
class PongGame:
    def __init__(self):
        self.running = False

    def run_game(self):
        self.running = True
        # Initialize Pygame
        pygame.init()

        #defineret vores vindue når spillet starter
        WIDTH, HEIGHT = 800, 500
        
        FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))

        #størrelsen på spillet når det starter (Starter med det samme spillet åbner) 
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        #titel på vores vindue
        pygame.display.set_caption("Pong!")
        CLOCK = pygame.time.Clock()
        
        #Paddles - vores spiller og computer visuelt
        player = pygame.Rect(50, HEIGHT/2-25, 5,75) #størrelsen på vores paddles
        bot = pygame.Rect(WIDTH-50, HEIGHT/2-25, 5, 75)

        #bolden - 
        ball = pygame.Rect(WIDTH/2-5, HEIGHT/2-5, 10, 10) #størrelsen på bolden
        #farten på bolden i x- og y-aksen 
        x_speed, y_speed = 1, 1 #hvis x=1 så rykker den til højre. Hvis x=-1 så rykker den til venstre. derved y=1 ned og y=-1 op

        player_score, bot_score = 0, 0 #starter pointsystemet med 0-0

        #"while-loop" som kører mens programmet er igang
        while True:
            
            #movement for player
            keys_pressed = pygame.key.get_pressed()

            #movements opad - Dette opdatere også positionen for vores paddles
            if keys_pressed[pygame.K_UP]: #definere hvilken key på tastaturet
                if player.top > 0: #begrænser hvor højt vores paddle kan gå op
                    player.top -=2 #hvor højt vores paddle går op pr. gang man trykker
            #movement nedad
            if keys_pressed[pygame.K_DOWN]: 
                if player.bottom < HEIGHT: 
                    player.bottom +=2
            
            #afslutter vores program uden at det opstår errors
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #boldens logik
            #top og bund detection -  sørger for at bolden forbilver inden for vores vindue
            if ball.y >= HEIGHT: #Hvis boldens y-koordinat er større eller lig højden af vinduet så skal den ændre sin retning fra op til ned (-1)
                y_speed = -1
            if ball.y <= 0: #Hvis boldens y-koordinat er større eller lig bunden af vinduet så skal den ændre sin retning fra ned til op (1)
                y_speed = 1
            
            #højre og venstre detection - sørger for at bolden bliver centreret hvis der bliver scoret eller skifter retning hvis den rammer en paddle
            if ball.x >= WIDTH: #hvis bolden x-koordinat er større end/lig med vinduet (højre side)
                player_score += 1 #tilføjer point
                ball.center = (WIDTH/2, HEIGHT/2) # centrere vores bold efter der er blevet scoret
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1]) #når bolden centreres sendes den i en tilfældig retning
            #hvis computer scorer
            if ball.x <= 0:
                bot_score += 1
                ball.center = (WIDTH/2, HEIGHT/2) # centrere vores bold efter der er blevet scoret
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1]) #når bolden centreres sendes den i en tilfældig retning
        
            #padlle collision detection
            if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
                x_speed = 1
            if bot.x - ball.width <= ball.x <= bot.x and ball.y in range(bot.top-ball.width, bot.bottom+ball.width):
                x_speed = -1


            #score-system
            
            #visuelt vores score-system
            player_score_text = FONT.render(str(player_score), True, 'white')
            bot_score_text = FONT.render(str(bot_score), True, 'white')

            #boldens movement som også bliver opdateret imens programmet kører
            ball.x += x_speed *1
            ball.y += y_speed *1

            #bot-paddle-ai (meget simpel - umulig sværhedsgrad)
            if bot.y < ball.y and bot.bottom < HEIGHT: #følger efter boldens y-koordinat
                bot.top += 1
            if bot.bottom > ball.y and bot.top > 0:
                bot.bottom += -1

            #opdatere vores skrærm så ting der bevæger sig ikke forbliver på skræmen når de bevæger sig.
            SCREEN.fill('black')
        
            #tegner vores paddles, bolden og score-system
            pygame.draw.rect(SCREEN, "white", player)
            pygame.draw.rect(SCREEN, "white", bot)
            pygame.draw.circle(SCREEN, 'white', ball.center, 5)

            SCREEN.blit(player_score_text, (WIDTH/2+25, 25))
            SCREEN.blit(bot_score_text, (WIDTH/2-25, 25))

            #updatere spillet med 300 ticks
            pygame.display.update()
            CLOCK.tick(300)



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


