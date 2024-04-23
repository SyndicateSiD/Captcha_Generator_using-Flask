from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['C:/Users/KIIT/Downloads/fonts-20240227T135424Z-001/fonts/ChelseaMarketsr.ttf', 'C:/Users/KIIT/Downloads/fonts-20240227T135424Z-001/fonts/DejaVuSanssr.ttf'])

random_number = str(randint(100000, 999999))
data = image.generate(random_number)
assert isinstance(data, BytesIO)
image.write(random_number, 'out.png')

def verify():
    global random_number
    x = t1.get("0.0", END)
    if int(x) == int(random_number):
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global random_number
    random_number = str(randint(100000, 999999))
    data = image.generate(random_number)
    assert isinstance(data, BytesIO)
    image.write(random_number, 'out.png')
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.update()

root = Tk()
photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=300, width=300)
t1 = Text(root, height=10, width=50)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()
