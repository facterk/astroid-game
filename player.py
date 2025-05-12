import pygame
from circleshape import CircleShape
from constants import *
from shots import Shot
class Player(CircleShape):
    containers = ()
    def __init__(self,x,y,):
        super().__init__(x , y , PLAYER_RADIUS, *Player.containers)
        self.rotation = 0
        self.shot_timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 
        return self.rotation
    

    def update(self, dt):
        if self.shot_timer > 0 :
            self.shot_timer -= dt
            if self.shot_timer < 0:
                self.shot_timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        if self.shot_timer > 0 :
            return 
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
        shot.velocity = velocity
        self.shot_timer = PLAYER_SHOOT_COOLDOWN