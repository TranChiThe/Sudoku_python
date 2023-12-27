import pygame
import sys
class Menu:
    def __init__(self) -> None:
        self.running = True
        self.__screen_size = (850, 650)
        self.__screen = pygame.display.set_mode(self.__screen_size[0:2])
        self.easy = False
        self.medium = False
        self.hard = False
        self.very_hard = False
        self.insane = False
        self.custom = False
        self._continue = False
        self.guide = False
        self.quit = False
        self.error_data = False
        self.time_press_btn = 0
        pygame.display.set_caption("Sudoku")
        
    def init_btn(self):
        self.easy = False
        self.medium = False
        self.hard = False
        self.very_hard = False
        self.insane = False
        self.custom = False
        self._continue = False
        self.guide = False  
        self.quit = False
        
    def draw_warning_continue(self):
        font = pygame.font.Font(None, 24)
        text = font.render("You don't have data", True, "red")
        text_rect = text.get_rect(center=(130, 500))
        self.__screen.blit(text, text_rect)
        
    def loop(self):
        clock = pygame.time.Clock()
        current_time = 0
        while self.running:
            # Vẽ background 
            bg = pygame.image.load("bg73.jpg")
            bg = pygame.transform.scale(bg, (850, 650))
            self.__screen.blit(bg, (0, 0))
            
            # Tạo ra các nurt nhấn cho menu
            EASY_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 200 - 30),
                                 text_input="Easy",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (100, 40)
                                 )
            
            MEDUIM_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 250 - 30),
                                 text_input="Medium",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (150, 40)
                                 )
            
            HARD_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 300 - 30),
                                 text_input="Hard",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (100, 40)
                                 )
            
            VERY_HARD_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 350 - 30),
                                 text_input="Very_hard",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (200, 40)
                                 )
            
            INSANE_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 400 - 30),
                                 text_input="Insane",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (150, 40)
                                 )
            
            CUSTOM_BUTTON = Button(screen= self.__screen,
                                 pos=(425, 450 - 30),
                                 text_input="Custom",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (150, 40)
                                 )
            
            CONTINUE_BUTTON = Button(screen= self.__screen,
                                 pos=(100, 600 - 50),
                                 text_input="Continue",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (170, 40)
                                 )
            
            GUIDE_BUTTON = Button(screen= self.__screen,
                                 pos=(300 - 20, 600 - 50),
                                 text_input="Guide",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (120, 40)
                                 )
            
            QUIT_BUTTON = Button(screen= self.__screen,
                                 pos=(780 - 75, 600 - 135),
                                 text_input="Quit",
                                 font=pygame.font.Font(None, 30),
                                 base_color= "#ffffff" ,
                                 hovering_color= "#ff8c00",
                                 size= (100, 40)
                                 )
             # Tiêu đề game
            font = pygame.font.Font(None, 60)
            text = font.render("SUDOKU", True, "#ffffff")
            text_rect = text.get_rect(center = (425, 100))
            self.__screen.blit(text, text_rect)
            current_time = pygame.time.get_ticks()
            # Sự kiện cảnh báo data
            if self.error_data:
                self.draw_warning_continue()
            if current_time - self.time_press_btn > 1500:
                self.error_data = False
                
            # Xữ lý các sự kiện nút nhấn trên giao diện 
            menu_mouse_pos = pygame.mouse.get_pos()
            for button in [EASY_BUTTON, MEDUIM_BUTTON, HARD_BUTTON, VERY_HARD_BUTTON, INSANE_BUTTON, CUSTOM_BUTTON, CONTINUE_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
                button.changeColor(menu_mouse_pos)
                button.update()
                
            # Kiểm tra sự kiện
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.easy= True
                        self.running = False
                        
                    if MEDUIM_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.medium= True
                        self.running = False
                        
                    if HARD_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.hard= True
                        self.running = False
                        
                    if VERY_HARD_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.very_hard= True
                        self.running = False
                        
                    if INSANE_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.insane= True
                        self.running = False
                        
                    if CUSTOM_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.custom= True
                        self.running = False
                        
                    if CONTINUE_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self._continue= True
                        self.running = False
                        
                    if GUIDE_BUTTON.checkForInput(menu_mouse_pos):
                        self.init_btn()
                        self.guide= True
                        self.running = False
                        
                    if QUIT_BUTTON.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(60)
                    
    
class Button:
    def __init__(self, screen, pos, text_input, font, base_color, hovering_color, size):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.x_size = size[0]
        self.y_size = size[1]
        self.screen = screen
        self.text_input = text_input
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = pygame.draw.rect(self.screen,
                                     (225, 225, 225),
                                     ((self.x_pos - (self.x_size // 2), self.y_pos - (self.y_size // 2 - 1)),
                                     (self.x_size, self.y_size)),
                                     1, 20
                                     )  
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
        
    def update(self):
        self.screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


            