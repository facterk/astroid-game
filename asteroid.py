import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    containers = ()
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius, *Asteroid.containers)

    def draw(self,screen):
        result = pygame.draw.circle(screen,"white",self.position , self.radius , 2)
        return result
    
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20 , 50)

        vel1 = self.velocity.rotate(random_angle)*1.2
        vel2 = self.velocity.rotate(-random_angle)*1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS


        ast1 = Asteroid(self.position.x , self.position.y ,new_radius)
        ast1.velocity = vel1

        ast2 = Asteroid(self.position.x , self.position.y ,new_radius)
        ast2.velocity = vel2

