from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from PIL import Image, ImageTk
from SeeChem_Functions_Image import Load_png

# background
def Create_background(master, image_path):
    try:
        bg_image = Image.open(image_path)
        width = master.winfo_width() or 1024
        height = master.winfo_height() or 768
        bg_image = bg_image.resize((width, height), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        
        canvas = Canvas(master, width=width, height=height, highlightthickness=0, bd=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=bg_photo)
        
        def Resize(e):
            try:
                new_img = Image.open(image_path).resize((e.width, e.height), Image.LANCZOS)
                canvas.config(width=e.width, height=e.height)
                canvas.delete("all")
                canvas.image = ImageTk.PhotoImage(new_img)
                canvas.create_image(0, 0, anchor="nw", image=canvas.image)
            except: pass
        
        master.bind('<Configure>', Resize)
        return canvas, bg_photo
        
    except:
        master.config(bg='#2c3e50')
        return None, None



# create pages
def Create_topbars(
        parentpage, location_specific#, function_more, 
        #function_account
        ):
    topbarframe = Frame(parentpage, bg="#090E9A", borderwidth=2)
    topbarframe.pack(fill=X)

    logosmall = Load_png("imagebase/SeeChemLogo101.png", width=30)
    logosmalllabel = Label(topbarframe, image=logosmall, bg="#090E9A")
    logosmalllabel.pack(side=LEFT)

    page_location = Label(topbarframe, text="SeeChem - " + location_specific, font=("Poppins", 25, "bold"),bg="#090E9A" ,fg="#FFFFFF")
    page_location.pack(side=LEFT)

    more_icon = Load_png("imagebase/more_icon.png", width=20)
    more_btn = Button(topbarframe, image=more_icon)#, command=function_more)
    more_btn.pack(side=RIGHT)

    account_icon = Load_png("imagebase/account_icon.png", width=20)
    account_btn = Button(topbarframe, image=account_icon)#, command=function_account)
    account_btn.pack(side=RIGHT)

# create about us button
def Create_aboutus(parentpage):
    about_us_frame = Frame(parentpage)
    about_us_frame.pack(padx=10, pady=50, side="bottom", anchor="w")

    about_us_btn = Button(about_us_frame, text="About us", font=("TeluguSangamMN", 20))
    about_us_btn.pack()

    about_us_txt = Label(
        about_us_frame, text="SeeChem Group All Rights Reserved", font=("AppleBraille", 10)
        )
    about_us_txt.pack()