import pygame
from base import GUIBase
pygame.init()

class Squares(GUIBase):
    def __init__(self, 
                 value: int,
                 pos: tuple,
                 widthpos: tuple,
                 screen: pygame.Surface,
                 changeable: bool
                 ):
        
        super().__init__(0, screen)
        self.__value = value
        self.__pos = pos
        self.__widthpos = widthpos
        self.__changeable = changeable
        self.__pencil = 0
        self.__selected = False
        self.__wrong = False
        self.__unit_selected = False
        self.__is_same_num = False 
    
    @property
    def changeable(self):
        return self.__changeable
        
    @property
    def value(self)->int:
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value
    
    @property
    def selected(self):
        return self.__selected
    @selected.setter
    def selected(self, s: bool):
        self.__selected = s
    
    @property
    def pencil(self):
        return self.__pencil
    @pencil.setter
    def pencil(self, p: int):
        self.__pencil = p
    
    @property
    def wrong(self):
        return self.__wrong
    @wrong.setter
    def wrong(self, w: bool):
        self.__wrong = w
        
    
    @property
    def unit_selected(self):
        return self.__unit_selected

    @unit_selected.setter
    def unit_selected(self, w: bool):
        self.__unit_selected = w
        
    
    @property
    def is_same_num(self):
        return self.__is_same_num

    @is_same_num.setter
    def is_same_num(self, w: bool):
        self.__is_same_num = w
        
    red = (220, 20, 60) 
    darkgray = (169, 169, 169)   
    slategray = (112, 128, 144)
    blue = (135, 206, 235)
    def draw(self):
        space = self.__widthpos[0] // 9
        r, c = (self.__pos[0] * space ) + 225, (self.__pos[1] * space) + 100    
        if not self.__changeable:
            qsize = self.__widthpos[0] // 9
            pygame.draw.rect(self.screen, (135, 206, 235),((r, c), (qsize, qsize)))
        else:
            qsize = self.__widthpos[0] // 9
            pygame.draw.rect(self.screen, (169, 169, 169), ((r, c), (qsize, qsize)))
            
        # event selected  
        if self.__selected:
            pygame.draw.rect(self.screen, (255, 228, 225), ((r, c), (space, space)))
        
        #unit slected
        if self.__unit_selected:
            pygame.draw.rect(self.screen, (204, 242, 255), ((r, c), (space, space)))
        
        # is same number
        if self.__is_same_num:
            pygame.draw.rect(self.screen, (201, 139, 76), ((r, c), (space, space)))
        
        if self.__value != 0:
            font = pygame.font.Font(None, 30)
            if  self.__wrong:
                rgb = (234, 72, 54)
            else:
                rgb = (0, 0, 0)
            v = font.render(str(self.__value), 1, rgb)
            self.screen.blit(v, 
                              (
                                 int(r + ((space / 2) - (v.get_width() / 2))),
                                 int(c + ((space / 2) - (v.get_height() / 2))) 
                              ),
                             )
        elif self.__pencil != 0:
            font = pygame.font.Font(None, 24)
            v = font.render(str(self.__pencil),1,(0, 0, 0))
            self.screen.blit(v,
                             (
                                 int(r + ((space / 2) - (v.get_width() / 2)) - 8),
                                 int(c + ((space / 2) - (v.get_height() / 2)) -8) 
                             ),
                             )
            
