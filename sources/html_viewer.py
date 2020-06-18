import tkinter as tk
from tkinter import messagebox
from cefpython3 import cefpython as cef
import threading
import sys


def init(html):
    def test_thread():
        sys.excepthook = cef.ExceptHook
        # window_info = cef.WindowInfo(frame.winfo_id())
        # window_info.SetAsChild(frame.winfo_id(), rect)
        cef.Initialize()
        browser = cef.CreateBrowserSync(
            # window_info,
            url=html
        )
        cef.MessageLoop()

    root = tk.Tk()
    root.geometry("800x600")
    threading._start_new_thread(lambda name, depla: test_thread(), ("a", 2))
    # frame = tk.Frame(root, bg='blue', height=500, width=800)
    # frame2 = tk.Frame(root, bg='white', height=200)
    # frame.pack(side='top', fill='x')
    # frame2.pack(side='top', fill='x')

    # tk.Button(frame2, text='Exit', command=on_closing).pack(side='left')
    # tk.Button(frame2, text='Show something',
    #         command=lambda: messagebox.showinfo('TITLE', 'Shown something')).pack(side='right')

    # rect = [0, 0, 800, 500]
    # print('browser: ', rect[2], 'x', rect[3])

    # thread = threading.Thread(target=)
    # thread.start()
    # root.mainloop()
