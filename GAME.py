#! /usr/bin/env python

import os, sys, random, pygame
from pygame.locals import *

from mapa import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = pygame.Rect(30, 30, 14, 14)
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 1
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def respawn(self):
        self.rect = pygame.Rect(30, 30, 14, 14)

    def tpup(self):
        self.move_single_axis(0, -60)
    
    def tpdown(self):
        self.move_single_axis(0, 60)
    
    def tpleft(self):
        self.move_single_axis(-60, 0)
    
    def tpright(self):
        self.move_single_axis(60, 0)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
 
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

        for up in ups:
            if self.rect.colliderect(up.rect):
                player.tpup()

        for down in downs:
            if self.rect.colliderect(down.rect):
                player.tpdown()

        for right in rights:
            if self.rect.colliderect(right.rect):
                player.tpright()

        for left in lefts:
            if self.rect.colliderect(left.rect):
                player.tpleft()

        for end in ends:
            if self.rect.colliderect(end.rect):
                sound_effect_fart = pygame.mixer.Sound("sounds/Extremely Loud Fart Sound Effect.mp3")
                sound_effect_fart.play()
                font = pygame.font.SysFont("Roboto Mono", 300, True, False)
                font.set_underline(True)
                text = font.render("You Won!!?", True,(255, 255, 255), (0, 0, 0))
                textrect = text.get_rect()
                textrect.center = ((1920//2, 1080//2))
                screen.blit(text, textrect)
                pygame.display.flip()
                pygame.time.delay(5000)
                pygame.quit()
                sys.exit()

        for respawn in respawns:
            if self.rect.colliderect(respawn.rect):
                player.respawn()

        for jumpscare in jumpscares:
            if self.rect.colliderect(jumpscare.rect):
                js = pygame.image.load("images/michael.png")
                js = pygame.transform.scale(js, (1920, 1080))
                screen.blit(js, (1, 1))
                pygame.display.flip()

                #sound_effect = pygame.mixer.Sound("sounds/Extremely Loud Fart Sound Effect.mp3")
                sound_effect_michael = pygame.mixer.Sound("sounds/Scream Sound Effect (TERRIFYING).mp3")
                sound_effect_michael.play()

        for blackbgf in blackbgsf:
            blackbg = pygame.image.load("images/player_blacked.png")
            screen.blit(blackbg, (1, 1))
            pygame.display.flip()

"""    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.direction.x = -1
            if key[pygame.K_LSHIFT]:
                self.direction.x = -10
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
            if key[pygame.K_LSHIFT]:
                self.direction.x = 10
        else:
            self.direction.x = 0

        if key[pygame.K_UP]:
            self.direction.y = -1
            if key[pygame.K_LSHIFT]:
                self.direction.y = -10
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
            if key[pygame.K_LSHIFT]:
                self.direction.y = 10
        else:
            self.direction.y = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
"""
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        walls.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/wall.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Up(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        ups.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/up.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Down(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        downs.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/down.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Left(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        lefts.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/left.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Right(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        rights.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/right.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class End(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        ends.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/end.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Reset(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        respawns.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/reset.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Jumpscare(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        jumpscares.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/jumpscare.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
class Blackbg(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        blackbgsf.append(self)
        super().__init__(group)
        self.image = pygame.image.load("images/player_blacked.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, 0)
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.zoom_scale = 2
        self.internal_surf_size = (1920,1080)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h
 
         #pozadi
        #self.ground_surf = pygame.image.load("images/pozadi.png").convert_alpha()
        #self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self,player):
        self.center_target_camera(player)
        self.internal_surf.fill((0, 0, 0))
         #pozadi
        #ground_offset = self.ground_rect.topleft - self.offset
        #self.display_surface.blit(self.ground_surf,ground_offset)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image, offset_pos)

        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))
        self.display_surface.blit(scaled_surf,scaled_rect)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("zlaty bludistak")
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)

clock = pygame.time.Clock()
camera_group = CameraGroup()
player = Player((30,30),camera_group)
walls = []
ups = []
downs = []
lefts = []
rights = []
ends = []
respawns = []
jumpscares = []
blackbgsf = []
level = mapa

x = y = 0
for row in level:
    for col in row:
        if col == "@":
            Wall((x, y),camera_group)
        if col == "R":
            Reset((x,y),camera_group)
        if col == "W":
            End((x,y),camera_group)
        if col == "=":
            Up((x, y),camera_group)
        if col == "+":
            Down((x, y),camera_group)
        if col == "#":
            Left((x, y),camera_group)
        if col == "*":
            Right((x, y),camera_group)
        if col == "J":
            Jumpscare((x,y),camera_group)
        x += 16
    y += 16
    x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            player.respawn()
 
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
        if key[pygame.K_LSHIFT]:
            player.move(-10, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
        if key[pygame.K_LSHIFT]:
            player.move(10, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
        if key[pygame.K_LSHIFT]:
            player.move(0, -10)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
        if key[pygame.K_LSHIFT]:
            player.move(0, 10)

    if e.type == pygame.MOUSEWHEEL:
        camera_group.zoom_scale += e.y * 0.03

    # Draw the scene
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for end in ends:
        pygame.draw.rect(screen, (255, 0, 0), end.rect)
    for respawn in respawns:
        pygame.draw.rect(screen, (100, 0, 200), respawn.rect)
    for up in ups:
        pygame.draw.rect(screen, (255, 200, 100), up.rect)
    for down in downs:
        pygame.draw.rect(screen, (255, 200, 200), down.rect)
    for left in lefts:
        pygame.draw.rect(screen, (255, 100, 100), left.rect)
    for right in rights:
        pygame.draw.rect(screen, (255, 100, 200), right.rect)
    for jumpscare in jumpscares:
        pygame.draw.rect(screen, (10, 10, 10),jumpscare.rect)
    for blackbgf in blackbgsf:
        pygame.draw.rect(screen, (10, 10, 10),blackbgf.rect)
    # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))

    camera_group.update()
    camera_group.custom_draw(player)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(360)
 
pygame.quit()