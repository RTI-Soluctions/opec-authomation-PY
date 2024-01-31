import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Opec Automation")
        self.geometry("1280x720")

        self.grid_rowconfigure(0, weigth=1)
        self.grid_columnconfigure(1, weigth=1)

        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "src/img"
        )
        self.small_logo = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "small_logo.png")),
            size=(26, 26),
        )
        self.banner_home = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "banner_home.png")),
            size=(500, 150),
        )
        self.add_user_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "add_user_image.png")),
            size=(20, 20),
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
