from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
from datatime_manager import DateTimeManager
from weatherdata import DateTempManager  # Ganti 'weather_fetcher' dengan nama file yang sesuai
from indicator_lamp import IndicatorManager
# from smart_garden_system import SmartGardenSystem
# from smart_garden_new import BackgroundChecker

class HomeGUI:
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
        # self.checker = BackgroundChecker

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.pack()

        # SUHU

        self.datetime_manager = DateTempManager(
            self.master,
            x_temperature=840.0, y_temperature=290.0,
            size_temp=25,
            city_name="Semarang",  # Ganti dengan nama kota yang diinginkan
            api_key="3ed277858179018f75bd1bf7c6f092e3"  # Ganti dengan kunci API OpenWeatherMap Anda
        )

        # ==================

        #JAM
        self.datetime_manager = DateTimeManager(
            self.master,
            x_hourtime=815.0, y_hourtime=240.0,
            x_daystime=855.0, y_daystime=180.0,
            x_datetime=835.0, y_datetime=213.0,
            size_hour=37
        )
        # ==================
        
        self.image_img_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_img_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_img_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_img_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.button_img_33 = PhotoImage(file=self.relative_to_assets("button_121.png"))
        self.button_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))

        self.background_home_gui()
        self.header_home_gui()
        self.menu_button_home_gui()
        self.time_home()
        self.logo_home_gui()
        self.logo_background_home_gui()
        self.footer_home_gui()
        # self.indicator_manager = IndicatorManager()

        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/New folder/home/build/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/home_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/home_assets")
        return ASSETS_PATH / Path(path)

    def background_home_gui(self):
        self.canvas.place(x=0, y=0)
        image_1 = self.canvas.create_image(
            500.0,
            400.0,
            image=self.image_img_1
        )

    def header_home_gui(self):
        self.canvas.create_text(
            81.0,
            151.0,
            anchor="nw",
            text="Hello",
            fill="#029107",
            font=("Montserrat", 80 * -1, "bold")
        )
        self.canvas.create_text(
            81.0,
            250.0,
            anchor="nw",
            text="Stemba!",
            fill="#191E27",
            font=("Montserrat", 96 * -1, "bold")
        )

    def menu_button_home_gui(self):
        button_1 = Button(
            image=self.button_img_33,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_statistics_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_1.place(
            x=399.0,
            y=115.0,
            width=83.0,
            height=24.0
        )

        button_2 = Button(
            self.canvas,
            image=self.button_img_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_manual_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_2.place(
            x=500.0,
            y=115.0,
            width=72.0,
            height=24.0
        )

        button_3 = Button(
            self.canvas,
            image=self.button_img_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_help_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_3.place(
            x=586.0,
            y=118.0,
            width=40.0,
            height=21.0
        )

    def time_home(self):
        image_2 = self.canvas.create_image(
                    891.0,
                    347.0,
                    image=self.image_image_2
                )
        self.canvas.create_text(
            810.0,
            350.0,
            anchor="nw",
            text="System Status : ",
            fill="#000000",
            font=("Montserrat", 20 * -1, "bold")
        )
        self.indicator_manager = IndicatorManager(self.canvas)
        self.indicator_manager.standby_indicator()

    def logo_home_gui(self):
        self.canvas.create_text(
        119.924560546875,
        29.75469970703125,
        anchor="nw",
        text="Smart Garden System",
        fill="#000000",
        font=("Montserrat", 24 * -1, "bold")
        )
        
        image_3 = self.canvas.create_image(
        56.0,
        41.0,
        image=self.image_image_3
        )

    def logo_background_home_gui(self):
        image_4 = self.canvas.create_image(
        708.0,
        -350.0,
        image=self.image_image_4
        )

    def footer_home_gui(self):
        self.canvas.create_text(
        447.0,
        554.0,
        anchor="nw",
        text="©2024 XIII TEDK 1",
        fill="#ADADAD",
        font=("MontserratRoman SemiBold", 11 * -1)
    )

    def open_statistics_gui(self):
        self.master.destroy()
        subprocess.run(["python", "menu_gui_oop.py"])
    
    def open_manual_gui(self):
        self.master.destroy()
        subprocess.run(["python", "manual_gui_oop.py"])
        # manual_gui = ManualGUI(self.master)
    
    def open_help_gui(self):
        self.master.destroy()
        subprocess.run(["python", "help_gui_oop.py"])
        
if __name__ == "__main__":
    root = Tk()
    app = HomeGUI(root)
    root.mainloop()
