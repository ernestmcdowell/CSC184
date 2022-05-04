import pygame, sys, time
from settings import *
from level import Level

class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Atlas')
        self.clock = pygame.time.Clock()
        self.level = Level()
 
    def run(self):
        last_time = time.time()
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # game logic
            
            pygame.display.update()
            self.screen.fill('black')
            self.level.run()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()