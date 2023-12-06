import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
gfile = ''
# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')
'''
tkinter.filedialog.askopenfilenames(**options)
Create an Open dialog and
return the selected filename(s) that correspond to
existing file(s).
screenshot
'''
def select_file():
    filetypes = (('wav files', '*.wav'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    gfile = filename
    # tkinter.messagebox — Tkinter message prompts
    showinfo(title='Selected File',message=filename)
    gfile_label = ttk.Label(root, text=gfile)
    gfile_label.pack(side="bottom")
    open_button.pack(expand=True)
    # run the application
    root.mainloop()
# open button
open_button = ttk.Button(root,text='Open a File',command=select_file)
