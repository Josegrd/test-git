from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
from datatime_manager import DateTimeManager

class MenuGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1024x600")
        self.master.title("Menu GUI")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = 1024
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f'{window_width}x{window_height}+{x}+{y}')

        self.canvas = Canvas(
            master,
            bg="#000000",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.image_image_13 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        self.image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        self.image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        self.image_image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        self.image_image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))

        # TODO: Tambahkan fungsi-fungsi GUI lainnya sesuai kebutuhan
        self.menu_background()
        self.button_home_menu()
        self.button_manual_menu()
        self.button_help_menu()
        self.jadwal_penyiraman()
        self.jadwal_penerangan()
        self.logo_menu()
        self.time_menu()
        self.sidebar_menu_background()
        self.footer_menu()

        # ===================================
        # JAM
        self.datetime_manager = DateTimeManager(
            self.master,
            x_hourtime=504.0, y_hourtime=360.0,
            x_daystime=504.0, y_daystime=193.0,
            x_datetime=504.0, y_datetime=228.0,
            size_hour=35
        )
        # =================

        self.canvas.pack()
        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/restore/backu/Menu/build/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/menu_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/menu_assets")
        return ASSETS_PATH / Path(path)

    def menu_background(self):
        self.canvas.place(x=0, y=0)
        image_1 = self.canvas.create_image(
            0,
            500.0,
            image=self.image_image_1
        )
        
        self.canvas.create_text(
        51.0,
        115.0,
        anchor="nw",
        text="Statistics",
        fill="#191E27",
        font=("Montserrat", 36 * -1, "bold"))

    def button_home_menu(self):
        self.button_image_1
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.open_home_gui,
            relief="flat"
        )
        button_1.place(
            x=447.0,
            y=39.0,
            width=82.0,
            height=24.0
        )

    def button_manual_menu(self):
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.open_manual_gui,
            relief="flat"
        )
        button_2.place(
            x=545.0,
            y=38.5,
            width=72.0,
            height=24.0
        )

    def button_help_menu(self):
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.open_help_gui,
            relief="flat"
        )
        button_3.place(
            x=634.0,
            y=41.5,
            width=38.0,
            height=21.0
        )

    # TODO: Tambahkan definisi fungsi-fungsi GUI lainnya sesuai kebutuhan
    
    def jadwal_penyiraman(self):
        image_13 = self.canvas.create_image(
            269.0,
            265.0,
            image=self.image_image_13
        )

        self.canvas.create_text(
            91.0,
            222.0,
            anchor="nw",
            text="JADWAL\nPENYIRAMAN",
            fill="#191E27",
            font=("Montserrat", 16 * -1, "bold")
        )

        image_3 = self.canvas.create_image(
            104.0,
            308.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            136.0,
            287.0,
            anchor="nw",
            text="Pagi \n07.00",
            fill="#737373",
            font=("Montserrat Regular", 16 * -1)
        )

        self.canvas.create_text(
            261.0,
            288.0,
            anchor="nw",
            text="Siang\n12.00",
            fill="#737373",
            font=("Montserrat Regular", 16 * -1)
        )

        image_4 = self.canvas.create_image(
            230.0,
            308.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            387.0,
            287.0,
            anchor="nw",
            text="Sore\n17.00",
            fill="#737373",
            font=("Montserrat Regular", 16 * -1)
        )

        image_5 = self.canvas.create_image(
            355.0,
            309.0,
            image=self.image_image_5
        )
        
        

    def jadwal_penerangan(self):
        image_6 = self.canvas.create_image(
            269.0,
            442.0,
            image=self.image_image_6
        )

        self.canvas.create_text(
            91.0,
            400.0,
            anchor="nw",
            text="JADWAL\nPENERANGAN",
            fill="#191E27",
            font=("Montserrat", 16 * -1, "bold")
        )

        self.canvas.create_text(
            136.0,
            466.0,
            anchor="nw",
            text="Pagi\n06.00",
            fill="#737373",
            font=("Montserrat Regular", 16 * -1)
        )

        image_7 = self.canvas.create_image(
            102.0,
            483.0,
            image=self.image_image_7
        )

        self.canvas.create_text(
            262.0,
            465.0,
            anchor="nw",
            text="Sore\n17.00",
            fill="#737373",
            font=("Montserrat Regular", 16 * -1)
        )

        image_8 = self.canvas.create_image(
            233.0,
            485.0,
            image=self.image_image_8
        )
    
    
    def logo_menu(self):
        self.canvas.create_text(
            84.0,
            36.0,
            anchor="nw",
            text="Smart Garden System",
            fill="#191E27",
            font=("Montserrat", 20 * -1, "bold")
        )

        image_9 = self.canvas.create_image(
            43.0,
            43.0,
            image=self.image_image_9
        )
    # logo_menu(canvas, image_image_9)
    # LOGO MENU END


    # TIME MENU START
    def time_menu(self):

        image_10 = self.canvas.create_image(
            602.0,
            354.0,
            image=self.image_image_10
        )
    # time_menu(canvas, image_image_10)
    # TIME MENU END


    # SIDEBAR MENU BACKGROUND START
    def sidebar_menu_background(self):
        image_11 = self.canvas.create_image(
            1537.0,
            442.0,
            image=self.image_image_11,
        )
        
    def footer_menu(self):
        self.canvas.create_text(
            285.0,
            566.0,
            anchor="nw",
            text="©2024 XIII TEDK 1",
            fill="#827E7E",
            font=("Montserrat SemiBold", 11 * -1)
        )
        
    def open_manual_gui(self):
        self.master.destroy()
        subprocess.run(["python", "manual_gui_oop.py"])  
    
    def open_home_gui(self):
        self.master.destroy()
        subprocess.run(["python", "home_gui_oop.py"])  
    
    def open_help_gui(self):
        self.master.destroy()
        subprocess.run(["python", "help_gui_oop.py"])  
    
    
    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    menu_gui = MenuGUI(root)
    menu_gui.run()
