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
        self.returnButton()
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        
            self.button = Button(self, text="Pong", command=self.start_Pong)
            self.button.grid(column=2, row=2, sticky='nsew')

    def returnButton(self):
        self.menuReturn = Button(self, text="back to menu", background="white", height=2, width=10, command=self.navReturn)
        self.menuReturn.grid(column=0, row=4, columnspan=1, rowspan=2,  sticky='swen')

    #funktion som navigere tilbage til hovedmenu (Frame)
    def navReturn(self):
        self.Controller.menu.tkraise()

    def start_Pong(self):
        game = PongGame(800, 500)
        game.run()


class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 2

    def move_up(self):
        if self.top > 0:
            self.top -= self.speed

    def move_down(self, screen_height):
        if self.bottom < screen_height:
            self.bottom += self.speed

class Ball(pygame.Rect):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.x_speed = 1
        self.y_speed = 1

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def reset(self, screen_width, screen_height):
        self.center = (screen_width // 2, screen_height // 2)
        self.x_speed = random.choice([-1, 1])
        self.y_speed = random.choice([-1, 1])

    def x_velocity(self):
        self.x_speed *= -1

    def y_velocity(self):
        self.y_speed *= -1

class Bot(Paddle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def track_ball(self, ball, screen_height):
        if self.top < ball.centery and self.bottom < screen_height:
            self.move_down(screen_height)
        if self.bottom > ball.centery and self.top > 0:
            self.move_up()

class PongGame:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pong!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Consolas", int(screen_width / 20))
        self.player = Paddle(50, screen_height // 2 - 25, 5, 75)
        self.bot = Bot(screen_width - 50, screen_height // 2 - 25, 5, 75)
        self.ball = Ball(screen_width // 2 - 5, screen_height // 2 - 5, 5)
        self.player_score = 0
        self.bot_score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.player.move_up()
        if keys_pressed[pygame.K_DOWN]:
            self.player.move_down(self.screen_height)

    def update_game(self):
        self.ball.move()

        # Ball collision detection
        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball.y_velocity()

        if self.ball.right >= self.screen_width:
            self.bot_score += 1  # Increment bot's score when ball goes off right side
            self.ball.reset(self.screen_width, self.screen_height)

        if self.ball.left <= 0:
            self.player_score += 1  # Increment player's score when ball goes off left side
            self.ball.reset(self.screen_width, self.screen_height)

        # Paddle collision detection
        if self.player.left - self.ball.radius <= self.ball.left <= self.player.left and self.ball.centery in range(self.player.top, self.player.bottom):
            self.ball.x_velocity()

        if self.bot.right + self.ball.radius >= self.ball.right >= self.bot.right and self.ball.centery in range(self.bot.top, self.bot.bottom):
            self.ball.x_velocity()

        # Bot AI
        self.bot.track_ball(self.ball, self.screen_height)


    def draw_game(self):
        self.screen.fill("black")
        pygame.draw.rect(self.screen, "white", self.player)
        pygame.draw.rect(self.screen, "white", self.bot)
        pygame.draw.circle(self.screen, "white", self.ball.center, self.ball.radius)

        player_score_text = self.font.render(str(self.player_score), True, "white")
        bot_score_text = self.font.render(str(self.bot_score), True, "white")
        self.screen.blit(player_score_text, (self.screen_width // 2 + 25, 25))
        self.screen.blit(bot_score_text, (self.screen_width // 2 - 25, 25))

        pygame.display.update()

    def run(self):
        while True:
            self.handle_events()
            self.handle_input()
            self.update_game()
            self.draw_game()
            self.clock.tick(300)

#Frame til potentielt tredje spil
class TEST(Frame):
    def __init__(self, Controller):
        Frame.__init__(self, Controller)
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