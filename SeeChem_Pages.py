from tkinter import *
from tkinter import ttk
from SeeChem_Functions import Load_svg, Load_png, Create_topbars

# root
root=Tk()
root.title("SeeChem App")
root.geometry("1024x768")

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

#2
welcome_page_frame.grid(row=0, column=0, sticky="nsew")
home_page_frame.grid(row=0, column=0, sticky="nesw")

#3
pages["welcome"] = welcome_page_frame
pages["home"] = home_page_frame

# class
class welcome_page():
    def __init__(self, master):

        # text
        self.w_txtframe = Frame(master)
        self.w_txtframe.pack(padx=50, pady=80, anchor="w")

        self.w_text1 = Label(self.w_txtframe, text="Welcome to SeeChem", font=("Poppins", 80, "bold"))
        self.w_text1.grid(row=0, column=0, sticky="w")

        self.w_text2 = Label(self.w_txtframe, text="where you start your chemistry", font=("Poppins", 50))
        self.w_text2.grid(row=1, column=0, sticky="w")

        # btn
        self.w_btnframe = Frame(master)
        self.w_btnframe.pack(padx=100, pady=50, anchor="w")

        self.w_btn_log = Button(
            self.w_btnframe, text="➔ Log in", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_log.grid(row=0, column=0, sticky="w")

        self.w_btn_sign = Button(
            self.w_btnframe, text="➔ Create Account", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_sign.grid(row=1, column=0, sticky="w")

        self.w_btn_guest = Button(
            self.w_btnframe, text="➔ Continue as a guest", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_guest.grid(row=2, column=0, sticky="w")

        # image
        self.w_logoframe = Frame(master)
        self.w_logoframe.pack(padx=30, pady=50, anchor="sw")

        self.logobig = Load_png("imagebase/SeeChemLogo101.png", width = 200)
        self.logobiglabel = Label(self.w_logoframe, image=self.logobig)
        self.logobiglabel.pack()

w = welcome_page(welcome_page_frame)

class home_page():
    def __init__(self, master):

        Create_topbars(master, "Home Page")

h = home_page(home_page_frame)

pages["home"].tkraise()
root.mainloop()
