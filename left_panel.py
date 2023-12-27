import pygame
import time
from base import GUIBase
from parallel import Threads

class LeftPanel(GUIBase):
    def __init__(self, solver, size: tuple, screen: pygame.Surface):
        super().__init__(size, screen)
        self.time = Time(self.size, self.screen)
        self.hints = Hints(self.size, self.screen)
        self.options = Options(solver, self.size, self.screen)
        self.gamesystem = GameSystem(self.size, self.screen)
        
    def draw(self):
        self.time.draw()
        self.hints.draw()
        self.options.draw()
        self.gamesystem.draw()
        
class GameSystem(GUIBase):
    def __init__(self, size: tuple, screen: pygame.Surface):
        super().__init__((size[0], size[1] // 9), screen)
        self.__wrongs_counter = 0
        self.__lost = False
        self.__won = False
        
    def reset(self):
        self.__lost = False
        self.__won = False
        self.__wrongs_counter = 0
        
    def get_wrongs_counter(self):
        return self.__wrongs_counter
    
    def set_wrongs_counter(self, value:int):
        self.__wrongs_counter = value
    
        
    @property
    def wrongs_counter(self):
        if self.__wrongs_counter < 5:
            self.__wrongs_counter += 1
        else:
            self.__lost = True
            
    @property
    def lost(self)->bool:
        return self.__lost
    @lost.setter
    def lost(self, value: bool):
        self.__lost = value
        
    @property 
    def won(self)->bool:
        return self.__won
    @won.setter
    def won(self, value: bool):
        self.__won = value
        
    def draw(self):
        w = 1 
        self._type("Info", (225, 225, 225), (20, 30), 30)
        pygame.draw.rect(self.screen,
                         (225, 225, 225),
                         ((65, 20), (44*3 + 10, 44)),
                         1
                         )
        # Cập nhật các trạng thái đúng sai 
        if self.__won:
            self._type("You won", (255, 255, 255), (100, 32), 28)
        elif not self.__lost:
            self._type("X " * self.__wrongs_counter, (234, 72, 54), (70, 35), 30)
        else:
            self._type("You lost", (255, 255, 255), (100, 35), 28)
            
            
class Options(GUIBase):
    def __init__(self, solver, size: tuple, screen: pygame.Surface):
        super().__init__(size, screen)
        self.__threads = Threads()
        self.__solver = solver
        self.__run = False
        self.__buttons = [
            Button(*i, (44*2, 44), self.screen)
            for i in (
                (self.start, (), (4, 8), "Auto", 24, (100, 500 + 44 * 1 )),
                (self.solve_all, (), (4, 8), "Fast", 24, (100 + 44*2+10, 500 + 44*1)),
                (self.kill, (), (5, 8), "Stop", 24, (100, 500 + 44 * 2 + 10)),
                (self.solve_selected, (), (-8, 8), "Selected", 24, (100 + 44*2 + 10, 500 + 44 * 2 + 10)),
                (self.reset, (), (4, 8), "Reset", 24, (450, 500 + 44 * 1)),
                (self.menu, (), (4, 8), "Jump", 24, (450, 500 + 44 * 2 + 10)),
                (self.pencil, (), (2, 8), "Pencil", 24, (30 + 700, 100 + 44 * 1)),
                (self.value, (), (2, 8), "Value", 24, (30 + 700, 100 + 44 * 2 + 10)),
                (self.top, (), (3, 8), "Top", 24, (60, 180)),
                (self.bottom, (), (-2, 8), "Bottom", 24, (60, 330)),
                (self.right, (), (-2, 8), "Left", 24, (10, 255)),
                (self.left, (), (4, 8), "Right", 24, (120, 255)),
                (self.jump, (), (2, 8), "Back", 24, (550, 500 + 44 * 2 + 10)),
                (self.deletes, (), (1, 8), "Delete", 24, (550, 500 + 44 * 1))
            )
        ]
        
    def menu(self):
        return True
    def pencil(self):
        return True
    def value(self):
        return True
    def top(self):
        return True
    def bottom(self):
        return True
    def right(self):
        return True
    def left(self):
        return True
    def jump(self):
        return True
    def deletes(self):
        return True
    def start(self):
        if not self.__run:
            self.__solver.kill = False
            self.__solver.e = True
            self.__threads.start(self.__solver.auto_solver)
            self.__run = True
            
    def kill(self):
        self.__solver.kill = True
        self.__threads.stop()
        self.__run = False
        
    def solve_all(self)->bool:
        s = self.__solver.solve(self.__solver.board.board)
        self.__solver.board.update_squares()
        return s
    
    def solve_selected(self, board: list, pos: tuple):
        solution = self.__solver.solve(board)
        if solution and pos:
            self.__solver.board.board[pos[0]][pos[1]] = board[pos[0]][pos[1]]
            self.__solver.board.update_squares()
        return solution
    
    def reset(self)->bool:
        self.kill()
        for r in range(9):
            for c in range(9):
                if self.__solver.board.squares[r][c].changeable:
                    self.__solver.board.board[r][c] = 0
        
        if self.__solver.board.wrong:
            self.__solver.board.clear
            
        self.__solver.board.update_squares()
        return True
    
    
    @property
    def buttons(self)->list:
        return self.__buttons
    
    # Vẽ các nút lên giao diện
    def draw(self):
        for b in self.__buttons:
            b.draw()
        self._type(f"Solver", (255, 255, 255), (20,550), 30)   
        self._type(f"Option", (255, 255, 255), (370, 550), 30)
        self._type(f"Control", (255, 255, 255), (20, 150), 30)
    

class Time(GUIBase):
    def __init__(self, size: tuple, screen: pygame.Surface):
        super().__init__((size[0], size[1] // 9), screen)
        self.__init_time = time.time()
        self.__end_time = None
        self.__continue_time = 0.0
        
    @property
    def init_time(self):
        return self.__init_time
    @init_time.setter
    def init_time(self, value: time.time):
        self.__init_time = value 
        
    @property
    def end_time(self):
        return self.__end_time
    @end_time.setter
    def end_time(self, value: time.time):
        self.__end_time = value
        
    @property
    def continue_time(self):
        return self.__continue_time
    @continue_time.setter
    def continue_time(self, value: float):
        self.__continue_time = value
        
    def __time_formatter(self, delta: float)->str:
        hms = [delta // 60 // 60 , delta // 60, delta % 60]
        for i in range(len(hms)):
            hms[i] = f"0{int(hms[i])}" if hms[i] < 10 else  f"{int(hms[i])}"
        return f"{hms[0]}:{hms[1]}:{hms[2]}"
    
    def draw(self):
        if self.__end_time:
            ftime = self.__time_formatter((self.__end_time - self.__init_time) + self.continue_time)      
            self._type(f"{ftime}",
                       (225, 225, 225),
                       (self.size[1] * 9 + 100, 60),
                       40
                       )
            
        else:   
            ftime = self.__time_formatter((time.time() - self.__init_time) + self.continue_time)
            self._type(f"{ftime}",
                       (225, 225, 225),
                       (self.size[1] * 9 + 100, 60),
                       40
                       )

            
class Hints(GUIBase):
    def __init__(self, size: tuple, screen: pygame.Surface):
        super().__init__((size[0], size[1]), screen)
        self.__hint = "Status: Everything is well"
        self.__hint_option = "Option: Pencil"
        self.__hint_warning = "Warning"
        
    @property
    def hint(self):
        return self.__hint
    @hint.setter
    def hint(self, value: str):
        self.__hint = value
        
    @property
    def hint_option(self):
        return self.__hint_option
    @hint_option.setter
    def hint_option(self, value_op: str):
        self.__hint_option = value_op
        
    @property
    def hint_warning(self):  
        return self.__hint_warning
    @hint_warning.setter
    def hint__warning(self, value_w: str):
        self.__hint_warning = value_w
    
    def draw(self):
        self._type(f"{self.__hint}",
                   (225, 225, 225),
                   (20, 80),
                   26
                   )      
    def draw_option(self):
        self._type(f"{self.__hint_option}",
                   (225, 225, 225),
                   (720, 80),
                   26
                   )     
        
    def draw_warning(self):
        self._type(f"{self.__hint_warning}",
                   (225, 225, 225),
                   (20, 100),
                   26
                   )     
        
        
        
class Button(GUIBase):
    def __init__(self,
                 target,
                 _args: tuple,
                 s: tuple,
                 innertxt: str,
                 fontsize: int,
                 pos: tuple,
                 size: tuple,
                 screen: pygame.Surface,
                 ):
        
        super().__init__(size, screen)
        self.__target = target
        self.__args = _args
        self.__s = s
        self.__innertxt = innertxt
        self.__fontsize = fontsize
        self.__pos = pos
        self.__fill = (0, 0, 0)
        self.__color = (96, 87, 193)
        self.__bg_box = None
        
    @property
    def bg_box(self):
        return self.__bg_box
    
    @property
    def innertxt(self):
        return self.__innertxt
    
    @property
    def click_range(self):
        return self.__click_range
    
    @property
    def reset(self):
        self.__fill = (0, 0 ,0)
        self.__w = 1
        self.__color = (96, 87, 193)   
        
    def click(self, args: tuple = ()):
        self.__fill = (255, 0, 0)
        self.__w = 2
        self.__color = (124, 252, 0)
        
        if self.__args:
            return self.__target(self.__args)
        elif args:
            return self.__target(*args)
        else:
            return self.__target()
        
    def draw(self):
        self.__bg_box = pygame.draw.rect(self.screen,
                                         self.__color,
                                         (self.__pos, 
                                         self.size)
                                         )
        
        for i in range(2):
            pygame.draw.line(self.screen,
                             (255, 255, 255),
                             (self.__pos[0], self.__pos[1] + 44*i),
                             (self.__pos[0] + 88, self.__pos[1] + 44*i), 
                             2
                             )
            pygame.draw.line(self.screen,
                             (225, 255, 255),
                             (self.__pos[0] + 88*i, self.__pos[1]),
                             (self.__pos[0] + 88*i, self.__pos[1] + 44), 
                             2
                             )
        self._type(self.__innertxt,
                   "#ffffff",
                   (
                       self.__pos[0] + self.size[0] // 4 + self.__s[0],
                       self.__pos[1] + self.size[1] // 8 + self.__s[1],
                   ),
                   self.__fontsize
                   )          
                   
                   
