from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Learn To Code at Codemy.com")
#root.iconbitmap("C:/Users/liams/PycharmProjects/pythonGUI/venv/Scripts/anime.png")

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/liams/PycharmProjects/imageViewer/venv/Scripts/waifu.jfif"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/liams/PycharmProjects/imageViewer/venv/Scripts/waifu2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/liams/PycharmProjects/imageViewer/venv/Scripts/waifu3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/liams/PycharmProjects/imageViewer/venv/Scripts/waifu4.ico"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/liams/PycharmProjects/imageViewer/venv/Scripts/waifu5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan = 3)

def forward(imagenumber):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[imagenumber-1])
    button_forward = Button(root, text=">>", command=lambda: forward(imagenumber+1))
    button_back = Button(root, text="<<", command=lambda: back(imagenumber-1))

    if imagenumber == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image "+str(imagenumber)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0,columnspan=3, sticky=W+E)


def back(imagenumber):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[imagenumber - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(imagenumber + 1))
    button_back = Button(root, text="<<", command=lambda: back(imagenumber - 1))

    if imagenumber == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image " + str(imagenumber) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="<<", command = lambda: back(), state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command = lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0,columnspan=3, sticky=W+E)
root.mainloop()

