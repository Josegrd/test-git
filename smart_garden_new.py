# background_checker.py
import datetime
import time
from tkinter import Tk, Canvas, Label
import threading

# import pyautogui
import sys
from queue import Queue


running_count = 0
class BackgroundChecker:
    def __init__(self): #, root=None
        self.pause_resume_event = threading.Event()
        self.stop_event = threading.Event()
        # self.thread = None
        # self.root = root
        # self.label = Label(root, text="Status: Running")
        # self.label.pack()

        self.relay_pin_1 = 2
        self.relay_pin_2 = 3
        self.running_count = 0
        self.kondisi_relay_1 = False
        self.kondisi_relay_2 = False

        self.ambang_kelembaban = 500  # Sesuaikan dengan nilai yang sesuai
        self.manual_pump = False
        self.manual_light = False
        self.is_running = False
        self.break_flag = False

    def toggle_manual_pump(self):
        # Mengaktifkan atau menonaktifkan relay pompa secara manual
        if self.manual_pump:
            # self.deactivate_relay(23)  # Relay untuk pompa
            # self.deactivate_relay(5)  # Relay untuk lampu indikator
            print("Pompa Mateekkk")
        else:
            # self.activate_relay(23)  # Relay untuk pompa
            # self.activate_relay(5)  # Relay untuk lampu indikator
            print("pompa murup cok")
        self.manual_pump = not self.manual_pump

    def toggle_manual_light(self):
        # Mengaktifkan atau menonaktifkan relay light secara manual
        if self.manual_light:
            # self.deactivate_relay(4)  # Relay untuk sistem penerangan
            # self.deactivate_relay(5)  # Relay untuk lampu indikator
            print("Lampu Mateekkk cok")
        else:
            # self.activate_relay(4)  # Relay untuk sistem penerangan
            # self.activate_relay(5)  # Relay untuk lampu indikator
            print("Lampu Murupp")
        self.manual_light = not self.manual_light

    # def _type_and_enter(self, text=None):
    #     keyboard = Controller()
    #     keyboard.type(text)
    #     time.sleep(2)
    #     keyboard.press('\n')
    #     keyboard.release('\n')

    def _analyse_things(self):

        for x in range(1000):
            current_time = datetime.datetime.now()
            if self.stop_event.is_set():
                print('Exiting')
                print()
                sys.exit()
                break
            else:
                self.pause_resume_event.wait()
                print(current_time.second)

                # soil_moisture = self.read_soil_moisture()
                # Cek waktu (pukul 7 pagi, 10 pagi, 3 sore)
                if current_time.hour in [7, 10, 16] and current_time.minute == 0:
                    # self.activate_pump(15, current_time.second)  # 5 menit (300)
                    print("pompa menyala")
                    pass
                elif current_time.hour >= 17 or current_time.hour < 6:
                    print("lampu nyala")
                    # self.activate_light()  # 5 menit (300)
                else:
                    pass

                # Tunda pengecekan selama 1 menit
                time.sleep(1)

                # if x == 10:
                #     self._type_and_enter('x')
                #     self._type_and_enter("\n")
                #     time.sleep(2)

    def start(self):
        self.thread = threading.Thread(target=self._analyse_things)
        self.thread.start()

    def pause_resume(self):
        global running_count
        if self.pause_resume_event.is_set():
            self.pause_resume_event.clear()
            time.sleep(0.3)
            print('******')
            print('paused')
            print('******')
        else:
            running_count += 1
            if running_count == 1:
                self.start()
            else:
                pass
            time.sleep(0.3)
            self.pause_resume_event.set()

    def pause_manual(self):
        if self.pause_resume_event.is_set():
            self.pause_resume_event.clear()
            time.sleep(0.3)
            print('******')
            print('paused manual')
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

    def update_label(self, text):
        self.label.config(text=text)