import pygame
import sys
import time
from pygame.locals import *
import random
import pygame.freetype


pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 56)
screen = pygame.display.set_mode((800,600 ), 0, 32)
red = (255, 0, 0)
purple = (255, 0, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
frequencies = {'left': 0.1, 'right': 0.05, 'up': 0.03333, 'down': 0.025}

class rectangle():
    def __init__(self, x, y, width, height, color, frequency,direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.frequency = frequency
        self.text = font.render(direction, True,(255,255, 255))
    def blinking(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()
        time.sleep(self.frequency)
        pygame.draw.rect(screen, black, (self.x, self.y, self.width, self.height))
        pygame.display.update()
        time.sleep(self.frequency)
    def draw_rect(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()
    def draw_text(self):
        screen.blit(self.text, (self.x+150, self.y+125))
        pygame.display.update()
    def draw(self):
        self.draw_rect()
        self.draw_text()

def random_blinking(rect):
    nums = 0
    rounds = 2.5 / rect.frequency
    while nums<=rounds:
        rect.blinking()
        nums += 1

trials = 4
red_rec = rectangle(0, 0, 400, 300, red, frequencies['left'],'left')
purple_rec = rectangle(400, 0, 400, 300, purple, frequencies['right'],'right')
green_rec = rectangle(0, 300, 400, 300, green, frequencies['up'],'up')
blue_rec = rectangle(400, 300, 400, 300, blue, frequencies['down'],'down')
rectangles = {red_rec: 0, purple_rec: 0, green_rec: 0, blue_rec: 0}

def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        red_rec.draw()
        purple_rec.draw()
        green_rec.draw()
        blue_rec.draw()
        time.sleep(1)    

        if(len(rectangles)!=0):
            random_rectangle = random.choice(list(rectangles.keys()))
            rectangles[random_rectangle] += 1
            if rectangles[random_rectangle] == trials:
                del rectangles[random_rectangle]
            random_blinking(random_rectangle)
        


main()
    