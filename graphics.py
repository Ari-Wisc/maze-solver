import time
from tkinter import Tk, BOTH, Canvas

class Window(Tk):
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
class Cell ( ):
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win


    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        color="black" if self.has_left_wall else "white"
    # if self.has_left_wall:
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, color)
    # if self.has_top_wall:
        color="black" if self.has_top_wall else "white"

        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, color)
    # if self.has_right_wall:
        color="black" if self.has_right_wall else "white"
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, color)
    # if self.has_bottom_wall:
        color="black" if self.has_bottom_wall else "white"
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        self_center= Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)
        to_center = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        line = Line(self_center, to_center)
        self._win.draw_line(line, color)


# class Maize:
#     def __init__(
#         self,
#         x1,
#         y1,
#         num_rows,
#         num_cols,
#         cell_size_x,
#         cell_size_y,
#         win,
#     ):
#         self._x1 = x1
#         self._y1 = y1
#         self._num_rows = num_rows
#         self._num_cols = num_cols
#         self._cell_size_x = cell_size_x
#         self._cell_size_y = cell_size_y
#         self._win = win
#         self._cells = self._create_cells()
#         for i in range(self._num_rows):
#             row = []
#             for j in range(self._num_cols):
#                 cell = Cell(self._win)
#                 self._draw_cell(i, j)
#     def _create_cells(self):
#         cells = []
#         for i in range(self._num_rows):
#             row = []
#             for j in range(self._num_cols):
#                 cell = Cell(self._win)
#                 row.append(cell)
#             cells.append(row)




#         return cells
#     def _draw_cell(self, i, j):
#         x1 = self._x1 + j * self._cell_size_x
#         y1 = self._y1 + i * self._cell_size_y
#         x2 = x1 + self._cell_size_x
#         y2 = y1 + self._cell_size_y
#         self._cells[i][j].draw(x1, y1, x2, y2)
#     def _animate(self):
#         while True:
#             self._win.redraw()
#             time.sleep(0.4)        
        