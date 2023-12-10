# View.py
import os
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Module import analyze_wav

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Upload and Analysis GUI")
        self.master.geometry("800x600")

        self.file_path = None
        self.current_plot_container = None

        self.create_widgets()

    def create_widgets(self):
        # File import button
        self.import_button = tk.Button(self.master, text="Import File", command=self.import_file)
        self.import_button.pack(pady=10)

        # File name label
        self.file_label = tk.Label(self.master, text="No file selected")
        self.file_label.pack(pady=5)

        # Upload button
        self.upload_button = tk.Button(self.master, text="Upload", state="disabled", command=self.upload_file)
        self.upload_button.pack(pady=10)

        # Plot buttons
        self.plot_button_low = tk.Button(self.master, text="Low", command=lambda: self.plot_button_clicked("low"))
        self.plot_button_low.pack(side="left", padx=5)

        self.plot_button_mid = tk.Button(self.master, text="Mid", command=lambda: self.plot_button_clicked("mid"))
        self.plot_button_mid.pack(side="left", padx=5)

        self.plot_button_high = tk.Button(self.master, text="High", command=lambda: self.plot_button_clicked("high"))
        self.plot_button_high.pack(side="left", padx=5)

    def import_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select a .wav file",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
        )
        if self.file_path:
            # Get only the filename from the path
            filename = os.path.basename(self.file_path)
            self.file_label.config(text=f"File selected: {filename}")
            self.upload_button.config(state="normal")

    def upload_file(self):
        duration, frequencies = analyze_wav(self.file_path)

        print(f"Duration of the audio: {duration:.2f} seconds")
        print("Frequencies in the audio:")
        for i, freq in enumerate(frequencies):
            print(f"Frequency {i}: {freq} Hz")

        # Display the new plot in a container
        self.plot_data(duration, frequencies)

    def plot_data(self, duration, frequencies):
        # Remove the current plot container if it exists
        if self.current_plot_container:
            self.current_plot_container.destroy()

        # Create a new plot based on the selected type
        fig, ax = plt.subplots()
        ax.plot(frequencies, color='r')  # Adjust the plot as needed
        ax.set_title("Frequency-Domain Signal")
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')

        # Display the new plot in a container
        self.current_plot_container = tk.Frame(self.master)
        self.current_plot_container.pack(side="top", fill="both", expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.current_plot_container)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side="top", fill="both", expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

