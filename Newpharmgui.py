#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:15:38 2022

@author: afroza
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Button
from PIL import ImageTk, Image, ImageFilter
import mysql
import mysql.connector
#from pynput import keyboard
import tkinter.ttk as ttk
from tkinter import Entry, Button, Canvas, messagebox
import cv2
import numpy as np

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

class LoginWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mckesson Rx Enterprise - Login")
        self.resizable(width=False, height=False)
        window_width= 750
        window_height=500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.configure(background="white")

        self.pharmacydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            port=3306,
            database="pharmgui",
        )

        self.my_cursor = self.pharmacydb.cursor()

        self.my_canvas = Canvas(self, width=750, height=500, bg='White')
        self.my_canvas.pack(fill="both", expand=True)

        self.orange = Label(self.my_canvas, text='World Class Pharmacy Systems', font=('Trajan Pro', 18),
                            fg='white', bg='#DA7533', width=67, anchor="e")
        self.orange.config(height=1)
        self.orange.place(x=3, y=150)

        self.new_pic = ImageTk.PhotoImage(Image.open("EnterpriseRx.png").resize((172, 44), Image.ANTIALIAS))
        self.new_pic2 = ImageTk.PhotoImage(Image.open("Mickey.png").resize((183, 43), Image.ANTIALIAS))
        self.Mick = Label(self, image=self.new_pic2, bg='white')
        self.Mick.place(x=4, y=60)

        self.Pillori = ImageTk.PhotoImage(Image.open("pillbottlesblurgrey.png"), Image.ANTIALIAS)

        self.my_canvas.create_image(380, 290, image=self.Pillori)
        self.my_canvas.create_text(245, 258, text='Username', fill='black', font=("Vintage Typewriter", 12, 'italic'))
        self.my_canvas.create_text(245, 293, text='Password', fill='black', font=("Vintage Typewriter", 12, 'italic'))
        self.my_canvas.create_text(240, 237, text='Enter your Username and Password to log in',
                                   font=("Vintage Typewriter", 10, 'italic'), fill=('black'))

        self.EntImLab = Label(self, image=self.new_pic, bg='white', bd=0, highlightthickness=0, relief='ridge')
        self.EntImLab.place(x=570, y=95)

        self.Username_Entry = Entry(self.my_canvas, fg='black', borderwidth=0, bd=0, highlightthickness=0)
        self.Password_Entry = Entry(self.my_canvas, fg='black', show='*', borderwidth=0, bd=0, highlightthickness=0,
                                    relief='sunken')

        self.Username_Entry.place(x=290, y=250)
        self.Password_Entry.place(x=290, y=285)

        self.Username_Entry.configure(background='white')
        self.Password_Entry.configure(background='white')

        #self.Button_login = Button(self, text='Login', command=self.correct_login, font=('Trajan Pro', 11, 'italic'),
        #                           bd=0, highlightthickness=0, relief='ridge', borderwidth=0, height=2, width=5)

        #self.Buttonloginwindow = self.my_canvas.create_window(390, 340, window=self.Button_login)
        self.logbutton_canvas = tk.Canvas(self.my_canvas, width=70, height=25, bg='white', highlightthickness=0, relief="raised")
        self.logbutton_canvas.create_text(35, 10, text='Login', fill='black', font=('Trajan Pro', 11, 'italic'))
        self.logbutton_canvas.place(x=330, y=340)
        self.logbutton_canvas.bind("<Button-1>", self.correct_login)

    def correct_login(self, event):
        username = self.Username_Entry.get()
        password = self.Password_Entry.get()

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


class MainWindow(Toplevel):
    def __init__(self):
        super().__init__()
        #self.attributes('-fullscreen',True)

        screen_width = self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        self.geometry(f'{screen_width}x{screen_height}')
        self.new_pic = ImageTk.PhotoImage(Image.open("EnterpriseRx.png").resize((172, 44), Image.ANTIALIAS))
        self.new_pic2 = ImageTk.PhotoImage(Image.open("Mickey.png").resize((183,43),Image.ANTIALIAS))
        #self.geometry('1700x1600')
        self.EntImLab2 = Label(self, image=self.new_pic, bg='white')
        self.EntImLab2.place(x=1270, y=100)
        self.orange1 = Label(self, text='World Class Pharmacy Systems', font=('Trajan Pro', 13), fg='white',
                             bg='dark orange', width=290)
        self.orange1.place(x=0, y=150)
        self.Mick2 = Label(self, image=self.new_pic2, bg='white')
        self.Mick2.place(x=0, y=50)
        self.my_menu = Menu(self)
        self.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.activity_menu = Menu(self.my_menu)
        self.tools_menu = Menu(self.my_menu)
        self.RxQueues_menu = Menu(self.my_menu)
        self.Search_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.my_menu.add_cascade(label="Activities", menu=self.activity_menu)
        self.my_menu.add_cascade(label="Tools", menu=self.tools_menu)
        self.my_menu.add_cascade(label="Rx Queues", menu=self.RxQueues_menu)
        self.my_menu.add_cascade(label="Search", menu=self.Search_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.Rx_reception = Frame(self, width=400, height=400, bg='white')
        self.Rx_data = Frame(self, width=400, height=400, bg='white')
        self.Rx_product = Frame(self, width=400, height=400, bg='white')
        self.Rx_Allrx = Frame(self, width=400, height=400, bg='')
        self.Rx_s_Patient = Frame(self, width=400, height=400, bg='#d6cfbd')
        self.Rx_p_Patient = Frame(self, width=1515, height=1000, bg='#bdaa8b')
        self.Rx_prof_Patient = Frame(self, width=1515,height=1000, bg='#d6cfbd')

        self.RxQueues_menu.add_command(label="Reception", command=self.rx_rec)
        self.RxQueues_menu.add_command(label="Data Entry", command=self.rx_dat)
        self.RxQueues_menu.add_command(label="Product Dispensing", command=self.rx_prod)
        self.RxQueues_menu.add_command(label="Verification", command=self.our_command)
        self.RxQueues_menu.add_command(label="Release to Patient", command=self.our_command)
        self.RxQueues_menu.add_command(label="DUR Exception", command=self.our_command)
        self.RxQueues_menu.add_command(label="General Exception", command=self.our_command)
        self.RxQueues_menu.add_command(label="All Rx Status", command=self.rx_all_rx)
        self.RxQueues_menu.add_command(label="Order Grouping", command=self.our_command)
        self.RxQueues_menu.add_command(label="Adjudication Exception", command=self.our_command)
        self.RxQueues_menu.add_command(label="Contact Manager", command=self.our_command)
        self.RxQueues_menu.add_command(label="Fill on Arrival", command=self.our_command)
        self.Search_menu.add_command(label="Patient", command=self.rx_s_patient)
        self.hide_frames


        # Add menu commands
        # ...

        # Initially display the rx_all_rx frame.
        self.rx_all_rx()


        self.mainloop()

    def hide_frames(self):
        self.Rx_reception.pack_forget()
        self.Rx_data.pack_forget()
        self.Rx_product.pack_forget()
        self.Rx_s_Patient.pack_forget()
        self.Rx_Allrx.pack_forget()
        self.Rx_s_Patient.forget()
        self.Rx_prof_Patient.forget()

    def rx_rec(self):
        self.hide_frames()
        self.Rx_reception.pack(fill="both", expand=1)

    def rx_dat(self):
        self.hide_frames()
        self.Rx_data.pack(fill="both", expand=1)

    def rx_prod(self):
        self.hide_frames()
        self.Rx_product.pack(fill="both", expand=True)
        #swidth = self.winfo_width.get()
        #sheight= self.winfo_height.get()
        #self.Rx_product.place(x=0,y=0, width=swidth, height=sheight)
        Findanrx = Canvas(self.Rx_product, width=200, height=150, bg='#d6cfbd', relief=SUNKEN, borderwidth=0)
        Findanrx.place(x=0, y=0)
        Findanrx.create_text(50, 20, text='Find an Rx', fill="black", font=('Trajan Pro', 13, 'bold'))
        Findanrx.create_text(55, 40, text='Scan or Enter Rx#:', fill="black", font=('Trajan Pro', 10,))
        scanentry = Entry(self.Rx_product, fg='white', borderwidth=0, bg='white', relief=SUNKEN, width=20)
        scanentry.place(x=8, y=50)
        Filterby = Canvas(self.Rx_product, width=1300, height=150, bg='#d6cfbd', relief=SUNKEN, borderwidth=5)
        Filterby.place(x=200, y=0)
        Filterby.create_text(40, 20, text='Filter By:', fill="black", font=('Trajan Pro', 13, 'bold'))
        Filterby.create_text(140, 30, text='Promise Time:', fill="black", font=('Trajan Pro', 12))
        Filterby.create_text(140, 60, text='Rx #-Store #:', fill="black", font=('Trajan Pro', 12))
        Filterby.create_text(140, 90, text='Store Number:', fill="black", font=('Trajan Pro', 12))
        Filterby.create_text(140, 120, text='Patient Name:', fill="black", font=('Trajan Pro', 12))



        promise_entry = Entry(self.Rx_product, fg='black', borderwidth=0, bg='white', width=15, relief=SUNKEN)
        rxstorenum_entry = Entry(self.Rx_product, fg='black', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        Storenum_entry = Entry(self.Rx_product, fg='black', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        Ptname_entry = Entry(self.Rx_product, fg='black', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        promise_entry.place(x=400, y=15)
        rxstorenum_entry.place(x=400, y=45)
        Storenum_entry.place(x=400, y=75)
        Ptname_entry.place(x=400, y=105)
        Mainprod = Canvas(self.Rx_product, width=1500, height=850, bg='#bdaa8b', relief=SUNKEN, borderwidth=0)
        Mainprod.place(x=0, y=150)
        canvas_width = 1420
        num_columns = 7
        column_width = canvas_width // num_columns

        style = ttk.Style()
        style.configure("Custom.Treeview", background="#bdaa8b", fieldbackground="#bdaa8b", foreground="black")
        style.configure("Custom.Treeview.Column", width=3000)
        style.configure("Custom.Treeview.Separator", background="black", fieldbackground='black',foreground="black")
        style.configure("Custom.Treeview.Heading", foreground="black", font=("Helvetica", 12, "bold"))
        style.configure("Custom.Treeview", borderwidth=1)
        style.configure("Custom.Treeview.Heading", borderwidth=10)
        style.configure("Custom.Treeview.Column", borderwidth=10)

        self.tableframe = Canvas(self.Rx_product, width=1420, height=350, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
        self.tableframe.place(x=5, y=160)
        #PrintButton = tk.Button(self.Rx_product, text="Print Selected Order",width=11,height=2, bg='black', fg='white')
        #PrintButton.place(x=1250,y=450)

        self.printbutton_canvas = tk.Canvas(self.Rx_product, width=150, height=25, bg='#d6cfbd', highlightthickness=0, relief=SUNKEN)
        self.printbutton_canvas.create_text(70, 10, text='Print Selected Order', fill='black', font=('Trajan Pro', 11, 'bold'))
        self.printbutton_canvas.place(x=1095, y=450)

        self.printbbutton_canvas = tk.Canvas(self.Rx_product, width=150, height=25, bg='#d6cfbd', highlightthickness=0, relief=SUNKEN)
        self.printbbutton_canvas.create_text(70, 10, text='Print Batch', fill='black', font=('Trajan Pro', 11, 'bold'))
        self.printbbutton_canvas.place(x=1250, y=450)

        self.okbbutton_canvas = tk.Canvas(self.Rx_product, width=45, height=25, bg='#bdaa8b', highlightthickness=0, relief=SUNKEN, borderwidth=3)
        self.okbbutton_canvas.create_text(25, 12, text='OK', fill='black', font=('Trajan Pro', 11, 'bold'))
        self.okbbutton_canvas.place(x=145, y=80)


        # Create a Treeview widget within the canvas
        table = ttk.Treeview(self.tableframe, style="Custom.Treeview", columns=("Promise Time", "Rx#-Store#", "Patient name", "Product", "Quantity", "Delivery", "Printed"), show="headings")
        table.heading("Promise Time", text="Promise Time")
        table.heading("Rx#-Store#", text="Rx store number")
        table.heading("Patient name", text="Patient name")
        table.heading("Product", text="Product")
        table.heading("Quantity", text="Quantity")
        table.heading("Delivery", text="Delivery")
        table.heading("Printed", text="Printed")
        table.column("#0", width=0, stretch=NO)  # Hide the default first column
        table.column("Promise Time", width=column_width, anchor='center')
        table.column("Rx#-Store#", width=column_width, anchor='center')
        table.column("Patient name", width=column_width, anchor='center')
        table.column("Product", width=column_width, anchor='center')
        table.column("Quantity", width=column_width, anchor='center')
        table.column("Delivery", width=column_width, anchor='center')
        table.column("Printed", width=column_width, anchor='center')

        self.tableframe.create_window((0, 0), window=table, anchor='nw')


        self.tableframe.configure(scrollregion=self.tableframe.bbox('all'))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Ahnaf Rahman", "Amlodipine 10 MG TAB", 90, "Pick-up", "Yes"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Kaira Yee", "Sertraline 10 MG TAB", 30, "Pick-up", "Yes"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Giselle Kho", " Adderall 10 MG TAB", 60, "Pick-up", "Yes"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Giselle Kho", " Vyvanse 60 MG TAB", 30, "Pick-up", "Yes"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Giselle Kho", " Alprazolam 2 MG TAB", 90, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Giselle Kho", " Hailey Fe 1-20 MG TAB", 84, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Giselle Kho", " Zolpidem 5 MG TAB", 30, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Nabila Souder", "Amphetamine Salts 10 MG TAB", 90, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Nabila Souder", "Zolpidem 5 MG TAB", 30, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Jodi Grieve", "Olanzapine 20 MG TAB", 60, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Jodi Grieve", "Lamotrigine 200 MG TAB", 90, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Christopher Glennon", "Lorazepam 2 MG TAB", 120, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Christopher Glennon", "Testosterone Gel 1.62%", 300, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Christopher Glennon", "Tadalafil 20 MG TAB", 169, "Pick-up", "No"))
        table.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Stephen Waldman", "Progesterone 200 MG TAB", 169, "Pick-up", "No"))
        style = ttk.Style()

        def on_row_select(event):
            selected_item = table.selection()

            if selected_item:
                selected_row = table.item(selected_item)
                selected_name = selected_row['values'][2]
                db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

                db_connection.cursor.execute('SELECT * from patientsinfo WHERE full_name= %s', (selected_name,))
                result = db_connection.cursor.fetchone()

                if result:
                    self.rx_P_patient(result)

        table.bind("<Double-Button-1>", on_row_select)
        cap = cv2.VideoCapture(0)
        video_label = tk.Label(self.Rx_product)
        video_label.place(x=10, y=530)  # You can set the position according to your layout

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        self.update_image(cap, video_label)

    def update_image(self, cap, label):
        ret, frame = cap.read()
        # Resize the frame
        frame = cv2.resize(frame, (320, 320))  # Set the dimensions (width, height)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT, dp=1.2,
            minDist=30, param1=50,
            param2=30, minRadius=10,
            maxRadius=30
        )
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        label.after(10, self.update_image, cap, label)  # refresh image


        # ... (your existing code)

        # Create a label to display the video



    def rx_P_patient(self,result=None):
        self.hide_frames()
        self.Rx_p_Patient.pack()
        if result:
            name, address, contact_number = result[1], result[2], result[3]  # Adjust indices based on your table structure

        # Display the information on Pprod1 canvas
        #Pprod1.create_text(20, 20, text=f"Name: {name}", anchor='w', font=('Trajan Pro', 12))
        #Pprod1.create_text(20, 60, text=f"Address: {address}", anchor='w', font=('Trajan Pro', 12))
        #Pprod1.create_text(20, 100, text=f"Contact: {contact_number}", anchor='w', font=('Trajan Pro', 12))
        Pprod = Canvas(self.Rx_p_Patient, width=1500, height=700, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
        Pprod1 = Canvas(self.Rx_p_Patient, width=480, height=150, bg='#eceadf', border=None)
        Pprod2 = Canvas(self.Rx_p_Patient, width=480, height=150, bg='#eceadf', border=None)
        Pprod3 = Canvas(self.Rx_p_Patient, width=480, height=150, bg='#eceadf', border=None)
        Pprod1.place(x=10,y=20)
        Pprod2.place(x=500,y=20)
        Pprod3.place(x=990,y=20)
        Pprod.place(x=0, y=200)



    def rx_s_patient(self):
        self.hide_frames()

        search_window = Toplevel(self)
        search_window.title("Search Patient")
        search_window.geometry("1350x600")
        search_window.configure(bg='#d6cfbd')

        self.Rx_s_Patient.pack(fill="both", expand=1)

        Lnameentry = Entry(search_window, bg='white', fg='black', width=25)
        Lnameentry.place(x=20, y=50)
        Fnameentry = Entry(search_window, bg='white', fg='black')
        Fnameentry.place(x=270, y=50)
        DOBentry = Entry(search_window, bg='white', fg='black')
        DOBentry.place(x=520, y=50)
        Lnamecanvas = Canvas(search_window, bg='#d6cfbd',width=300,height=20,bd=0, highlightthickness=0, relief='ridge')
        Lnamecanvas.place(x=18,y=20)
        Lnamecanvas.create_text(120,10,text="Last Name (Min chars:4) and/or Phone",fill='black', font=('Vintage Typewriter', 12))
        andcanvas = Canvas(search_window, bg='#d6cfbd',width=50,height=20,bd=0, highlightthickness=0, relief='ridge')
        andcanvas.place(x=470,y=55)
        andcanvas.create_text(20,10,text="and/or",fill='black', font=('Vintage Typewriter', 12))
        Fnamecanvas = Canvas(search_window, bg='#d6cfbd',width=187,height=20,bd=0, highlightthickness=0, relief='ridge')
        Fnamecanvas.place(x=270,y=20)
        Fnamecanvas.create_text(80,10,text="First Name (Min chars:2)",fill='black', font=('Vintage Typewriter', 12))
        DOBcanvas = Canvas(search_window, bg='#d6cfbd',width=187,height=20,bd=0, highlightthickness=0, relief='ridge')
        DOBcanvas.place(x=500,y=20)
        DOBcanvas.create_text(80,10,text="Date of Birth",fill='black', font=('Vintage Typewriter', 12))
        #search_button = Button(search_window, text="Search", command=lambda: self.search_patient(Lnameentry, Fnameentry, DOBentry))
        #search_button.place(x=220, y=100)
        search_button = tk.Canvas(search_window, width=80, height=25, bg='#d6cfbd', highlightthickness=0, relief="raised", borderwidth=3)
        search_button.create_text(43, 12, text='Search Local', fill='black', font=('Vintage Typewriter', 12))
        search_button.place(x=640, y=100)
        search_button.bind("<Button-1>", lambda event: self.search_patient(event, Lnameentry, Fnameentry, DOBentry))
        search_buttonc = tk.Canvas(search_window, width=105, height=25, bg='#d6cfbd', highlightthickness=0, relief="raised", borderwidth=3)
        search_buttonc.create_text(54, 12, text='Search Corporate', fill='black', font=('Vintage Typewriter', 12))
        search_buttonc.place(x=730, y=100)
        search_buttonc.bind("<Button-1>", lambda event: self.search_patient(event, Lnameentry, Fnameentry, DOBentry))

        #s = ttk.Style
        #s.configure("Treeview", background="#bdaa8b",foreground="white")
        #s.configure("Treeview.Heading", background="#bdaa8b",foreground="white")

        style = ttk.Style()
        style.configure("Custom.Treeview", background="#bdaa8b", fieldbackground="#bdaa8b", foreground="black")
        #style.configure("Custom.Treeview.Column", width=3000)
        style.configure("Custom.Treeview.Separator", background="black", fieldbackground='black',foreground="black")
        style.configure("Custom.Treeview.Heading", foreground="black", font=("Helvetica", 12))
        style.configure("Custom.Treeview", borderwidth=1)
        style.configure("Custom.Treeview.Heading", borderwidth=10, background="d6cfbd")
        #style.configure("Custom.Treeview.Column", borderwidth=10)


        self.tree = ttk.Treeview(search_window, style="Custom.Treeview", show="headings")
        self.tree["columns"] = ("first_name", "last_name",  "address_1", "city","state", "phone", "dob")
        self.tree.heading("first_name", text="First Name")
        self.tree.heading("last_name", text="Last Name")
        self.tree.heading("address_1", text="Street")
        self.tree.heading("city", text="City")
        self.tree.heading("state", text="State")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("dob", text="DOB")
        self.tree.column("first_name", width=5)
        self.tree.column("last_name", width=100)
        self.tree.column("address_1", width=100)
        self.tree.column("city", width=50)
        self.tree.column("state", width=100)
        self.tree.column("phone", width=50)
        self.tree.column("dob", width=50)


        self.tree.place(x=20,y=150,width=1300, height=400)



    def search_patient(self,event, Lnameentry, Fnameentry, DOBentry):
        last_name = Lnameentry.get()
        first_name = Fnameentry.get()
        dob = DOBentry.get()
        db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
        if last_name and first_name:
            db_connection.cursor.execute(
                    'SELECT * FROM patientsinfo WHERE first_name LIKE %s AND last_name LIKE %s', (f"{first_name}%", f"{last_name}%"))


        elif dob and last_name:
            db_connection.cursor.execute('SELECT * FROM patientsinfo WHERE Dateofbirth = %s AND last_name LIKE %s', (dob, f"{last_name}%"))

        elif last_name:
            db_connection.cursor.execute(

                    'SELECT * FROM patientsinfo WHERE last_name LIKE %s', (f"{last_name}%",))
        elif dob:
            db_connection.cursor.execute(
                   'SELECT * FROM patientsinfo WHERE Dateofbirth=%s', (dob,))




        patient = db_connection.cursor.fetchall()

        self.display_patients(patient)

    def display_patients(self, patients):
        style="Custom.Treeview"

        self.tree.delete(*self.tree.get_children())  # Clear current items in the treeview.

        for patient in patients:
            self.tree.insert("", "end", values=(patient['first_name'], patient['last_name'], patient['address_1'], patient['city'], patient['state'], patient['phone'], patient['Dateofbirth']))
        def on_row_selects(event):
            selected_item = self.tree.selection()

            if selected_item:
                selected_row = self.tree.item(selected_item)
                l_name = selected_row['values'][1]
                f_name= selected_row['values'][0]
                print(l_name)
                print(f_name)
                db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

                db_connection.cursor.execute('SELECT * from patientsinfo WHERE last_name= %s AND first_name=%s', (l_name,f_name))
                self.result = db_connection.cursor.fetchone()
                print(self.result)

                if self.result:
                    self.rx_Profile_patient(self.result)
                else:
                    print("Noresults")
            else:
                print("noitem")
        self.tree.bind("<Double-Button-1>", on_row_selects)

    def rx_Profile_patient(self,result=None):
        print("hellloooo")
        self.hide_frames()
        self.Rx_prof_Patient = Frame(self, width=1515,height=1000, bg='#d6cfbd')
        self.Rx_prof_Patient.pack()
        if result:
            print("hello")

    def rx_all_rx(self):
        self.hide_frames()
        self.Rx_Allrx.pack(fill="both",expand=True)

        #swidth = self.winfo_width.get()
        #sheight= self.winfo_height.get()
        #self.Rx_Allrx.place(x=0,y=0, width=swidth, height=sheight)
        scanentry = Entry(self.Rx_product, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=20)
        scanentry.place(x=8, y=50)
        Filterbya = Canvas(self.Rx_Allrx, width=1500, height=150, bg='#d6cfbd', relief=SUNKEN, borderwidth=5)
        Filterbya.place(x=0, y=0)
        Filterbya.create_text(40, 20, text='Filter By:', fill="black", font=('Trajan Pro', 13, 'bold'))
        Filterbya.create_text(140, 30, text='Promise Time:', fill="black", font=('Trajan Pro', 12))
        Filterbya.create_text(140, 60, text='Rx #-Store #:', fill="black", font=('Trajan Pro', 12))
        Filterbya.create_text(140, 90, text='Store Number:', fill="black", font=('Trajan Pro', 12))
        Filterbya.create_text(140, 120, text='Patient Name:', fill="black", font=('Trajan Pro', 12))
        promise_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=15)
        rxstorenum_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
        Storenum_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
        Ptname_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
        promise_entry.place(x=400, y=15)
        rxstorenum_entry.place(x=400, y=45)
        Storenum_entry.place(x=400, y=75)
        Ptname_entry.place(x=400, y=105)
        Mainprod = Canvas(self.Rx_Allrx, width=1500, height=850, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
        Mainprod.place(x=0, y=150)
        Userinfo = Canvas(self.Rx_Allrx, width=1500, height=100, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
        Userinfo.place(x=0,y=730)
    def our_command(self):
        pass


if __name__ == '__main__':
    root_login = LoginWindow()
    root_login.mainloop()
