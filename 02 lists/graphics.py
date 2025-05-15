import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.window = tk.Tk()
        self.window.title("Canvas")
        self.canvas = tk.Canvas(self.window, width=width, height=height)
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.click_x = None
        self.click_y = None
        self.canvas.bind("<Motion>", self._mouse_move)
        self.canvas.bind("<Button-1>", self._mouse_click)
        self.window.update()

    def _mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _mouse_click(self, event):
        self.click_x = event.x
        self.click_y = event.y

    def create_rectangle(self, left, top, right, bottom, color):
        return self.canvas.create_rectangle(left, top, right, bottom, fill=color, outline=color)

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color, outline=color)

    def find_overlapping(self, left, top, right, bottom):
        return self.canvas.find_overlapping(left, top, right, bottom)

    def get_mouse_x(self):
        self.window.update()
        return self.mouse_x

    def get_mouse_y(self):
        self.window.update()
        return self.mouse_y

    def moveto(self, item, x, y):
        self.canvas.coords(item, x, y, x + 20, y + 20)

    def wait_for_click(self):
        self.click_x = None
        self.click_y = None
        while self.click_x is None or self.click_y is None:
            self.window.update()

    def get_last_click(self):
        return self.click_x, self.click_y
