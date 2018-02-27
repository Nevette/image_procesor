from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL.Image


class MainFrame:
    second_img = None

    def __init__(self, frame):
        self.frame = frame
        frame.title("Image Procesor")
        frame.resizable(width=TRUE, height=TRUE)
        frame.geometry('{}x{}'.format(600, 600))

        menu = Menu(app)
        app.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=self.choose_file)
        filemenu.add_command(label="Exit", command=app.quit)

        operations = Menu(menu)
        menu.add_cascade(label="Operations", menu=operations)
        operations.add_command(label="Greyscale", command=self.convert_to_greyscale)
        operations.add_command(label="Brightness")

        # second box for image
        self.frame2 = Frame(frame, bg="green", width=200, height=150)
        self.frame2.pack(side=LEFT, anchor=N)

        select_field = StringVar(app)
        # initial value
        select_field.set('Greyscale')
        choices = ['Greyscale', 'Brightness', 'Contrast']
        option = OptionMenu(app, select_field, *choices)
        option.pack(side='left', anchor=S)

        self.start_button = Button(frame, text="Start")
        self.start_button.pack(side=LEFT, anchor=S)

        w = Scale(frame, from_=0, to=10, orient=HORIZONTAL)
        w.pack(side=RIGHT, anchor=S)

    def choose_file(self):
        # open dialog window
        first_image = "C:/Users/Agnieszka/Documents/a.png"  # filedialog.askopenfilename()
        image = PIL.Image.open(first_image)

        # set image size
        size = 200, 200
        image.thumbnail(size, Image.ANTIALIAS)

        first_photo = ImageTk.PhotoImage(image)
        img = Label(self.frame, image=first_photo)
        img.image = first_photo
        img.place(x=0, y=0)

        size2 = 200, 200
        image.thumbnail(size2, Image.ANTIALIAS)

        self.second_img = image
        self.update_second_image(image)

    def convert_to_greyscale(self):
        image_data = self.second_img.load()

        # TODO: add checking image type
        for x in range(self.second_img.width):
            for y in range(self.second_img.height):
                rgb = image_data[x, y]
                grey = int((rgb[0] + rgb[1] + rgb[2])/3)
                image_data[x, y] = (grey, grey, grey, rgb[3])  # if jpg: image_data[x, y] = (grey, grey, grey)

        self.update_second_image(self.second_img)

    def update_second_image(self, image_data):
        second_photo = ImageTk.PhotoImage(image_data)
        img2 = Label(self.frame, image=second_photo)
        img2.image = second_photo
        img2.place(x=300, y=0)


app = Tk()
my_gui = MainFrame(app)
app.mainloop()
