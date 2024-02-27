from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
import subprocess
from home_gui_oop import HomeGUI
from smart_garden_new import BackgroundChecker
from manual_gui_oop import ManualGUI
import threading
# from smart_garden_system import SmartGardenSystem
class HeadingGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.geometry("1024x600")
        self.master.title("Heading")


        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = 1024
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f'{window_width}x{window_height}+{x}+{y}')

        self.canvas = Canvas(
            self.master,
            bg="#000000",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # self.is_running = True
        self.checker = checker

        self.image_img_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.button_header_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))

        self.background_desktop()
        self.footer_copyright()
        self.title_header()
        self.buttons_header()

        self.canvas.pack()
        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/restore/backu/Heading/build/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/heading_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/heading_assets")
        return ASSETS_PATH / Path(path)

    def background_desktop(self):
        self.canvas.place(x=0, y=0)
        image_1 = self.canvas.create_image(
            1700.0,
            1150.0,
            image=self.image_img_1
        )

    def footer_copyright(self):
        self.canvas.create_text(
            450.0,
            541.0,
            anchor="nw",
            text="©2024 XIII TEDK 1",
            fill="#FFF6F6",
            font=("Montserrat ExtraBold", 12 * -1)
        )

    def title_header(self):
        self.canvas.create_text(
            200.0,
            205.0,
            anchor="nw",
            text="SMART GARDEN SYSTEM",
            fill="#FFF4F4",
            font=("Montserrat", 48 * -1, "bold")
        )

    def buttons_header(self):
        button_image_1 = self.button_header_1
        button_1 = Button(
            image=button_image_1,
            bd=0,
            activebackground="#111111",
            command=self.start_system,
            relief="flat"
        )
        button_1.place(
            x=339.0,
            y=300.0,
            width=329.0,
            height=77.0
        )


    def open_home_gui(self):
        subprocess.run(["python", "home_gui_oop.py"])
        self.master.destroy()


    def start_system(self):
        home_gui = ManualGUI(self.master, checker)
        self.checker.pause_resume()
        # self.garden_system.start_system(self)
        # self.master.destroy()
        # root = Tk()
        # home_gui = HomeGUI(root)
        # root.mainloop()
        # self.open_home_gui()
        # self.garden_system.start_system()
        # threading.Thread(target=self.garden_system.start_system, daemon=True).start()

if __name__ == "__main__":
    # root = Tk()
    # app = HeadingGUI(root)
    # root.mainloop()

    root = Tk()
    # garden_system = SmartGardenSystem()
    checker =BackgroundChecker()
    heading_gui = HeadingGUI(root, checker)
    # heading_gui.check_system_status()  # Contoh penggunaan atribut is_running
    root.mainloop()
