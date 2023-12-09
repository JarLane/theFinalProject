from view import View
from model import Model

class Controller:
    def __init__(self, model, view):

        self.model = model
        self.view = view
    def save(self):


        try:
            # save the model
            #  self.model.sound = sound
            self.model.sound()
            self.view.select_file()
            # show a success message
            #self.view.show_info(f'The sound {sound}saved')
        except ValueError as error:
            # show an error message
            self.view.show_error(error)


if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model, view)
    Controller.save()

