from Database import DatabaseConnection
from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb
import tkinter as tk
from PIL import Image, ImageTk


def ContactPrescriberQueue(self):
    self.hide_frames()
    self.Contact_Queue_Frame.pack()
    # Create variable to hold screen width
    swidth = self.winfo_width()
    sheight = self.winfo_height()


    self.contact_table_treeframe = Canvas(self.DUR, width=swidth/1.01, height=350, bg='pink', relief=SUNKEN, borderwidth=5)

    self.contact_table_treeframe.pack(expand=True, fill="both")
    




    #PrintButton = tk.Button(self.Rx_product, text="Print Selected Order",width=11,height=2, bg='black', fg='white')
    #PrintButton.place(x=1250,y=450)


    self.new_table_tree = ttk.Treeview(self.contact_table_treeframe, style="PatientDrugReview.Treeview", columns=("Promise Time", "Rx#-Store#", "Patient name", "Product"), show="headings")
    self.new_table_tree.heading("Promise Time", text="Promise Time")
    self.new_table_tree.heading("Rx#-Store#", text="Rx store number")
    self.new_table_tree.heading("Patient name", text="Patient name")
    self.new_table_tree.heading("Product", text="Product")
    self.new_table_tree.column("Promise Time", width=300)
    self.new_table_tree.column("Rx#-Store#",width=300)
    self.new_table_tree.column("Patient name",width=300)
    self.new_table_tree.column("Product",width=300)


    #self.new_table_tree.column("#0", width=0, stretch=NO)  # Hide the default first column


    self.contact_table_treeframe.create_window((0, 0), window=self.new_table_tree, anchor='nw')

    self.new_table_tree.pack(fill="both", expand=True)
    #db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

   # db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
    #result = db_connection.cursor.fetchone()

    self.contact_table_treeframe.configure(scrollregion=self.contact_table_treeframe.bbox('all'))
    self.new_table_tree.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Ahnaf Rahman", "Rosuvastatin 10 MG TAB"))

def ContactPrescriber(self):
    self.hide_frames()
    self.Contact_frame.pack(fill="both", expand=True)
    print('clicked')
    canvas = Canvas(
        self.Contact_frame,
        bg = "#118AB0",
        height = 737,
        width = 1267,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        183.0,
        151.0,
        1083.0,
        411.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1267.0,
        132.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        426.0,
        7.0,
        863.0,
        126.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_rectangle(
        6.0,
        6.0,
        288.0,
        125.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_rectangle(
        979.0,
        7.0,
        1261.0,
        126.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_text(
        995.0,
        16.0,
        anchor="nw",
        text="Medication Name:\nNDC:\nOn Hand:\nAllocated:",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        439.0,
        15.0,
        anchor="nw",
        text="Prescriber Name:\nPrescriber Address:\nPrescriber Fax:\nPrescriber Phone:\n",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        13.0,
        13.0,
        anchor="nw",
        text="Patient Name:\nPatient Phone:\n",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    canvas.create_rectangle(
        8.0,
        441.0,
        1261.0,
        725.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        956.0,
        449.0,
        1254.0,
        717.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_rectangle(
        497.0,
        449.0,
        795.0,
        717.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_rectangle(
        19.0,
        449.0,
        317.0,
        717.0,
        fill="#0B0B0B",
        outline="")

    canvas.create_text(
        26.0,
        462.0,
        anchor="nw",
        text="Prescriber Response\n\n\n",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        968.0,
        461.0,
        anchor="nw",
        text="Notes\n",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )



    swidth = self.winfo_width()
    sheight = self.winfo_height()
    print(sheight)
    self.Mainprod3 = Canvas(self.Contact_frame, width=swidth, height=sheight, bg='black', borderwidth=5)
    self.Mainprod3.pack(fill="both", expand=True)
    self.information = Canvas(self.Mainprod3, width=400, height=400, bg='black', relief=SUNKEN, borderwidth=5)
    self.information.grid(row=0, column=0)

    # Create entry boxes
    self.PatientNameEntry = tb.Entry(self.information, bootstyle="info")
    self.PatientNameEntry.place(relx=0.8, rely=0.05)
    self.PatientDOBEntry = tb.Entry(self.information, bootstyle="info")
    self.PatientDOBEntry.place(relx=0.8, rely=0.15)
    self.PatientPhoneEntry = tb.Entry(self.information, bootstyle="info")
    self.PatientPhoneEntry.place(relx=0.8, rely=0.25)
    self.PrescriberNameEntry = tb.Entry(self.information, bootstyle="info")
    self.PrescriberNameEntry.place(relx=0.8, rely=0.35)
    self.PrescriberPhoneEntry = tb.Entry(self.information, bootstyle="info")
    self.PrescriberPhoneEntry.place(relx=0.8, rely=0.45)
    self.PrescriberFaxEntry = tb.Entry(self.information, bootstyle="info")
    self.PrescriberFaxEntry.place(relx=0.8, rely=0.55)
    # Insert dummy data for the above entry boxes
    self.PatientNameEntry.insert(0, "John Doe")
    self.PatientDOBEntry.insert(0, "01/01/2001")
    self.PatientPhoneEntry.insert(0, "123-456-7890")
    self.PrescriberNameEntry.insert(0, "Jane Doe")
    self.PrescriberPhoneEntry.insert(0, "098-765-4321")
    self.PrescriberFaxEntry.insert(0, "098-765-4321")


    # Create labels
    label_y_start = 0.05
    label_y_increment = 0.098

    self.PatientNameLabel = Label(self.information, text="Patient Name", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PatientNameLabel.place(relx=0.1, rely=label_y_start)
    self.PatientDOBLabel = Label(self.information, text="Patient DOB", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PatientDOBLabel.place(relx=0.1, rely=label_y_start + label_y_increment)
    self.PatientPhoneLabel = Label(self.information, text="Patient Phone Number", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PatientPhoneLabel.place(relx=0.1, rely=label_y_start + 2 * label_y_increment)
    self.PrescriberNameLabel = Label(self.information, text="Prescriber Name", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PrescriberNameLabel.place(relx=0.1, rely=label_y_start + 3 * label_y_increment)
    self.PrescriberPhoneLabel = Label(self.information, text="Prescriber Phone Number", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PrescriberPhoneLabel.place(relx=0.1, rely=label_y_start + 4 * label_y_increment)
    self.PrescriberFaxLabel = Label(self.information, text="Prescriber Fax Number", font=("Trajan Pro", 12), fg='white', bg='black')
    self.PrescriberFaxLabel.place(relx=0.1, rely=label_y_start + 5 * label_y_increment)



# Open the image file

    # Create a label that will be exactly centered in the prescriptionimage canvas and that says "Prescription Image"

    # Create a button that will allow the user to upload the prescription image
    self.buttonframe = Canvas(self.Mainprod3, width=400, height=100, bg='black')
    self.buttonframe.place(relx=0.6, rely=0.97, anchor='center') # Anchor 's' will place it at the bottom

    self.UploadButton = tb.Button(self.buttonframe, text="Upload Prescription Image", bootstyle='info')

    # Create a button that will allow the user to submit the prescription
    self.SubmitButton = tb.Button(self.buttonframe, text="Submit Prescription", bootstyle='info')

    # Create a button that will allow the user to go back to the homepage
    self.HomeButton = tb.Button(self.buttonframe, text="Home", bootstyle='info')

    # Create a button that will allow the user to cancel the prescription
    self.CancelButton = tb.Button(self.buttonframe, text="Cancel Prescription", bootstyle='info')

    # Create a button that will allow user to resend the prescription to the workflow
    self.ResendButton = tb.Button(self.buttonframe, text="Approve Resend to Workflow", bootstyle='info')

    # Create a button that will allow the user to deny the prescription
    self.DenyButton = tb.Button(self.buttonframe, text="Deny Prescription", bootstyle='info')


    # Make all the buttons that i just created, side by side and at the bottom of main prod3
    # Create a frame that will hold all the buttons and then put them side by side

    # Place the buttons in the buttonframe
    self.UploadButton.grid(row=0,column=0)
    self.SubmitButton.grid(row=0,column=1)
    self.HomeButton.grid(row=0,column=2)
    self.CancelButton.grid(row=0,column=3)
    self.ResendButton.grid(row=0,column=4)
    self.DenyButton.grid(row=0,column=5)


    # Create a canvas on the Mainprod3, that will hold all the information about how many times the prescriber was contacted

    # Create a canvas on the Mainprod3 that will hold a treeview, that will show all the times the prescriber was contacted, this will hold information like what the contact method was, what date it was etc.
    self.contactlogframe = Canvas(self.Mainprod3, width=400, height=400, bg='black', relief=SUNKEN, borderwidth=5)
    self.contactlogframe.place(relx=0.6, rely=0.4, anchor='center')
    # Create a label that will be exactly centered in the contactlogframe canvas and that says "Contact Log"
    self.ContactLogLabel = Label(self.contactlogframe, text="Contact Log", font=("Trajan Pro", 12), fg='white', bg='black')
    self.ContactLogLabel.place(relx=0.5, rely=0.05, anchor='center')
    # Create a button that will allow the user to add a new contact log
    self.AddContactLogButton = tb.Button(self.contactlogframe, text="Add Contact Log", bootstyle='info')
    # Create a button that will allow the user to delete a contact log
    self.DeleteContactLogButton = tb.Button(self.contactlogframe, text="Delete Contact Log", bootstyle='info')
    # Create a button that will allow the user to edit a contact log
    self.EditContactLogButton = tb.Button(self.contactlogframe, text="Edit Contact Log", bootstyle='info')
    # Create a button that will allow the user to view a contact log
    self.ViewContactLogButton = tb.Button(self.contactlogframe, text="View Contact Log", bootstyle='info')
    # Create a button that will allow the user to go back to the homepage
    self.HomeButton2 = tb.Button(self.contactlogframe, text="Home", bootstyle='info')
    # Place the buttons in the contactlogframe
    self.AddContactLogButton.grid(row=0,column=0)
    self.DeleteContactLogButton.grid(row=0,column=1)
    self.EditContactLogButton.grid(row=0,column=2)
    self.ViewContactLogButton.grid(row=0,column=3)
    self.HomeButton2.grid(row=0,column=4)
    # Create a treeview that goes on the contactlogframe canvas
    # Create a treeview that will show all the times the prescriber was contacted, this will hold information like what the contact method was, what date it was etc.
    self.contactlogtableframe = Canvas(self.Mainprod3, width=swidth//3, height=400, bg='black', relief=SUNKEN, borderwidth=5)
    self.contactlogtableframe.grid(row=0, column=1)
    # Create a Treeview widget within the canvas
    # Create a style for the treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", background="black", fieldbackground="black", foreground="white")

    table = ttk.Treeview(self.contactlogtableframe, style="Custom.Treeview", columns=("Contact Method", "Contact Reason", "Date", "Time", "Response"), show="headings")
    table.heading("Contact Method", text="Contact Method")
    table.heading("Contact Reason", text="Contact Reason")
    table.heading("Date", text="Date")
    table.heading("Time", text="Time")
    table.column("#0", width=0, stretch=NO)  # Hide the default first column
    table.column("Contact Method", width=int(int(((self.swidth/1.0999999))))//6, anchor='center')
    table.column("Contact Reason", width=int(int(((self.swidth/1.0999999))))//5, anchor='center')
    table.column("Date", width=int(int(((self.swidth/1.0999999))))//7, anchor='center')
    table.column("Time", width=int(int(((self.swidth/1.0999999))))//6, anchor='center')

    table.pack()

    # Insert dummy data into the table
    table.insert("", "end", values=("Phone", "Medication Change: Simvastatin 10 MG", "01/01/2024", "12:00 PM", "Sent"))
    table.insert("", "end", values=("Fax", "Medication Change: Simvastatin 10 MG", "01/01/2024", "12:00 PM", "Pending"))
    table.insert("", "end", values=("Phone", "Medication Change: Simvastatin 10 MG", "01/01/2024", "12:00 PM", "Pending"))
    table.insert("", "end", values=("Fax", "Medication Change: Simvastatin 10 MG", "01/01/2024", "12:00 PM", "Pending"))
    table.insert("", "end", values=("Phone", "Medication Change: Simvastatin 10 MG", "01/02/2024", "12:00 PM", "Approved"))



    image_path = "PNGS/samplescript.png"
    original_image = Image.open(image_path)

    # Get the dimensions of the canvas
    canvas_width = 400
    canvas_height = 600

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
    self.prescriptionimage = Canvas(self.Mainprod3, width=canvas_width, height=canvas_height, bg='black', relief=SUNKEN, borderwidth=5)
    self.prescriptionimage.grid(row=1, column=0)
    self.prescriptionimage.create_image(canvas_width / 2.0, canvas_height / 2.2, image=resized_photo)

    # Keep a reference to the PhotoImage object to prevent it from being garbage collected
    self.prescriptionimage.image = resized_photo





    # Create a button that will allow the user to upload the prescription image
    #self.UploadButton = tb.Button(self.information2, text="Resend to Workflow")
    #self.UploadButton.grid(row=0,column=0)
    # Create a button that will allow the user to submit the prescription
    #self.CancelPrescriptionButton = tb.Button(self.information2, text="CancelPrescription")
    #self.CancelPrescriptionButton.grid(row=0,column=1)
    # Create a button that will allow the user to go back to the homepage
