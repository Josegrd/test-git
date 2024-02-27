from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

class HelpGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1024x600")
        self.master.configure(bg="#ffffff")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = 1024
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        self.canvas = Canvas(
            self.master,
            bg = "#EBE9EE",
            height = 600,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack()
        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        
        self.background_help_gui()
        self.button_menu_help_gui()
        self.footer_help_gui()
        self.moreInfo_help_gui()
        self.guide_help_gui()
        self.logo_help_gui()

        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/New folder/home/help_gui/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/help_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/help_assets")
        return ASSETS_PATH / Path(path)

    def background_help_gui(self):
        self.canvas.place(x = 0, y = 0)
        image_1 = self.canvas.create_image(
            700.0,
            500.0,
            image=self.image_image_1
        )
    
    def button_menu_help_gui(self):
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_home_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_1.place(
            x=724.0,
            y=32.0,
            width=82.0,
            height=24.0
        )

        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_manual_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_2.place(
            x=822.0,
            y=32.0,
            width=72.0,
            height=24.0
        )

        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_statistics_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_3.place(
            x=911.0,
            y=32.0,
            width=73.0,
            height=21.0
        )
        
    def footer_help_gui(self):
        self.canvas.create_text(
            447.0,
            554.0,
            anchor="nw",
            text="©2024 XIII TEDK 1",
            fill="#000000",
            font=("Montserrat", 11 * -1, "bold")
        )
        
        image_2 = self.canvas.create_image(
            800.0,
            966.0,
            image=self.image_image_2
        )

    def moreInfo_help_gui(self):
        image_3 = self.canvas.create_image(
            848.0,
            231.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            775.0,
            164.0,
            anchor="nw",
            text="More Infomation :",
            fill="#000000",
            font=("Montserrat", 16 * -1, "bold")
        )

        self.canvas.create_text(
            775.0,
            200.0,
            anchor="nw",
            text="Tugas Akhir \nXIII TEDK 1\n2024",
            fill="#000000",
            font=("Montserrat SemiBold", 16 * -1)
        )

    def guide_help_gui(self):
        self.canvas.create_text(
            120.0,
            148.0,
            anchor="nw",
            text="GUIDE :",
            fill="#191E27",
            font=("Montserrat", 20 * -1, "bold")
        )
        self.canvas.create_text(
            142.0,
            190.0,
            anchor="nw",
            text="1.    Alat ini bisa digunakan\n      secara manual maupun\n      diset secara otomatis\n"
                 "2.   Kami sudah mengatur\n      waktu waktu ideal untuk\n      menyalakan penyiram\n      taman dan penerangan\n      lampu\n"
                 "3.   Jika ingin menjalankan\n      secara manual, klik\n      menu Manual",
            fill="#000000",
            font=("Montserrat Medium", 15 * -1)
        )

    def logo_help_gui(self):
        image_4 = self.canvas.create_image(
            188.0,
            43.0,
            image=self.image_image_4
        )
        
    def open_statistics_gui(self):
        self.master.destroy()
        subprocess.run(["python", "menu_gui_oop.py"])    
    
    def open_manual_gui(self):
        self.master.destroy()
        subprocess.run(["python", "manual_gui_oop.py"])  
    
    def open_home_gui(self):
        self.master.destroy()
        subprocess.run(["python", "home_gui_oop.py"])

if __name__ == "__main__":
    root = Tk()
    app = HelpGUI(root)
    root.mainloop()
