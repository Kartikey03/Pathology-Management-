#PATHLOGY LAB MANAGEMENT SYSTEM
import webbrowser #importing webbrowser module
from datetime import date #importing date module
from tkinter import *  #importing all modules from tkinter library
from tkinter import messagebox  #importing messagebox module from tkinter
from PIL import Image, ImageTk, ImageFilter #importing all modules from PIL library
import mysql.connector #importing mysql connector module
con=mysql.connector.connect(host ='localhost', user ='root', password ='12345') #connection object
cur=con.cursor() #cursor object

pbill1 = "Payment Done"
bg_color='#FFFFFF'
root=Tk()
root.title('Pathology Management System')
root.iconbitmap('D:/lab.ico')


image=Image.open('D:/bg.png').convert('RGB')

# Get the window dimensions
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Resize the image to fit the window
image = image.resize((window_width, window_height))

blur=image.filter(ImageFilter.BLUR)
bgimage= ImageTk.PhotoImage(blur)
bg_label = Label(root, image=bgimage)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#creating database pathlab
cur.execute("create database if not exists pathlab")

#opening database pathlab
cur.execute("use pathlab")

#creating table pat
cur.execute('''create table if not exists pat
(id integer primary key,
name varchar(30),
age integer,
gender varchar(50),
blood varchar(20),
address varchar(100),
bill varchar(100)) ''')



#exit pathlabs
def close1():
    root.destroy()

    
#about us
def about():
    ab=Toplevel()
    ab.title('About us')
    ab.iconbitmap('D:/info.ico')
    ab.configure(bg=bg_color) 
    ab.geometry('1200x600')

    # Create a canvas
    canvas = Canvas(ab)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a scrollbar
    scrollbar = Scrollbar(ab, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to contain the widgets
    frame = Frame(canvas)

    info_label=Label(frame, text="""Project Description:

The Pathology Management System is a sophisticated and user-friendly Python-based program designed to streamline the management of patient records, billing, and receipts. 
With its intuitive graphical interface, this system simplifies the complexities of pathology management for both patients and administrators.
Patients can effortlessly add their records, conveniently pay bills through a dedicated bill window, and generate printable bill receipts for reference. 
The system puts patients in control of their healthcare journey, providing a seamless and efficient experience.
Administrators have enhanced authority to manage the system effectively. 
They can add, update, and delete patient details, ensuring accurate and up-to-date records. 
Administrators can also generate bill receipts for patients, enabling seamless financial transactions. 
The system empowers administrators with comprehensive tools to handle diverse administrative tasks.

Future Enhancements:

1. Integration with Online Payment Gateways: 
Enhancing the billing module by integrating popular online payment gateways would offer patients more payment options, 
ensuring secure and convenient transactions.

2. Electronic Medical Records (EMR) Integration: 
Integrating the system with electronic medical records systems would enable the seamless exchange of patient data, 
enhancing the accessibility and accuracy of medical records.

3. Reporting and Analytics: 
Implementing robust reporting and analytics capabilities would empower administrators to generate valuable insights from system data, 
facilitating data-driven decision-making and performance tracking.

4. Mobile Application Development: 
Developing a mobile application would extend accessibility, allowing patients and administrators to access the system on-the-go, 
improving convenience and user experience.

5. Enhanced Security Measures: 
Strengthening the system's security measures through data encryption, user authentication, 
and regular security updates would safeguard patient information and ensure compliance with privacy regulations.

6. Integration with Laboratory Equipment: 
Integrating the system with laboratory equipment would automate data capture, 
minimizing errors and enhancing efficiency in the laboratory workflow.

7. Multi-Language Support: 
Adding multi-language support would cater to diverse users, ensuring inclusivity and improving user satisfaction.

These future enhancements will further optimize the Pathology Management System, enhancing its capabilities, security, and user experience. 
The project aims to provide a comprehensive and efficient solution for streamlined record-keeping, billing management, and overall pathology administration.""",
                     font=('Calibri',12), bg=bg_color, fg='black')
    info_label.pack()

    # Place the frame inside the canvas
    canvas.create_window(0, 0, anchor=NW, window=frame)

    # Update the scroll region
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    
#update query
def edit():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()
    
    pid = pu_id.get()
    pname = pu_name.get()
    page = pu_age.get()
    pgender = pu_gender.get()
    pblood = pu_blood.get()
    paddress = pu_address.get()
    pid = pu_id.get()
          
    if update_box.get() == pid:
        cur.execute("update pat set id=%s, name=%s, age=%s, gender=%s, blood=%s, address=%s where id = %s",
                    (pid, pname, page, pgender, pblood, paddress, pid))
        messagebox.showinfo('Updated', 'Record Successfully Updated.')

    update_box.delete(0, END)
    
    con.commit()
    con.close()

    editor.destroy()
    edit1.destroy()   
#entering details in entry boxes to update records 
def update2():
    if update_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')

    else:
        global editor
        editor=Toplevel()
        editor.title('Update Patient Data')
        editor.iconbitmap('D:/lab.ico')
        editor.geometry("750x450")
        editor.configure(bg=bg_color)

        con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where id = " + update_box.get())
        data = cur.fetchall()

        #create global variables for text box
        global pu_id
        global pu_name
        global pu_age
        global pu_gender
        global pu_blood
        global pu_address
        
        #making text boxes
        pu_id=Entry(editor, width=30, relief=GROOVE)
        pu_id.grid(row=1, column=1, padx=60, pady=(10,0))

        pu_name=Entry(editor, width=30, relief=GROOVE)
        pu_name.grid(row=2, column=1)

        pu_age=Entry(editor, width=30, relief=GROOVE)
        pu_age.grid(row=3, column=1)

        pu_gender=Entry(editor, width=30, relief=GROOVE)
        pu_gender.grid(row=4, column=1)

        pu_blood=Entry(editor, width=30, relief=GROOVE)
        pu_blood.grid(row=5, column=1)

        pu_address=Entry(editor, width=30, relief=GROOVE)
        pu_address.grid(row=6, column=1)

        #creating Labels
        wel_label=Label(editor, text="NOW, YOU CAN UPDATE ANYTHING HERE", font=('Calibri',15), bg=bg_color, fg='black')
        wel_label.grid(row=0, column=1, pady=50)
        
        id_label=Label(editor, text="Patient Id :", font=('Calibri',15), bg=bg_color, fg='black')
        id_label.grid(row=1, column=0, pady=(10,0))

        name_label=Label(editor, text="Patient Name :", font=('Calibri',15), bg=bg_color, fg='black')
        name_label.grid(row=2, column=0)

        age_label=Label(editor, text="Patient Age :", font=('Calibri',15), bg=bg_color, fg='black')
        age_label.grid(row=3, column=0)

        gend_label=Label(editor, text="Patient Gender :", font=('Calibri',15), bg=bg_color, fg='black')
        gend_label.grid(row=4, column=0)

        blood_label=Label(editor, text="Patient's Blood Group :", font=('Calibri',15), bg=bg_color, fg='black')
        blood_label.grid(row=5, column=0)

        add_label=Label(editor, text="Patient Address :", font=('Calibri',15), bg=bg_color, fg='black')
        add_label.grid(row=6, column=0)
       
        #looping through the results
        for rec in data:
            pu_id.insert(0, rec[0])
            pu_name.insert(0, rec[1])
            pu_age.insert(0, rec[2])
            pu_gender.insert(0, rec[3])
            pu_blood.insert(0, rec[4])
            pu_address.insert(0, rec[5])
           
        #create save button
        b9= Button(editor, text="Save Above Record", relief=GROOVE, bg=bg_color, fg='black', command=edit)
        b9.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

        con.commit()
        con.close()        
#making window to input the id which user want to update     
def update1():
    global edit1
    edit1=Toplevel()
    edit1.title('Enter ID')
    edit1.iconbitmap('D:/lab.ico')
    edit1.geometry("500x120")
    edit1.configure(bg=bg_color)

    global update_box
    update_box=Entry(edit1, width=30, relief=GROOVE)
    update_box.grid(row=10, column=1, pady=(20,0))
        
    update_label=Label(edit1, text="Enter Patient Id to Update the Record :", font=('Calibri',10), bg=bg_color, fg='black')
    update_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    #create delete query button
    b4= Button(edit1, text="Update Record", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=update2)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

   
#delete query
def delete2():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()
    
    if delete_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')
        
    else:
        msgbox2 = messagebox.askquestion('Confirm Deletion ?', 'Delete Record. Are you sure You want to Delete Record?')
        if msgbox2 == 'yes':
            cur.execute("delete from pat where id = " + delete_box.get())
            messagebox.showinfo('Deleted', 'Record successfully Deleted.')

        else:
            messagebox.showinfo('Canceled', 'Record Deletion Canceled.')
        
    delete_box.delete(0, END)
    del1.destroy()
    con.commit()
    con.close()
#making window to input the id which user want to delete
def delete1():
    global del1
    del1=Toplevel()
    del1.title('Enter ID')
    del1.iconbitmap('D:/lab.ico')
    del1.geometry("500x120")
    del1.configure(bg=bg_color)

    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    global delete_box
    delete_box=Entry(del1, width=30, relief=GROOVE)
    delete_box.grid(row=10, column=1, pady=(20,0))
        
    delete_label=Label(del1, text="Enter Patient Id to Delete the Record :", font=('Calibri',10), bg=bg_color, fg='black')
    delete_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    #create delete query button
    b4= Button(del1, text="Delete Record", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=delete2)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

  
#showing all records
def show_all():
    global show
    show=Toplevel()
    show.title('Patient Data')
    show.iconbitmap('D:/lab.ico')
    show.configure(bg=bg_color)

    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    cur.execute("select * from pat")
    data = cur.fetchall()

    print_rec1=''    
    for rec1 in data:  
        print_rec1 += str(rec1[0]) +  "\n"

    print_rec2=''    
    for rec2 in data:  
        print_rec2 += str(rec2[1]) +  "\n"

    heading_id=Label(show, text="ID", font=('Calibri',13, "bold"), bg=bg_color, fg='black')
    heading_id.grid(row=0, column=0, padx=(20,10), pady=(30,10))

    heading_name=Label(show, text="NAME", font=('Calibri',13, "bold"), bg=bg_color, fg='black')
    heading_name.grid(row=0, column=1, padx=(100,10), pady=(30,10))

    data_label1=Label(show, text=print_rec1, font=('Calibri',10, "bold"), bg=bg_color, fg='black')
    data_label1.grid(row=1, column=0)

    data_label2=Label(show, text=print_rec2, font=('Calibri',10, "bold"), bg=bg_color, fg='black')
    data_label2.grid(row=1, column=1, padx=(100,10))

    con.close()
    

#closing windows of showing ne data query
def close3():
    show2.destroy()

def enter_close():
    enter.destroy()
    
def close2():
    show1.destroy()
    show2.destroy()


def entry_1():
    if enter_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')
    else:
        con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where id= " + enter_box.get())
        data = cur.fetchall()

        record1 = ''
        for rec1 in data:
            record1 += str(rec1[0])
            
        record2 = ''
        for rec2 in data:
            record2 += str(rec2[1])
            
        record3 = ''
        for rec3 in data:
            record3 += str(rec3[2])
            
        record4 = ''
        for rec4 in data:
            record4 += str(rec4[3])
            
        record5 = ''
        for rec5 in data:
            record5 += str(rec5[4])
            
        record6 = ''
        for rec6 in data:
            record6 += str(rec6[5])

        record7 = ''
        for rec7 in data:
            record7 += str(rec7[6])

        class Patient:
            def __init__(self, name, age, blood_group, status, tests):
                self.name = name
                self.age = age
                self.blood_group = blood_group
                self.status = status
                self.tests = tests
                


        def generate_receipt(patient):
            receipt_content = f"Name: {patient.name}\nAge: {patient.age}\nBlood Group: {patient.blood_group}\nBill Status: {patient.status}\nDate: {date.today().strftime('%d/%m/%Y')}\n\n"
            receipt_content += "Test Name\t\tPrice\n"
            receipt_content += "--------------------------------\n"

            total_amount = 0
            for test_name, test_price in patient.tests.items():
                receipt_content += f"{test_name}\t\t{test_price}\n"
                total_amount += test_price

            receipt_content += "--------------------------------\n"
            receipt_content += "Total Amount:\t\t{total_amount}\n"

            return receipt_content


        def print_receipt(patient):
            receipt_content = generate_receipt(patient)
            
            # Create an HTML file with the receipt content
            html_content = f"<pre>{receipt_content}</pre>"
            with open("receipt.html", "w") as file:
                file.write(html_content)

            # Open the HTML file in a web browser
            webbrowser.open("receipt.html")


        def show_receipt(patient):
            receipt_content = generate_receipt(patient)

            window = Toplevel()
            window.title("Bill Receipt")

            receipt_text = Text(window, height=10, width=40, font=("Courier New", 12), bd=0, bg="#F0F0F0", padx=10, pady=10)
            receipt_text.insert(END, receipt_content)
            receipt_text.configure(state="disabled")
            receipt_text.pack()

            total_label = Label(window, text=f"Total Amount: {sum(patient.tests.values()):.2f}", font=("Arial", 12, "bold"))
            total_label.pack(pady=10)

            print_button = Button(window, text="Print", command=lambda: print_receipt(patient), font=("Arial", 12, "bold"))
            print_button.pack(pady=10)

        # Example usage
        patient = Patient(record2, record3, record5, record7, {"Culture Urine Test": 850.00, "Allergy Gluten": 6600.00})
        show_receipt(patient)


def show_one1():
    if show_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')
        
    else:
        global show1
        show1=Toplevel()
        show1.title('Patient Record')
        show1.iconbitmap('D:/lab.ico')
        show1.configure(bg=bg_color)
        
        con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where id= " + show_box.get())
        data = cur.fetchall()

        #creating Labels
        wel_label=Label(show1, text="RECORD OF THE PATIENT", font=('Calibri',15), bg=bg_color, fg='black')
        wel_label.grid(row=0, column=1, padx=(0,100), pady=(35,30))
            
        id_label=Label(show1, text="Patient Id :", font=('Calibri',15), bg=bg_color, fg='black')
        id_label.grid(row=1, column=0, padx=(50,0))

        name_label=Label(show1, text="Patient Name :", font=('Calibri',15), bg=bg_color, fg='black')
        name_label.grid(row=2, column=0, padx=(50,0))

        age_label=Label(show1, text="Patient Age :", font=('Calibri',15), bg=bg_color, fg='black')
        age_label.grid(row=3, column=0, padx=(50,0))

        gend_label=Label(show1, text="Patient Gender :", font=('Calibri',15), bg=bg_color, fg='black')
        gend_label.grid(row=4, column=0, padx=(50,0))

        blood_label=Label(show1, text="Patient's Blood Group :", font=('Calibri',15), bg=bg_color, fg='black')
        blood_label.grid(row=5, column=0, padx=(50,0))

        add_label=Label(show1, text="Patient Address :", font=('Calibri',15), bg=bg_color, fg='black')
        add_label.grid(row=6, column=0, padx=(50,0))

        bill_label=Label(show1, text="Bill Status :", font=('Calibri',15), bg=bg_color, fg='black')
        bill_label.grid(row=7, column=0, padx=(50,0))
        
        record1 = ''
        for rec1 in data:
            record1 += str(rec1[0]) + "\n"
            
        record2 = ''
        for rec2 in data:
            record2 += str(rec2[1]) + "\n"
            
        record3 = ''
        for rec3 in data:
            record3 += str(rec3[2]) + "\n"
            
        record4 = ''
        for rec4 in data:
            record4 += str(rec4[3]) + "\n"
            
        record5 = ''
        for rec5 in data:
            record5 += str(rec5[4]) + "\n"
            
        record6 = ''
        for rec6 in data:
            record6 += str(rec6[5]) + "\n"

        record7 = ''
        for rec7 in data:
            record7 += str(rec7[6]) + "\n"

        id_label1=Label(show1, text=record1, font=('Calibri',15), bg=bg_color, fg='black')
        id_label1.grid(row=1, column=1, padx=50, pady=(20,0))

        id_label2=Label(show1, text=record2, font=('Calibri',15), bg=bg_color, fg='black')
        id_label2.grid(row=2, column=1, padx=50, pady=(20,0))

        id_label3=Label(show1, text=record3, font=('Calibri',15), bg=bg_color, fg='black')
        id_label3.grid(row=3, column=1, padx=50, pady=(20,0))

        id_label4=Label(show1, text=record4, font=('Calibri',15), bg=bg_color, fg='black')
        id_label4.grid(row=4, column=1, padx=50, pady=(20,0) )

        id_label5=Label(show1, text=record5, font=('Calibri',15), bg=bg_color, fg='black')
        id_label5.grid(row=5, column=1, padx=50, pady=(20,0) )

        id_label6=Label(show1, text=record6, font=('Calibri',15), bg=bg_color, fg='black')
        id_label6.grid(row=6, column=1, padx=50, pady=(20,0))

        id_label7=Label(show1, text=record7, font=('Calibri',15), bg=bg_color, fg='black')
        id_label7.grid(row=7, column=1, padx=50, pady=(20,0))
        
        #create close button
        b10= Button(show1, text="Close Record", relief=GROOVE, bg=bg_color, fg='black', command=close2)
        b10.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

        show_box.delete(0, END)        
        con.close()           
#making window to input the id which user want to see
def show_one2():
    global show2
    show2=Toplevel()
    show2.title('Enter ID')
    show2.iconbitmap('D:/lab.ico')
    show2.geometry("500x140")
    show2.configure(bg=bg_color)

    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    global show_box
    show_box=Entry(show2, width=30, relief=GROOVE)
    show_box.grid(row=10, column=1, pady=(20,0))
        
    show_label=Label(show2, text="Enter Patient Id to display that Record :", font=('Calibri',10), bg=bg_color, fg='black')
    show_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    #create show_one query button
    b4= Button(show2, text="Show Record", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=show_one1)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

    #create close window button
    bu= Button(show2, text="Close Window", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=close3)
    bu.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

    con.close()


#submit function for people who have not done the payment
def submit_pn():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    #getting the data from the database 
    pid = pa_id.get()
    pname = pa_name.get()
    page = pa_age.get()
    pgender = pa_gender.get()
    pblood = pa_blood.get()
    paddress = pa_address.get()

    #insert the values in the table
    cur.execute("insert into pat (id, name, age, gender, blood, address, bill) values(%s, %s, %s, %s, %s, %s,%s)",
                (pid, pname, page, pgender, pblood, paddress, str(sum(bill_list)) +'/- left for Payment'))
    
    #clearing the text boxes
    pa_id.delete(0, END)
    pa_name.delete(0, END)
    pa_age.delete(0, END)
    pa_gender.delete(0, END)
    pa_blood.delete(0, END)
    pa_address.delete(0, END)

    con.commit()
    con.close()
#submit function for people who have done the payment
def submit_pd():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    #getting the data from the database 
    pid = pa_id.get()
    pname = pa_name.get()
    page = pa_age.get()
    pgender = pa_gender.get()
    pblood = pa_blood.get()
    paddress = pa_address.get()
    
    #insert the values in the table
    cur.execute("insert into pat (id, name, age, gender, blood, address, bill) values(%s, %s, %s, %s, %s, %s,%s)",
                (pid, pname, page, pgender, pblood, paddress, pbill1))
    
    #clearing the text boxes
    pa_id.delete(0, END)
    pa_name.delete(0, END)
    pa_age.delete(0, END)
    pa_gender.delete(0, END)
    pa_blood.delete(0, END)
    pa_address.delete(0, END)

    con.commit()
    con.close()


#payment messages for google pay   
def billw4_3():
    if gpay_box.get() == '':
            messagebox.showerror('Error !', 'Mobile No. not Provided')
            
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'Pin not Provided')
            
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")

    b3.destroy()
    bw1.destroy()
    bw2.destroy()
    bw3.destroy()
    
#payment messages for credit card
def billw4_2():
    if gpay_box.get() == '':
            messagebox.showerror('Error !', 'Card No. not Provided')
            
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'Pin not Provided')
            
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")

    b2.destroy()
    bw1.destroy()
    bw2.destroy()
    bw3.destroy()
#payment messages for debit card
def billw4_1():
    if gpay_box.get() == '':
            messagebox.showerror('Error !', 'Card No. not Provided')
            
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'Pin not Provided')
            
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")

    b1.destroy()
    bw1.destroy()
    bw2.destroy()
    bw3.destroy()
#asking for debit card details
def billw4():
    if var.get()==1:
        global b1
        b1=Toplevel()
        b1.title('Payments')
        b1.iconbitmap('D:/lab.ico')
        b1.configure(bg=bg_color)

        global gpay_box
        global gpay_box1
        
        gpay_box=Entry(b1, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(b1, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(b1, text="Please Enter Your Debit Card Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(b1, text="Please Enter Your 4-digit ATM pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        nb=Button(b1, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=billw4_1)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#asking for credit card details
    if var.get()==2:
        global b2
        b2=Toplevel()
        b2.title('Payments')
        b2.iconbitmap('D:/lab.ico')
        b2.configure(bg=bg_color)

        gpay_box=Entry(b2, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(b2, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(b2, text="Please Enter Your Credit Card Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(b2, text="Please Enter Your Credit Card Pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        nb=Button(b2, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=billw4_2)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#asking for google pay details
    if var.get()==3:
        global b3
        b3=Toplevel()
        b3.title('Payments')
        b3.iconbitmap('D:/lab.ico')
        b3.configure(bg=bg_color)

        gpay_box=Entry(b3, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(b3, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(b3, text="Please Enter Your Mobile Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(b3, text="Please Enter Your 4-digit UPI pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        nb=Button(b3, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=billw4_3)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#payment message for cash payment
    if var.get()==4:
        messagebox.showinfo('Cash Payment', '''
You Can Now Pay your Bill on our reception via Cash
        And Please take your report Tomorrow.
                          Thank You''')
        bw1.destroy()
        bw2.destroy()
        bw3.destroy()

#window for selecting mode of payment  
def billw3():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()
    
    cur.execute("Update pat set bill =" + "'Payment Done'" + " where id =" + bill_box.get())
    
    global bw3
    bw3=Toplevel()
    bw3.title('Payments')
    bw3.iconbitmap('D:/lab.ico')
    bw3.configure(bg=bg_color)
    
    global var
    var=IntVar()
    Rb=Radiobutton(bw3, text='Debit Card', variable=var, value=1, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=1, column=0, padx=(10,0), pady=10)

    Rb=Radiobutton(bw3, text='Credit Card', variable=var, value=2, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=2, column=0, padx=(10,0), pady=10)

    Rb=Radiobutton(bw3, text='Google Pay', variable=var, value=3, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=1, column=2, pady=10)

    Rb=Radiobutton(bw3, text='Cash', variable=var, value=4, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=2, column=2, pady=10)

    mode=Label(bw3, text="Please Select the mode of Payment", font=('Calibri',15, "bold"), bg=bg_color, fg='black')
    mode.grid(row=0, column=1, padx=10, pady=10)

    nextb=Button(bw3, text='Next', relief=GROOVE, bg=bg_color, fg='black', command=billw4)
    nextb.grid(row=5, column=1, padx=10, pady=10, ipadx=100)

    con.commit()
    con.close()
#window for showing amount of bill left
def billw2():
    if bill_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id Not Provided !')
        bw1.destroy()
    else:
        con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where id =" + bill_box.get())
        a= cur.fetchall()
        
        record7 = ''
        for rec7 in a:
            record7 += str(rec7[6])
            
        if record7 == pbill1:
            messagebox.showinfo('Payment Done', 'Payment has been Done with this Id.')
            bw1.destroy()
            
        else:
            global bw2
            bw2=Toplevel()
            bw2.title('Enter Id')
            bw2.iconbitmap('D:/lab.ico')
            bw2.geometry("500x120")
            bw2.configure(bg=bg_color)

            l=Label(bw2, text ='Amount to be Paid:', font=('Calibri',14), bg=bg_color, fg='black')
            l.grid(row=35, column=0, padx=(27,5), pady=(25,0))

            l=Label(bw2, text = record7, font=('Calibri',14) ,bg=bg_color, fg='black')
            l.grid(row=35, column=1, pady=(20,0))

            b= Button(bw2, text="Pay", font=('Calibri',10), relief=GROOVE,  bg=bg_color, fg='black', command=billw3)
            b.grid(row=40, column=1, pady=2, padx=20, ipadx=100)
#making window to input the id for which user want to pay the bill
def billw1():
    global bw1
    bw1=Toplevel()
    bw1.title('Enter Id')
    bw1.iconbitmap('D:/lab.ico')
    bw1.geometry("500x120")
    bw1.configure(bg=bg_color)
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    global bill_box
    bill_box=Entry(bw1, width=30, relief=GROOVE)
    bill_box.grid(row=10, column=1, pady=(20,0))
        
    bill_label=Label(bw1, text="Enter Patient Id to Pay Bill :", font=('Calibri',10), bg=bg_color, fg='black')
    bill_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    b4= Button(bw1, text="Open Bill Summary", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=billw2)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)


#function to pay bill later          
def leave():
    submit_pn()
    add.destroy() 
    bill.destroy()
    test.destroy()


#asking details for all mode of payments    
def pay():
#asking details for debit card
    if var.get()==1:
        global debit1
        debit1=Toplevel()
        debit1.title('Payments')
        debit1.iconbitmap('D:/lab.ico')
        debit1.configure(bg=bg_color)

        global gpay_box
        global gpay_box1
        
        gpay_box=Entry(debit1, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(debit1, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(debit1, text="Please Enter Your Debit Card Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(debit1, text="Please Enter Your 4-digit ATM pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        gpay_label2=Label(debit1, text="Amount to be Paid :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label2.grid(row=2, column=0, padx=(27,10), pady=(20,0))

        gpay_label3=Label(debit1, text=str(sum(bill_list)) + '/-', font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label3.grid(row=2, column=1, padx=(27,10), pady=(20,0))

        nb=Button(debit1, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=pin1)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#asking details for credit card
    if var.get()==2:
        global debit2
        debit2=Toplevel()
        debit2.title('Payments')
        debit2.iconbitmap('D:/lab.ico')
        debit2.configure(bg=bg_color)

        gpay_box=Entry(debit2, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(debit2, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(debit2, text="Please Enter Your Credit Card Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(debit2, text="Please Enter Your Credit Card Pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        gpay_label2=Label(debit2, text="Amount to be Paid :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label2.grid(row=2, column=0, padx=(27,10), pady=(20,0))

        gpay_label3=Label(debit2, text=str(sum(bill_list)) + '/-', font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label3.grid(row=2, column=1, padx=(27,10), pady=(20,0))

        nb=Button(debit2, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=pin2)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#asking details for google pay
    if var.get()==3:
        global debit3
        debit3=Toplevel()
        debit3.title('Payments')
        debit3.iconbitmap('D:/lab.ico')
        debit3.configure(bg=bg_color)

        gpay_box=Entry(debit3, width=30, relief=GROOVE)
        gpay_box.grid(row=0, column=1, padx=(27,10), pady=(20,0))

        gpay_box1=Entry(debit3, width=30, relief=GROOVE)
        gpay_box1.grid(row=1, column=1, padx=(27,10), pady=(20,0))

        gpay_label=Label(debit3, text="Please Enter Your Mobile Number :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label.grid(row=0, column=0, padx=(27,10), pady=(20,0))

        gpay_label1=Label(debit3, text="Please Enter Your 4-digit UPI pin :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label1.grid(row=1, column=0, padx=(27,10), pady=(20,0))

        gpay_label2=Label(debit3, text="Amount to be Paid :", font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label2.grid(row=2, column=0, padx=(27,10), pady=(20,0))

        gpay_label3=Label(debit3, text=str(sum(bill_list)) + '/-', font=('Calibri',12), bg=bg_color, fg='black')
        gpay_label3.grid(row=2, column=1, padx=(27,10), pady=(20,0))

        nb=Button(debit3, text='Pay', relief=GROOVE, bg=bg_color, fg='black', command=pin3)
        nb.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=100)
#payment message for cash payment
    if var.get()==4:
        messagebox.showinfo('Cash Payment', '''
You Can Now Pay your Bill on our reception via Cash
        And Please take your report Tomorrow.
                          Thank You''')
        payment.destroy()
        bill.destroy()
        test.destroy()
#payment messages for debit card        
def pin1():
    if gpay_box.get() == '':
            messagebox.showerror('Error !', 'Card No. not Provided')
            
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'Pin not Provided')
            
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")
        debit1.destroy()
        payment.destroy()
        test.destroy()
        bill.destroy()
        add.destroy()
#payment messages for credit card     
def pin2():
    if gpay_box.get() == '':
        messagebox.showerror('Error !', 'Card No. not Provided')
        
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'Pin not Provided')
        
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")
        debit2.destroy()
        payment.destroy()
        add.destroy()
        test.destroy()
        bill.destroy()
#payment messages for google pay        
def pin3():    
    if gpay_box.get() == '':
            messagebox.showerror('Error !', 'Mobile Number not Provided')
            
    elif gpay_box1.get() == '':
        messagebox.showerror('Error !', 'UPI pin not Provided')
            
    else:
        messagebox.showinfo('Payment Over', """Payment Successfull. You can Take Your Report Tomorrow.
                                        Thank You""")
        debit3.destroy()
        payment.destroy()
        add.destroy()
        test.destroy()
        bill.destroy()
#window to select mode of payment
def total():
    global payment
    payment=Toplevel()
    payment.title('Payments')
    payment.iconbitmap('D:/lab.ico')
    payment.configure(bg=bg_color)
    
    global var
    var=IntVar()
    Rb=Radiobutton(payment, text='Debit Card', variable=var, value=1, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=1, column=0, padx=(10,0), pady=10)

    Rb=Radiobutton(payment, text='Credit Card', variable=var, value=2, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=2, column=0, padx=(10,0), pady=10)

    Rb=Radiobutton(payment, text='Google Pay', variable=var, value=3, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=1, column=2, pady=10)

    Rb=Radiobutton(payment, text='Cash', variable=var, value=4, font=('Calibri',12, "bold"), bg=bg_color, fg='black')
    Rb.grid(row=2, column=2, pady=10)

    mode=Label(payment, text="Please Select the mode of Payment", font=('Calibri',15, "bold"), bg=bg_color, fg='black')
    mode.grid(row=0, column=1, padx=10, pady=10)

    nextb=Button(payment, text='Next', relief=GROOVE, bg=bg_color, fg='black', command=pay)
    nextb.grid(row=5, column=1, padx=10, pady=10, ipadx=100)

    submit_pd()
#showing bill summary   
def bills():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    global bill_list
    global bill
    bill_list=[]
    bill=Toplevel()
    bill.title("Patient's Bill")
    bill.iconbitmap('D:/lab.ico')
    bill.configure(bg=bg_color)

    global C1var
    global C2var
    global C3var
    global C4var
    global C5var
    global C6var
    global C7var
    global C8var
    global C9var
    global C10var
    global C11var
    global C12var
    global C13var
    global C14var
    global C15var
    global C16var
    global C17var
    global C18var
    global C19var
    global C20var
    global C21var
    global C22var
    global C23var
    global C24var
    global C25var
    global C26var
    global C27var
    global C28var
    global C29var
    global C30var

    C1var=var1.get()
    C2var=var2.get()
    C3var=var3.get()
    C4var=var4.get()
    C5var=var5.get()
    C6var=var6.get()
    C7var=var7.get()
    C8var=var8.get()
    C9var=var9.get()
    C10var=var10.get()
    C11var=var11.get()
    C12var=var12.get()
    C13var=var13.get()
    C14var=var14.get()
    C15var=var15.get()
    C16var=var16.get()
    C17var=var17.get()
    C18var=var18.get()
    C19var=var19.get()
    C20var=var20.get()
    C21var=var21.get()
    C22var=var22.get()
    C23var=var23.get()
    C24var=var24.get()
    C25var=var25.get()
    C26var=var26.get()
    C27var=var27.get()
    C28var=var28.get()
    C29var=var29.get()
    C30var=var30.get()

    l0=Label(bill, text ="PATIENTS' BILL SUMMARY", font=('Calibri',15), bg=bg_color, fg='black')
    l0.grid(row=0, column=1, padx=10, pady=10)

    heading_id=Label(bill, text="TEST NAME", font=('Calibri',13), bg=bg_color, fg='black')
    heading_id.grid(row=1, column=0)

    heading_name=Label(bill, text="TEST PRICE (INR)", font=('Calibri',13), bg=bg_color, fg='black')
    heading_name.grid(row=1, column=2)

    if C1var == 1:
        l=Label(bill, text =c1.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=3, column=0)

        l=Label(bill, text =a1, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=3, column=2)

        bill_list.append(int(a1))

    if C2var == 1:
        l=Label(bill, text =c2.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=4, column=0)

        l=Label(bill, text =a2, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=4, column=2)

        bill_list.append(int(a2))

    if C3var == 1:
        l=Label(bill, text =c3.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=5, column=0)

        l=Label(bill, text =a3, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=5, column=2)

        bill_list.append(int(a3))

    if C4var == 1:
        l=Label(bill, text =c4.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=6, column=0)

        l=Label(bill, text =a4, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=6, column=2)

        bill_list.append(int(a4))

    if C5var == 1:
        l=Label(bill, text =c5.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=7, column=0)

        l=Label(bill, text =a5, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=7, column=2)

        bill_list.append(int(a5))

    if C6var == 1:
        l=Label(bill, text =c6.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=8, column=0)

        l=Label(bill, text =a6, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=8, column=2)

        bill_list.append(int(a6))

    if C7var == 1:
        l=Label(bill, text =c7.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=9, column=0)

        l=Label(bill, text =a7, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=9, column=2)

        bill_list.append(int(a7))

    if C8var == 1:
        l=Label(bill, text =c8.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=10, column=0)

        l=Label(bill, text =a8, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=10, column=2)

        bill_list.append(int(a8))

    if C9var == 1:
        l=Label(bill, text =c9.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=11, column=0)

        l=Label(bill, text =a9, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=11, column=2)

        bill_list.append(int(a9))

    if C10var == 1:
        l=Label(bill, text =c10.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=12, column=0)

        l=Label(bill, text =a10, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=12, column=2)
        
        bill_list.append(int(a10))

    if C11var == 1:
        l=Label(bill, text =c11.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=13, column=0)

        l=Label(bill, text =a11, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=13, column=2)

        bill_list.append(int(a11))

    if C12var == 1:
        l=Label(bill, text =c12.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=14, column=0)

        l=Label(bill, text =a12, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=14, column =2)

        bill_list.append(int(a12))

    if C13var == 1:
        l=Label(bill, text =c13.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=15, column=0)

        l=Label(bill, text =a13, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=15, column=2)

        bill_list.append(int(a13))

    if C14var == 1:
        l=Label(bill, text =c14.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=16, column=0)

        l=Label(bill, text =a14, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=16, column=2)

        bill_list.append(int(a14))

    if C15var == 1:
        l=Label(bill, text =c15.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=17, column=0)

        l=Label(bill, text =a15, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=17, column=2)

        bill_list.append(int(a15))

    if C16var == 1:
        l=Label(bill, text =c16.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=18, column=0)

        l=Label(bill, text =b1, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=18, column=2)

        bill_list.append(int(b1))

    if C17var == 1:
        l=Label(bill, text =c17.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=19, column=0)

        l=Label(bill, text =b2, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=19, column=2)

        bill_list.append(int(b2))


    if C18var == 1:
        l=Label(bill, text =c18.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=20, column=0)

        l=Label(bill, text =b3, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=20, column=2)

        bill_list.append(int(b3))

    if C19var == 1:
        l=Label(bill, text =c19.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=21, column=0)

        l=Label(bill, text =b4, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=21, column=2)

        bill_list.append(int(b4))

    if C20var == 1:
        l=Label(bill, text =c20.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=22, column=0)

        l=Label(bill, text =b5, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=22, column=2)

        bill_list.append(int(b5))

    if C21var == 1:
        l=Label(bill, text =c21.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=23, column=0)

        l=Label(bill, text =b6, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=23, column=2)

        bill_list.append(int(b6))

    if C22var == 1:
        l=Label(bill, text =c22.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=24, column=0)

        l=Label(bill, text =b7, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=24, column=2)

        bill_list.append(int(b7))

    if C23var == 1:
        l=Label(bill, text =c23.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=25, column=0)

        l=Label(bill, text =b8, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=25, column=2)

        bill_list.append(int(b8))

    if C24var == 1:
        l=Label(bill, text =c24.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=26, column=0)

        l=Label(bill, text =b9, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=26, column=2)

        bill_list.append(int(b9))

    if C25var == 1:
        l=Label(bill, text =c25.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=27, column=0)

        l=Label(bill, text =b10, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=27, column=2)

        bill_list.append(int(b10))

    if C26var == 1:
        l=Label(bill, text =c26.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=28, column=0)

        l=Label(bill, text =wb11, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=28, column=2)

        bill_list.append(int(wb11))

    if C27var == 1:
        l=Label(bill, text =c27.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=29, column=0)

        l=Label(bill, text =b12, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=29, column=2)

        bill_list.append(int(b12))

    if C28var == 1:
        l=Label(bill, text =c28.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=30, column=0)

        l=Label(bill, text =b13, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=30, column=2)

        bill_list.append(int(b13))

    if C29var == 1:
        l=Label(bill, text =c29.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=31, column=0)

        l=Label(bill, text =b14, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=31, column=2)

        bill_list.append(int(b14))

    if C30var == 1:
        l=Label(bill, text =c30.cget('text'), font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=32, column=0)

        l=Label(bill, text =b15, font=('Calibri',11), bg=bg_color, fg='black')
        l.grid(row=32, column=2)

        bill_list.append(int(b15))

    #label for Total Amount
    l=Label(bill, text ='Total Amount :', font=('Calibri',14), bg=bg_color, fg='black')
    l.grid(row=35, column=0)

    l=Label(bill, text =str(sum(bill_list)) + '/-', font=('Calibri',14) ,bg=bg_color, fg='black')
    l.grid(row=35, column=2)

    b= Button(bill, text="Pay Now", font=('Calibri',10), relief=GROOVE,  bg=bg_color, fg='black', command=total)
    b.grid(row=40, column=1, pady=2, padx=20, ipadx=100)

    b= Button(bill, text="Pay Later", font=('Calibri',10), relief=GROOVE,  bg=bg_color, fg='black', command=leave)
    b.grid(row=42, column=1, pady=2, padx=20, ipadx=97.5)
#test function to show test list
def tests():

    if pa_id.get() == '' :
        messagebox.showerror('Error !', 'Id not provided !')

    elif pa_name.get() == '' :
        messagebox.showerror('Error !', 'Name not provided !')

    elif pa_age.get() == '' :
        messagebox.showerror('Error !', 'Age not provided !')

    elif pa_gender.get() == '' :
        messagebox.showerror('Error !', 'Gender not Specified !')

    elif pa_blood.get() == '' :
        messagebox.showerror('Error !', 'Blood Group not provided !')

    elif pa_address.get() == '' :
        messagebox.showerror('Error !', 'Address not provided !')

    else:
        global test
        test=Toplevel()
        test.title("Patient's Tests")
        test.iconbitmap('D:/lab.ico')
        test.geometry("1200x700")
        test.configure(bg=bg_color)

        global a1
        global a2
        global a3
        global a4
        global a5
        global a6
        global a7
        global a8
        global a9
        global a10
        global a11
        global a12
        global a13
        global a14
        global a15
        
        a1="25000"
        a2="13000"
        a3="10000"
        a4="4900"
        a5="4500"
        a6="3099"
        a7="3500"
        a8="800"
        a9="1200"
        a10="4500"
        a11="3350"
        a12="4000"
        a13="3500"
        a14="1300"
        a15="1000"

        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        global b7
        global b8
        global b9
        global b10
        global wb11
        global b12
        global b13
        global b14
        global b15
        
        b1="850"
        b2="2200"
        b3="900"
        b4="3500"
        b5="6600"
        b6="1000"
        b7="2500"
        b8="600"
        b9="2500"
        b10="800"
        wb11="900"
        b12="5000"
        b13="1450"
        b14="5500"
        b15="2200"

        global var1
        global var2
        global var3
        global var4
        global var5
        global var6
        global var7
        global var8
        global var9
        global var10
        global var11
        global var12
        global var13
        global var14
        global var15
        global var16
        global var17
        global var18
        global var19
        global var20
        global var21
        global var22
        global var23
        global var24
        global var25
        global var26
        global var27
        global var28
        global var29
        global var30
        
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6= IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()
        var21 = IntVar()
        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        var25 = IntVar()
        var26 = IntVar()
        var27 = IntVar()
        var28 = IntVar()
        var29 = IntVar()
        var30 = IntVar()

        global c1
        global c2
        global c3
        global c4
        global c5
        global c6
        global c7
        global c8
        global c9
        global c10
        global c11
        global c12
        global c13
        global c14
        global c15
        global c16
        global c17
        global c18
        global c19
        global c20
        global c21
        global c22
        global c23
        global c24
        global c25
        global c26
        global c27
        global c28
        global c29
        global c30
        
        #list of tests in lab
        #creating check buttons 
        c1=Checkbutton(test, text="Oncorpo Heredity Cancer Risk ", variable = var1, onvalue=1, offvalue=0,  font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c1.grid(row=1, column=0, sticky=W , pady=(10,0))

        c2=Checkbutton(test, text="Allergy Comprehensive Profile", variable=var2, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c2.grid(row=2, column=0, sticky=W , pady=(10,0))

        c3=Checkbutton(test, text="Allergy Regional Panel", variable=var3, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c3.grid(row=3, column=0, sticky=W, pady=(10,0))

        c4=Checkbutton(test, text="Obesity Panel", variable=var4, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c4.grid(row=4, column=0, sticky=W, pady=(10,0))
                        
        c5=Checkbutton(test, text="Enhance Liver Fibrosis", variable=var5, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c5.grid(row=5, column=0, sticky=W, pady=(10,0))
                        
        c6=Checkbutton(test, text="Sugar Comprehensive", variable=var6, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c6.grid(row=6, column=0, sticky=W, pady=(10,0))
                        
        c7=Checkbutton(test, text="Chronic Fatigue Syndrome", variable=var7, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c7.grid(row=7, column=0, sticky=W, pady=(10,0))
                        
        c8=Checkbutton(test, text="X-Rays", variable=var8, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c8.grid(row=8, column=0, sticky=W, pady=(10,0))
                        
        c9=Checkbutton(test, text="Ultrasounds", variable=var9, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c9.grid(row=9, column=0, sticky=W, pady=(10,0))
                        
        c10=Checkbutton(test, text="MRIs", variable=var10, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c10.grid(row=10, column=0, sticky=W, pady=(10,0))
                        
        c11=Checkbutton(test, text="HIV 1 and 2 Antibodies", variable=var11, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c11.grid(row=11, column=0, sticky=W, pady=(10,0))
                        
        c12=Checkbutton(test, text="Immunity check  package", variable=var12, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c12.grid(row=12, column=0, sticky=W, pady=(10,0))
                        
        c13=Checkbutton(test, text="Thyroid Comprehensive Panel", variable=var13, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c13.grid(row=13, column=0, sticky=W, pady=(10,0))
                        
        c14=Checkbutton(test, text="Sugar Advance", variable=var14, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c14.grid(row=14, column=0, sticky=W, pady=(10,0))

        c15=Checkbutton(test, text="Culture Stool Test", variable=var15, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c15.grid(row=15, column=0, sticky=W, pady=(10,0))
                
        #next column
        c16=Checkbutton(test, text="Culture Urine Test", variable=var16, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c16.grid(row=1, column=4, sticky=W, pady=(10,0))

        c17=Checkbutton(test, text="Insulin Antibodies", variable=var17, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c17.grid(row=2, column=4, sticky=W, pady=(10,0))
                        
        c18=Checkbutton(test, text="Dengue Fever Antibodies", variable=var18, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c18.grid(row=3, column=4, sticky=W, pady=(10,0))
                        
        c19=Checkbutton(test, text="Zinc Serum / Plasma", variable=var19, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c19.grid(row=4, column=4, sticky=W, pady=(10,0))
                        
        c20=Checkbutton(test, text="Allergy Gluten", variable=var20, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c20.grid(row=5, column=4, sticky=W, pady=(10,0))
                        
        c21=Checkbutton(test, text="Pregnancy Tests", variable=var21, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c21.grid(row=6, column=4, sticky=W, pady=(10,0))
                        
        c22=Checkbutton(test, text="Insulin Fasting", variable=var22, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c22.grid(row=7, column=4, sticky=W, pady=(10,0))
                        
        c23=Checkbutton(test, text="Heamoglobin", variable=var23, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c23.grid(row=8, column=4, sticky=W, pady=(10,0))
                        
        c24=Checkbutton(test, text="Anaemia Check Complete", variable=var24, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c24.grid(row=9, column=4, sticky=W, pady=(10,0))
                        
        c25=Checkbutton(test, text="Red Blood Cells (RBC)", variable=var25, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c25.grid(row=10, column=4, sticky=W, pady=(10,0))
                        
        c26=Checkbutton(test, text="black Blood Cells (WBC)", variable=var26, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c26.grid(row=11, column=4, sticky=W, pady=(10,0))
                        
        c27=Checkbutton(test, text="Hypertension Panel", variable=var27, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c27.grid(row=12, column=4, sticky=W, pady=(10,0))
                        
        c28=Checkbutton(test, text="Allergy Milk", variable=var28, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c28.grid(row=13, column=4, sticky=W, pady=(10,0))
                        
        c29=Checkbutton(test, text="Allergy Mushroom", variable=var29, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c29.grid(row=14, column=4, sticky=W, pady=(10,0))
                        
        c30=Checkbutton(test, text="Iron Check", variable=var30, onvalue=1, offvalue=0,font=('Calibri',12, "bold"), bg=bg_color, fg='black')
        c30.grid(row=15, column=4, sticky=W, pady=(10,0))

        #making Price Labels
        l0=Label(test, text ="PATIENTS' TESTS LIST", font=('Calibri',15), bg=bg_color, fg='black')
        l0.grid(row=0, column=3, pady=(10,0))
     
        l1=Label(test, text ="25000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l1.grid(row=1, column=2, sticky=W, pady=(10,0), ipadx=(50))
        l2=Label(test, text ="13000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l2.grid(row=2, column=2, sticky=W, pady=(10,0), ipadx=(50))

        l3=Label(test, text ="10000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l3.grid(row=3, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l4=Label(test, text ="4900/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l4.grid(row=4, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l5=Label(test, text ="4500/-", font=('Calibri',12), bg=bg_color, fg='black')
        l5.grid(row=5, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l6=Label(test, text ="3099/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l6.grid(row=6, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l7=Label(test, text ="3500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l7.grid(row=7, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l8=Label(test, text ="800/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l8.grid(row=8, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l9=Label(test, text ="1200/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l9.grid(row=9, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l10=Label(test, text ="4500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l10.grid(row=10, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l11=Label(test, text ="3350/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l11.grid(row=11, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l12=Label(test, text ="4000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l12.grid(row=12, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l13=Label(test, text ="3500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l13.grid(row=13, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l14=Label(test, text ="1300/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l14.grid(row=14, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l15=Label(test, text ="1000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l15.grid(row=15, column=2, sticky=W, pady=(10,0), ipadx=(50))

        #next column
        l16=Label(test, text ="850/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l16.grid(row=1, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l17=Label(test, text ="2200/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l17.grid(row=2, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l18=Label(test, text ="900/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l18.grid(row=3, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l19=Label(test, text ="3500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l19.grid(row=4, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l20=Label(test, text ="6600/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l20.grid(row=5, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l21=Label(test, text ="1000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l21.grid(row=6, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l22=Label(test, text ="2500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l22.grid(row=7, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l23=Label(test, text ="600/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l23.grid(row=8, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l24=Label(test, text ="2500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l24.grid(row=9, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l25=Label(test, text ="800/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l25.grid(row=10, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l26=Label(test, text ="900/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l26.grid(row=11, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l27=Label(test, text ="5000/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l27.grid(row=12, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l28=Label(test, text ="1450/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l28.grid(row=13, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l29=Label(test, text ="5500/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l29.grid(row=14, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l30=Label(test, text ="2200/-", font=('Calibri',12),  bg=bg_color, fg='black')
        l30.grid(row=15, column=5, sticky=W, pady=(10,0), ipadx=(50))

        #making next Button
        b11= Button(test, text=" NEXT ", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=bills)
        b11.grid(row=6, column=6, pady=2, padx=20, ipadx=100)

        
#add the patient data
def add_data():          
    global add
    add=Toplevel()
    add.title('Adding Patient Record')
    add.iconbitmap('D:/lab.ico')
    add.geometry("550x350")
    add.configure(bg=bg_color)

    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()
    global pa_id
    global pa_name
    global pa_age
    global pa_gender
    global pa_blood
    global pa_address
    
    #making text boxes
    pa_id=Entry(add, width=30, relief=GROOVE)
    pa_id.grid(row=1, column=1, padx=60, pady=(10,0))
    
    pa_name=Entry(add, width=30, relief=GROOVE)
    pa_name.grid(row=2, column=1)

    pa_age=Entry(add, width=30, relief=GROOVE)
    pa_age.grid(row=3, column=1)

    pa_gender=Entry(add, width=30, relief=GROOVE)
    pa_gender.grid(row=4, column=1)

    pa_blood=Entry(add, width=30, relief=GROOVE)
    pa_blood.grid(row=5, column=1)

    pa_address=Entry(add, width=30, relief=GROOVE)
    pa_address.grid(row=6, column=1)
    
    #creating Labels    
    id_label=Label(add, text=" Enter Patient Id :", font=('Calibri',15), bg=bg_color, fg='black')
    id_label.grid(row=1, column=0, pady=(10,0))

    name_label=Label(add, text="Enter Patient Name :", font=('Calibri',15), bg=bg_color, fg='black')
    name_label.grid(row=2, column=0)

    age_label=Label(add, text="Enter Patient Age :", font=('Calibri',15), bg=bg_color, fg='black')
    age_label.grid(row=3, column=0)

    gend_label=Label(add, text="Enter Patient Gender :", font=('Calibri',15), bg=bg_color, fg='black')
    gend_label.grid(row=4, column=0)

    blood_label=Label(add, text="Enter Patient's Blood Group :", font=('Calibri',15), bg=bg_color, fg='black')
    blood_label.grid(row=5, column=0)

    add_label=Label(add, text="Enter Patient Address :", font=('Calibri',15), bg=bg_color, fg='black')
    add_label.grid(row=6, column=0)
    
    #create next Button
    b2= Button(add, text=" NEXT ", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=tests)
    b2.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=103)

    con.commit()
    con.close()

def enter_id():
    global enter
    enter=Toplevel()
    enter.title('Enter ID')
    enter.iconbitmap('D:/lab.ico')
    enter.geometry("500x140")
    enter.configure(bg=bg_color)

    con=mysql.connector.connect(host ='localhost', user ='root', password ='12345', database='pathlab')
    cur=con.cursor()

    global enter_box
    enter_box=Entry(enter, width=30, relief=GROOVE)
    enter_box.grid(row=10, column=1, pady=(20,0))
        
    enter_label=Label(enter, text="Enter Patient Id to display that Record :", font=('Calibri',10), bg=bg_color, fg='black')
    enter_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    #create show_one query button
    b4= Button(enter, text="Show Record", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=entry_1)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

    #create close window button
    bu= Button(enter, text="Close Window", font=('Calibri',10), relief=GROOVE, bg=bg_color, fg='black', command=enter_close)
    bu.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

    con.close()

# labels
h_label=Label(root, text="PATHOLOGY MANAGEMENT", font=('Arial Bold',40) , fg="black")
h_label.grid(row=0, column=1, padx=40, pady=20)

main_label=Label(root, text="ADMINISTRATOR WINDOW", font=('Arial',30, "bold"), fg='black')
main_label.grid(row=1, column=1, padx=40, pady=(10,5))

#create add data Button
b1= Button(root, text="Add Patient Record", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=add_data)
b1.grid(row=7, column=1, ipadx=108.3, pady=(20,14))

#create show_all query button
b3= Button(root, text="Show all Patients' List", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=show_all)
b3.grid(row=8, column=1, ipadx=99.5, pady=14)

#create show_one query button
b4= Button(root, text="Show Patient's Summary", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=show_one2)
b4.grid(row=11, column=1, ipadx=93, pady=14)

#create delete button
b5= Button(root, text="Delete Patient Record", font=('Arial',10,"bold"), relief=GROOVE, fg='black', command=delete1)
b5.grid(row=21, column=1, ipadx=100, pady=14)

#create update button
b6= Button(root, text="Update Patient Record", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=update1)
b6.grid(row=23, column=1, ipadx=99., pady=14)

#create about button
b7= Button(root, text="(i) Learn More about this System", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=about)
b7.grid(row=25, column=1, ipadx=73, pady=(20,14))

#create exit button
b8= Button(root, text="Exit System", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=close1)
b8.grid(row=26, column=1, ipadx=130, pady=(14, 23))

#create bill summary button
bs= Button(root, text="Pay Bill", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=billw1)
bs.grid(row=12, column=1, ipadx=144, pady=14)

#create receipt generation button
bs= Button(root, text="Generate Receipt", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=enter_id)
bs.grid(row=24, column=1, ipadx=116, pady=14)


root.mainloop()
