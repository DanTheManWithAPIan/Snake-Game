import pygame
import random
from pygame.locals import (
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT
)

pygame.init()
pygame.display.set_caption('Daniel Snake Game')
width = 500
height = 500
max_width = 500
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
points = pygame.font.Font(None, 45)


class Snake:
    def __init__(self):
        self.vel = 20
        self.length = 1
        self.facing = 'S'
        # Payer below until Apple
        self.snake = []
        self.x = 20
        self.y = 20
        self.tail = [(self.x, self.y)]
        self.player_surface = pygame.Surface((20, 20))
        self.rect = self.player_surface.get_rect(topleft=(self.x, self.y))
        self.snake.append(self.rect)

    def display_head(self):
        self.player_surface.fill(green)
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(screen, green, self.rect, 0)

    def render_tail(self):
        if len(player.tail) > self.length:
            self.tail.pop(-1)
        self.tail = self.tail[:player.length]
        # Draw Snake and tail
        for segment in self.tail:
            pygame.draw.rect(screen, green, (segment[0], segment[1], 20, 20))


class Apple:
    def __init__(self):
        self.app_x = random.randrange(20, 480, 20)
        self.app_y = random.randrange(20, 480, 20)
        self.apple_surface = pygame.Surface((22, 22))
        self.apple_rect = None

    def display_apple(self):
        # filling the apple red
        self.apple_surface.fill(red)
        # updating the apple rect
        self.apple_rect = self.apple_surface.get_rect(topleft=(self.app_x, self.app_y))
        # if the player and apple are in the same square reset the apple coordinates and add 1 length to the snake
        if player.x == self.app_x and player.y == self.app_y:
            self.app_x = random.randrange(20, 480, 20)
            self.app_y = random.randrange(20, 480, 20)
            player.length += 1
        pygame.draw.rect(screen, red, self.apple_rect, 0)


player = Snake()
apple = Apple()


# Draw grid function for drawing background grid
def draw_grid():
    block_size = 20
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, green, rect, 1)


# Detecting if the player leaves the screen or hits themselves
def lose_detection():
    if player.y > max_width - 40 or player.y < 20 or player.x > max_width - 40 or player.x < 20:
        return True
    for pos, i in player.tail[1:]:
        if player.x == pos and player.y == i:
            print(pos, i)
            return True


def points_score():
    point_surface = points.render(str(player.length), True, (255, 255, 255))
    screen.blit(point_surface, (2, 2))


def main_game_loop():
    running = True
    counter = 0
    while running:
        pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pressed_key[K_ESCAPE]:
                running = False
            if pressed_key[K_UP]:
                player.facing = 'N'
            if pressed_key[K_RIGHT]:
                player.facing = 'E'
            if pressed_key[K_LEFT]:
                player.facing = 'W'
            if pressed_key[K_DOWN]:
                player.facing = 'S'

        counter += 1
        if lose_detection():
            running = False

        if player.facing == 'N' and counter == 250:
            counter = 0
            player.y -= player.vel
            player.tail.insert(0, (player.x, player.y))
        if player.facing == 'E' and counter == 250:
            counter = 0
            player.x += player.vel
            player.tail.insert(0, (player.x, player.y))
        if player.facing == 'W' and counter == 250:
            counter = 0
            player.x -= player.vel
            player.tail.insert(0, (player.x, player.y))
        if player.facing == 'S' and counter == 250:
            counter = 0
            player.y += player.vel
            player.tail.insert(0, (player.x, player.y))

        screen.fill(black)
        draw_grid()
        player.render_tail()
        apple.display_apple()
        player.display_head()
        points_score()
        pygame.display.flip()


main_game_loop()
