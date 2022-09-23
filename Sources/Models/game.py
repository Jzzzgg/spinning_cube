from Models.exceptionHandling import GameError 
import pygame


class Game:
    def __init__(self):
        # Initializing variable
        print("Initializing game ...")
        self.running = True
        try:
            # Call initGame function to create the game
            self.initGame()
        except Exception as e:
            print("Failed to initializing game:", e)

    def initGame(self):
        # Setting the attributes
        self.setting()
        print("Game initializing successfully!")
        while self.running:
            # Quit the game window when user click on close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        self.quit_game()
        return 
        
    def setting(self):
        #Initializing the game window
        pygame.init()
        pygame.display.set_caption('Spinning')
        (width, height) = (1000, 1000)
        screen = pygame.display.set_mode([width, height])
        icon = pygame.image.load(r'.\Assets\icon.jpg')
        pygame.display.set_icon(icon)
        # Fill the background with white
        screen.fill((255, 255, 255))
        # Flip the display
        pygame.display.flip()
        return 

    def quit_game(self):
        print("Quiting the game ...")
        # Quit.
        pygame.quit()
        print("Quited")
        return