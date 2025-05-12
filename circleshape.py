import pygame
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, *groups):
        super().__init__(*groups)
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else :
            super().__init__()
    
    def draw(self, screen):
        result = pygame.draw.polygon(screen,"white", self.triangle(), 2)
        return result

    def update(self,dt):
        pass

    def collision_check(self, target):
        distance = self.position.distance_to(target.position)
        return distance <= (self.radius + target.radius)