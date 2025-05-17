from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cairosvg
import io

# image
def Load_png(file_path, width = None):
    original = Image.open(file_path)
    width = width
    ratio = width / original.width
    height = int(original.height * ratio)
    resized = original.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized)

def Load_svg(file_path, width=None):
    png_data = cairosvg.svg2png(url=file_path, output_width=width)
    img_pil = Image.open(io.BytesIO(png_data))
    return ImageTk.PhotoImage(img_pil)

# create pages
def Create_topbars(parentpage, specific):
    topbarframe = Frame(parentpage, bg="#090E9A", borderwidth=2)
    topbarframe.pack(fill=X)

    logosmall = Load_svg("imagebase/SeeChemLogo101.svg", width=30)
    logosmalllabel = Label(topbarframe, image=logosmall, bg="#090E9A")
    logosmalllabel.pack(side=LEFT)

    page_location = Label(topbarframe, text="SeeChem - " + specific, font=("Poppins", 25, "bold"),bg="#090E9A" ,fg="#FFFFFF")
    page_location.pack(side=LEFT)

    more_icon = Load_svg("imagebase/more_icon.svg", width=20)
    more_btn = Button(topbarframe, image=more_icon)
    more_btn.pack(side=RIGHT)

    account_icon = Load_svg("imagebase/account_icon.svg", width=20)
    account_btn = Button(topbarframe, image=account_icon)
    account_btn.pack(side=RIGHT)