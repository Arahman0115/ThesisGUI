from Database import DatabaseConnection
from tkinter import *
from tkinter import ttk
import textwrap
import tkinter as tk
from functools import partial
from tkinter.font import Font
import ttkbootstrap as tb


def Drug_Review(self):
    self.hide_frames()
    self.DUR.pack(fill="both", expand=True)
    print('clicked')
    swidth = self.winfo_width()
    sheight = self.winfo_height()
    self.Mainprod1 = Canvas(self.DUR, width=swidth, height=sheight, bg='red', relief=SUNKEN, borderwidth=5)

    self.newstyle3= ttk.Style()
    self.newstyle3.configure("PatientDrugReview.Treeview", background="black", fieldbackground="black", foreground="white")
    self.newstyle3.configure("PatientDrugReview.Treeview.Column", width=3000)
    self.newstyle3.configure("PatientDrugReview.Treeview.Separator", background="white", fieldbackground='black',foreground="black")
    self.newstyle3.configure("PatientDrugReview.Treeview.Heading", foreground="white", font=("Helvetica", 12, "bold"))
    self.newstyle3.configure("PatientDrugReview.Treeview", borderwidth=1, width=swidth//1.01)
    self.newstyle3.configure("PatientDrugReview.Treeview.Heading", borderwidth=10)
    self.newstyle3.configure("PatientDrugReview.Treeview.Column", borderwidth=10)

    self.new_table_treeframe = Canvas(self.DUR, width=swidth/1.01, height=350, bg='pink', relief=SUNKEN, borderwidth=5)

    self.new_table_treeframe.pack(expand=True, fill="both")



    #PrintButton = tk.Button(self.Rx_product, text="Print Selected Order",width=11,height=2, bg='black', fg='white')
    #PrintButton.place(x=1250,y=450)


    self.new_table_tree = ttk.Treeview(self.new_table_treeframe, style="PatientDrugReview.Treeview", columns=("Promise Time", "Rx#-Store#", "Patient name", "Product"), show="headings")
    self.new_table_tree.heading("Promise Time", text="Promise Time")
    self.new_table_tree.heading("Rx#-Store#", text="Rx store number")
    self.new_table_tree.heading("Patient name", text="Patient name")
    self.new_table_tree.heading("Product", text="Product")
    self.new_table_tree.column("Promise Time", width=300)
    self.new_table_tree.column("Rx#-Store#",width=300)
    self.new_table_tree.column("Patient name",width=300)
    self.new_table_tree.column("Product",width=300)


    #self.new_table_tree.column("#0", width=0, stretch=NO)  # Hide the default first column


    self.new_table_treeframe.create_window((0, 0), window=self.new_table_tree, anchor='nw')

    self.new_table_tree.pack(fill="both", expand=True)
    #db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

   # db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
    #result = db_connection.cursor.fetchone()

    self.new_table_treeframe.configure(scrollregion=self.new_table_treeframe.bbox('all'))
    self.new_table_tree.insert("", "end",values=("2023-08-15 10:30:00", "6003823-1618", "Ahnaf Rahman", "Rosuvastatin 10 MG TAB"))



    def on_row_select(event):
        new_selected_item = self.new_table_tree.selection()
        print(new_selected_item)

        if new_selected_item:
            selected_row = self.new_table_tree.item(new_selected_item)
            print(selected_row)
            self.FULL_name = selected_row['values'][2]
            self.Drug_name = selected_row['values'][3]
            DRUGIE = self.Drug_name.split()[0]
            print(DRUGIE)


            #print(self.l_name)
            #print(self.f_name)
            db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

            db_connection.cursor.execute('SELECT * from patientsinfo WHERE full_name = %s', (self.FULL_name,))
            self.results = db_connection.cursor.fetchone()
            #db_connection.cursor.execute('SELECT genotype FROM  WHERE full_name')
            if self.results:
                USER_ID = self.results['user_id']
                DRUG= DRUGIE
                self.last = self.results['last_name']
                self.first = self.results['first_name']
                self.dateb = self.results['Dateofbirth']

                sql_query = """
                            SELECT drug_name, GROUP_CONCAT(drug_conflict, ', ') AS drug_conflicts
                            FROM drug_review
                            WHERE user_id = %s
                                AND drug_name = %s
                                AND drug_conflict LIKE '%CC%'
                            GROUP BY drug_name
                            ORDER BY drug_name
                            """

                db_connection.cursor.execute(sql_query, (USER_ID, DRUG,))
                self.drug_review_info = db_connection.cursor.fetchall()
                self.rx_Patient_Drug_Review(self.results, self.drug_review_info, self.last,self.first, self.dateb)
            else:
                print("Noresults")
        else:
            print("noitem")
    self.new_table_tree.bind("<Double-Button-1>", on_row_select)

def rx_Patient_Drug_Review(self, info, drugrevinfo, lastname, firstname, dob):
    print('YES')
    self.hide_frames()
    screen_width = self.winfo_screenwidth()
    print(screen_width)
    screen_height = self.winfo_screenheight()
    self.rx_Patient_Drug_Review_frame.pack(fill="both", expand=True)

    self.informationcanvas = Canvas(self.rx_Patient_Drug_Review_frame, width=screen_width + 200, height=screen_height//3, bg='red')
    self.informationcanvas.grid(row=0,column=0)

    self.drug_table_treeframe = Canvas(self.rx_Patient_Drug_Review_frame, width=screen_width, height=screen_height, bg='black', relief=SUNKEN, borderwidth=5)
    self.drug_table_treeframe.grid(row=1,column=0)

    self.genotypecanvas = Canvas(self.rx_Patient_Drug_Review_frame, width=screen_width, height=screen_height//3, bg='black')
    self.genotypecanvas.grid(row=2,column=0)
    self.restcanvas = Frame(self.rx_Patient_Drug_Review_frame, width=screen_width, height=screen_height//2, bg='black')
    self.restcanvas.grid(row=3,column=0)

    genotypelabel = Label(self.genotypecanvas, anchor='w', text="Product Name: Rosuvastatin SLCO1B1 Genotype:CC Variant:rs4149056 Genotype:CT ",bg="black", fg="white", font=("Helvetica", 12, "bold"))
    genotypelabel.grid(row=0,column=0)
    # Create a label for the self.restcanvas that says "Approve" and another label next to it that says "Deny - Send to MD"


    def ourcommand():
        pass
    # Create text that says "Approve" for this canvas:
    # Create text that says "Deny" for this canvas: self.denybutton_canvas = tk.Canvas(self.my_canvas, width=70, height=25, bg='white', highlightthickness=0, relief="raised")
    self.approvebuttonframe = tk.Frame(self.restcanvas, bd=2, relief="raised")
    self.approvebuttonframe.grid(row=0, column=0)

    self.approvebutton_canvas = tk.Canvas(self.approvebuttonframe, width=70, height=25, bg='white', highlightthickness=0)
    self.approvebutton_canvas.pack(fill='both', expand=True)

    text_id = self.approvebutton_canvas.create_text(35, 10, text='Approve', fill='white', font=('Vintage Typewriter', 11, 'italic'))
        # Create a small frame to hold the self.approvebutton_canvas and give it a bd of 2 and relief of raised
    # Create a small frame to hold the self.denybutton_canvas and give it a bd of 2 and relief of raised



    # Create text that says "Deny" for this canvas:
    # Create frame to hold denybuttonCanvas
    self.denybuttonframe = tk.Frame(self.restcanvas, bd=2, relief="raised")
    self.denybuttonframe.grid(row=0, column=1)

    self.denybutton_canvas = tk.Canvas(self.denybuttonframe, width=70, height=25, bg='white', highlightthickness=0)
    self.denybutton_canvas.pack(fill='both',expand=True)
    text_id2 = self.denybutton_canvas.create_text(35, 10, text='Deny', fill='white', font=('Vintage Typewriter', 11, 'italic'))
    self.denybutton_canvas.bind("<Button-1>", ourcommand())


    # Create a frame to contain the TreeView widget


    newstyle2 = ttk.Style()
    newstyle2.configure("Drug.Treeview", background="black", fieldbackground="black", foreground="white")
    newstyle2.configure("Drug.Treeview.Heading", foreground="white", font=("Helvetica", 12, "bold"))
    newstyle2.configure("Drug.Treeview.Heading", borderwidth=10)
    newstyle2.configure("Drug.Treeview.Column", borderwidth=10)

    # Create the TreeView widget inside the frame
    self.drug_table_tree = ttk.Treeview(self.drug_table_treeframe, style='Drug.Treeview', show="headings")
    self.drug_table_tree["columns"] = ["Drug Name", "Conflict"]
    self.drug_table_tree.column("#0", width=120)
    self.drug_table_tree.column("Drug Name", width=200)
    self.drug_table_tree.column("Conflict", width=1300, stretch=True)

    self.drug_table_tree.heading("Drug Name", text="Drug Name")
    self.drug_table_tree.heading("Conflict", text="Conflict")
    self.drug_table_tree.grid(row=0,column=0,sticky="nsew")

    #self.drug_table_treeframe.create_window((0, 0), window=self.drug_table_tree)


    first_name_label = Label(self.informationcanvas, text="First Name", bg="black", fg="white", font=("Vintage Typewriter", 12))
    first_name_label.grid(row=0,column=0)
    first_name_entry = tb.Entry(self.informationcanvas, bootstyle="info")
    first_name_entry.insert(0,firstname)
    first_name_entry.grid(row=0,column=1)

    last_name_label = Label(self.informationcanvas, text="Last Name", bg="black", fg="white", font=("Vintage Typewriter", 12))
    last_name_label.grid(row=0,column=2)
    last_name_entry = Entry(self.informationcanvas, bg='white', fg='black', width=25)
    last_name_entry.insert(0,lastname)
    last_name_entry.grid(row=0,column=3)

    dob_label = Label(self.informationcanvas, text="Date of Birth", bg="black", fg="white", font=("Vintage Typewriter", 12))
    dob_label.grid(row=0,column=4)
    dob_entry = Entry(self.informationcanvas, bg='white', fg='black', width=25)
    dob_entry.insert(0,dob)
    dob_entry.grid(row=0,column=5)
    # Configure the canvas scroll region
    #self.drug_table_treeframe.configure(scrollregion=self.drug_table_treeframe.bbox('all'))



    for row in self.drug_table_tree.get_children():
        self.drug_table_tree.delete(row)
    for row in drugrevinfo:
        self.drug_table_tree.insert('', 'end', values=(row['drug_name'], ""))
        for conflict in row['drug_conflicts'].split(','):
            self.drug_table_tree.insert('', 'end', values=("", (conflict.strip())))




    #selected_item = self.new_table_tree.selection()

    #if selected_item:
    #    selected_row = self.new_table_tree.item(selected_item)#\

#        NAME = selected_row['values'][0]
#        print(NAME)

        #db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
        #db_connection.cursor.execute("SELECT genetic_info_id FROM final_genetic_info WHERE gene = %s", (NAME,))
        #genetic_info_id = db_connection.cursor.fetchone()

        #print(genetic_info_id)

        # Corrected DELETE query for final_genetic_info table
        #if genetic_info_id:
        #    db_connection.cursor.execute('DELETE from final_genetic_info WHERE genetic_info_id= %s', (genetic_info_id['genetic_info_id'],))
        #    db_connection.connection.commit()

