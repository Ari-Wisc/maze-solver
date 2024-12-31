from tkinter import Tk, BOTH, Canvas

class Window(Tk):
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Tkinter Window")

        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False

        # Connect the close method to the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

# Main function to create and manage the window
def main():
    win = Window(800, 600)
    win.wait_for_close()

