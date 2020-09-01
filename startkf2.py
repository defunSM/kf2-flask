import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

EndTask = ctypes.windll.user32.EndTask

#CreateWindow = ctypes.windll.user32.CreateWindowW

titles = []
hwnds = []

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        if buff.value != '':
            titles.append(buff.value)
            hwnds.append(hwnd)
        else:
            pass
    return True


#EndTask(hwnds[2], 1, 0)

def main():

    EnumWindows(EnumWindowsProc(foreach_window), 0)
# Ignore unnamed window titles and only display named windowed titles
    for title, hwnd in zip(titles, hwnds):
        print(title, ' - ', hwnd)

    #CreateWindow("Main", "MainWindow", 0, 300, 300, 1000, 1000, 0, 0, 0, 0)

main()