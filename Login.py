from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Button
from PIL import ImageTk, Image, ImageFilter
from Database import DatabaseConnection
from mainwindow import MainWindow
import mysql.connector
import ttkbootstrap as tb




class LoginWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Nexus Controls - Login")
        self.resizable(width=False, height=False)
        style = tb.Style(theme='pharmtheme')
    # Apply the style to the root window
        style.theme_use('pharmtheme')
        window_width= 750
        window_height=500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)



        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.configure(background="black")

        self.pharmacydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            port=3306,
            database="pharmgui",
        )

        self.my_cursor = self.pharmacydb.cursor()

        self.my_canvas = Canvas(self, width=750, height=500, bg='black') #Control the Color of the Background
        self.my_canvas.pack(fill="both", expand=True)
        #self.newcanvas= Canvas(self.my_canvas, width=20, height=20, bg='black')
        #self.newcanvas.place(x=window_width//2, y=window_height//2)

        self.blue = Label(self.my_canvas, text='Pharmacogenomic Systems', font=("Vintage Typewriter", 14, 'italic'),
                            fg='black', bg='white', width= screen_width//20, anchor="center")
        self.blue.config(height=1)

        self.blue.place(relx=0.5,rely=0.32, anchor='center')

        self.NC = ImageTk.PhotoImage(Image.open("PNGS/NC3-R.png").resize((180, 130)))
        #self.new_pic2 = ImageTk.PhotoImage(Image.open("PNGS/Mickey.png").resize((183, 43), Image.ANTIALIAS))
        #self.Mick = Label(self, image=self.new_pic2, bg='white')
        #self.Mick.place(x=4, y=60)
        self.Pillori = ImageTk.PhotoImage(Image.open("PNGS/blackpillblurred.png").resize((window_width,300)))


        canvas_center_x = self.winfo_reqwidth() // 2
        canvas_center_y = self.winfo_reqheight() // 2
        print (canvas_center_x, canvas_center_y)

        image_width = self.Pillori.width()
        image_height = self.Pillori.height()

        image_x = canvas_center_x - (image_width // 2)
        image_y = canvas_center_y - (image_height // 2)


        self.my_canvas.create_image(380 , 300, image=self.Pillori)
        self.my_canvas.create_text(245, 258, text='Username', fill='white', font=("Vintage Typewriter", 12, 'italic'))
        self.my_canvas.create_text(245, 293, text='Password', fill='white', font=("Vintage Typewriter", 12, 'italic'))
        self.my_canvas.create_text(window_width//2, 237, text='Enter your Username and Password to log in',
                                   font=("Vintage Typewriter", 10, 'italic'), fill=('white'))

        canvas_center_x = self.winfo_reqwidth() // 2
        canvas_center_y = self.winfo_reqheight() // 2

        image_width = self.Pillori.width()
        image_height = self.Pillori.height()

        image_x = canvas_center_x - (image_width // 2)
        image_y = canvas_center_y - (image_height // 2)


       
        self.EntImLab = Label(self, image=self.NC, bg = "black", bd=0, highlightthickness=0, relief='ridge')
        self.update_idletasks()  # Ensure that the widget is updated before getting its dimensions
  
        
        self.EntImLab.place(relx=0.5, rely=0.15, anchor='center')

    

     

        # Make the Entries above into tb.Entry widgets
        self.Username_Entry = tb.Entry(self.my_canvas, bootstyle='info')
        self.Password_Entry = tb.Entry(self.my_canvas, bootstyle='info')
        self.Username_Entry.place(x=290, y=250)
        self.Password_Entry.place(x=290, y=285)

        #self.Button_login = Button(self, text='Login', command=self.correct_login, font=('Trajan Pro', 11, 'italic'),
        #                           bd=0, highlightthickness=0, relief='ridge', borderwidth=0, height=2, width=5)

        #self.Buttonloginwindow = self.my_canvas.create_window(390, 340, window=self.Button_login)

        self.logbutton = tb.Button(self.my_canvas, text='Login', bootstyle='info', command=lambda: self.correct_login())
        self.logbutton.place(relx=0.43,rely=0.65)


    def correct_login(self):
        username = self.Username_Entry.get()
        password = self.Password_Entry.get()
        db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
        try:
            db_connection.cursor.execute('SELECT Username, Password FROM UserEntry WHERE Username = %s AND Password = %s', (username, password))
            result = db_connection.cursor.fetchone()

            if result:
                # Close the database cursor and connection
                db_connection.cursor.close()


                # Create the main window
                main_window = MainWindow()

                self.destroy()
            else:
                incorrect = Label(self, text="Incorrect Username/Password", font=('Trajan Pro', 11), fg='red', bg='white')
                incorrect.place(x=290, y=300)

        except mysql.connector.Error as err:
            # Handle database errors gracefully
            print(f"Database error: {err}")
            db_connection.cursor.close()
            db_connection.close()

