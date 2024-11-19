from tkinter import Tk, Button

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Wolff Dictionary Normalizer")
        self.geometry("360x210")

        # Create a button and bind the left mouse button click event
        self.button = Button(self, text="My simple app.")
        self.button.bind("<Button-1>", self.handle_button_press)  # Bind the button click event
        self.button.pack()

    def handle_button_press(self, event):
        self.destroy() 