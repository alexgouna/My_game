import tkinter as tk


class my_game(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("My Game")
        self.geometry('1280x720')
        self.configure(background='black')

    def start(self):
        self.mainloop()


def start_game():
    app = my_game()
    app.start()