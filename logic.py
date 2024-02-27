import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("800x600")

        self.current_frame = None
        self.show_frame(FirstFrame)

    def show_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

class FirstFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="First Frame")
        label.pack(pady=10)

        # Load the background image for GUI 1
        self.background_image_1 = tk.PhotoImage(file="assets/heading_assets/image_1.png")
        background_label = tk.Label(self, image=self.background_image_1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        button = tk.Button(self, text="Go to Second Frame", command=self.go_to_second_frame)
        button.pack(pady=10)

    def go_to_second_frame(self):
        self.master.show_frame(SecondFrame)

class SecondFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Second Frame")
        label.pack(pady=10)

        # Load the background image for GUI 2
        self.background_image_2 = tk.PhotoImage(file="assets/heading_assets/images.png")
        background_label = tk.Label(self, image=self.background_image_2)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        button = tk.Button(self, text="Go to First Frame", command=self.go_to_first_frame)
        button.pack(pady=10)

    def go_to_first_frame(self):
        self.master.show_frame(FirstFrame)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
