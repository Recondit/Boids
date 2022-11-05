#Imports
import pygame
import sys
import math
from random import *
from boids import Boids
from button import Button


#Configuration
pygame.init()
fps=100
fpsClock=pygame.time.Clock()
width,height = 1280 , 720
screen = pygame.display.set_mode((width,height))


light = pygame.Color("#DBBEA1")
dark = pygame.Color("#04151F")
#Game Configuration
n = 10
radius = 10




 












def length2D(vec):
    return math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])

def draw_boids(sc, boids):
    for boid in boids:
        pygame.draw.circle(sc, light, boid.pos, radius)
        # pg.draw.circle(sc, "yellow", boid.pos, boid.perception/2, 1)

def draw_menu(sc):
    pygame.draw.rect(sc , light , pygame.Rect(30 , 30 , 60 , 60))
    
#Game Loop
if __name__ == "__main__": 
    boids = Boids(n , radius , width , height)
    while True:
        screen.fill(dark)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_boids(screen, boids.boids)
        draw_menu(screen)
        boids.run()

            



        pygame.display.set_caption("$~Boids ~fps: " + str(round(fpsClock.get_fps(), 2)))
        pygame.display.update()
        fpsClock.tick(fps)
