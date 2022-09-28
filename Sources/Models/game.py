from Models.exceptionHandling import Error 
import pygame
import time


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
        
        
        # Game thread
        while self.running:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                        self.spinning_cube()
                

        # call quit function to quit the game
        self.quit_game()

        return 
        
    def setting(self):
        #Initializing the game window
        pygame.init()

        #Set title
        pygame.display.set_caption('Spinning')

        #Set window size
        (width, height) = (1000, 1000)
        self.screen = pygame.display.set_mode([width, height])

        #Set icon
        icon = pygame.image.load(r'.\Assets\icon.jpg')
        pygame.display.set_icon(icon)

        # Fill the background with white
        self.screen.fill((255, 255, 255))

        #Draw Cube Button
        self.darw_button('black', 'white', 'Cube', (0, 0), (50 , 25))

        #Draw Heart Button
        self.darw_button('black', 'white', 'Heart', (52, 0), (50 , 25))
        
        # Flip the display
        pygame.display.flip()
        
        return 

    def darw_button(self, bg_color, text_color, info, location, size):
        #Read input args
        color_light = text_color
        color_dark = bg_color
        x, y = location
        weight, hight = size
        FONT_FAMILY = "Gill Sans"

        #Set font
        font = pygame.font.SysFont(FONT_FAMILY,19) 
        text = font.render(info , True , color_light)

        #Draw button
        pygame.draw.rect(self.screen, color_dark, [x, y, weight , hight])
        self.screen.blit(text , (x , y))

        pygame.display.flip()

        return


    def spinning_cube(self):

        
        # Draw Square
        self.darw_square('black', (400,400), (200,200))

        pygame.display.flip()


    def darw_square(self, color, location, size):
        x, y = location
        weight, height = size
        orgianl_weight = weight
        orgianl_hight = height
        rotate = True

        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, weight, height))


        for _ in range(100): 
            # Drawing Rectangle
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, color, pygame.Rect(x, y, weight, height))
            print('loop', _ , rotate)
            print(not (0 < weight < orgianl_weight))
            
            pygame.display.flip()
            if  weight < 0 or  weight > orgianl_weight:
                rotate = not rotate 
            if rotate: 
                weight -= 20
                x += 10
                time.sleep(0.08)
                pygame.draw.rect(self.screen, color, pygame.Rect(x, y, weight, height))
            else:
                weight += 20
                x -= 10
                time.sleep(0.08)
                pygame.draw.rect(self.screen, color, pygame.Rect(x, y, weight, height))
                
            pygame.display.flip()
        
        #flip
        pygame.display.flip()
        
    def fill_screen(self):
        pass

    def quit_game(self):
        # Quit.
        print("Quiting the game ...")
        pygame.quit()
        print("Quited")
        return