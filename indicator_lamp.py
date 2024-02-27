from tkinter import Canvas, PhotoImage
from pathlib import Path

class IndicatorManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/New folder/home/build/assets/frame0")
        # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/select/Desktop/TA/Garden/oop/assets/home_assets")
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/home_assets")
        return ASSETS_PATH / Path(path)

    def on_indicator(self):
        image_5 = self.canvas.create_image(
            889.0,
            448.0,
            image=self.image_image_5
        )

    def standby_indicator(self):
        image_6 = self.canvas.create_image(
            889.0,
            448.0,
            image=self.image_image_6
        )

    def running_indicator(self):
        image_7 = self.canvas.create_image(
            889.0,
            448.0,
            image=self.image_image_7
        )
