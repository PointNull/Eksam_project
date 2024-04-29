import pygame
import random
import math


# Initialiser Pygame
pygame.init()

# Set up displayet
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("min aimlab")


# Cirkel klasse
class Circle:
    def __init__(self, radius):
        # Initialiser cirklens randomkoordinater, radius, hits og misses
        self.radius = radius
        self.circleX, self.circleY = self.generate_random_position()
        self.circleHits = 0
        self.circleMisses = 0

    def generate_random_position(self):
        # Generer en random position for cirklen indenfor skærmens kanter
        circleX = random.randint(self.radius, width - self.radius)
        circleY = random.randint(self.radius, height - self.radius)
        return circleX, circleY

    def draw(self, screen):
        # tegn cirklen på skærmen
        pygame.draw.circle(screen, 'black', (self.circleX, self.circleY), self.radius)

    def respawn(self):
        # Flyt cirklen til en ny random position
        self.circleX, self.circleY = self.generate_random_position()

mouse_pos = pygame.mouse.get_pos()

class Player:
    def __init__(self):
        # Initialiser musens position
        self.mousePosition = (0,0)

    def update(self):
        # Opdater musens position
        self.mousePosition = pygame.mouse.get_pos()

    def get_position(self):
        # returner positionens værdig til variablen
        return self.mousePosition
    

class Topbar:
    
    def __init__(self):
        # Initialiser vores værdier til Topbaren
        self.hits = 0
        self.misses = 0
        self.font = pygame.font.Font(None, 36)  
        self.startTime = pygame.time.get_ticks()
    def updateHits(self, hits):
        # Opdater hits
        self.hits = hits

    def updateMisses(self, misses):
        # Opdater misses
        self.misses = misses

    def draw(self, screen):
        # Fremstille tekstens font
        textSurfaceHits = self.font.render("Hits: " + str(self.hits), True, (0, 0, 0))
        textSurfaceMisses = self.font.render("Misses: " + str(self.misses), True, (0, 0, 0))
        # Beregn placering af misses
        missesText_width = textSurfaceMisses.get_width()
        screen_width = screen.get_width()
        missesText_width = screen_width - missesText_width - 10
        # Beregn tiden med timer
        elapsed_time = (pygame.time.get_ticks() - self.startTime) // 1000
        textSurfaceTimer = self.font.render("Time: " + str(elapsed_time), True, (0, 0, 0))
        # Generer textSurface på toppen af skærmen
        screen.blit(textSurfaceHits, (10, 10))
        screen.blit(textSurfaceMisses, (screen_width - missesText_width - 10, 10))
        screen.blit(textSurfaceTimer, (10, 50))

# Main funktion
def main():
    running = True
    clock = pygame.time.Clock()

    # Lav et cirkel objekt
    circle = Circle(28)

    # Lav et spiller objekt
    player = Player()

    # lav et topbar objekt
    topbar = Topbar()
    
    # Dette er et while loop som altid kører da det kører når programmet kører
    while running:
        screen.fill('white')

        # Generer ciklen på skærmen
        circle.draw(screen)

        # Opdater spillerens position(musen)
        player.update()

        # Generer topbaren på skærmen
        topbar.draw(screen)
        
        # For Loop for det forskellige events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Respawn cirklen og læg 1 til enten hits eller misses, når ventre mus er trykket
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Venstre musseknap
                    if distance <= circle.radius:
                        circle.respawn()
                        circle.circleHits += 1  # Læg 1 til hits tælleren
                        topbar.updateHits(circle.circleHits)
                    else:
                        circle.circleMisses += 1 # Læg 1 til misses tælleren
                        topbar.updateMisses(circle.circleMisses)
        # Tjek om mussen er indenfor cirklens radius
        distance = math.sqrt((player.mousePosition[0] - circle.circleX) ** 2 + (player.mousePosition[1] - circle.circleY) ** 2)

        # Skift cirklen farve til rød hvis mus er indenfor radius
        if distance <= circle.radius:
            circle.color = 'red' 
        else:
            circle.color = 'black'
        
        # Generer cirklen med cirklens givne farve
        pygame.draw.circle(screen, circle.color, (circle.circleX, circle.circleY), circle.radius)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()