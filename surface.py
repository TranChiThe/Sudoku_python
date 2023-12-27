def convertStrToGrid(gridStr):
    count_loop = 0
    Grid = []                              # Lưới sudoku
    row = []                                # Hàng để lưu các số từ chuỗi
    for i in range(0, 81):
        if gridStr[i] == '0':
            row.append(0)
        else:
            row.append(int(gridStr[i]))
        count_loop += 1
        if count_loop % 9 == 0:              # Nếu đủ 9 số thì thêm hàng đó vào lưới
            Grid.append(row)
            row = []                           # Làm rỗng lại hàng
    return Grid 