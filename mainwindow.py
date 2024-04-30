from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageFilter

import numpy as np
from Database import DatabaseConnection
import tkinter as tk
from RxProduct import ProductQueue
from Rx_Dat import rx_dat
from Rx_Rec import rx_rec
from Rx_Search import search_patient, display_patients, rx_s_patient, rx_Profile_patient, save_info
from Rx_ALL_rx import rx_all_rx
from Homepage import HomePage
from DUR import Drug_Review, rx_Patient_Drug_Review
from Contact import ContactPrescriber




class MainWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Nexus Controls")

        #self.attributes('-fullscreen',True)

        screen_width = self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        self.geometry(f'{screen_width}x{screen_height}')
        #self.new_pic = ImageTk.PhotoImage(Image.open("PNGS/EnterpriseRx.png").resize((172, 44), Image.ANTIALIAS))
        #self.new_pic2 = ImageTk.PhotoImage(Image.open("PNGS/Mickey.png").resize((183,43),Image.ANTIALIAS))
        #self.geometry('1700x1600')
        #self.EntImLab2 = Label(self, image=self.new_pic, bg='white')
        #self.EntImLab2.place(x=1270, y=100)
        #self.orange1 = Label(self, text='World Class Pharmacy Systems', font=('Trajan Pro', 13), fg='white',
        #                     bg='dark orange', width=290)
        #self.orange1.place(x=0, y=150)
        #self.Mick2 = Label(self, image=self.new_pic2, bg='white')
        #self.Mick2.place(x=0, y=50)
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
        self.bind("<Control-s>", rx_s_patient)

        self.my_menu.add_cascade(label="Rx Queues", menu=self.RxQueues_menu)
        self.my_menu.add_cascade(label="Search", menu=self.Search_menu, accelerator="Ctrl+S")
        self.bind("<Control-s>", rx_s_patient)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.Rx_reception = Frame(self, width=1515, height=1000, bg='white')
        self.Rx_data = Frame(self, width=1515, height=1000, bg='white')
        self.Rx_Allrx = Frame(self, width=1515, height=1000, bg='black')
        self.Rx_s_Patient = Frame(self, width=400, height=400, bg='black')
        self.Rx_p_Patient = Frame(self, width=1515, height=1000, bg='black')
        self.Rx_prof_Patient = Frame(self, width=1515,height=1000, bg='black')
        self.rx_Patient_Drug_Review_frame = Frame(self, width=screen_width,height=screen_height,bg='black')
        self.Contact_frame = Frame(self, width=screen_width, height=screen_height, bg='black')

        self.Rx_homepage = Frame(self, width=screen_width, height= screen_height, bg='black')
        self.DUR = Frame(self, width=screen_width, height=screen_height, bg='black')

        self.RxQueues_menu.add_command(label="Reception", command=self.rx_rec)
        self.RxQueues_menu.add_command(label="Data Entry", command=self.rx_dat)
        self.RxQueues_menu.add_command(label="Product Dispensing", command=self.instantiate_product_queue)
        self.RxQueues_menu.add_command(label="Verification", command=self.our_command)
        self.RxQueues_menu.add_command(label="Release to Patient", command=self.our_command)
        self.RxQueues_menu.add_command(label="Verification 2", command=self.Drug_Review)
        self.RxQueues_menu.add_command(label="General Exception", command=self.our_command)
        self.RxQueues_menu.add_command(label="All Rx Status", command=self.rx_all_rx)
        self.RxQueues_menu.add_command(label="Order Grouping", command=self.our_command)
        self.RxQueues_menu.add_command(label="Adjudication Exception", command=self.our_command)
        self.RxQueues_menu.add_command(label="Contact", command=self.ContactPrescriber)
        self.RxQueues_menu.add_command(label="Fill on Arrival", command=self.our_command)
        self.Search_menu.add_command(label="Patient", command=self.rx_s_patient)
        self.Search_menu.add_command(label="Prescriber", command=self.HomePage)
        self.product_queue = None
        self.hide_frames


        # Add menu commands
        # ...

        # Initially display the rx_all_rx frame.
        self.rx_all_rx()


        self.mainloop()
    def instantiate_product_queue(self):
        # Instantiate the ProductQueue
         
        self.product_queue = ProductQueue(parent=self)
        self.hide_frames()  # Hide all other frames
        self.product_queue.pack(fill="both", expand=True)  # Display the ProductQueue frame
    def hide_frames(self):
        self.Rx_reception.pack_forget()
        self.Rx_data.pack_forget()
        self.Rx_s_Patient.pack_forget()
        self.Rx_Allrx.pack_forget()
        self.Rx_s_Patient.forget()
        self.Rx_prof_Patient.forget()
        self.Rx_homepage.forget()
        self.DUR.pack_forget()
        self.rx_Patient_Drug_Review_frame.pack_forget()
        self.Contact_frame.pack_forget()
        if self.product_queue:
            self.product_queue.pack_forget()





    Drug_Review = Drug_Review

    HomePage = HomePage
    rx_s_patient = rx_s_patient
    search_patient = search_patient
    save_info = save_info
    display_patients = display_patients
    rx_rec = rx_rec
    rx_dat = rx_dat
    rx_Profile_patient = rx_Profile_patient
    rx_Patient_Drug_Review = rx_Patient_Drug_Review
    rx_all_rx = rx_all_rx
    ContactPrescriber = ContactPrescriber
    






    def our_command(self):
        pass