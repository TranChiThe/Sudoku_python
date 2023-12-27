import pygame
class GUIBase:
    def __init__(self, size: tuple, screen: pygame.Surface):
        self.__size = size
        self.__screen = screen
        
    @property
    def size(self):
        return self.__size
    
    @property
    def screen(self):
        return self.__screen
    
    def draw(self):
        pass
    
    def draw_option(self):
        pass
    
    def _type(self, txt: str, rgb: tuple, pos: tuple, fsize: int):
        font = pygame.font.Font(None, fsize)
        v = font.render(txt, 1, rgb)
        self.__screen.blit(v, pos)