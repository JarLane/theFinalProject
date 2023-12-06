import re
class Model:
def __init__(self, sound):
    self.sound = sound
    # use property decorator to use getters & setters
    # define email an attribute of Model
@property
def sound(self):
    return self.__sound
@sound.setter
    def sound(self, value):

        # create regular expression to match email input
        pattern = r'.wav'

#check for match between reg_ex and input
    if re.fullmatch(pattern, value):
        self.__sound = value
    else:
        raise ValueError(f'Invalid sound file, must be: {value}')
def save(self):
    """
    Save the email into a file
    :return:
    """
    with open('email_input.txt', 'a') as f:
        f.write(self.email + '\n')