from tkinter import *
from PIL import ImageTk, Image

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.state('iconic')
        self.window.resizable(0,0)

        #   Background Image
        self.bg_frame = Image.open('/home/akash/Programs/Python/PBL/Final/images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        #   Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.lgn_frame.place(x=210,y=70)

        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text = self.txt, font = ('yu gothic ui', 25, 'bold'),
                             bg = '#040405', fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)

        #   Left Side Image
        self.side_image = Image.open('/home/akash/Programs/Python/PBL/Final/images/vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg = '#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        #   Sign in Image
        self.sign_in_image = Image.open('/home/akash/Programs/Python/PBL/Final/images/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg = '#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text = 'Sign In', bg = '#040405', fg = 'white',
                                   font = ('yu gothic ui', 17, 'bold'))
        self.sign_in_label.place(x=650, y=240)

        #   Username
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405",
                                    fg="#6b6a69", font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        #   Username Icon
        self.username_icon = Image.open('/home/akash/Programs/Python/PBL/Final/images/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg = '#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        #   Password
        self.password_label = Label(self.lgn_frame, text='Password', bg='#040405',
                                    font=('yu gothic ui', 13, 'bold'), fg='#4f4e4d')
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405',
                                    fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=440)

        #   Password Icon
        self.password_icon = Image.open('/home/akash/Programs/Python/PBL/Final/images/password_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        #   Login Button
        self.lgn_button = Image.open('/home/akash/Downloads/Compressed/Tkinter Login Page/images/btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', relief=FLAT, font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=19, y=11)

        #   Forgot Password
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=600, y=510)

        #   Sign Up
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='/home/akash/Downloads/Compressed/Tkinter Login Page/images/register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)



def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()

if __name__ == '__main__':
    page()