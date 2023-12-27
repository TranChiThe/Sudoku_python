import pygame
from solver import Solver
from random import randint, shuffle

class Generator:
    def  __init__(self):
        self.__solver = Solver()
        self.__DIFICULTY = {
            "easy":        62, #62
            "medium":      53,
            "hard":        44,
            "very-hard":   35,
            "insane":      26,
        }
        
        self.__listNum = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
    
    def fillGid(self, grid):
        pos = self.__solver.nextpos(grid)
        # Xáo trộn các số
        shuffle(self.__listNum)
        if not pos:
            return True
        for n in self.__listNum:
            if not self.__solver.exists(grid, n, pos):
                grid[pos[0]][pos[1]] = n
                if self.fillGid(grid):
                    return True
                grid[pos[0]][pos[1]] = 0
        return False   
    
    
    def generate(self, dificulty):
        # Tạo ra tất cả các ô trống có giá trị ban đầu là 0
        grid = [[0 for r in range(9)] for c in range(9)]
        self.fillGid(grid)
        for i in range(0, 81 - int(self.__DIFICULTY[dificulty])):
            row =  randint(0, 8)
            col = randint(0, 8)
            # Loại bỏ 1 số ô trống cần thiết để tạo độ khó
            while grid[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            grid[row][col] = 0
        return grid
    
    