from model import Model
from view import View


class Controller:
    def __init__(self, model, view):

        self.model = model
        self.view = view
    def save(self):
        from model import Model
        from view import View

        class Controller:
            def __init__(self, model, view):
                self.model = model
                self.view = view

            def save(self, sound):
                try:
                    self.model.sound = sound
                    self.model.save("input.wav", "output.wav")  # Pass input and output file names

                except ValueError as error:
                    # show an error message
                    self.view.show_error(error)

'''
if __name__ == '__main__':
    #model = Model(view.gfile)
    view = View()
    model = Model('sound.wav')
    controller = Controller(model, view)
    controller.save()
'''