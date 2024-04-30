from tkinter import *
from tkinter import ttk
import tkinter as tk
from Database import DatabaseConnection
import ttkbootstrap as tb
from PIL import Image, ImageTk

class ProductQueue(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Define and initialize any instance variables here
        self.Rx_product = Frame(self, width=1515, height=1000, bg='white')
        window_width = 1515
        self.Rx_product.pack(fill="both", expand=True)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(screen_height)
        #self.Rx_product.place(x=0,y=0, width=screen_width, height=screen_height)
        self.Findanrx = tb.Frame(self.Rx_product, width=500, height=500)  # Modify the width parameter to the desired width
        self.Findanrx.place(x=0,y=0)        
        Findanrx_label = Label(self.Findanrx, text='Find an Rx', fg='white', bg='red', font=('Vintage Typewriter ', 13, 'bold'))
        Findanrx_label.pack()
        Findanrx_text = Label(self.Findanrx, text='Scan or Enter Rx#:', fg='white', bg='red', font=('Vintage Typewriter ', 10))
        Findanrx_text.pack()
        scanentry = Entry(self.Findanrx, fg='white', bg='red', font=('Vintage Typewriter ', 10))
        scanentry.pack()
        Filterby_frame = tb.Frame(self.Rx_product, width=3000, height=screen_height // 5)
        Filterby_frame.place(x=200, y=0)
        Filterby_label = Label(Filterby_frame, text='Filter By:', fg='white', bg='red', font=('Vintage Typewriter ', 13, 'bold'))
        Filterby_label.pack()
        Filterby_promise_label = Label(Filterby_frame, text='Promise Time:', fg='white', bg='red', font=('Vintage Typewriter ', 12))
        Filterby_promise_label.pack()
        Filterby_rxstore_label = Label(Filterby_frame, text='Rx #-Store #:', fg='white', bg='red', font=('Vintage Typewriter ', 12))
        Filterby_rxstore_label.pack()
        Filterby_storenum_label = Label(Filterby_frame, text='Store Number:', fg='white', bg='red', font=('Vintage Typewriter ', 12))
        Filterby_storenum_label.pack()
        Filterby_ptname_label = Label(Filterby_frame, text='Patient Name:', fg='white', bg='red', font=('Vintage Typewriter ', 12))
        Filterby_ptname_label.pack()
        
  

        promise_entry = Entry(self.Rx_product, fg='white', borderwidth=0, bg='white', width=15, relief=SUNKEN)
        rxstorenum_entry = Entry(self.Rx_product, fg='white', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        Storenum_entry = Entry(self.Rx_product, fg='white', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        Ptname_entry = Entry(self.Rx_product, fg='white', borderwidth=0, bg='white', relief=SUNKEN, width=60)
        promise_entry.place(x=400, y=15)
        rxstorenum_entry.place(x=400, y=45)
        Storenum_entry.place(x=400, y=75)
        Ptname_entry.place(x=400, y=105)
        Mainprod = tb.Frame(self.Rx_product, width=screen_width, height=screen_height//1.1, relief="groove")
        Mainprod.place(x=0, y=150)
        canvas_width = 1420
        num_columns = 7

        style = ttk.Style()
        style.configure("Custom.Treeview", background="white", fieldbackground="white", foreground="white")
        style.configure("Custom.Treeview.Column", width=3000)
        style.configure("Custom.Treeview.Separator", background="white", fieldbackground='white',foreground="white")
        style.configure("Custom.Treeview.Heading", foreground="white", font=("Helvetica", 12, "bold"))
        style.configure("Custom.Treeview", borderwidth=1, width=screen_width//1.01)
        style.configure("Custom.Treeview.Heading", borderwidth=10)
        style.configure("Custom.Treeview.Column", borderwidth=10)

        self.tableframe = Canvas(self.Rx_product, width=screen_width, height=350, bg='white', borderwidth=5)
        self.tableframe.place(relx=.1, rely=.2)

        self.printbutton = tb.Button(self.Rx_product, text="Print Selected Order", bootstyle="info")
        self.printbutton.place(x=1095, y=450)
        self.printbbutton = tb.Button(self.Rx_product, text="Print Batch", bootstyle="info")
        self.printbbutton.place(x=1250, y=450)
        self.okbutton = tb.Button(self.Rx_product, text="OK", bootstyle="info")
        self.okbutton.place(x=1405, y=450)

        def update_display():
            self.tableframe.update_idletasks()

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
        table.column("Promise Time", width=int(int(((screen_width/1.0999999))))//6, anchor='center')
        table.column("Rx#-Store#", width= int(((screen_width/1.0999999)))//6, anchor='center')
        table.column("Patient name", width=int(((screen_width/1.0999999)))//7, anchor='center')
        table.column("Product", width=int(((screen_width/1.099999999999)))//5, anchor='center')
        table.column("Quantity", width=int(((screen_width/1.0999999)))//6, anchor='center')
        table.column("Delivery", width=int(((screen_width/1.0999999)))//8, anchor='center')
        table.column("Printed", width=int(((screen_width/1.0999999)))//9, anchor='center')

        self.tableframe.create_window((0, 0), window=table, anchor='w')
        
        self.tableframe.configure(scrollregion=self.tableframe.bbox('all'))
        
        table.insert("", "end", values=("2023-08-15 10:30:00", "6003823-1618", "Christopher Glennon", "Testosterone Gel 1.62%", 300, "Pick-up", "No"))

        # Create a label that will hold a counter of how many prescriptions are in the table
        # Create the counter that will count how many prescriptions there are in the table
        self.prescription_counter = Label(self.tableframe, text="Prescriptions in Product: 0", font=('Vintage Typewriter ', 12), fg='white', bg='white')
        self.prescription_counter.place(x=0, rely=.6)

        # Create a function that will update the counter
        def update_counter():
            # Retrieve the number of items in the table
            items_in_table = len(table.get_children())
            # Update the counter label with the count
            self.prescription_counter.config(text=f"Prescriptions: {items_in_table}", font=('Vintage Typewriter', 12))

        # Use the update_counter() function to display the count of prescriptions onto the prescription counter label
        update_counter()

        update_display()

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
        self.PatientProductScreen = Canvas(self.Rx_product, width=screen_width, height=screen_height//2, bg='red', relief=SUNKEN, borderwidth=5)
        self.PatientProductScreen.place(x=0, y=500, width=screen_width, height=screen_height // 2)



    def rx_P_patient(self,result=None):
        if result:
            name = result['full_name']
            address = result['address_1']
            contact_number = result['phone']

        # Display the information on Pprod1 canvas

        Pprod1 = Canvas(self.PatientProductScreen, width=480, height=150, bg='#eceadf', border=None)
        Pprod2 = Canvas(self.PatientProductScreen, width=480, height=150, bg='#eceadf', border=None)
        Pprod3 = Canvas(self.PatientProductScreen, width=480, height=150, bg='#eceadf', border=None)
        Pprod1.create_text(20, 20, text=f"Name: {name}", anchor='w', font=('Vintage Typewriter ', 12), fill='white')
        Pprod1.create_text(20, 60, text=f"Address: {address}", anchor='w', font=('Vintage Typewriter ', 12), fill='white')
        Pprod1.create_text(20, 100, text=f"Contact: {contact_number}", anchor='w', font=('Vintage Typewriter ', 12), fill='white')
        Pprod1.place(x=10,y=20)
        Pprod2.place(x=500,y=20)
        Pprod3.place(x=990,y=20)
        # Create a canvas that will later hold the prescription image

        # Display rosuvastatin.jpg onto the Pprod4 canvas
        image_path = "PNGS/am.png"
        original_image = Image.open(image_path)

        # Get the dimensions of the canvas
        canvas_width = 480
        canvas_height = 150

        # Calculate the aspect ratio of the image
        image_width, image_height = original_image.size
        aspect_ratio = image_width / image_height

        # Calculate the dimensions of the resized image to fit within the canvas
        if aspect_ratio > canvas_width / canvas_height:
            # The image is wider than the canvas
            new_width = canvas_width
            new_height = int(canvas_width / aspect_ratio)
        else:
            # The image is taller than the canvas
            new_height = canvas_height
            new_width = int(canvas_height * aspect_ratio)

        # Resize the image with LANCZOS resampling
        resized_image = original_image.resize((new_width, new_height), resample=Image.LANCZOS)

        # Convert the resized image to a PhotoImage object
        resized_photo = ImageTk.PhotoImage(resized_image)

        # Create the canvas and insert the resized image
        self.pillinformation = Canvas(self.PatientProductScreen, width=480, height=150, bg='#eceadf', border=None)
        self.pillinformation.place(relx=.8, rely=.1)

        # Draw text directly onto the canvas
        # Create a frame underneath pillinformation that will hold pillname pillndc and pillquantity
        self.pillinfo = Canvas(self.PatientProductScreen, width=480, height=300, bg='#eceadf', border=None)
        self.pillinfo.place(relx=.8, rely=.4)
        self.pillinfo.create_text(20, 20, text="Pill Name: Amoxicillin 500 MG", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 50, text="Pill NDC: 12-3456-789-01", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 80, text="Pill Quantity: 30", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 110, text="Pill Expiration Date: 2023-08-15", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 140, text="Pill Manufacturer: Pfizer", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 170, text="Pill Description: Antibiotic", anchor='w', font=('Vintage Typewriter ', 9), fill='white')
        self.pillinfo.create_text(20, 200, text="Pill Directions: Take 1 tablet by mouth", anchor='w', font=('Vintage Typewriter ', 9), fill='white')

        Pprod4 = Canvas(self.pillinformation, width=480, height=150, bg='#eceadf', border=None)
        Pprod4.place(x=0, y=0)  # Adjust the placement as needed
        Pprod4.create_image(0, 0, anchor='nw', image=resized_photo)

        # Keep a reference to the PhotoImage object to prevent it from being garbage collected
        Pprod4.image = resized_photo

        # Create a canvas that will hold the prescription information
        Pprod5 = Canvas(self.PatientProductScreen, width=480, height=150, bg='#eceadf', border=None)
        Pprod5.place(x=500, y=200)
