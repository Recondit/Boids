from random import *
from boid import Boid


class Boids:
    def __init__(self , number , radius , width , height):
        self.boids = [Boid(randint(0 , width-1) , randint(0 , height-1), radius , width , height , i) for i in range(number)]
    
    def run(self):
        for boid in self.boids:
            boid.run()
            boid.behaviour(self.boids)


    
