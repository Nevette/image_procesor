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

        # second box for image
        self.frame2 = Frame(frame, bg="green", width=200, height=150)
        self.frame2.pack(side=LEFT, anchor=N)

        self.select_file_button = Button(frame, command=self.choose_file_button, text="Select file")
        self.select_file_button.pack(side=LEFT, anchor=S)

        self.choose_operation_button = Button(frame, text="Choose operation")

        self.start_button.pack(side=LEFT, anchor=S)


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
