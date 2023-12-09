from tkinter import Tk, Label, Button
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


'''
tkinter.filedialog.askopenfilenames(**options)
Create an Open dialog and
return the selected filename(s) that correspond to
existing file(s).
screenshot
'''
class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        gfile = ''
        # create the root window
        self.root = Tk()
        self.root.title('Sound data modeling final')
        self.root.resizable(False, False)
        self.root.geometry('300x150')
    #def __init__(self, data=None):
        #self.root = root
        self.gfile = ''

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """

        self.controller = controller
    def select_file(self):
        filetypes = (('wav files', '*.wav'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        gfile = filename
        # tkinter.messagebox — Tkinter message prompts
        showinfo(title='Selected File',message=filename)
        gfile_label = ttk.Label(self.root, text=gfile)
        gfile_label.pack(side="bottom")
        open_button = ttk.Button(self.root, text='Open a File', command=View.select_file)
        open_button.pack(expand=True)

        # run the application
        self.root.mainloop()
    # open button
        def save_button_clicked(self):
            """
            Handle button click event
            :return:
            """

        if self.controller:
            self.controller.save(self.get())

#open_button = ttk.Button(root,text='Open a File',command=View.select_file)

'''
import scipy.io
from scipy.io import wavfile

wav_fname = 'output.wav'
samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[len(data.shape) - 1]}")
print(f"sample rate = {samplerate}Hz")
length = data.shape[0] / samplerate
print(f"length = {length}s")
import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
sample_rate, data = wavfile.read('16bitmono.wav')
spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, \
NFFT=1024, cmap=plt.get_cmap('autumn_r'))
cbar = plt.colorbar(im)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
cbar.set_label('Intensity (dB)')
plt.show()
'''