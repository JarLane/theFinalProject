class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def save(self, sound):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            # save the model
            self.model.sound = sound
            self.model.sound()
            # show a success message
            self.view.show_success(f'The sound {sound}saved')
        except ValueError as error:
            # show an error message
            self.view.show_error(error)