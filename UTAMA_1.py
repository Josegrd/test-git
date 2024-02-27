import tkinter as tk
from PIL import ImageTk
import sqlite3
import pyglet
import datetime
import time
from tkinter import Tk, Canvas, Label
# import RPi.GPIO as GPIO
import threading

class SmartGardenSystem:
    def __init__(self, root=None):
        # Setup GPIO
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(23, GPIO.OUT)  # Relay untuk pompa
        # GPIO.setup(4, GPIO.OUT)   # Relay untuk sistem penerangan
        # GPIO.setup(5, GPIO.OUT)   # Relay untuk lampu indikator
        self.root = root
        self.label = Label(root, text="Status: Running")
        self.label.pack()
        self.thread = None
        self.kondisi_relay_1 = False
        self.kondisi_relay_2 = False

        self.ambang_kelembaban = 500  # Sesuaikan dengan nilai yang sesuai
        self.manual_pump = False
        self.manual_light = False
        self.is_running = False
        self.break_flag = False
        self.threadAction = threading.Thread(target=self.run)

        # Inisialisasi GUI (Anda mungkin perlu menyesuaikannya dengan GUI yang sudah Anda buat)
        # self.root = root
        # self.canvas = Canvas(self.root)
        # self.setup_gui()


    def toggle_manual_pump(self):
        # Mengaktifkan atau menonaktifkan relay pompa secara manual
        if self.kondisi_relay_1:
            # self.deactivate_relay(23)  # Relay untuk pompa
            # self.deactivate_relay(5)  # Relay untuk lampu indikator
            print("Pompa Mati")
        else:
            # self.activate_relay(23)  # Relay untuk pompa
            # self.activate_relay(5)  # Relay untuk lampu indikator
            print("pompa nyala")
        # self.manual_pump = not self.manual_pump

    def toggle_manual_light(self):
        # Mengaktifkan atau menonaktifkan relay light secara manual
        if self.kondisi_relay_2:
            # self.deactivate_relay(4)  # Relay untuk sistem penerangan
            # self.deactivate_relay(5)  # Relay untuk lampu indikator
            print("Lampu nyala")
        else:
            # self.activate_relay(4)  # Relay untuk sistem penerangan
            # self.activate_relay(5)  # Relay untuk lampu indikator
            print("Lampu mati")
        # self.kondisi_relay_2 = not self.kondisi_relay_2

    def activate_relay(self, relay_pin, text):
        # GPIO.output(relay_pin, GPIO.HIGH)
        print(f"relay {text} nyala")

    def activate_relay_pump(self, relay_pin, duration, times):
        # GPIO.output(relay_pin, GPIO.HIGH)
        # print("relay nyala")
        if times <= 15:
            print(f"Aktifkan sprinkler selama {duration} detik, sekarang detik ke-{times}")
        print("relay pompa mati")

    def deactivate_relay(self, relay_pin, text):
        # GPIO.output(relay_pin, GPIO.LOW)
        print(f"relay {text} mati")

    def activate_pump(self, duration, second):
        self.activate_relay_pump(23, duration, second)  # Relay untuk pompa
        # time.sleep(duration)

    def activate_light(self):
        self.activate_relay(4, "sistem lampu")  # Relay untuk sistem penerangan

    def deactivate_light(self):
        self.deactivate_relay(4, "sistem lampu")

    def activate_indicator(self):
        self.activate_relay(5, "indicator")  # Relay untuk lampu indikator

    def deactivate_indicator(self):
        self.deactivate_relay(5, "indicator")

    def is_automatic_light(self):
        current_time = datetime.datetime.now()
        return current_time.hour >= 17 or current_time.hour < 6

    def run(self):
        while not self.is_running:
            current_time = datetime.datetime.now()
            print(current_time)

            # soil_moisture = self.read_soil_moisture()
            # Cek waktu (pukul 7 pagi, 10 pagi, 3 sore)
            if current_time.hour in [7, 10, 16] and current_time.minute == 0:
                self.activate_pump(15, current_time.second)  # 5 menit (300)
                pass

            # Cek kelembaban tanah
            # elif soil_moisture < self.ambang_kelembaban:
            #     self.activate_pump(120, current_time.second)  # 2 menit

            # Cek otomatisasi sistem penerangan
            # if self.is_automatic_light():
            #     self.activate_light()
            # else:
            #     self.deactivate_light()
            elif current_time.hour >= 17 or current_time.hour < 6:
                self.activate_light()  # 5 menit (300)
            else:
                pass


            # Tunda pengecekan selama 1 menit
            time.sleep(1)

    def update_label(self, text):
        self.label.config(text=text)

    def start_system(self):
        print("System Running")
        self.is_running = False
        self.break_flag = False
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop_system(self):
        print("System Mati")
        self.is_running = True
        self.break_flag = True


# set colours
bg_colour = "#000000"

# load custom fonts
# pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
# pyglet.font.add_file("fonts/Shanti-Regular.ttf")


def clear_widgets(frame):
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    # stack frame 1 above frame 2
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    # create logo widget


    # create label widget for instructions
    tk.Label(
        frame1,
        text="ready for your random recipe?",
        bg=bg_colour,
        fg="white",
        font=("Montserrat", 14)
    ).pack()

    # create button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("Montserrat", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command= lambda : starting(smart_garden_system)
    ).pack(pady=20)

    logo_img = ImageTk.PhotoImage(file="assets/heading_assets/image_1.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    def starting(sgs_instance):
        print("running")
        sgs_instance.start_system()
        load_frame2()

def load_frame2():
    clear_widgets(frame1)
    # stack frame 2 above frame 1
    frame2.tkraise()
    frame2.pack_propagate(False)

    # create logo widget
    logo_img = ImageTk.PhotoImage(file="assets/heading_assets/button_1.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    # recipe title widget
    tk.Label(
        frame2,
        text="joseeeeee",
        bg=bg_colour,
        fg="white",
        font=("Montserrat", 20)
    ).pack(pady=25, padx=25)

    # recipe ingredients widgets

    # 'back' button widget
    tk.Button(
        frame2,
        text="BACK",
        font=("Montserrat", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(pady=20)


# initiallize app with basic settings
root = tk.Tk()
root.title("Recipe Picker")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1024
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# place app in the center of the screen (alternative approach to root.eval())
# x = root.winfo_screenwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('500x600+' + str(x) + '+' + str(y))

# create a frame widgets
frame1 = tk.Frame(root, width=1024, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack()
frame2.pack()

# place frame widgets in window
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

smart_garden_system = SmartGardenSystem(root)


# load the first frame
load_frame1()

# run app
root.mainloop()