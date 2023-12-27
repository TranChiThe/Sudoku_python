import pygame
import sys
from menu import Button

class Guide:
    def __init__(self) -> None:
        self.running = True
        self.__screen_size = (850, 650)
        self.__screen = pygame.display.set_mode(self.__screen_size[0:2])
        pygame.display.set_caption("Sudoku")
    
    def __del__(slef):
        pass
    
    def loop(self):
        while self.running:
            background = pygame.image.load("bg74.jpg")
            background = pygame.transform.scale(background, (850, 650))
            self.__screen.blit(background, (0, 0))
            
            MENU_BUTTON = Button(screen= self.__screen,
                                 pos= (425, 600 - 50),
                                 text_input= "Menu",
                                 font= pygame.font.Font(None, 28),
                                 base_color= "#ffffff",
                                 hovering_color= "#ff8c00", 
                                 size= (100, 40)
                                 )
            
            font = pygame.font.Font(None, 25)
            font_title = pygame.font.Font(None, 30)
            font_intro_title = pygame.font.Font(None, 25)
            font_intro = pygame.font.Font(None, 25)
            
            line_title1 = font_title.render("How to play sudoku", True, "white")
            line1 = font.render("In Sudoku, you must complete the grid so each row, column and 3-by-3 box (in bold borders)", True, "#ffffff")
            line1_1 = font.render("contains every digit 1 through 9.", True, "#ffffff")
            line2 = font.render("No row, column, or 3×3 box can feature the same number twice.",True, "#ffffff")
            line3 = font.render("That means each row, column, and 3×3 square in a Sudoku puzzle must contain ONLY one 1,",True, "#ffffff")
            line3_1 = font.render("one 2, one 3, one 4, one 5, one 6, one 7, one 8, and one 9.",True, "#ffffff")
            line_title_2 = font_title.render("Introduce", True, "#ffffff")
            intro1 = font_intro_title.render("Developer:",True, "#ffffff")
            intro1_1 = font_intro.render("Tran Chi The_B2003923",True, "#ffffff")
            #version
            intro2 = font_intro_title.render("Version:",True, "#ffffff")
            intro2_2 = font_intro.render("1.0 (demo)",True, "#ffffff")
            #release
            intro3 = font_intro_title.render("Release:",True, "#ffffff")
            intro3_3 = font_intro.render("12/09/2023",True, "#ffffff")
            #engine
            intro4 = font_intro_title.render("Engine:",True, "#ffffff")
            intro4_4 = font_intro.render("Python, pygame",True, "#ffffff")
            
            self.__screen.blit(line_title1,(44, 180 - 15))
            self.__screen.blit(line1,(44, 220 - 30))
            self.__screen.blit(line1_1,(44, 240 - 30))
            self.__screen.blit(line2,(44, 260 - 30))
            self.__screen.blit(line3,(44, 280 - 30))
            self.__screen.blit(line3_1,(44, 300 - 30))
            self.__screen.blit(line_title_2,(44, 330 - 15))
            #developer
            self.__screen.blit(intro1,(44, 370 - 30))
            self.__screen.blit(intro1_1,(140, 370 - 30))
            #version
            self.__screen.blit(intro2,(44, 390 - 30))
            self.__screen.blit(intro2_2,(120, 390 - 30))
            #release
            self.__screen.blit(intro3,(44, 410 - 30))
            self.__screen.blit(intro3_3,(120, 410 - 30))
            #Engine
            self.__screen.blit(intro4,(44, 430 - 30))
            self.__screen.blit(intro4_4,(115, 430 - 30))
            
            # lấy vị trí chuột trên màn hình
            menu_mouse_pos = pygame.mouse.get_pos()
            for button in [MENU_BUTTON]:
                button.changeColor(menu_mouse_pos)
                button.update()
             # Sự kiện thoát Game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(menu_mouse_pos):
                        self.running = False
            pygame.display.update()
            
