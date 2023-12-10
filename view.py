import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Upload GUI")
        self.master.geometry("600x400")

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
        self.upload_button = tk.Button(self.master, text="Upload", state=tk.DISABLED, command=self.upload_file)
        self.upload_button.pack(pady=10)

        # Plot buttons
        self.plot_button_low = tk.Button(self.master, text="Low", command=lambda: self.plot_button_clicked("low"))
        self.plot_button_low.pack(side=tk.LEFT, padx=5)

        self.plot_button_mid = tk.Button(self.master, text="Mid", command=lambda: self.plot_button_clicked("mid"))
        self.plot_button_mid.pack(side=tk.LEFT, padx=5)

        self.plot_button_high = tk.Button(self.master, text="High", command=lambda: self.plot_button_clicked("high"))
        self.plot_button_high.pack(side=tk.LEFT, padx=5)

    def import_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            # Get only the filename from the path
            filename = os.path.basename(self.file_path)
            self.file_label.config(text=f"File selected: {filename}")
            self.upload_button.config(state=tk.NORMAL)

    def upload_file(self):
        # Add your file upload logic here
        print(f"Uploading file: {self.file_path}")

    def plot_button_clicked(self, plot_type):
        # Remove the current plot container if it exists
        if self.current_plot_container:
            self.current_plot_container.destroy()

        # Create a new plot based on the selected type
        if plot_type == "low":
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [4, 5, 6])  # Replace with your low plot data
            ax.set_title("Low Plot")
        elif plot_type == "mid":
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [7, 8, 9])  # Replace with your mid plot data
            ax.set_title("Mid Plot")
        elif plot_type == "high":
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [10, 11, 12])  # Replace with your high plot data
            ax.set_title("High Plot")

        # Display the new plot in a container
        self.current_plot_container = tk.Frame(self.master)
        self.current_plot_container.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.current_plot_container)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
