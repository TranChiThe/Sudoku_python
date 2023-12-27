import pygame
from base import GUIBase
from solver import Solver
from square import Squares

class Board(GUIBase):
    def __init__(self, size: tuple, board: list, screen: pygame.Surface):
        super().__init__(size, screen)
        self.__solver = Solver(self)
        self.__board = board
        self.__squares = [
            [
                Squares(
                    self.__board[c][r],
                    (r, c),
                    (self.size[0], self.size[1]),
                    self.screen,
                    True if self.__board[c][r] == 0 else False,
                                    
                )
                for r in range(9)
            ]
            for c in range(9)
        ]
                        
                        

        self.__bg_box = None
        self.__selected = (-1, -1)
        self.__wrong = None
        self.__units_list = None
        self.__same_num_list = None
        
    @property 
    def board(self)->list:
        return self.__board
    @board.setter
    def board(self, board: list):
        self.__board = board
        self.__squares = [
            [
                Squares(
                    #Truy cập hàng r và cột c
                    self.__board[c][r],
                    (r, c),
                    (self.size[0], self.size[1]),
                    self.screen,
                    True if self.__board[c][r] == 0 else False,
                                    
                )
                for r in range(9)
            ]
            for c in range(9)
        ]
        
        
    @property 
    def wrong(self):
        return self.__wrong
    
    @property
    def squares(self)->list:
        return self.__squares
    
    def update_squares(self):
        for r in range(9):
            for c in range(9):
                # Gán giá trị bảng vào ô
                self.__squares[r][c].value = self.__board[r][c]
                self.__squares[r][c].pencil = 0
                
    # Xóa giá trị ô trong bảng            
    def delete_squares(self):
        if self.selected:
            self.clear
            self.clear_state()
      
                
    def update_units_list(self):
        if self.__selected:
            self.__units_list = []
            i, j = self.__selected
            for num in range(9):
                # Kiểm tra tọa độ ô không trùng với ô được chọn
                if (i, num) != self.__selected:
                    self.__units_list.append((i, num))
                if (num, j) != self.__selected:
                    self.__units_list.append((num, j))
            
            num_i = i // 3
            num_j = j // 3
            for x in range(num_i * 3, num_i * 3 + 3):
                for y in range(num_j * 3, num_j * 3 + 3):
                    # Kiểm tra không trùng tọa độ với ô được chọn
                    if (x, y) != self.__selected:
                        self.__units_list.append((x, y))
    
    # Cập nhật các ô có giá trị trùng với ô được chọn                    
    def update__same_num_list(self):
        if self.__selected:
            i, j = self.__selected
            if self.__board[i][j] != 0:
                self.__same_num_list = []
                # Duyệt qua toàn bộ bảng
                for r in range(9):
                    for c in range(9):
                        # Kiểm tra tọa độ có cùng giá trị ô được chọn và khác vị trí được chọn
                        if self.__board[r][c] == self.__board[i][j] and (r, c) != (i, j):
                            self.__same_num_list.append((r, c))
            else:
                self.__same_num_list = None                    
    
    @property
    def selected(self):
        return self.__selected
    
    def clear_state(self):
        # Kiểm tra các ô cùng hàng, cùng cột và cùng khối
        if self.__units_list:
            for num in self.__units_list:
                r, c = num
                self.__squares[r][c].unit_selected = False
            # Đánh dấu không có ô nào được chọn
            self.__units_list = None
        
        # Kiểm tra các ô có cùng giá trị
        if self.__same_num_list:
            for num in self.__same_num_list:
                r, c = num
                self.__squares[r][c].is_same_num = False
            # Không có ô nào được chọn có cùng giá trị
            self.__same_num_list = None
            
    @selected.setter
    def selected(self, pos: tuple):
        if not self.__wrong:
            if self.__selected != None:
                # Bỏ chọn ô đã chọn trước đó
                self.__squares[self.__selected[0]][self.__selected[1]].selected = False
            if pos:
                # Lựa chọn giá trị mới tại pos
                self.__selected = pos
                self.__squares[self.__selected[0]][self.__selected[1]].selected = True
                self.clear_state()
                self.update_units_list()
                self.update__same_num_list()
            else:
                self.__selected = None
                
                
    @property
    def get_pencil(self)->int:
        r, c = self.__selected
        return self.__squares[r][c].pencil
    
    def set_pencil(self, p: int):
        r, c, = self.__selected
        if self.__squares[r][c].value == 0:
            self.__squares[r][c].pencil = p
            
    def set_pencil_save(self, pos: tuple, p: int):
        r, c = pos
        if self.__squares[r][c].value == 0:
            self.__squares[r][c].pencil = p
            
    @property
    def get_value(self):
        r, c = self.__selected
        return self.__squares[r][c].value
    
    def set_value(self)->str:
        r, c = self.__selected
        if self.get_value == 0:
            pencil = self.get_pencil
            if pencil != 0:
                # Đánh dấu tọa độ ô có cùng giá trị với ô pencil không hợp lệ
                w = self.__solver.exists(self.__board, pencil, (r, c))
                if w:
                    self.__squares[r][c].wrong = True
                    self.__squares[w[0]][w[1]].wrong = True
                    self.__squares[r][c].value = pencil
                    self.__board[r][c] = pencil
                    self.__wrong = w
                    return "wrong"
                else:
                    self.__squares[r][c].value = pencil
                    self.__board[r][c] = pencil
                    # Tạo bảng sao cho bảng lưới sudoku                 
                    copy = [ [] for r in range(9)]
                    for r in range(9):
                        for c in range(9):
                            copy[r].append(self.__board[r][c])
                    if not self.__solver.solve(copy):  
                        return "contradictory"
                    return "success"
                
    def set_value_save(self, pos: tuple, value: int)->str:
        r, c = pos
        if value != 0:
            w = self.__solver.exists(self.__board, value, (r, c))
            if w:
                self.__squares[r][c].wrong = True
                self.__squares[w[0]][w[1]].wrong = True
                self.__squares[r][c].value = value
                self.__board[r][c] = value
                self.__wrong = w
                return "wrong"
            else:
                self.__squares[r][c].value = value
                self.__board[r][c] = value
                copy = [[] for r in range(9)]
                for r in range(9):
                    for c in range(9):
                        copy[r].append(self.__board[r][c])
                if not self.__solver.solve(copy):
                    return "contradictory"
                return "success"
            
            
    @property
    def clear(self):
        r, c = self.__selected
        self.__squares[r][c].value = 0
        self.__squares[r][c].pencil = 0
        self .__board[r][c] = 0
        self.clear_state()
        if self.__wrong:
            self.__squares[r][c].wrong = False
            self.__squares[self.__wrong[0]][self.__wrong[1]].wrong = False
            self.__wrong = None
            
            
    @property
    def isfinished(self):
        return not self.__solver.nextpos(self.__board)
        
        
    def set_sq_value(self, value: int, pos: tuple):
        self.__squares[pos[0]][pos[1]].value = value
        
    def get_bg_box(self):
        return self.__bg_box
    
    def draw(self):
        # Vẽ khung cho lưới sudoku tại vị  trí 225, 100
        self.__bg_box = pygame.draw.rect(self.screen,
                                         (255, 225, 225),
                                         pygame.Rect(225, 100, 396, 396)  # (x, y, width, height)
                                         )
        for r in range(9):
            for c in range(9):
                # Kiểm tra (c, r) có nằm trong danh sách các ô được chọn hay không
                if self.__units_list and (c, r) in self.__units_list:
                    self.__squares[c][r].unit_selected = True
                # Kiểm tra (c, r) có nằm trong danh sách các ô có cùng giá trị hay không
                if self.__same_num_list and (c, r) in self.__same_num_list:
                    self.__squares[c][r].is_same_num = True
                self.__squares[c][r].draw()
        # Khoảng cách giữa các ô trong lưới      
        space = self.size[0] // 9
        for r in range(10):
            if r % 3 == 0:
                w = 3
            else: 
                w = 1
            # Vẽ các đường ngang
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (225, (r * space) + 100),
                             (space * 9 + 225, (r * space) + 100),
                             w
                             )
            # Vẽ các đường dọc
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             ((r * space) + 225, 100),
                             ((r * space) + 225, space * 9 + 100), 
                             w
                             )