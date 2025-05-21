from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from SeeChem_Functions import Load_svg, Load_png
from SeeChem_Functions import Create_topbars, Create_background, Create_aboutus

# root
root=Tk()
root.title("SeeChem App")
root.geometry("1024x768")
# root.attributes('-fullscreen', True) # to force into full screen
root.wm_attributes("-transparent", 0)

# seechem icon
seechem_icon = PhotoImage(file="imagebase/SeeChem_icon.png")
root.iconphoto(True, seechem_icon)

# main_container
main_container = Frame(root)
main_container.pack(fill="both", expand=True)

main_container.grid_rowconfigure(0, weight=1)
main_container.grid_columnconfigure(0, weight=1)

# pages
pages={}

#1
welcome_page_frame = Frame(main_container)
home_page_frame = Frame(main_container)
periodic_table_chart_frame = Frame(main_container)
simulator_frame = Frame(main_container)

#2
welcome_page_frame.grid(row=0, column=0, sticky="nsew")
home_page_frame.grid(row=0, column=0, sticky="nesw")
periodic_table_chart_frame.grid(row=0, column=0, sticky="nesw")
simulator_frame.grid(row=0, column=0, sticky="nesw")

#3
pages["welcome"] = welcome_page_frame
pages["home"] = home_page_frame
pages["periodict"] = periodic_table_chart_frame
pages["simulator"] = simulator_frame

# class
class welcome_page():
    def __init__(self, master):

        # background (
        # when the functions all finished, 
        # simple remove the '#' and change all the widgets master to self.canvas
        #)
        #self.canvas, self.bg_photo = Create_background(master, "imagebase/welcome_page_bg.png")

        # button functions
        def Log_in():
            pages["home"].tkraise()
        
        # text
        self.w_txtframe = Frame(master)
        self.w_txtframe.pack(padx=50, pady=80, anchor="w")

        self.w_text1 = Label(self.w_txtframe, text="Welcome to SeeChem", font=("Poppins", 80, "bold"), bg="white")
        self.w_text1.grid(row=0, column=0, sticky="w")

        self.w_text2 = Label(self.w_txtframe, text="where you start your chemistry", font=("Poppins", 50), bg="white")
        self.w_text2.grid(row=1, column=0, sticky="w")

        # btn
        self.w_btnframe = Frame(master)
        self.w_btnframe.pack(padx=100, pady=50, anchor="w")

        self.w_btn_log = Button(
            self.w_btnframe, text="➔ Log in", command=Log_in, font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_log.grid(row=0, column=0, pady=5, sticky="w")

        self.w_btn_sign = Button(
            self.w_btnframe, text="➔ Create Account", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_sign.grid(row=1, column=0, pady=5, sticky="w")

        self.w_btn_guest = Button(
            self.w_btnframe, text="➔ Continue as a guest", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_guest.grid(row=2, column=0, pady=5, sticky="w")

        # logo & image
        self.w_logoframe = Frame(master)
        self.w_logoframe.pack(padx=30, pady=50, side="bottom", anchor="w")

        self.logobig = Load_png("imagebase/SeeChemLogo101.png", width=200)
        self.logobiglabel = Label(self.w_logoframe, image=self.logobig)
        self.logobiglabel.pack()

        self.logotxt = Label(self.w_logoframe, text="SeeChem Group All Rights Reserved", font=("AppleBraille", 20))
        self.logotxt.pack()

w = welcome_page(welcome_page_frame)

class home_page():
    def __init__(self, master):

        Create_topbars(master, "Home Page")

        # button functions

        # periodic_table
        def Periodic_table():
            pages["periodict"].tkraise()

        # simulator
        def Simulator():
            pages["simulator"].tkraise()

        # image
        # cp = Load_png("imagebase/homepage_cp_image.png", width=200)
        
        # text
        self.h_txtframe = Frame(master)
        self.h_txtframe.pack(pady=50, anchor="center")

        self.h_text1 = Label(self.h_txtframe, text="Set up the experiments…", font=("LaoSangamMN", 50))
        self.h_text1.pack()

        # btn
        self.h_frame_container = Frame(master)
        self.h_frame_container.pack(padx=100, pady=30, anchor="center")
        
        self.h_btnframe = Frame(self.h_frame_container)
        self.h_btnframe.grid(row=0, column=0, padx=50)

        self.h_btn_pt = Button(self.h_btnframe, text="Periodic Table", font=("LaoSangamMN", 30), command=Periodic_table)
        self.h_btn_pt.grid(row=0, column=0, sticky="nw")

        self.h_btn_sml = Button(self.h_btnframe, text="Simulator", font=("LaoSangamMN", 30), command=Simulator)
        self.h_btn_sml.grid(row=0, column=1)

        self.h_btn_cp = Button(self.h_btnframe, text="Chemical \n Principles", font=("LaoSangamMN", 30))
        self.h_btn_cp.grid(row=1, column=0)

        self.h_btn_il = Button(self.h_btnframe, text="If in Lab", font=("LaoSangamMN", 30))
        self.h_btn_il.grid(row=1, column=1)

        # recently created
        self.recentframe = Frame(self.h_frame_container)
        self.recentframe.grid(row=0, column=1, padx=50)

        self.h_recent_txt = Label(self.recentframe, text="Recently Created", font=("LaoSangamMN", 30))
        self.h_recent_txt.pack(side=TOP)

        # about us
        Create_aboutus(master)

h = home_page(home_page_frame)

class periodic_table_chart():
    def __init__(self, master):

        Create_topbars(master, "Periodic Tabel Chart")

        # image
        
        # text

        # about us
        Create_aboutus(master)
        

p = periodic_table_chart(periodic_table_chart_frame)

class simulator():
    def __init__(self, master):

        Create_topbars(master, "Simulator")

        # image

        # text

        # about us
        Create_aboutus(master)

s = simulator(simulator_frame)

pages["home"].tkraise()
root.mainloop()
