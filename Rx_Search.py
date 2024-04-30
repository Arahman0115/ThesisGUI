from Database import DatabaseConnection
from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
import ttkbootstrap as tb
from ttkbootstrap import DateEntry




def rx_s_patient(self):
    self.hide_frames()

    self.search_window = Toplevel(self)
    self.search_window.title("Search Patient")
    self.search_window.geometry("1350x600")
    self.search_window.configure(bg='black')

    self.Rx_s_Patient.pack(fill="both", expand=1)

    Lnameentry = Entry(self.search_window, bg='white', fg='black', width=45)
    Fnameentry = Entry(self.search_window, bg='white', fg='black', width=30)
    # Make a the DOBentry a DataEntry
    DOBentry = DateEntry(self.search_window,  width=15, startdate="")
    DOBentry.place(relx=.4, rely=0.07)



    # Make the Lnamecanvs into a label
    Lnamelabel = tb.Label(self.search_window,text="Last Name (Min chars:4) and/or Phone", font=("Vintage Typewriter", 12))
    Lnamelabel.place(relx=0.01, rely=0.03)
    Fnamelabel = tb.Label(self.search_window, text="First Name (Min chars:2)", font=("Vintage Typewriter", 12))
    Fnamelabel.place(relx=.25, rely=0.03)
    DOBlabel = tb.Label(self.search_window, text="Date of Birth", font=("Vintage Typewriter", 12))
    DOBlabel.place(relx=.4, rely=0.03)
    # Position the Entries so that they are directly below the Canvases
    Lnameentry.place(relx=0.01, rely=0.07)
    Fnameentry.place(relx=.25, rely=0.07)
    

    #search_button = Button(self.search_window, text="Search", command=lambda: self.search_patient(Lnameentry, Fnameentry, DOBentry))
    #search_button.place(x=220, y=100)
    
    search_button = tb.Button(self.search_window, text="Search Local", bootstyle='info', command=lambda: self.search_patient( Lnameentry, Fnameentry, DOBentry))
    search_buttonc = tb.Button(self.search_window, text="Search Corporate", bootstyle='info', command=lambda: self.search_patient( Lnameentry, Fnameentry, DOBentry))
    new_pt_button = tb.Button(self.search_window, text="New Patient", bootstyle='info', command=lambda : self.rx_Profile_patient( self.result, self.dob,self.last_name,self.first_name))


    # Position the buttons with relx and rely so that they appear above the treeview
    search_button.place(relx=0.5, rely=0.15)
    search_buttonc.place(relx=0.57, rely=0.15)
    new_pt_button.place(relx=0.66, rely=0.15)

    #s = ttk.Style
    #s.configure("Treeview", background="#bdaa8b",foreground="white")
    #s.configure("Treeview.Heading", background="#bdaa8b",foreground="white")


    self.style = ttk.Style()
    self.style.configure("Custom.Treeview", background="black", fieldbackground="black", foreground="white")
    #style.configure("Custom.Treeview.Column", width=3000)
    self.style.configure("Custom.Treeview.Separator", background="white", fieldbackground='white',foreground="white")
    self.style.configure("Custom.Treeview.Heading", foreground="white", font=("Helvetica", 12))
    self.style.configure("Custom.Treeview", borderwidth=1)
    self.style.configure("Custom.Treeview.Heading", borderwidth=10, background="white")
    #style.configure("Custom.Treeview.Column", borderwidth=10)


    self.tree = ttk.Treeview(self.search_window, style="Custom.Treeview", show="headings")
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


def search_patient(self, Lnameentry, Fnameentry, DOBentry):
    self.last_name = Lnameentry.get()
    self.first_name = Fnameentry.get()
    self.dob = DOBentry.entry.get()

    db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
    if self.last_name and self.first_name:
        db_connection.cursor.execute(
                'SELECT * FROM patientsinfo WHERE first_name LIKE %s AND last_name LIKE %s', (f"{self.first_name}%", f"{self.last_name}%"))


    elif self.dob and self.last_name:
        db_connection.cursor.execute('SELECT * FROM patientsinfo WHERE Dateofbirth = %s AND last_name LIKE %s', (self.dob, f"{self.last_name}%"))

    elif self.last_name:
        db_connection.cursor.execute(

                'SELECT * FROM patientsinfo WHERE last_name LIKE %s', (f"{self.last_name}%",))
    elif self.dob:
        db_connection.cursor.execute(
                'SELECT * FROM patientsinfo WHERE Dateofbirth=%s', (self.dob,))




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
            self.l_name = selected_row['values'][1]
            self.f_name= selected_row['values'][0]
            #print(self.l_name)
            #print(self.f_name)
            db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')

            db_connection.cursor.execute('SELECT * from patientsinfo WHERE last_name= %s AND first_name=%s', (self.l_name,self.f_name))
            self.result = db_connection.cursor.fetchone()
            if self.result:
                self.dob = self.result['Dateofbirth']

            if self.result:
                self.rx_Profile_patient(self.result, self.l_name,self.f_name, self.dob)
                print(self.dob)
            else:
                print("Noresults")
        else:
            print("noitem")
    self.tree.bind("<Double-Button-1>", on_row_selects)



def rx_Profile_patient(self, result, la_name, fi_name, dob):
    if hasattr(self, "background_frame"):
        self.background_frame.destroy()
    if dob:
        print(dob)
    else:
        print("nodob")
    self.search_window.destroy()
    screen_width = self.winfo_screenwidth()
    screen_height=self.winfo_screenheight()
    self.background_frame = Frame(self.Rx_s_Patient, bg = "blue", width = screen_width, height = screen_height)

    self.background_frame.pack(expand=1, fill="both")




    self.nstyle = ttk.Style()
    self.nstyle.configure("Custom.TNotebook.Tab", background="blue")

    self.notebook = ttk.Notebook(self.background_frame)
    self.notebook.configure(style="Custom.TNotebook")

    self.notebook.pack(expand=1,fill="both")



    tab1 = Frame(self.notebook, bg="black")
    tab2 = Frame(self.notebook, bg="black")
    tab3 = Frame(self.notebook, bg="black")
    tab4 = Frame(self.notebook, bg="black")
    tab5 = Frame(self.notebook, bg="black")
    tab6 = Frame(self.notebook, bg="black")
    tab7 = Frame(self.notebook, bg="black")

    # Pack and unpack the notebook widget to apply the changes to the colors
    self.notebook.pack(expand=1, fill="both")

    self.notebook.add(tab1, text="1. Patient Info")
    self.notebook.add(tab2, text="2. Allergies")
    self.notebook.add(tab3, text="3. Insurance")
    self.notebook.add(tab4, text="4. Presriptions")
    self.notebook.add(tab5, text="5. Transactions")
    self.notebook.add(tab6, text="6. Genomics")
    self.notebook.add(tab7, text="7. Drug Review")

    first_name_label = tb.Label(tab1, text="First Name", font=("Vintage Typewriter", 12))
    first_name_entry = Entry(tab1, bg='white', fg='black', width=25)
    first_name_entry.insert(0,fi_name)

    # place the first name label and entry next to each other
    first_name_label.place(relx=0.01, rely=0.02)
    first_name_entry.place(relx=0.07, rely=0.02)
  
    last_name_label = tb.Label(tab1, text="Last Name", font=("Vintage Typewriter", 12))


    last_name_entry = Entry(tab1, bg='white', fg='black', width=25)
    last_name_entry.insert(0,la_name)
    # place the label and entry above next to each other
    last_name_label.place(relx=0.2, rely=0.02)
    last_name_entry.place(relx=0.27, rely=0.02)

    

    dob_label = tb.Label(tab1, text="Date of Birth", font=("Vintage Typewriter", 12))
    dob_entry = Entry(tab1, bg='white', fg='black', width=25)
    dob_entry.insert(0,dob)
    dob_label.place(relx=0.4, rely=0.02)
    dob_entry.place(relx=0.47, rely=0.02)
    # place the label and entry above next to each other


  


    # Create content for Tab 1
    #label1 = Label(tab1, text=f"First Name: {fname}", font=("Arial", 20))
    #label1.pack(padx=10, pady=10)

    # Create content for Tab 2
    label2 = Label(tab2, text="Content for Tab 2", font=("Arial", 20))
    label2.pack(padx=10, pady=10)

    # Create content for Tab 4, a list of random prescriptions in a treeview that has the columns: medication name, refills, prescriber, instructions
    # Create a treeview widget within tab4
    tree = ttk.Treeview(tab4, style="Custom.Treeview", columns=("medication_name", "refills", "prescriber", "instructions"))
    tree.heading("medication_name", text="Medication Name")
    tree.heading("refills", text="Refills")
    tree.heading("prescriber", text="Prescriber")
    tree.heading("instructions", text="Instructions")
    tree.column("medication_name", width=200)
    tree.column("refills", width=100)
    tree.column("prescriber", width=200)
    tree.column("instructions", width=200)
    # Place the tree 
    tree.pack(expand=1, fill="both")
    # Insert dummy data into the tree
    tree.insert("", "end", values=("Alprazolam 1 MG", 2, "Dr. A", "Take 1 tablet daily"))
    tree.insert("", "end", values=("Clonazepam 2 MG", 1, "Dr. B", "Take 2 tablets daily"))
    tree.insert("", "end", values=("Simvastatin 20 MG", 3, "Dr. C", "Take 3 tablets daily"))
    


    self.tree_view_genetic_style = ttk.Style()
    self.tree_view_genetic_style.configure("Custom.Treeview", background="#3A3A3A", fieldbackground="#3A3A3A", foreground="white")
    self.tree_view_genetic_style.configure("Custom.Treeview", foreground="black", font=("Helvetica", 12))
    self.tree_view_genetic_style.configure("Custom.Treeview", borderwidth=10, background="d6cfbd")

    #TREEVIEW TO HOLD INFO REGARDING GENETIC VARIANT

    self.tree_genetic_variant = ttk.Treeview(tab6, style="Custom.Treeview", show="headings")
    self.tree_genetic_variant["columns"] = ("gene", "genevar",  "disease", "genotype")
    self.tree_genetic_variant.heading("gene", text="Gene")
    self.tree_genetic_variant.heading("genevar", text="Genetic Variant")
    self.tree_genetic_variant.heading("disease", text="Disease")
    self.tree_genetic_variant.heading("genotype", text="Genotype")

    self.tree_genetic_variant.place(x=20,y=50,width=1300, height=400)
    # Insert the value of "CT" in to the tree under Genotype
    self.tree_genetic_variant.insert("", "end", values=("SLCO1B1", "rs414956", "Hypertension", "CT"))


    self.tree_view_geneticinfo_style = ttk.Style()
    self.tree_view_geneticinfo_style.configure("Custom.Treeview", background="#3A3A3A", fieldbackground="#3A3A3A", foreground="white")
    self.tree_view_geneticinfo_style.configure("Custom.Treeview", foreground="white", font=("Helvetica", 12))
    self.tree_view_geneticinfo_style.configure("Custom.Treeview", borderwidth=10, background="#3A3A3A")

    #TREEVIEW HOLDING DRUG CONFLICT DATA
    self.tree_geneticinfo_variant = ttk.Treeview(tab7, style="Custom.Treeview", show="headings")
    self.tree_geneticinfo_variant["columns"] = ("drug_name", "drug_conflicts")
    self.tree_geneticinfo_variant.heading("drug_name", text="Drug Name")
    self.tree_geneticinfo_variant.heading("drug_conflicts", text="Drug Conflict")

    # Make the button above into a tb.button
    vardelete_button = tb.Button(tab7, text="Delete", bootstyle='info', command=lambda: delete_entry_variant(self))
    vardelete_button.place(x=150, y=500)

    self.tree_geneticinfo_variant.place(x=20,y=50,width=1300, height=400)

    db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
    db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
    user_id_result = db_connection.cursor.fetchone()
    user_id = user_id_result['user_id']
    db_connection.cursor.execute(
        'SELECT * FROM final_genetic_info WHERE user_id = %s', (user_id,)
    )
    allinfo = db_connection.cursor.fetchall()
    #print(allinfo)
    if allinfo:
        for parameter in allinfo:
            self.tree_genetic_variant.insert("", "end", values=(parameter['gene'], parameter['genetic_variant'], parameter['disease']))
    else:

        # Handle the case where some values are missing
        print("Some values are missing in the result dictionary.")
    self.result = result

    db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
    db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
    user_id_result = db_connection.cursor.fetchone()
    user_id = user_id_result['user_id']
    query = """
                            SELECT drug_name, GROUP_CONCAT(drug_conflict, ', ') AS drug_conflicts
                            FROM drug_review
                            WHERE user_id = %s
                            GROUP BY drug_name
                            ORDER BY drug_name
                            """
    db_connection.cursor.execute(query, (user_id,))

    drugreviewinfo = db_connection.cursor.fetchall()

    #print(drugreviewinfo)
    if drugreviewinfo:
        
        for row in self.tree_geneticinfo_variant.get_children():
            self.tree_geneticinfo_variant.delete(row)
        for row in drugreviewinfo:
            drug_name = row['drug_name']
            drug_conflicts = row['drug_conflicts']
            # Insert drug name in one row
            self.tree_geneticinfo_variant.insert('', 'end', values=(drug_name, ""))
            # Insert each drug conflict in a separate row below the drug name
            for conflict in drug_conflicts.split(','):
                self.tree_geneticinfo_variant.insert('', 'end', values=("", conflict.strip()))


    else:
        # Handle the case where some values are missing
        print("Some values are missing in the result dictionary.")
        



    #132d5e

    EntryAndAddCanvas = Canvas(tab6, width=1200, height=300, bg='#3A3A3A', highlightthickness=0, relief="raised")
    EntryAndAddCanvas.place(x=20, y=470)

    EntryCanvasWidth = EntryAndAddCanvas.winfo_width()


    GeneEntryText = Canvas(EntryAndAddCanvas, bg='#3A3A3A', width=40, height=20, bd=0, highlightthickness=0, relief='ridge')
    GeneEntryText.place(x=137,y=40)
    GeneEntryText.create_text(20, 10, text="Gene", fill='white', font=('Vintage Typewriter', 12))

    GeneticVariantEntryText = Canvas(EntryAndAddCanvas, bg='#3A3A3A', width=120, height=20, bd=0, highlightthickness=0, relief='ridge')
    GeneticVariantEntryText.place(x=334,y=40)
    GeneticVariantEntryText.create_text(55, 10, text="Genetic Variant", fill='white', font=('Vintage Typewriter', 12))

    DiseaseEntryText = Canvas(EntryAndAddCanvas, bg='#3A3A3A', width=100, height=20, bd=0, highlightthickness=0, relief='ridge')
    DiseaseEntryText.place(x=570,y=40)
    DiseaseEntryText.create_text(50, 10, text="Disease", fill='white', font=('Vintage Typewriter', 12))

    # Create EntrytextCanvas and text in it for the genotype
    GenotypeEntryText = Canvas(EntryAndAddCanvas, bg='#3A3A3A', width=100, height=20, bd=0, highlightthickness=0, relief='ridge')
    GenotypeEntryText.place(x=800, y=40)
    GenotypeEntryText.create_text(50, 10, text="Genotype", fill='white', font=('Vintage Typewriter', 12))

    # Create entrybox for GEnotype and place it above the text canvas
    GenotypeEntry = Entry(EntryAndAddCanvas, bg='white', fg='black', width=25)
    GenotypeEntry.place(x=790, y=10)

    GeneEntry = Entry(EntryAndAddCanvas, bg='white', fg='black', width=25)
    GeneEntry.place(x=60,y=10)

    GeneticVariantEntry = Entry(EntryAndAddCanvas, bg='white', fg='black', width=25)
    GeneticVariantEntry.place(x=300, y=10)

    DiseaseEntry = Entry(EntryAndAddCanvas, bg='white', fg='black', width=25)
    DiseaseEntry.place(x=540,y=10)

    #add_genetic_variant_button = tk.Canvas(EntryAndAddCanvas,bg='#323232',width=100,height=20,bd=0, highlightthickness=0, relief='raised' )
    #add_genetic_variant_button.place(x=20,y=100)
    #add_genetic_variant_button.create_text(50,10,text="Add Information",fill='white', font=('Vintage Typewriter', 12))
    #add_genetic_variant_button.bind("<Button-1>", lambda event, GeneEntry=GeneEntry, GeneticVariantEntry=GeneticVariantEntry, DiseaseEntry=DiseaseEntry, GenotypeEntry=GenotypeEntry: self.save_info(GeneEntry, GeneticVariantEntry, DiseaseEntry,GenotypeEntry, self.l_name, self.f_name))
    # make the button addgeneticvariant into tb.Button
    add_genetic_variant_button = tb.Button(EntryAndAddCanvas, text="Add Information", command=lambda: save_info(self, GeneEntry, GeneticVariantEntry, DiseaseEntry, GenotypeEntry, self.l_name, self.f_name))
    add_genetic_variant_button.place(x=20, y=100)




   # Make deletebutton into a tb.Button
    delete_button = tb.Button(EntryAndAddCanvas, text="Delete", command=lambda: delete_entry(self))
    delete_button.place(x=150, y=100)

    self.notebook.pack(expand=1, fill="both")






def save_info(self, GeneEntry, GeneticVariantEntry, DiseaseEntry, GenotypeEntry, la_name, fi_name):
    Gene = GeneEntry.get()
    GeneticVariant = GeneticVariantEntry.get()
    Disease = DiseaseEntry.get()
    Genotype = GenotypeEntry.get()



    url = f'https://api.pharmgkb.org/v1/data/variantAnnotation?location.genes.symbol={Gene}&location.fingerprint={GeneticVariant}'
    headers = {'accept': 'application/json'}

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json().get("data", [])

        # Extracted outside the loop to ensure drug review insertion for each drug name
        drug_reviews = []

        for item in data:
            # Extract the "score" field from the current item
            score = item.get("score", 0)

            # Check if the score is above or equal to 0
            if score >= 3:
                # Extract the "sentence" field from the current item
                sentence = item.get("sentence", "")
                #print("Sentence:", sentence)

                # Extract the related chemicals for the current item
                related_chemicals = item.get("relatedChemicals", [])

                # Extract chemical names for the current item
                drug_names = [chemical.get("name") for chemical in related_chemicals]
                #print("Drug Names:", drug_names)

                # Append drug names and sentences to the drug_reviews list
                drug_reviews.extend([(drug_name, sentence) for drug_name in drug_names])

        # Continue with the rest of your function logic

        # Fetch user_id based on last_name and first_name
        db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
        db_connection.cursor.execute('SELECT user_id FROM patientsinfo WHERE last_name = %s AND first_name = %s', (la_name, fi_name))
        result = db_connection.cursor.fetchone()

        if result:
            user_id = result['user_id']

            # Insert data into final_genetic_info table
            sql_insert_genetic_info = 'INSERT INTO final_genetic_info (user_id, gene, genetic_variant, disease) VALUES (%s, %s, %s, %s)'
            values_genetic_info = (user_id, Gene, GeneticVariant, Disease, Genotype)

            db_connection.cursor.execute(sql_insert_genetic_info, values_genetic_info)
            db_connection.connection.commit()

            # Insert data into drug_review table for each drug_name and associated sentence
            for drug_name, drug_sentence in drug_reviews:
                sql_insert_drug_review = 'INSERT INTO drug_review (user_id, drug_name, drug_conflict) VALUES (%s, %s, %s)'
                values_drug_review = (user_id, drug_name, drug_sentence)

                db_connection.cursor.execute(sql_insert_drug_review, values_drug_review)
                db_connection.connection.commit()

        else:
            print("User not found.")

    else:
        print(f"Request failed with status code: {response.status_code}")



# create a a delete entry function
def delete_entry(self):
    selected_item = self.tree_genetic_variant.selection()

    if selected_item:
            selected_row = self.tree_genetic_variant.item(selected_item)

            GENE = selected_row['values'][0]
            print(GENE)

            db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
            db_connection.cursor.execute("SELECT genetic_info_id FROM final_genetic_info WHERE gene = %s", (GENE,))
            genetic_info_id = db_connection.cursor.fetchone()

            print(genetic_info_id)

            # Corrected DELETE query for final_genetic_info table
            if genetic_info_id:
                db_connection.cursor.execute('DELETE from final_genetic_info WHERE genetic_info_id= %s', (genetic_info_id['genetic_info_id'],))
                db_connection.connection.commit()

                self.tree_genetic_variant.delete(selected_item)
    else:
        print("No item selected.")

def delete_entry_variant(self):
    selected_item = self.tree_geneticinfo_variant.selection()

    if selected_item:
        selected_row = self.tree_geneticinfo_variant.item(selected_item)
        drug_name = selected_row['values'][0]

        db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')
        db_connection.cursor.execute("SELECT review_id FROM drug_review WHERE drug_name = %s", (drug_name,))
        review_id_result = db_connection.cursor.fetchone()


        if review_id_result:
            review_id = review_id_result['review_id']
            db_connection.cursor.execute('DELETE FROM drug_review WHERE review_id = %s', (review_id,))
            db_connection.connection.commit()
            self.tree_geneticinfo_variant.delete(selected_item)
        else:
            print("No review ID found for selected drug.")
    else:
        print("No item selected.")

#Check