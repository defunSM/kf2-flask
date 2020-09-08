
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from os import path
# Select KF2 Path

# Validates KF2 Path
def validation(path_to_KF2):
    check_file = path_to_KF2 + "/Binaries/Win64/steam_api64.dll"
    if path.exists(check_file):
        return path_to_KF2
    else:
        # make pop up
        messagebox.showwarning("Wrong Directory Selected", "Can not find steam_api64.dll for KF2 (Most likely wrong KF2 Path please select the 'KillingFloor2' folder.")
        selectDir()


# Asks for KillingFloor2 Folder
def selectDir():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()
    print(file_path)
    if file_path:
        validation(file_path)
    else:
        messagebox.showwarning("No Directory Selected", "No KF2 Directory selected please select")
        return ""

    return file_path # Return KF2 FolderPath
