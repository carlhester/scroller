import pygame
import sys
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, x, y):
        super(Platform, self).__init__()
        self.x = x
        self.y = y
    
        #create the level art
        imgGround = pygame.image.load('green.png').convert()
        imgGroundSurf = pygame.Surface((32,32))
        self.platform = pygame.transform.scale(imgGround, (32,32), imgGroundSurf)
        #imgGroundSurf.blit(imgGround, (self.x, self.y))

        self.rect = imgGroundSurf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self, screen):
        screen.blit(self.platform, self.rect)


class Player(Sprite):
    def __init__(self, screen, x, y):
        super(Player, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.x = x
        self.y = y
        self.left = self.right = self.up = self.down = 0

        imgPlayer = pygame.image.load('bread.png').convert()
        imgPlayerSurf = pygame.Surface((72,72), pygame.SRCALPHA).convert()
        imgPlayerSurf.blit(imgPlayer, (0,0))

        self.character = pygame.transform.scale(imgPlayerSurf, (32,32))
        self.rect = imgPlayerSurf.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

    def update(self, screen):
        screen.blit(self.character, self.rect)

def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(50)

    # our canvas
    screen_width = 640
    screen_height = 480
    bg_color = (0,0,0)
    DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    # keep track of everything that can collide
    player_entities = pygame.sprite.Group()
    level_entities = pygame.sprite.Group()

    #instantiate the player 
    player = Player(DISPLAYSURF, 0, 0)
    player_entities.add(player)


    # draw the map
    level =["########################",
            "#                      #",
            "#             ##       #",
            "#     ###              #",
            "#      #               #",
            "#     ###      ###     #",
            "#                      #",
            "#                 ###  #",
            "#            ##        #",
            "#                      #",
            "#     ###  ###         #",
            "#  ###                 #",
            "#                      #",
            "#                      #",
            "########################"]
    board_x = 0
    board_y = 0    
    for x in level:
        for y in x:
            if y == "#":
                platform = Platform(board_x, board_y)
                platform.update(DISPLAYSURF)
                level_entities.add(platform)
            board_x += 32
        board_y += 32
        board_x = 0

    while True:
        DISPLAYSURF.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                   player.left = 1
                if event.key == pygame.K_RIGHT:
                    player.right = 1
                if event.key == pygame.K_UP:
                   player.up = 1
                if event.key == pygame.K_DOWN:
                    player.down = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.left = 0
                if event.key == pygame.K_RIGHT:
                    player.right = 0
                if event.key == pygame.K_UP:
                    player.up = 0
                if event.key == pygame.K_DOWN:
                    player.down = 0

        if player.left == 1:
            for i in level_entities:
                i.rect.centerx += 5 
        if player.right == 1:
            for i in level_entities:
                i.rect.centerx -= 5 
        if player.up == 1:
            for i in level_entities:
                i.rect.centery += 5 
        if player.down == 1:
            for i in level_entities:
                i.rect.centery -= 5 








        for i in player_entities:
            i.update(DISPLAYSURF)

        for i in level_entities:
            i.update(DISPLAYSURF)

        pygame.display.update()


if __name__ == "__main__":
    run_game()
