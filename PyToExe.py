import tkinter as tk
from tkinter import filedialog
import subprocess

class ExeConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Python to Exe Converter")

        self.label = tk.Label(master, text="Select a Python file and an icon (optional) to convert to exe:")
        self.label.grid(row=0, column=0, columnspan=2, pady=5)

        self.python_file_label = tk.Label(master, text="Python File:")
        self.python_file_label.grid(row=1, column=0, sticky="e")

        self.python_file_path = tk.StringVar()
        self.python_file_entry = tk.Entry(master, textvariable=self.python_file_path, width=40)
        self.python_file_entry.grid(row=1, column=1, padx=5)

        self.python_file_button = tk.Button(master, text="Browse", command=self.select_python_file)
        self.python_file_button.grid(row=1, column=2)

        self.icon_label = tk.Label(master, text="Icon (optional):")
        self.icon_label.grid(row=2, column=0, sticky="e")

        self.icon_path = tk.StringVar()
        self.icon_entry = tk.Entry(master, textvariable=self.icon_path, width=40)
        self.icon_entry.grid(row=2, column=1, padx=5)

        self.icon_button = tk.Button(master, text="Browse", command=self.select_icon)
        self.icon_button.grid(row=2, column=2)

        self.onefile_var = tk.BooleanVar()
        self.onefile_checkbox = tk.Checkbutton(master, text="One File", variable=self.onefile_var)
        self.onefile_checkbox.grid(row=3, column=0, columnspan=3, sticky="w", padx=5)

        self.noconsole_var = tk.BooleanVar()
        self.noconsole_checkbox = tk.Checkbutton(master, text="No Console", variable=self.noconsole_var)
        self.noconsole_checkbox.grid(row=4, column=0, columnspan=3, sticky="w", padx=5)

        self.convert_button = tk.Button(master, text="Convert to Exe", command=self.convert_to_exe)
        self.convert_button.grid(row=5, column=0, columnspan=3, pady=10)

    def select_python_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.python_file_path.set(file_path)

    def select_icon(self):
        file_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if file_path:
            self.icon_path.set(file_path)

    def convert_to_exe(self):
        python_file = self.python_file_path.get()
        if not python_file:
            self.show_message("Please select a Python file.")
            return

        pyinstaller_command = ["pyinstaller", "--onefile" if self.onefile_var.get() else "", "--noconsole" if self.noconsole_var.get() else ""]

        icon_path = self.icon_path.get()
        if icon_path:
            pyinstaller_command.extend(["--icon", icon_path])

        pyinstaller_command.append(python_file)

        subprocess.call([x for x in pyinstaller_command if x])
        self.show_message("Conversion to exe completed.")

    def show_message(self, message):
        popup = tk.Toplevel()
        popup.title("Message")
        label = tk.Label(popup, text=message)
        label.pack(padx=20, pady=10)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=5)

def main():
    root = tk.Tk()
    app = ExeConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
