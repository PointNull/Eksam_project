#pong game
import pygame, sys, random

#starter pygame 
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

player_score, bot_score = 0, 0 #starter pointsystemet med 0

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