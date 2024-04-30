
from tkinter import *
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

def rx_all_rx(self):
    self.hide_frames()
    self.Rx_Allrx.pack(fill="both",expand=True)

    self.swidth = self.winfo_screenwidth()
    self.sheight= self.winfo_screenheight()
    self.scanentry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=20)
    self.scanentry.place(x=8, y=50)
    self.Filterbya = Canvas(self.Rx_Allrx, width=self.swidth, height=self.sheight, bg='#d6cfbd', relief=SUNKEN, borderwidth=5)
    self.Filterbya.place(x=0, y=0)
    self.Filterbya.create_text(40, 20, text='Filter By:', fill="white", font=('Vintage Typewriter ', 13, 'bold'))
    self.Filterbya.create_text(140, 30, text='Promise Time:', fill="white", font=('Vintage Typewriter ', 12))
    self.Filterbya.create_text(140, 60, text='Rx #-Store #:', fill="white", font=('Vintage Typewriter ', 12))
    self.Filterbya.create_text(140, 90, text='Store Number:', fill="white", font=('Vintage Typewriter ', 12))
    self.Filterbya.create_text(140, 120, text='Patient Name:', fill="white", font=('Vintage Typewriter ', 12))
    promise_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=15)
    rxstorenum_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
    Storenum_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
    Ptname_entry = Entry(self.Rx_Allrx, fg='black', borderwidth=1, bg='white', relief=SUNKEN, width=60)
    promise_entry.place(x=400, y=15)
    rxstorenum_entry.place(x=400, y=45)
    Storenum_entry.place(x=400, y=75)
    Ptname_entry.place(x=400, y=105)
    Mainprod = Canvas(self.Rx_Allrx, width=self.swidth, height=self.sheight, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
    Mainprod.place(x=0, y=150)
    #Userinfo = Canvas(self.Rx_Allrx, width=1500, height=100, bg='#bdaa8b', relief=SUNKEN, borderwidth=5)
    #Userinfo.place(x=0,y=730)

    self.tableframe = Canvas(self.Rx_Allrx, width=self.swidth/1.01, height=350, bg='black', relief=SUNKEN, borderwidth=5)
    self.tableframe.place(x=5, y=160)
    #PrintButton = tk.Button(self.Rx_Allrx, text="Print Selected Order",width=11,height=2, bg='black', fg='white')
    #PrintButton.place(x=1250,y=450)



    def update_display():
        self.tableframe.update_idletasks()
        

    # Create a Treeview widget within the canvas
    table = ttk.Treeview(self.tableframe, style="Custom.Treeview", columns=("Promise Time", "Rx#-Store#", "Patient name", "Product","Quantity", "Delivery"), show="headings")
    table.heading("Promise Time", text="Promise Time")
    table.heading("Rx#-Store#", text="Rx store number")
    table.heading("Patient name", text="Patient name")
    table.heading("Product", text="Product")
    table.heading("Quantity", text="Quantity")
    table.heading("Delivery", text="Delivery")
    table.column("#0", width=0, stretch=NO)  # Hide the default first column
    table.column("Promise Time", width=int(int(((self.swidth/1.0999999))))//6, anchor='center')
    table.column("Rx#-Store#", width= int(((self.swidth/1.0999999)))//6, anchor='center')
    table.column("Patient name", width=int(((self.swidth/1.0999999)))//6, anchor='center')
    table.column("Product", width=int(((self.swidth/1.099999999999)))//6, anchor='center')
    table.column("Delivery", width=int(((self.swidth/1.0999999)))//6, anchor='center')

    self.tableframe.create_window((0, 0), window=table, anchor='nw')
    #db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

   # db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
    #result = db_connection.cursor.fetchone()

    self.tableframe.configure(scrollregion=self.tableframe.bbox('all'))

    update_display()