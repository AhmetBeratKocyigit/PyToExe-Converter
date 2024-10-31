# Python to EXE Converter

This is a simple GUI-based application built using Python's `tkinter` library. It allows users to convert Python `.py` scripts into standalone `.exe` files using `PyInstaller`. The tool also supports optional icon selection for the generated executable and offers additional options for customization.

## Features

- Select a Python file to convert to `.exe`.
- Optional icon selection for the `.exe` file.
- Option to create a single `.exe` file (`--onefile`).
- Option to suppress the console window (`--noconsole`).
- User-friendly GUI with easy-to-navigate interface.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `PyInstaller` (install using `pip install pyinstaller`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/AhmetBeratKocyigit/PyToExe-Converter
    ```
2. Install `PyInstaller` if you haven't already:
    ```bash
    pip install pyinstaller
    ```

## Usage

1. In the GUI:
    - Use the **Browse** button to select a Python file to convert.
    - (Optional) Use the **Browse** button next to **Icon** to select an `.ico` file to use as the icon for the `.exe`.
    - Check the **One File** option if you want a single executable.
    - Check the **No Console** option to suppress the console window.
2. Click **Convert to Exe** to start the conversion. A message box will appear upon completion.

## Notes

- The conversion process might take a few moments depending on the script size and the options selected.
- The resulting `.exe` file will be saved in the `dist` folder within the directory where the script is run.




