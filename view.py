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
        self.analysis_data = None  # Store analysis data for use in button clicks

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
        self.plot_button_low = tk.Button(self.master, text="Low", command=self.plot_button_clicked_low)
        self.plot_button_low.pack(side="left", padx=5)

        self.plot_button_mid = tk.Button(self.master, text="Mid", command=self.plot_button_clicked_mid)
        self.plot_button_mid.pack(side="left", padx=5)

        self.plot_button_high = tk.Button(self.master, text="High", command=self.plot_button_clicked_high)
        self.plot_button_high.pack(side="left", padx=5)

    def import_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All files", "*.*")]
        )

        if self.file_path:
            # Check if the file is a .wav file
            if not self.file_path.lower().endswith('.wav'):
                converted_file_path = self.convert_to_wav(self.file_path)
                if converted_file_path:
                    self.file_path = converted_file_path
                else:
                    print("Error converting file to .wav.")
                    return None

            # Get only the filename from the path
            filename = os.path.basename(self.file_path)
            self.file_label.config(text=f"File selected: {filename}")
            self.upload_button.config(state="normal")

    def upload_file(self):
        self.analysis_data = analyze_wav(self.file_path)
        if self.analysis_data is not None:
            duration, _, _, _ = self.analysis_data
            print(f"Duration of the audio: {duration:.2f} seconds")

    def plot_button_clicked_low(self):
        if self.analysis_data is not None:
            _, low_frequencies, _, _ = self.analysis_data
            self.plot_data(range(len(low_frequencies)), low_frequencies, "Low Frequencies", "Frequency (Hz)", "Amplitude", "Low Plot", "top")

    def plot_button_clicked_mid(self):
        if self.analysis_data is not None:
            _, _, mid_frequencies, _ = self.analysis_data
            self.plot_data(range(len(mid_frequencies)), mid_frequencies, "Mid Frequencies", "Frequency (Hz)", "Amplitude", "Mid Plot", "top")

    def plot_button_clicked_high(self):
        if self.analysis_data is not None:
            _, _, _, high_frequencies = self.analysis_data
            self.plot_data(range(len(high_frequencies)), high_frequencies, "High Frequencies", "Frequency (Hz)", "Amplitude", "High Plot", "top")

    def plot_data(self, x_values, y_values, title, xlabel, ylabel, plot_title, side):
        # Remove the current plot container if it exists
        if self.current_plot_container:
            self.current_plot_container.destroy()

        # Create a new plot based on the selected type
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, color='r')  # Adjust the plot as needed
        ax.set_title(plot_title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # Display the new plot in a container
        self.current_plot_container = tk.Frame(self.master)
        self.current_plot_container.pack(side=side, fill="both", expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.current_plot_container)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side="top", fill="both", expand=1)

# ... (rest of the code remains unchanged)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

