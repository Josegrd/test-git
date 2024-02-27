# main.py
import tkinter as tk
from py_todo import BackgroundChecker


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Background Checker GUI")

        # Buat objek BackgroundChecker
        self.checker = BackgroundChecker()

        # Tambahkan tombol Start
        self.btn_start = tk.Button(master, text="Start", command=self.checker.start)
        self.btn_start.pack(pady=10)

        # Tambahkan tombol Pause/Resume
        self.btn_pause_resume = tk.Button(master, text="Pause/Resume", command=self.checker.pause_resume)
        self.btn_pause_resume.pack(pady=10)

        # Tambahkan tombol Stop
        self.btn_stop = tk.Button(master, text="Stop", command=self.checker.stop)
        self.btn_stop.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()