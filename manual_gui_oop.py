from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
from datatime_manager import DateTimeManager
from smart_garden_new import BackgroundChecker
from home_gui_oop import HomeGUI
from datetime import datetime
# import RPi.GPIO as GPIO
# from heading_gui_oop import HeadingGUI
# from smart_garden_system import SmartGardenSystem
# from py_todo import BackgroundChecker


class ManualGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.geometry("1024x600")
        self.master.title("Manual GUI")

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
        self.checker = checker
        # self.checker = BackgroundChecker()

        # Inisialisasi GPIO
        self.relay_pin_1 = 2
        self.relay_pin_2 = 3
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.relay_pin_1, GPIO.OUT)
        # GPIO.setup(self.relay_pin_2, GPIO.OUT)
        self.kondisi_relay_1 = False
        self.kondisi_relay_2 = False


        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_image_44 = PhotoImage(file=self.relative_to_assets("button_44.png"))
        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_image_55 = PhotoImage(file=self.relative_to_assets("button_55.png"))
        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_image_66 = PhotoImage(file=self.relative_to_assets("button_66.png"))
        self.button_image_33 = PhotoImage(file=self.relative_to_assets("button_33.png"))
        self.image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))

        # TODO: Tambahkan fungsi-fungsi GUI lainnya sesuai kebutuhan
        self.background_manual()
        self.sidebar_manual()
        self.manual_control()
        # self.manual_time()
        self.manual_controls()
        self.footer_manual()
        self.manual_logo()

        self.canvas.pack()
        self.master.resizable(False, False)

        # ===================================
        # JAM
        self.datetime_manager = DateTimeManager(
            self.master,
            x_hourtime=489.0, y_hourtime=103.0,
            x_daystime=341.0, y_daystime=112.0,
            x_datetime=341.0, y_datetime=139.0,
            size_hour=48
        )
        # =================

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/restore/backu/Manual/build/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/manual_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/manual_assets")
        return ASSETS_PATH / Path(path)

    def background_manual(self):
        self.canvas.place(x=0, y=0)
        image_1 = self.canvas.create_image(
            1038.0,
            400.0,
            image=self.image_image_1
        )

    def sidebar_manual(self):
        image_2 = self.canvas.create_image(
            -500.0,
            442.0,
            image=self.image_image_2
        )

    def manual_control(self):
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.open_home_gui,
            relief="flat"
        )
        button_1.place(
            x=341.0,
            y=38.0,
            width=76.0,
            height=21.0
        )

        button_2 = Button(
            image=self.button_image_33,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_statistics_gui,
            relief="flat",
            bg="#ffffff"
        )
        button_2.place(
            x=440.0,
            y=36.0,
            width=72.0,
            height=24.0
        )

        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.open_help_gui,
            relief="flat"
        )
        button_3.place(
            x=533.0,
            y=38.5,
            width=38.0,
            height=21.0
        )

    def manual_time(self):
        pass

    def manual_controls(self):
        self.canvas.create_text(
            344.0,
            229.0,
            anchor="nw",
            text="Manual Controls",
            fill="#191E27",
            font=("Montserrat", 36 * -1, "bold")
        )

        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg="#ffffff",
            command=self.toggle_relay_1,
            # command=self.toggle_manual_pump,
            relief="flat"
        )
        self.button_4.place(
            x=357.0,
            y=317.0,
            width=179.0,
            height=173.0
        )

        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg="#ffffff",
            command=self.toggle_relay_2,
            # command=self.toggle_manual_light,
            relief="flat"
        )
        self.button_5.place(
            x=584.0,
            y=317.0,
            width=179.0,
            height=173.0
        )

        button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=self.stop_system,
            relief="flat"
        )
        button_6.place(
            x=811.0,
            y=317.0,
            width=179.0,
            height=173.0
        )

    def stop_system(self):
        # Memanggil fungsi stop_system dari objek SmartGardenSystem
        # self.garden_system.stop_system()
        # home_gui = HomeGUI(self.master)
        self.checker.pause_resume()
        self.master.destroy()
        subprocess.run(["python", "./headiing_gui_oop.py"])
        # Kembali ke heading_gui (Anda mungkin perlu menyesuaikan ini)
        # self.master.destroy()
        # subprocess.run(["python", "heading_gui_oop.py"])

    def toggle_relay_1(self):
        global kondisi_relay_1
        if not self.kondisi_relay_1:
            self.button_4.configure(image=self.button_image_44)
            self.kondisi_relay_1 = True
            self.toggle_manual_pumps()

        else:
            self.button_4.configure(image=self.button_image_4)
            self.kondisi_relay_1 = False
            self.toggle_manual_pumps()


    def toggle_relay_2(self):
        global kondisi_relay_2
        if not self.kondisi_relay_2:
            self.button_5.configure(image=self.button_image_55)
            self.kondisi_relay_2 = True
            self.toggle_manual_lights()

        else:
            self.button_5.configure(image=self.button_image_5)
            self.kondisi_relay_2 = False
            self.toggle_manual_lights()

    def toggle_manual_pumps(self):
        # Mengaktifkan atau menonaktifkan manual pump di SmartGardenSystem
        self.checker.toggle_manual_pump()
        # Menampilkan status manual pump (bisa diintegrasikan dengan GUI Anda)
        print(f"Manual Pump {'ON' if self.kondisi_relay_1 else 'OFF'}")

    def toggle_manual_lights(self):
        # Mengaktifkan atau menonaktifkan manual light di SmartGardenSystem
        self.checker.toggle_manual_light()
        # Menampilkan status manual light (bisa diintegrasikan dengan GUI Anda)
        print(f"Manual Light {'ON' if self.kondisi_relay_2 else 'OFF'}")

    def footer_manual(self):
        self.canvas.create_text(
            609.0,
            568.0,
            anchor="nw",
            text="©2024 XIII TEDK 1",
            fill="#827E7E",
            font=("Montserrat SemiBold", 11 * -1)
        )

    def manual_logo(self):
        self.canvas.create_text(
            707.0,
            31.0,
            anchor="nw",
            text="Smart Garden System",
            fill="#191E27",
            font=("Montserrat", 20 * -1, "bold")
        )

        image_9 = self.canvas.create_image(
            970.0,
            43.0,
            image=self.image_image_9
        )

    def open_statistics_gui(self):
        self.master.destroy()
        subprocess.run(["python", "menu_gui_oop.py"])

    def open_home_gui(self):
        self.master.destroy()
        subprocess.run(["python", "home_gui_oop.py"])

    def open_help_gui(self):
        self.master.destroy()
        subprocess.run(["python", "help_gui_oop.py"])

    def run(self):
        self.master.mainloop()

    # def aktifkan_relay_1(self):
    #     # GPIO.output(self.relay_pin_1, GPIO.HIGH)
    #     print("Yuk Disiram!")
    #
    # def matikan_relay_1(self):
    #     # GPIO.output(self.relay_pin_1, GPIO.LOW)
    #     print("Wes om, Banjir banjirr")
    #
    #
    # def aktifkan_relay_2(self):
    #     # GPIO.output(self.relay_pin_2, GPIO.HIGH)
    #     print("Anjay padang!")
    #
    # def matikan_relay_2(self):
    #     # GPIO.output(self.relay_pin_2, GPIO.LOW)
    #     print("Peteng Wae ben syahdu")



if __name__ == "__main__":
    root = Tk()
    # garden_system = SmartGardenSystem()
    checker = BackgroundChecker()
    manual_gui = ManualGUI(root, checker)
    root.mainloop()
