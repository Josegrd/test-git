from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from manual_gui_oop import ManualGUI
import threading
from datatime_manager import DateTimeManager
from datetime import datetime
import datetime
import time
import sys
from weatherdata import DateTempManager
from indicator_lamp import IndicatorManager
import RPi.GPIO as GPIO


class BackgroundChecker:
    def __init__(self):
        self.pause_resume_event = threading.Event()
        self.stop_event = threading.Event()

        self.running_count = 0
        self.manual_pump = False
        self.manual_light = False
        self.lampIndicator = False
        self.pumpIndicator = False
        self.is_pump_status = False
        self.is_light_status = False

        self.indicatorLamp = 1
        self.is_pump_on = False
        self.is_light_on = False

        self.window_width = 1024
        self.window_height = 600
        
        #self.check_indicator = threading.Thread(target=self.indicator_detact)
        #self.check_indicator.start()

        # PUMP TIME SETTINGS
        self.set_hour_pump = [7, 10, 16]
        self.set_minute_pump = 3
        self.set_minute_pump_end = self.set_minute_pump + 5
        #self.set_second_pump = 55
        #self.set_second_pump_end = 30

        # LIGHT TIME SETTINGS
        self.set_hour_light = [13, 16]
        self.set_hour_light_end = [16]
        self.set_minute_light = 7
        self.set_minute_light_end = self.set_minute_light + 1

        # GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        self.pin_relay_pompa = 17
        self.pin_relay_lampu = 27
        self.pin_relay_indicator = 22
        for i in range(2, 7):
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        GPIO.setup(self.pin_relay_pompa, GPIO.OUT)  # Relay untuk pompa
        GPIO.setup(self.pin_relay_lampu, GPIO.OUT)  # Relay untuk sistem penerangan
        GPIO.setup(self.pin_relay_indicator, GPIO.OUT)  # Relay untuk lampu indikator

    def activate_relay(self, relay_pin):
        GPIO.output(relay_pin, GPIO.HIGH)

    def deactivate_relay(self, relay_pin):
        GPIO.output(relay_pin, GPIO.LOW)

    def turn_on_pump(self):
        self.activate_relay(self.pin_relay_pompa)  # Relay untuk pompa
        self.deactivate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_pump_on = True
        #self.indicatorLamp = 2
        self.pumpIndicator = True
        self.indicator_detact()
        print("Pompa Menyala")
        

    def turn_off_pump(self):
        self.deactivate_relay(self.pin_relay_pompa)  # Relay untuk pompa
        self.activate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_pump_on = False
        #self.indicatorLamp = 1
        self.pumpIndicator = False
        self.indicator_detact()
        print("Pompa Mati")
        

    def turn_on_light(self):
        self.activate_relay(self.pin_relay_lampu)  # Relay untuk sistem penerangan
        self.deactivate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_light_on = True
        #self.indicatorLamp = 2
        self.lampIndicator = True
        self.indicator_detact()
        print("Lampu Menyala")
        

    def turn_off_light(self):
        self.deactivate_relay(self.pin_relay_lampu)  # Relay untuk sistem penerangan
        self.activate_relay(self.pin_relay_indicator)  # Relay untuk lampu indikator
        self.is_light_on = False
        #self.indicatorLamp = 1
        self.lampIndicator = False
        self.indicator_detact()
        print("Lampu Mati")
    
    def indicator_detact(self):
        if self.is_pump_on == True and self.is_light_on == False:
            self.indicatorLamp = 1
        elif self.is_pump_on == False and self.is_light_on == True:
            self.indicatorLamp = 1
        else:
            self.indicatorLamp = 2
        
        
    
    def not_status_pump(self):
        self.is_pump_status = not self.is_pump_status
        
    def not_status_light(self):
        self.is_light_status = not self.is_light_status
    
    def _analyse_things(self):
        for x in range(1000):
        #while True:
            current_time = datetime.datetime.now()
            if self.stop_event.is_set():
                print('Exiting')
                print()
                sys.exit()
                break
            else:
                self.pause_resume_event.wait()
                #print(current_time.second)
                #print(self.is_pump_status)
                if current_time.hour in self.set_hour_pump and current_time.minute == self.set_minute_pump: #and current_time.second == self.set_second_pump_start:
                    if self.is_pump_status == False:
                        self.turn_on_pump()  # Turn on pump
                    else:
                        pass
                elif current_time.hour in self.set_hour_pump and current_time.minute == self.set_minute_pump_end and current_time.second == 0: #and current_time.second >= self.set_second_pump_end:
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


class HeadingGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.title("SmartGardenTE1 1.0")
        self.master.configure(bg="#ffffff")
        self.master.attributes('-fullscreen', True)
        self.checker = checker
        self.master.geometry(f"{self.checker.window_width}x{self.checker.window_height}")
        #window_width = self.checker.window_width
        #window_height = self.checker.window_height
        self.master.bind('<Escape>', self.exit_application)

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # self.is_running = True

        self.image_img_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.button_header_1 = PhotoImage(file=self.relative_to_assets("button_1new.png"))

        self.background_desktop()
        self.footer_copyright()
        self.title_header()
        self.buttons_header()

        self.canvas.pack()
        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"//home/select/Desktop/final/oop2/assets/heading_assets")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"assets/heading_assets")
        return ASSETS_PATH / Path(path)

    def exit_application(self, event=None):
        self.master.destroy()

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
            bg="#133201",
            activebackground="#133201",
            command=self.start_system,
            relief="flat"
        )
        button_1.place(
            x=339.0,
            y=300.0,
            width=312.0,
            height=76.0
        )

    def start_system(self):
        self.checker.pause_resume()
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        home_gui = HomeGUI(root, self.checker)
        root.mainloop()


class ManualGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.title("SmartGardenTE1 1.0")
        self.master.configure(bg="#ffffff")
        self.master.attributes('-fullscreen', True)
        self.checker = checker
        self.master.geometry(f"{self.checker.window_width}x{self.checker.window_height}")
        self.master.bind('<Escape>', self.exit_application)

        self.canvas = Canvas(
            master, 
            bg="#ffffff",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # PUMP SETTINGS
        self.set_hour_pump = self.checker.set_hour_pump
        self.set_minute_pump = self.checker.set_minute_pump
        self.set_minute_pump_end = self.checker.set_minute_pump_end
        #self.set_second_pump = self.checker.set_second_pump
        #self.set_second_pump_end = self.checker.set_second_pump_end
        self.is_pump_on = self.checker.is_pump_on
        #self.is_pump_status = self.checker,is_pump_status

        # LIGHT SETTINGS
        self.set_hour_light = self.checker.set_hour_light
        self.set_minute_light = self.checker.set_minute_light
        self.set_minute_light_end = self.checker.set_minute_light_end
        self.set_hour_light_end = self.checker.set_hour_light_end
        self.is_light_on = self.checker.is_light_on

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

    def exit_application(self, event=None):
        self.master.destroy()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/final/oop2/assets/manual_assets")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"assets/manual_assets")
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
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.open_home_gui,
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
            command=self.open_statistics_gui,
            relief="flat",
            bg="#ffffff",
            activebackground="#ffffff",
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
            activebackground="#ffffff",
            highlightthickness=0,
            command=self.open_help_gui,
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

        button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            bg="#ffffff",
            activebackground="#ffffff",
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
        self.checker.pause_resume()
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        heading_gui = HeadingGUI(root, self.checker)
        root.mainloop()

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

    def open_statistics_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        menu_gui = MenuGUI(root, self.checker)
        root.mainloop()

    def open_home_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        home_gui = HomeGUI(root, self.checker)
        root.mainloop()

    def open_help_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        help_gui = HelpGUI(root, self.checker)
        root.mainloop()


class HomeGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.title("SmartGardenTE1 1.0")
        self.master.configure(bg="#ffffff")
        self.master.attributes('-fullscreen', True)
        self.checker = checker
        self.master.geometry(f"{self.checker.window_width}x{self.checker.window_height}")
        #screen_width = master.winfo_screenwidth()
        #screen_height = master.winfo_screenheight()
        #window_width = self.checker.window_width
        #window_height = self.checker.window_height
        #x = (screen_width - window_width) // 2
        #y = (screen_height - window_height) // 2
        #master.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.master.bind('<Escape>', self.exit_application)

        self.indicator_lamp = self.checker.indicatorLamp

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

        # JAM
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

    def exit_application(self, event=None):
        self.master.destroy()
        
    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/final/oop2/assets/home_assets")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"assets/home_assets")
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
            bg="#ffffff",
            activebackground="#ffffff",
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
            bg="#ffffff",
            activebackground="#ffffff",
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
            bg="#ffffff",
            activebackground="#ffffff",
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

        # Buat objek baru dari HeadingGUI
        root = Tk()
        menu_gui = MenuGUI(root, self.checker)
        root.mainloop()

    def open_manual_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        manual_gui = ManualGUI(root, self.checker)
        root.mainloop()

    def open_help_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        help_gui = HelpGUI(root, self.checker)
        root.mainloop()


class MenuGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.title("SmartGardenTE1 1.0")
        self.master.configure(bg="#ffffff")
        self.master.attributes('-fullscreen', True)
        self.checker = checker
        self.master.geometry(f"{self.checker.window_width}x{self.checker.window_height}")
        window_width = self.checker.window_width
        window_height = self.checker.window_height
        self.master.bind('<Escape>', self.exit_application)

        self.canvas = Canvas(
            master,
            bg="#ffffff",
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

    def exit_application(self, event=None):
        self.master.destroy()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/final/oop2/assets/menu_assets")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"assets/menu_assets")
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
            activebackground="#ffffff",
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
            activebackground="#ffffff",
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
            activebackground="#ffffff",
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

        # Buat objek baru dari HeadingGUI
        root = Tk()
        manual_gui = ManualGUI(root, self.checker)
        root.mainloop()

    def open_home_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        home_gui = HomeGUI(root, self.checker)
        root.mainloop()

    def open_help_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        help_gui = HelpGUI(root, self.checker)
        root.mainloop()


class HelpGUI:
    def __init__(self, master, checker):
        self.master = master
        self.master.title("SmartGardenTE1 1.0")
        self.master.configure(bg="#ffffff")
        self.master.attributes('-fullscreen', True)
        self.checker = checker
        self.master.geometry(f"{self.checker.window_width}x{self.checker.window_height}")
        window_width = self.checker.window_width
        window_height = self.checker.window_height
        self.master.bind('<Escape>', self.exit_application)

        self.canvas = Canvas(
            self.master,
            bg="#EBE9EE",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
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

    def exit_application(self, event=None):
        self.master.destroy()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/final/oop2/assets/help_assets")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"assets/help_assets")
        return ASSETS_PATH / Path(path)

    def background_help_gui(self):
        self.canvas.place(x=0, y=0)
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
            command=self.open_manual_gui,
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
            command=self.open_statistics_gui,
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

    def open_statistics_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        menu_gui = MenuGUI(root, self.checker)
        root.mainloop()

    def open_manual_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        manual_gui = ManualGUI(root, self.checker)
        root.mainloop()

    def open_home_gui(self):
        self.master.destroy()

        # Buat objek baru dari HeadingGUI
        root = Tk()
        home_gui = HomeGUI(root, self.checker)
        root.mainloop()


# background_checker.py
if __name__ == "__main__":
    # root = Tk()
    # app = HeadingGUI(root)
    # root.mainloop()

    root = Tk()
    # garden_system = SmartGardenSystem()
    checker = BackgroundChecker()
    heading_gui = HeadingGUI(root, checker)
    # heading_gui.check_system_status()  # Contoh penggunaan atribut is_running
    root.mainloop()
