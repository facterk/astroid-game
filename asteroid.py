import pygame
from circleshape import CircleShape
class Astroid(CircleShape):
    containers = ()
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius, *Astroid.containers)

    def draw(self,screen):
        result = pygame.draw.circle(screen,"white",self.position , self.radius , 2)
        return result
    
    def update(self, dt):
        self.position += self.velocity*dt