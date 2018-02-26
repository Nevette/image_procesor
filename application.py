from tkinter import *


class MainFrame:
    def __init__(self, frame):
        self.frame = frame
        frame.title("Image Procesor")
        frame.resizable(width=FALSE, height=FALSE)
        frame.geometry('{}x{}'.format(600, 400))

        self.frame1 = Frame(frame, bg="red", width=60, height=50)
        self.frame1.pack(side=LEFT, anchor=N)

        self.frame2 = Frame(frame, bg="green", width=60, height=50)
        self.frame2.pack(side=LEFT, anchor=N)

        self.select_file_button = Button(frame, text="Select file")
        self.select_file_button.pack(side=LEFT, anchor=S)

        self.choose_operation_button = Button(frame, text="Choose operation")
        self.choose_operation_button.pack(side=LEFT, anchor=S)

        self.start_button = Button(frame, text="Start")
        self.start_button.pack(side=LEFT, anchor=S)


app = Tk()
my_gui = MainFrame(app)
app.mainloop()