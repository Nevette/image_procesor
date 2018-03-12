from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from enum import Enum
import PIL.Image
from copy import copy


class MainFrame:
    source_image = None
    original_image = None
    chosen_operation = None
    using_alfa = False

    def __init__(self, frame):
        self.frame = frame
        frame.title("Image Procesor")
        frame.resizable(width=TRUE, height=TRUE)
        frame.geometry('{}x{}'.format(830, 450))

        menu = Menu(app)
        app.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=self.choose_file)
        filemenu.add_command(label="Exit", command=app.quit)

        operations = Menu(menu)
        menu.add_cascade(label="Operations", menu=operations)
        operations.add_command(label="Greyscale", command=self.convert_to_greyscale)
        operations.add_command(label="Brightness", command=self.convert_brightness)

        reset = Menu(menu)
        menu.add_cascade(label="Reset", menu=reset)
        reset.add_command(label="Reset current operation", command=self.reset_current_operation)
        reset.add_command(label="Reset to original photo", command=self.reset_to_original_photo)

        scale = Scale(frame, from_=-1, to=1, orient=HORIZONTAL, resolution=0.01, command=self.slider_value)
        scale.pack(side=BOTTOM, anchor=S)

    def choose_file(self):
        # open dialog window
        first_image = filedialog.askopenfilename()
        image = PIL.Image.open(first_image)

        if first_image.endswith(".png"):
            self.using_alfa = True

        # set image size
        size = 400, 400
        image.thumbnail(size, Image.ANTIALIAS)

        first_photo = ImageTk.PhotoImage(image)
        img = Label(self.frame, image=first_photo)
        img.image = first_photo
        img.place(x=0, y=0)

        size2 = 400, 400
        image.thumbnail(size2, Image.ANTIALIAS)

        self.source_image = image
        self.original_image = copy(image)
        self.update_second_image(image)

    def update_second_image(self, image_data):
        second_photo = ImageTk.PhotoImage(image_data)
        img2 = Label(self.frame, image=second_photo)
        img2.image = second_photo
        img2.place(x=420, y=0)

    def convert_to_greyscale(self):
        self.chosen_operation = Operation.GREYSCALE
        image_data = self.source_image.load()

        if self.using_alfa:
            for x in range(self.source_image.width):
                for y in range(self.source_image.height):
                    rgb = image_data[x, y]
                    grey = int((rgb[0] + rgb[1] + rgb[2])/3)
                    image_data[x, y] = (grey, grey, grey, rgb[3])
        else:
            for x in range(self.source_image.width):
                for y in range(self.source_image.height):
                    rgb = image_data[x, y]
                    grey = int((rgb[0] + rgb[1] + rgb[2])/3)
                    image_data[x, y] = (grey, grey, grey)

        self.update_second_image(self.source_image)

    def convert_brightness(self):
        self.chosen_operation = Operation.BRIGHTNESS

    def adjust_brightness(self, slider_value):
        image = copy(self.source_image)
        image_data = image.load()

        if self.using_alfa:
            for x in range(image.width):
                for y in range(image.height):
                    modifier = int(255 * float(slider_value))
                    rgb = image_data[x, y]
                    r = rgb[0] + modifier
                    g = rgb[1] + modifier
                    b = rgb[2] + modifier

                    image_data[x, y] = (r, g, b, rgb[3])
        else:
            for x in range(image.width):
                for y in range(image.height):
                    modifier = int(255 * float(slider_value))
                    rgb = image_data[x, y]
                    r = rgb[0] + modifier
                    g = rgb[1] + modifier
                    b = rgb[2] + modifier

                    image_data[x, y] = (r, g, b)

        self.update_second_image(image)

    def slider_value(self, value):
        if self.chosen_operation == Operation.BRIGHTNESS:
            self.adjust_brightness(value)

    # TODO check later if works properly
    def reset_current_operation(self):
        self.update_second_image(self.source_image)

    def reset_to_original_photo(self):
        image_data = self.original_image
        self.update_second_image(image_data)


class Operation(Enum):
    GREYSCALE = 1
    BRIGHTNESS = 2


app = Tk()
my_gui = MainFrame(app)
app.mainloop()
