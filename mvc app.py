from model import Model
from view import View
from controller import Controller
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.title('MVC pattern with Tkinter')
# create a model
        model = Model()
        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(model, view)
        # set the controller to view
        view.set_controller(controller)
        view.select_file()
if __name__ == '__main__':
    app = App()
    app.mainloop()