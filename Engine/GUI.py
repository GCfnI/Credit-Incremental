import pygame as py
class Button:
    def __init__(self, name, loading_dict, x, y, command, surface):
        self.surface = surface
        self.images = loading_dict[name]
        self.rect = self.images['unpressed'].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.command = command
        #Above handles the button position and the hitbox
        self.name  = name
    def display(self):
        pos = py.mouse.get_pos()
        left_click = py.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(pos):
            self.surface.blit(self.images['hovered'], (self.rect.x, self.rect.y))
            
            if left_click:
                self.clicked = True
                self.surface.blit(self.images['pressed'], (self.rect.x, self.rect.y))
                
            elif not left_click and self.clicked:
                self.clicked = False
                self.command()
        else:
            self.clicked = False
            self.surface.blit(self.images['unpressed'], (self.rect.x, self.rect.y))
