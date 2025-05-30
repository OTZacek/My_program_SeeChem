from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SeeChem_Functions_Image import Load_png
from SeeChem_Functions_Create_Pages import Create_topbars, Create_background, Create_aboutus

# root
root=Tk()
root.title("SeeChem App")
root.geometry("1024x768")
# root.attributes('-fullscreen', True) # to force into full screen

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
access_page_frame = Frame(main_container)
welcome_page_frame = Frame(main_container)
home_page_frame = Frame(main_container)
periodic_table_chart_frame = Frame(main_container)
simulator_frame = Frame(main_container)

#2
access_page_frame.grid(row=0, column=0, sticky="nesw")
welcome_page_frame.grid(row=0, column=0, sticky="nsew")
home_page_frame.grid(row=0, column=0, sticky="nesw")
periodic_table_chart_frame.grid(row=0, column=0, sticky="nesw")
simulator_frame.grid(row=0, column=0, sticky="nesw")

#3
pages["create_account"] = access_page_frame
pages["welcome"] = welcome_page_frame
pages["home"] = home_page_frame
pages["periodict"] = periodic_table_chart_frame
pages["simulator"] = simulator_frame

# class
class access_page():
    def __init__(self, master):

        USER_FILE = "SeeChem_users_accessinfo.rtf"

        self.canvas, self.bg_photo = Create_background(master, "imagebase/login_page_bg.png")

        login_frame = Frame(self.canvas)
        login_frame.pack(pady=350)

        self.username_label = Label(login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.username_entry = Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = Label(login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.password_entry = Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.confirm_password_label = Label(login_frame, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.confirm_password_entry = Entry(login_frame, show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        def save_user(username, password):
            with open(USER_FILE, "w") as f:
                f.write(f"{{\\rtf_User's Info\n")
                f.write(f"Username: {username}\\line\n")
                f.write(f"Password: {password}\\line\n")
                f.write("}")

        def create_account():
            username = self.username_entry.get()
            password = self.password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            
            if not username or not password or not confirm_password:
                messagebox.showwarning("Warning", "All fields are required!")
            elif confirm_password != password:
                messagebox.showerror("Error", "Passwords not match!")
            else:
                save_user(username, password)
                messagebox.showinfo("Success", "Welcome to SeeChem!")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_password_entry.delete(0, END)

        self.create_button = Button(login_frame, text="Create Account", command=create_account)
        self.create_button.grid(row=3, column=0, columnspan=2, pady=20)

a = access_page(access_page_frame)



class welcome_page():
    def __init__(self, master):

        # background (
        # when the functions all finished, 
        # simple remove the '#' and change all the widgets master to self.canvas
        #)
        self.canvas, self.bg_photo = Create_background(master, "imagebase/welcome_page_bg.png")

        # button functions
        def Log_in():
            messagebox.showwarning("Warning", "Log in page not yet finished... redirect to Homepage")
            pages["home"].tkraise()

        def Create_account():
            pages["create_account"].tkraise()
        
        # text
        self.w_txtframe = Frame(self.canvas)
        self.w_txtframe.pack(padx=50, pady=80, anchor="w")

        self.w_text1 = Label(self.w_txtframe, text="Welcome to SeeChem", font=("Poppins", 80, "bold"))
        self.w_text1.grid(row=0, column=0, sticky="w")

        self.w_text2 = Label(self.w_txtframe, text="where you start your chemistry", font=("Poppins", 50))
        self.w_text2.grid(row=1, column=0, sticky="w")

        # btn
        self.w_btnframe = Frame(self.canvas)
        self.w_btnframe.pack(padx=100, pady=50, anchor="w")

        self.w_btn_log = Button(
            self.w_btnframe, text="➔ Log in", command=Log_in, font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_log.grid(row=0, column=0, pady=5, sticky="w")

        self.w_btn_sign = Button(
            self.w_btnframe, text="➔ Create Account", command=Create_account, font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_sign.grid(row=1, column=0, pady=5, sticky="w")

        self.w_btn_guest = Button(
            self.w_btnframe, text="➔ Continue as a guest", font=("OpenSans", 30), relief="flat", highlightthickness=0)
        self.w_btn_guest.grid(row=2, column=0, pady=5, sticky="w")

        # logo & image
        self.w_logoframe = Frame(self.canvas)
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

pages["welcome"].tkraise()
root.mainloop()
