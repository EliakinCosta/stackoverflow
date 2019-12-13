from tkinter import *


class Game:

    def __init__(self, width, height):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=width, height=height)
        self.canvas.pack()
        self.background = PhotoImage(
            file="/Users/eliakin.almeida/Downloads/dbzss3.gif"
        )
        self.over = self.canvas.create_image(
            200, 200, image=self.background, anchor='center'
        )

    def mainloop(self):
        self.tk.mainloop()


if __name__ == '__main__':
    g = Game(1000, 400)
    new_image = PhotoImage(file="/Users/eliakin.almeida/Downloads/dbzss3.gif")
    g.canvas.itemconfig(
        g.over,
        image=new_image
    )
    g.mainloop()
