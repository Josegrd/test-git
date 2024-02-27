from tkinter import Tk, BOTH, Frame, Label, PhotoImage, Button, Canvas
import threading
from datatime_manager import DateTimeManager
from datetime import datetime
import datetime
import time
import sys
from weatherdata import DateTempManager
from indicator_lamp import IndicatorManager
# import RPi.GPIO as GPIO


class MainApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("SmartGardenTE1 1.0")
        self.geometry("1024x600")
        self.configure(bg="#ffffff")
        # self.attributes('-fullscreen', True)
        self.checker = BackgroundChecker()
        self.bind('<Escape>', self.exit_application)

        self.current_frame = None
        self.show_frame(HeadingGUI)

    def show_frame(self, frame_class):
        new_frame = frame_class(self, self.checker)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=BOTH, expand=True)

    def exit_application(self, event=None):
        self.destroy()

class HeadingGUI(Frame):
    def __init__(self, master, checker):
        super().__init__(master)
        self.master = master
        self.checker = checker

        self.canvas = Canvas(self, bg="#000000", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # Load the background image for GUI 1
        self.background_image_1 = PhotoImage(file="./assets/heading_assets/image_1.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image_1)

        self.button_header_1 = PhotoImage(file= "./assets/heading_assets/button_1new.png")

        self.footer_copyright()
        self.title_header()
        self.buttons_header()

    def go_to_home_gui(self):
        self.master.show_frame(HomeGUI)
        self.checker.pause_resume()

    def buttons_header(self):
        button_image_1 = self.button_header_1
        button_1 = Button(
            image=button_image_1,
            bd=0,
            bg="#133201",
            fg="#BFEA7C",
            command=self.go_to_home_gui,
            relief="flat"
        )
        button_1.place(
            x=339.0,
            y=300.0,
            width=312.0,
            height=76.0
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

class HomeGUI(Frame):
    def __init__(self, master, checker):
        super().__init__(master)
        self.master = master
        self.checker = checker
        self.indicator_lamp = self.checker.indicatorLamp

        self.canvas = Canvas(self, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)


        # LOAD IMAGE
        # self.image_img_1 = PhotoImage(file="./assets/home_assets/image_1.png")
        # self.image_img_2 = PhotoImage(file="./assets/home_assets/image_2.png")
        # self.image_img_3 = PhotoImage(file="./assets/home_assets/image_3.png")
        # self.image_img_4 = PhotoImage(file="./assets/home_assets/image_4.png")
        self.button_img_33 = PhotoImage(file="./assets/home_assets/button_33.png")
        self.button_img_2 = PhotoImage(file="./assets/home_assets/button_2.png")
        self.button_img_3 = PhotoImage(file="./assets/home_assets/button_3.png")
        self.image_image_2 = PhotoImage(file="./assets/home_assets/image_2.png")
        self.image_image_5 = PhotoImage(file="./assets/home_assets/image_5.png")
        self.image_image_6 = PhotoImage(file="./assets/home_assets/image_6.png")
        self.image_image_7 = PhotoImage(file="./assets/home_assets/image_7.png")
        self.image_image_3 = PhotoImage(file="./assets/home_assets/image_3.png")
        self.image_image_4 = PhotoImage(file="./assets/home_assets/image_4.png")

        # SUHU

        self.datetime_manager = DateTempManager(
            self,
            x_temperature=840.0, y_temperature=290.0,
            size_temp=25,
            city_name="Semarang",  # Ganti dengan nama kota yang diinginkan
            api_key="3ed277858179018f75bd1bf7c6f092e3"  # Ganti dengan kunci API OpenWeatherMap Anda
        )

        # ==================

        # JAM
        self.datetime_manager = DateTimeManager(
            self,
            x_hourtime=815.0, y_hourtime=240.0,
            x_daystime=855.0, y_daystime=180.0,
            x_datetime=835.0, y_datetime=213.0,
            size_hour=37
        )
        # ==================

        self.header_home_gui()
        self.logo_background_home_gui()
        self.logo_home_gui()
        self.menu_button_home_gui()
        self.time_home()
        self.footer_home_gui()

    def go_to_menu_gui(self):
        self.master.show_frame(MenuGUI)

    def go_to_manual_gui(self):
        self.master.show_frame(ManualGUI)

    def go_to_help_gui(self):
        self.master.show_frame(MenuGUI)

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

    def logo_background_home_gui(self):
        image_4 = self.canvas.create_image(
            708.0,
            -350.0,
            image=self.image_image_4
        )

    def menu_button_home_gui(self):
        button_1 = Button(
            image=self.button_img_33,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_menu_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#BFEA7C",
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
            command=self.go_to_manual_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#BFEA7C",
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
            command=self.go_to_help_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#BFEA7C",
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
        # self.indicator_manager.standby_indicator()
        if self.indicator_lamp == 1:
            self.indicator_manager.standby_indicator()
        elif self.indicator_lamp == 2:
            self.indicator_manager.running_indicator()

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

    def footer_home_gui(self):
        self.canvas.create_text(
            447.0,
            554.0,
            anchor="nw",
            text="©2024 XIII TEDK 1",
            fill="#ADADAD",
            font=("MontserratRoman SemiBold", 11 * -1)
        )

class MenuGUI(Frame):
    def __init__(self, master, checker):
        super().__init__(master)
        self.master = master
        self.checker = checker

        self.canvas = Canvas(self, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # LOAD IMAGE
        # self.image_image_1 = PhotoImage(file="./assets/menu_assets/image_1.png")
        self.button_image_1 = PhotoImage(file="./assets/menu_assets/button_1.png")
        self.button_image_2 = PhotoImage(file="./assets/menu_assets/button_2.png")
        self.button_image_3 = PhotoImage(file="./assets/menu_assets/button_3.png")
        self.image_image_13 = PhotoImage(file="./assets/menu_assets/image_6.png")
        self.image_image_3 = PhotoImage(file="./assets/menu_assets/image_3.png")
        self.image_image_4 = PhotoImage(file="./assets/menu_assets/image_4.png")
        self.image_image_5 = PhotoImage(file="./assets/menu_assets/image_5.png")
        self.image_image_6 = PhotoImage(file="./assets/menu_assets/image_6.png")
        self.image_image_7 = PhotoImage(file="./assets/menu_assets/image_7.png")
        self.image_image_8 = PhotoImage(file="./assets/menu_assets/image_8.png")
        self.image_image_9 = PhotoImage(file="./assets/menu_assets/image_9.png")
        self.image_image_10 = PhotoImage(file="./assets/menu_assets/image_10.png")
        self.image_image_11 = PhotoImage(file="./assets/menu_assets/image_11.png")

        # JAM
        self.datetime_manager = DateTimeManager(
            self.master,
            x_hourtime=504.0, y_hourtime=360.0,
            x_daystime=504.0, y_daystime=193.0,
            x_datetime=504.0, y_datetime=228.0,
            size_hour=35
        )
        # ==================

        self.button_home_menu()
        self.button_manual_menu()
        self.button_help_menu()
        self.jadwal_penyiraman()
        self.jadwal_penerangan()
        self.logo_menu()
        self.time_menu()
        self.sidebar_menu_background()
        self.footer_menu()

    def go_to_home_gui(self):
        self.master.show_frame(HomeGUI)

    def go_to_manual_gui(self):
        self.master.show_frame(ManualGUI)

    def go_to_help_gui(self):
        self.master.show_frame(HelpGUI)

    def sidebar_menu_background(self):
        image_11 = self.canvas.create_image(
            1537.0,
            442.0,
            image=self.image_image_11,
        )

    def button_home_menu(self):
        self.button_image_1
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.go_to_home_gui,
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
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.go_to_manual_gui,
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
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.go_to_help_gui,
            relief="flat"
        )
        button_3.place(
            x=634.0,
            y=41.5,
            width=38.0,
            height=21.0
        )

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

    def time_menu(self):
        image_10 = self.canvas.create_image(
            602.0,
            354.0,
            image=self.image_image_10
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

class ManualGUI(Frame):
    def __init__(self, master, checker):
        super().__init__(master)
        self.master = master
        self.checker = checker

        self.canvas = Canvas(self, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # LOAD IMAGE
        # self.image_image_1 = PhotoImage(file="./assets/manual_assets/image_1.png")
        self.image_image_2 = PhotoImage(file="./assets/manual_assets/image_2.png")
        self.button_image_1 = PhotoImage(file="./assets/manual_assets/button_1.png")
        self.button_image_2 = PhotoImage(file="./assets/manual_assets/button_2.png")
        self.button_image_3 = PhotoImage(file="./assets/manual_assets/button_3.png")
        self.button_image_4 = PhotoImage(file="./assets/manual_assets/button_4.png")
        self.button_image_44 = PhotoImage(file="./assets/manual_assets/button_44.png")
        self.button_image_5 = PhotoImage(file="./assets/manual_assets/button_5.png")
        self.button_image_55 = PhotoImage(file="./assets/manual_assets/button_55.png")
        self.button_image_6 = PhotoImage(file="./assets/manual_assets/button_6.png")
        self.button_image_66 = PhotoImage(file="./assets/manual_assets/button_66.png")
        self.button_image_33 = PhotoImage(file="./assets/manual_assets/button_33.png")
        self.image_image_9 = PhotoImage(file="./assets/manual_assets/image_9.png")

        # JAM
        self.datetime_manager = DateTimeManager(
            self.master,
            x_hourtime=489.0, y_hourtime=103.0,
            x_daystime=341.0, y_daystime=112.0,
            x_datetime=341.0, y_datetime=139.0,
            size_hour=48
        )

        # PUMP SETTINGS
        self.set_hour_pump = self.checker.set_hour_pump
        self.set_minute_pump = self.checker.set_minute_pump
        self.set_minute_pump_end = self.checker.set_minute_pump_end
        # self.set_second_pump = self.checker.set_second_pump
        # self.set_second_pump_end = self.checker.set_second_pump_end
        self.is_pump_on = self.checker.is_pump_on
        # self.is_pump_status = self.checker,is_pump_status

        # LIGHT SETTINGS
        self.set_hour_light = self.checker.set_hour_light
        self.set_minute_light = self.checker.set_minute_light
        self.set_minute_light_end = self.checker.set_minute_light_end
        self.set_hour_light_end = self.checker.set_hour_light_end
        self.is_light_on = self.checker.is_light_on

        self.sidebar_manual()
        self.manual_control()
        self.manual_controls()
        self.footer_manual()
        self.manual_logo()

        self.update_start_pump_button = threading.Thread(target=self.update_start_pump_button)
        self.update_start_pump_button.start()
        self.update_start_light_button = threading.Thread(target=self.update_start_light_button)
        self.update_start_light_button.start()
        self.update_is_pump = threading.Thread(target=self.update_is_on)
        self.update_is_pump.start()
        self.check_thread = threading.Thread(target=self.check_schedule)
        self.check_thread.start()

    def go_to_home_gui(self):
        self.master.show_frame(HomeGUI)

    def go_to_menu_gui(self):
        self.master.show_frame(MenuGUI)

    def go_to_help_gui(self):
        self.master.show_frame(HelpGUI)

    def sidebar_manual(self):
        image_2 = self.canvas.create_image(
            -500.0,
            442.0,
            image=self.image_image_2
        )

    def manual_control(self):
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#BFEA7C",
            highlightthickness=0,
            command=self.go_to_home_gui,
            relief="flat"
        )
        self.button_1.place(
            x=341.0,
            y=38.0,
            width=76.0,
            height=21.0
        )

        self.button_2 = Button(
            image=self.button_image_33,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_menu_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#BFEA7C",
        )
        self.button_2.place(
            x=440.0,
            y=36.0,
            width=72.0,
            height=24.0
        )

        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#BFEA7C-",
            highlightthickness=0,
            command=self.go_to_help_gui,
            relief="flat"
        )
        self.button_3.place(
            x=533.0,
            y=38.5,
            width=38.0,
            height=21.0
        )

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
            activebackground="#ffffff",
            command=self.toggle_pump,
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
            activebackground="#ffffff",
            command=self.toggle_light,
            relief="flat"
        )
        self.button_5.place(
            x=584.0,
            y=317.0,
            width=179.0,
            height=173.0
        )

        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.stop_system,
            relief="flat"
        )
        self.button_6.place(
            x=811.0,
            y=317.0,
            width=179.0,
            height=173.0
        )

    def stop_system(self):
        self.button_6.configure(image=self.button_image_66)
        self.master.show_frame(HeadingGUI)
        self.checker.pause_resume()
        # Buat objek baru dari HeadingGUI


    # PUMP SETTINGS BUTTON
    def toggle_pump(self):
        print(self.is_pump_on)
        if self.is_pump_on:
            self.checker.turn_off_pump()
            self.button_4.configure(image=self.button_image_4)
        else:
            self.checker.turn_on_pump()
            self.button_4.configure(image=self.button_image_44)
        print(self.is_pump_on)
        self.checker.not_status_pump()
        # self.checker.toggle_manual_pump()

    def update_is_on(self):
        while True:
            self.is_pump_on = self.checker.is_pump_on
            self.is_light_on = self.checker.is_light_on
            self.is_pump_status = self.checker.is_pump_status
            self.is_light_status = self.checker.is_light_status
            time.sleep(1)

    def check_schedule(self):
        while True:
            now = datetime.datetime.now()
            if now.hour in self.set_hour_pump and now.minute == self.set_minute_pump: #and now.second == self.set_second_pump_start:
                if self.is_pump_status == False:
                    self.button_4.configure(image=self.button_image_44)
                else:
                    pass
            elif now.hour in self.set_hour_pump and now.minute == self.set_minute_pump_end and now.second == 0:
                if self.is_pump_status == True:
                    self.button_4.configure(image=self.button_image_4) #Turn off pump if time is not 11:09:00
                else:
                    self.button_4.configure(image=self.button_image_4)
            elif now.hour in self.set_hour_light and now.minute == self.set_minute_light:
                if self.is_light_status == False:
                    self.button_5.configure(image=self.button_image_55)
                else:
                    pass
            elif now.hour in self.set_hour_light_end and now.minute == self.set_minute_light_end and now.second == 0:
                if self.is_light_status == True:
                    self.button_5.configure(image=self.button_image_5)
                else:
                    self.button_5.configure(image=self.button_image_5)
            time.sleep(1)  # Check every second

    def update_start_pump_button(self):
        if self.is_pump_on:
            self.button_4.configure(image=self.button_image_44)
        else:
            self.button_4.configure(image=self.button_image_4)

    # PUMP SETTINGS BUTTON END

    # =====================================================

    # LIGHT SETTINGS BUTTON
    def toggle_light(self):
        print(self.is_light_on)
        if self.is_light_on:
            self.checker.turn_off_light()
            self.button_5.configure(image=self.button_image_5)
        else:
            self.checker.turn_on_light()
            self.button_5.configure(image=self.button_image_55)
        print(self.is_light_on)
        self.checker.not_status_light()
        # self.checker.toggle_manual_light()

    def update_start_light_button(self):
        if self.is_light_on:
            self.button_5.configure(image=self.button_image_55)
        else:
            self.button_5.configure(image=self.button_image_5)

    # LIGHT SETTINGS BUTTON END

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

class HelpGUI(Frame):
    def __init__(self, master, checker):
        super().__init__(master)
        self.master = master
        self.checker = checker

        self.canvas = Canvas(self, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # LOAD IMAGE
        # self.image_image_1 = PhotoImage(file="./assets/help_assets/image_1.png")
        self.button_image_1 = PhotoImage(file="./assets/help_assets/button_1.png")
        self.button_image_2 = PhotoImage(file="./assets/help_assets/button_2.png")
        self.button_image_3 = PhotoImage(file="./assets/help_assets/button_3.png")
        self.image_image_2 = PhotoImage(file="./assets/help_assets/image_2.png")
        self.image_image_3 = PhotoImage(file="./assets/help_assets/image_3.png")
        self.image_image_4 = PhotoImage(file="./assets/help_assets/image_4.png")

        self.button_menu_help_gui()
        self.footer_help_gui()
        self.moreInfo_help_gui()
        self.guide_help_gui()
        self.logo_help_gui()

    def go_to_home_gui(self):
        self.master.show_frame(HomeGUI)

    def go_to_manual_gui(self):
        self.master.show_frame(ManualGUI)

    def go_to_menu_gui(self):
        self.master.show_frame(MenuGUI)

    def button_menu_help_gui(self):
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_home_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#ffffff",
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
            command=self.go_to_manual_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#ffffff",
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
            command=self.go_to_menu_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#ffffff",
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


class BackgroundChecker:
    def __init__(self):
        self.pause_resume_event = threading.Event()
        self.stop_event = threading.Event()

        self.running_count = 0
        # self.manual_pump = False
        # self.manual_light = False

        self.is_pump_status = False
        self.is_light_status = False

        self.lampIndicator = False
        self.pumpIndicator = False
        self.indicatorLamp = 1
        self.is_pump_on = False
        self.is_light_on = False

        self.window_width = 1024
        self.window_height = 600

        # PUMP TIME SETTINGS
        self.set_hour_pump = [7, 10, 16]
        self.set_minute_pump = 10
        self.set_minute_pump_end = self.set_minute_pump + 5
        self.js = 100

        # LIGHT TIME SETTINGS
        self.set_hour_light = [17]
        self.set_hour_light_end = [6]
        self.set_minute_light = 0
        self.set_minute_light_end = self.set_minute_light + 1

        # GPIO SETUP
        # GPIO.setmode(GPIO.BCM)
        # self.pin_relay_pompa = 17
        # self.pin_relay_lampu = 27
        # self.pin_relay_indicator = 22
        # for i in range(2, 7):
        #     GPIO.setup(i, GPIO.OUT)
        #     GPIO.output(i, GPIO.HIGH)
        # GPIO.setup(self.pin_relay_pompa, GPIO.OUT)  # Relay untuk pompa
        # GPIO.setup(self.pin_relay_lampu, GPIO.OUT)  # Relay untuk sistem penerangan
        # GPIO.setup(self.pin_relay_indicator, GPIO.OUT)  # Relay untuk lampu indikator

    def activate_relay(self, relay_pin):
        # GPIO.output(relay_pin, GPIO.HIGH)
        print("relay nyala")

    def deactivate_relay(self, relay_pin):
        # GPIO.output(relay_pin, GPIO.LOW)
        print("relay mati")
    def turn_on_pump(self):
        # self.activate_relay(self.pin_relay_pompa)  # Relay untuk pompa
        # self.deactivate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_pump_on = True
        # self.indicatorLamp = 2
        self.pumpIndicator = True
        # self.indicator_detact()
        print("Pompa Menyala")

    def turn_off_pump(self):
        # self.deactivate_relay(self.pin_relay_pompa)  # Relay untuk pompa
        # self.activate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_pump_on = False
        # self.indicatorLamp = 1
        self.pumpIndicator = False
        # self.indicator_detact()
        print("Pompa Mati")

    def turn_on_light(self):
        # self.activate_relay(self.pin_relay_lampu)  # Relay untuk sistem penerangan
        # self.deactivate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_light_on = True
        # self.indicatorLamp = 2
        self.lampIndicator = True
        # self.indicator_detact()
        print("Lampu Menyala")

    def turn_off_light(self):
        # self.deactivate_relay(self.pin_relay_lampu)  # Relay untuk sistem penerangan
        # self.activate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_light_on = False
        # self.indicatorLamp = 1
        self.lampIndicator = False
        # self.indicator_detact()
        print("Lampu Mati")

    # def indicator_detact(self):
    #     if self.is_pump_on == True and self.is_light_on == False:
    #         self.indicatorLamp = 1
    #     elif self.is_pump_on == False and self.is_light_on == True:
    #         self.indicatorLamp = 1
    #     else:
    #         self.indicatorLamp = 2

    def not_status_pump(self):
        self.is_pump_status = not self.is_pump_status

    def not_status_light(self):
        self.is_light_status = not self.is_light_status

    def _analyse_things(self):
        for x in range(1000):
            # while True:
            current_time = datetime.datetime.now()
            if self.stop_event.is_set():
                print('Exiting')
                print()
                sys.exit()
                break
            else:
                self.pause_resume_event.wait()
                print(current_time.second)
                # print(self.is_pump_status)
                if current_time.hour in self.set_hour_pump and current_time.minute == self.set_minute_pump:  # and current_time.second == self.set_second_pump_start:
                    if self.is_pump_status == False:
                        self.turn_on_pump()  # Turn on pump
                    else:
                        pass
                elif current_time.hour in self.set_hour_pump and current_time.minute == self.set_minute_pump_end and current_time.second == 0:  # and current_time.second >= self.set_second_pump_end:
                    if self.is_pump_status == True:
                        self.turn_off_pump()  # Turn off pump if time is not 11:09:00
                    else:
                        self.turn_off_pump()
                elif current_time.hour in self.set_hour_light and current_time.minute == self.set_minute_light:
                    if self.is_light_status == False:
                        self.turn_on_light()
                    else:
                        pass
                elif current_time.hour in self.set_hour_light_end and current_time.minute == self.set_minute_light_end and current_time.second == 0:
                    if self.is_light_status == True:
                        self.turn_off_light()
                    else:
                        self.turn_off_light()
                time.sleep(1)

    def start(self):
        print("******")
        print("Starting System")
        print("******")
        self.thread = threading.Thread(target=self._analyse_things)
        self.thread.start()

    def pause_resume(self):
        if self.pause_resume_event.is_set():
            self.pause_resume_event.clear()
            time.sleep(0.3)
            print('******')
            print('System Stopped!')
            print('******')
        else:
            self.running_count += 1
            if self.running_count == 1:
                self.start()
            else:
                pass
            time.sleep(0.3)
            self.pause_resume_event.set()

    def stop(self):
        self.stop_event.set()
        self.thread.join()

import tkinter as tk
import os
import time
from gpiozero import Button

# Fungsi untuk memasukkan Raspberry Pi ke mode sleep
def sleep_raspi():
    os.system("sudo systemctl suspend")

# Fungsi untuk mengaktifkan layar kembali
def activate_screen():
    # Memanggil fungsi untuk mengaktifkan layar kembali
    os.system("command_to_activate_screen") # Ganti dengan perintah untuk mengaktifkan layar

# Fungsi callback saat tombol ditekan
def button_pressed():
    # Memanggil fungsi untuk mengaktifkan layar kembali
    activate_screen()

# Inisialisasi tombol
button = Button(17)  # Ganti dengan nomor pin GPIO yang sesuai

# Menambahkan fungsi callback saat tombol ditekan
button.when_pressed = button_pressed

# Fungsi utama untuk menjalankan relay
def main():
    # Inisialisasi GUI
    root = tk.Tk()

    # Atur timeout untuk sleep
    timeout = 300  # 5 menit
    root.after(timeout * 1000, sleep_raspi)  # Konversi detik ke milidetik

    # Jalankan loop utama GUI
    root.mainloop()

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
