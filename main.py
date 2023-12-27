import pygame
pygame.init()
from menu import Menu
from gui import GUI
from generator import Generator
from gui_custom import Custom
from surface import convertStrToGrid
from guide import Guide
def main_menu():
    menu = Menu()
    gui = None
    custom = None
    guide = None    
    generator = Generator()
    while True:
        menu.loop()
        if menu.easy:
            menu.init_btn()
            gui = GUI(generator.generate("easy"))
        if menu.medium:
            menu.init_btn()
            gui = GUI(generator.generate("medium"))
        if menu.hard:
            menu.init_btn()
            gui = GUI(generator.generate("hard"))
        if menu.very_hard:
            menu.init_btn()
            gui = GUI(generator.generate("very-hard"))
        if menu.insane:
            menu.init_btn()
            gui = GUI(generator.generate("insane"))
        if menu.custom:
            menu.init_btn()
            custom = Custom()
            custom.loop()
            if custom.running == False and custom.state == "Play":
                custom.state = ""
                gui = GUI(custom.board)
            if custom.running == False and custom.state == "Menu":
                custom.state = ""
                menu.running = True
            if custom: 
                del custom
                custom = None
        if menu._continue:
            menu.init_btn()
            try:
                file = open("save_status.txt", "r")
                board = convertStrToGrid(file.readlines()[0])
                file.close()

                gui = GUI(board)
                gui.continue_game()
            except:
                menu.running = True
                menu.error_data = True
                continue
        if menu.guide:
            menu.init_btn()
            guide = Guide()
            guide.loop()
            if guide : del guide
            guide = None
            menu.running = True
        if menu.running == False :
            gui.running = True
            gui.loop()
            #gui.Jump_Mode()
            if gui: 
                del gui
                gui = None
        if gui == None:
            menu.running = True


main_menu()