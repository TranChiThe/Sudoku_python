import threading
import time

class Solver:
    def __init__(self, board= None, delay: float = 0.0):
        self.board = board
        self.__delay = delay / 1000
        self.__e = threading.Event()
        self.__kill = False
        self.__e.set()
        
    @property
    def delay(self):
        return self.__delay / 1000
    delay.setter
    def delay(self, delay: float):
        self.__delay = delay / 1000
    
    @property
    def e(self):
        return self.__e.is_set()
    
    @e.setter
    def e(self, set: bool):
        if set:
            self.__e.set()
        else:
            self.__e.clear()
    
    @property
    def kill(self):
        return self.__kill
    @kill.setter
    def kill(self, k: bool):
        self.__kill = k
      
   # Tìm vị trí kế tiếp chưa được giải trong lưới sudoku và trả về vị trí đó  
    def nextpos(self, board: list)->tuple:
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return()
    
    
    # Xữ lý các điều kiện quy tắc luật chơi sudoku
    def exists(self, board: list, n: int, row_col: tuple) -> tuple:
        # Kiểm tra số trùng  trên cột
        for c in range(len(board)):
            if board[row_col[0]][c] == n:
                return (row_col[0], c)
        
        # Kiểm tra số trùng trên hàng
        for r in range(len(board)):
            if board[r][row_col[1]] == n:
                return (r, row_col[1])

        # Kiểm tra số trùng trong lưới 3 x 3
        pos_square = ((row_col[0] // 3) * 3, (row_col[1] // 3) * 3)
        for r in range(pos_square[0], pos_square[0] + 3):
            for c in range(pos_square[1], pos_square[1] + 3):
                if board[r][c] == n:
                    return (r, c)
        return()
    
    
    # Giải lưới sudoku
    def solve(self, board: list) -> bool:
        # Tìm vị trí tiếp theo chưa được giải
        pos = self.nextpos(board)
        # Không còn vị trí -> Giải thành công
        if not pos:
            return True
        for n in range(1, 10):
            # Kiểm tra số theo quy tắc điều kiện
            if not self.exists(board, n, pos):
                # Đặt giá trị vào vị trí được chọn
                board[pos[0]][pos[1]] = n
                # Gọi hàm để giải các vị trí tiếp theo
                if self.solve(board):
                    return True
                # Quay lui lại bằng cách set lại giá trị rỗng
                board[pos[0]][pos[1]] = 0
        return False
        
    
    
    # Giải sudoku tự động
    def auto_solver(self) -> bool:
        if not self.__kill:
            # Tìm vị trí tiếp theo chưa được giải
            pos = self.nextpos(self.board.board)
            # Nếu không còn vị trí -> Đã giải xong
            if not pos:
                return True
            for n in range(1, 10):
                if not self.exists(self.board.board, n, pos):
                    # tạm dừng/ tiếp tục
                    self.__e.wait()
                    # Đặt trạng lại trạng thái cho bảng
                    self.board.set_sq_value(n, (pos[0], pos[1]))
                    self.board.board[pos[0]][pos[1]] = n
                    # Dừng 1 khoảng time
                    time.sleep(self.__delay)
                    # Tiếp tục giải
                    if self.auto_solver():
                        return True
                    if not self.__kill:
                        self.__e.wait()
                        # Quay lui 
                        #Đặt lại trạng thái cho bảng để xữ lý các số khác
                        self.board.set_sq_value(0, (pos[0], pos[1]))
                        self.board.board[pos[0]][pos[1]] = 0
            # Dừng 1 khoảng time trong lúc quay lui để thử các số khác
            time.sleep(self.__delay)
            return False
