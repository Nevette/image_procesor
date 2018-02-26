from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL.Image


class MainFrame:
    firstPhoto = None

    def __init__(self, frame):
        self.frame = frame
        frame.title("Image Procesor")

        frame.resizable(width=TRUE, height=TRUE)
        frame.geometry('{}x{}'.format(600, 600))

        menu = Menu(app)
        app.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=self.choose_file_button)
        filemenu.add_command(label="Exit", command=app.quit)

        # second box for image
        self.frame2 = Frame(frame, bg="green", width=200, height=150)
        self.frame2.pack(side=LEFT, anchor=N)

        select_field = StringVar(app)
        # initial value
        select_field.set('Grayscale')
        choices = ['Grayscale', 'Brightness', 'Contrast']
        option = OptionMenu(app, select_field, *choices)
        option.pack(side='left', anchor=S)

        self.start_button = Button(frame, text="Start")

        self.start_button.pack(side=LEFT, anchor=S)

        w = Scale(frame, from_=0, to=10, orient=HORIZONTAL)
        w.pack(side=RIGHT, anchor=S)

    def choose_file_button(self):
        # open dialog window
        first_image = filedialog.askopenfilename()
        image = PIL.Image.open(first_image)

        # set image size
        size = 200, 200
        image.thumbnail(size, Image.ANTIALIAS)

        first_photo = ImageTk.PhotoImage(image)
        img = Label(self.frame, image=first_photo)
        img.image = first_photo
        img.place(x=0, y=0)


app = Tk()
my_gui = MainFrame(app)
app.mainloop()
