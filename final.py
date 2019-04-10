##08:40 PM 09-07-2018

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import datetime
import os
cur=os.getcwd()
os.chdir('{}{}\code\logo'.format(cur[:3],cur[3:]))

class hospital:
    def __init__(self):

        self.root = Tk()
        self.root.title('Noa Medicity')
        self.root.geometry('1400x768+50+10')
        self.root.wm_iconbitmap('noa.ico')
        self.root.resizable(0, 0)
        self.home = ttk.Frame(self.root)
        self.pageone = ttk.Frame(self.root)
        self.pagetwo = ttk.Frame(self.root)
        self.pagethree = ttk.Frame(self.root)
        self.pagefour = ttk.Frame(self.root)
        self.pagefive = ttk.Frame(self.root)
        self.pagesix = ttk.Frame(self.root)
        self.pageseven = ttk.Frame(self.root)
        self.pageeight = ttk.Frame(self.root)
        self.pagenine = ttk.Frame(self.root)
        self.pageten = ttk.Frame(self.root)
        self.pageeleven = ttk.Frame(self.root)
        self.pagetwelve = ttk.Frame(self.root)

        for self.frame in (self.home, self.pageone, self.pagetwo,
                           self.pagethree, self.pagefour, self.pageeleven, self.pagetwelve):
            self.frame.place(x=0, y=0)

        for self.mframe in (self.pagefive,
                            self.pagesix, self.pageseven, self.pageeight,
                            self.pagenine, self.pageten):
            self.mframe.place(x=310, y=150)

        self.style = ttk.Style()
        self.login_screen()
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS NEW_USER (first_name TEXT NOT NULL ,'
                  ' last_name TEXT NOT NULL, username TEXT PRIMARY KEY NOT NULL, email TEXT NOT NULL,'
                  ' password TEXT NOT NULL, address TEXT NOT NULL, mobile_number INTEGER NOT NULL)')

        c.execute('CREATE TABLE IF NOT EXISTS STAFF (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,'
                  'name TEXT NOT NULL, gender TEXT NOT NULL, position TEXT NOT NULL,'
                  'salary INTEGER NOT NULL, mobile_number INTEGER NOT NULL, address TEXT NOT NULL)')

        c.execute(
            'CREATE TABLE IF NOT EXISTS PATIENT (pid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL,'
            ' gender TEXT NOT NULL, age INTEGER NOT NULL, mobile_number INTEGER NOT NULL,'
            ' address TEXT NOT NULL, disease TEXT NOT NULL, room_number INTEGER NOT NULL UNIQUE)')

        c.execute(
            'CREATE TABLE IF NOT EXISTS RECORD (pid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL,'
            'gender TEXT NOT NULL, age INTEGER NOT NULL, mobile_number INTEGER NOT NULL,address TEXT NOT NULL, '
            'disease TEXT NOT NULL, room_number INTEGER NOT NULL ,date_in TEXT,date_out TEXT, payment INTEGER )')

        c.execute(
            'CREATE TABLE IF NOT EXISTS FEEDBACK (name TEXT NOT NULL, email TEXT NOT NULL, comment TEXT NOT NULL)')

        c.close()
        conn.close()

    def login_screen(self):
        # page home
        self.home.tkraise()
        self.load = Image.open('hospitalimg.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = Label(self.home, image=self.logo)
        self.label.image = self.logo
        self.label.pack()
        self.style.configure('TButton', background='#bdbcbc')
        self.style.configure('TEntry', background='#bdbcbc')

        self.e_user = ttk.Entry(self.home, width=37, font=('Arial', 12))
        self.e_password = ttk.Entry(self.home, width=37, show='*', font=('Arial', 12))
        self.e_user.place(x=530, y=420)
        self.e_password.place(x=530, y=490)

        Button(self.home, width=10, text='Login', font=('Arial', 10),
               relief=GROOVE, command=self.login).place(x=680, y=570)
        Button(self.home, width=10, text='Exit', font=('Arial', 10),
               relief=GROOVE, command=self.root.destroy).place(x=780, y=570)

        self.keep = IntVar()
        self.remember = Checkbutton(self.home, text="Remember me",
                                    variable=self.keep, bg='#ffc416',
                                    onvalue=1, offvalue=0)
        self.remember.place(x=530, y=530)

    
    def login(self):

        
        if self.e_user.get() == 'admin':
            if self.e_password.get() == 'admin':
                self.e_user.delete(0, 'end')
                self.e_password.delete(0, 'end')
                self.admin_options()
            else:
                messagebox.showwarning('NOA MEDICITY', 'Invalid Username or Password')
                self.e_user.delete(0, 'end')
                self.e_password.delete(0, 'end')

        else: 
            dbpassword = self.dbid()
            if self.e_password.get() == dbpassword:
                if (self.keep.get() == 1):
                    pass
                elif (self.keep.get() == 0):
                    self.e_user.delete(0, 'end')
                    self.e_password.delete(0, 'end')
                self.main()
            elif self.error_message == 1 :
                messagebox.showwarning('NOA MEDICITY', 'Invalid Username or Password')
                self.e_user.delete(0, 'end')
                self.e_password.delete(0, 'end')
                
                
                
    def dbid(self):

        try:     
            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            c.execute("SELECT password FROM NEW_USER WHERE username= ? ", (self.e_user.get(),))
            data = c.fetchone()
            c.close()
            conn.close()
            for i in data:
                password = i
                
            
        except :
            messagebox.showwarning('NOA MEDICITY', 'Invalid Username or Password')
            self.e_user.delete(0, 'end')
            self.e_password.delete(0, 'end')
            self.error_message = 0

        else:
            self.error_message = 1
            return password
            

       
    def admin_options(self):
        # page one
        self.pageone.tkraise()
        self.load1 = Image.open('message.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageone, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.pack()

        Button(self.pageone, text='Create User', width=20, font=('Arial', 14),
               command=self.new_user, fg='black', bg='white', relief=GROOVE).place(x=350, y=330)
        Button(self.pageone, text='Remove User', width=20, font=('Arial', 14),
               command=self.remove_user, fg='black', bg='white', relief=GROOVE).place(x=350, y=380)
        Button(self.pageone, text='Add Staff Member', width=20, font=('Arial', 14),
               command=self.add_staff_member, fg='black', bg='white', relief=GROOVE).place(x=350, y=430)
        Button(self.pageone, text='Remove Staff member', width=20, font=('Arial', 14),
               command=self.remove_staff_member, fg='black', bg='white', relief=GROOVE).place(x=350, y=480)
        Button(self.pageone, text='Back', width=18, font=('Arial', 12),
               command=self.home.tkraise, fg='black', bg='white', relief=GROOVE).place(x=50, y=700)

    ########################################################

    def new_user(self):
        # page two
        self.pagetwo.tkraise()
        self.load = Image.open('new_user.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = Label(self.pagetwo, image=self.logo)
        self.label.image = self.logo
        self.label.pack()

        self.first_name = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')
        self.last_name = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')
        self.username = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')
        self.email = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')
        self.password = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), show='*', foreground='#181817')
        self.address = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')
        self.mobileno = ttk.Entry(self.pagetwo, width=26, font=('Arial', 17), foreground='#181817')

        self.first_name.place(x=750, y=250)
        self.last_name.place(x=750, y=300)
        self.username.place(x=750, y=350)
        self.email.place(x=750, y=400)
        self.password.place(x=750, y=450)
        self.address.place(x=750, y=500)
        self.mobileno.place(x=750, y=550)

        Button(self.pagetwo, width=14, text='Back', relief=GROOVE, font=('Arial', 13),
               command=self.pageone.tkraise).place(x=880, y=650)
        Button(self.pagetwo, width=14, text='Submit', relief=GROOVE, font=('Arial', 13),
               command=self.new_user_submit).place(x=1030, y=650)
        Button(self.pagetwo, width=14, text='Cancel', relief=GROOVE, font=('Arial', 13),
               command=self.new_user_clean).place(x=1180, y=650)

    def remove_user(self):
        # page three
        self.pagethree.tkraise()
        self.load = Image.open('remove_user.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = Label(self.pagethree, image=self.logo)
        self.label.image = self.logo
        self.label.pack()

        Button(self.pagethree, width=14, text='Back', relief=GROOVE, font=('Arial', 13),
               command=self.pageone.tkraise).place(x=480, y=550)
        Button(self.pagethree, width=14, text='Submit', relief=GROOVE, font=('Arial', 13),
               command=self.remove_user_submit).place(x=630, y=550)
        Button(self.pagethree, width=14, text='Cancel', relief=GROOVE, font=('Arial', 13),
               command=self.remove_user_clean).place(x=780, y=550)

        self.r_username = ttk.Entry(self.pagethree, width=26, font=('Arial', 17), foreground='#181817')
        self.r_password = ttk.Entry(self.pagethree, width=26, font=('Arial', 17), show='*', foreground='#181817')
        self.r_username.place(x=750, y=300)
        self.r_password.place(x=750, y=352)

    def add_staff_member(self):
        # page eleven
        self.pageeleven.tkraise()
        self.load1 = Image.open('add staff.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageeleven, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.pack()

        self.staff_var_gender=StringVar()
        self.staff_var_id=StringVar()
        self.staff_id = ttk.Entry(self.pageeleven, textvariable=self.staff_var_id,width=26, font=('Arial', 17), foreground='#181817')
        self.staff_name = ttk.Entry(self.pageeleven, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_gender = ttk.Combobox(self.pageeleven,textvariable=self.staff_var_gender, font=('Arial', 16), foreground='#181817')
        self.staff_position = ttk.Entry(self.pageeleven, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_salary = ttk.Entry(self.pageeleven, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_mobile_number = ttk.Entry(self.pageeleven, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_address = ttk.Entry(self.pageeleven, width=26, font=('Arial', 17), foreground='#181817')

        self.staff_id.place(x=750, y=250)
        self.staff_name.place(x=750, y=300)
        self.staff_gender.place(x=750, y=350, width=344)
        self.staff_position.place(x=750, y=400)
        self.staff_salary.place(x=750, y=450)
        self.staff_mobile_number.place(x=750, y=500)
        self.staff_address.place(x=750, y=550)
        self.staff_gender.configure(values=('Male','Female'))

        Button(self.pageeleven, width=14, text='Back', relief=GROOVE, font=('Arial', 13),
               command=self.pageone.tkraise).place(x=880, y=650)
        Button(self.pageeleven, width=14, text='Submit', relief=GROOVE, font=('Arial', 13),
               command=self.add_staff_submit).place(x=1030, y=650)
        Button(self.pageeleven, width=14, text='Cancel', relief=GROOVE, font=('Arial', 13),
               command=self.add_staff_clean).place(x=1180, y=650)

        try:
            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            c.execute('select id FROM STAFF')
            data = c.fetchall()
            c.close()
            conn.close()
            temp=[]
            for i in data:
                i=i[0]
                temp.append(i+1)
            self.id=max(temp)

        except Exception:

            self.id = 1

        self.staff_id.state(['disabled'])
        self.staff_var_id.set(self.id)

    def remove_staff_member(self):
        self.pagetwelve.tkraise()
        self.load1 = Image.open('remove staff.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagetwelve, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.pack()

        Button(self.pagetwelve, width=14, text='Back', relief=GROOVE, font=('Arial', 13),
               command=self.pageone.tkraise).place(x=480, y=550)
        Button(self.pagetwelve, width=14, text='Submit', relief=GROOVE, font=('Arial', 13),
               command=self.remove_staff_submit).place(x=630, y=550)
        Button(self.pagetwelve, width=14, text='Cancel', relief=GROOVE, font=('Arial', 13),
               command=self.remove_staff_clean).place(x=780, y=550)

        self.staff_rid = ttk.Entry(self.pagetwelve, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_rname = ttk.Entry(self.pagetwelve, width=26, font=('Arial', 17), foreground='#181817')
        self.staff_rid.place(x=750, y=295)
        self.staff_rname.place(x=750, y=347)

    ##########################################################

    def new_user_submit(self):

        try:

            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            first_name = self.first_name.get()
            last_name = self.last_name.get()
            username = self.username.get()
            email = self.email.get()
            password = self.password.get()
            address = self.address.get()
            mobile_number = int(self.mobileno.get())

            c.execute(
                " INSERT INTO NEW_USER (first_name,last_name,username,email,password,address,mobile_number) VALUES (?,?,?,?,?,?,?)",
                (first_name, last_name, username, email, password, address, mobile_number,))
            conn.commit()
            c.close()
            conn.close()

            messagebox.showinfo(title='New User', message='User Create Submitted!')


        except sqlite3.IntegrityError:

            messagebox.showwarning('ERROR', 'Username is already created')

            self.first_name.delete(0, 'end')
            self.last_name.delete(0, 'end')
            self.username.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
            self.address.delete(0, 'end')
            self.mobileno.delete(0, 'end')

        except:

            messagebox.showwarning('ERROR', 'Invalid Input')

            self.first_name.delete(0, 'end')
            self.last_name.delete(0, 'end')
            self.username.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
            self.address.delete(0, 'end')
            self.mobileno.delete(0, 'end')



        else:

            self.first_name.delete(0, 'end')
            self.last_name.delete(0, 'end')
            self.username.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
            self.address.delete(0, 'end')
            self.mobileno.delete(0, 'end')

    def new_user_clean(self):

        self.first_name.delete(0, 'end')
        self.last_name.delete(0, 'end')
        self.username.delete(0, 'end')
        self.email.delete(0, 'end')
        self.password.delete(0, 'end')
        self.address.delete(0, 'end')
        self.mobileno.delete(0, 'end')

    ###########################################################

    def remove_user_submit(self):

        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("DELETE FROM NEW_USER WHERE username = ? AND password = ? ",
                  (self.r_username.get(), self.r_password.get(),))
        conn.commit()
        c.close()
        conn.close()

        self.r_username.delete(0, 'end')
        self.r_password.delete(0, 'end')

        messagebox.showinfo(title='Remove User', message='User Remove Submitted!')

    def remove_user_clean(self):

        self.r_username.delete(0, 'end')
        self.r_password.delete(0, 'end')

    ###########################################################

    def add_staff_submit(self):
        
        
        try:
            name = self.staff_name.get()
            gender = self.staff_var_gender.get()
            position = self.staff_position.get()
            salary = int(self.staff_salary.get())
            mobile_number = int(self.staff_mobile_number.get())
            address = self.staff_address.get()

            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()

            c.execute(" INSERT INTO STAFF (id,name,gender,position,"
                      "salary,mobile_number,address) VALUES (NULL ,?,?,?,?,?,?)",
                      (name, gender, position, salary, mobile_number, address,))

            conn.commit()
            c.close()
            conn.close()

            messagebox.showinfo(title='Add Staff Member', message='New Staff Member Create Submitted!')

        except ValueError:

            messagebox.showwarning('ERROR', 'Invalid Entery')

            self.staff_id.delete(0, 'end')
            self.staff_name.delete(0, 'end')
            self.staff_gender.delete(0, 'end')
            self.staff_position.delete(0, 'end')
            self.staff_salary.delete(0, 'end')
            self.staff_mobile_number.delete(0, 'end')
            self.staff_address.delete(0, 'end')

        except:

            messagebox.showwarning('ERROR', 'Invalid Entery')

            self.staff_id.delete(0, 'end')
            self.staff_name.delete(0, 'end')
            self.staff_gender.delete(0, 'end')
            self.staff_position.delete(0, 'end')
            self.staff_salary.delete(0, 'end')
            self.staff_mobile_number.delete(0, 'end')
            self.staff_address.delete(0, 'end')

        else:
            self.staff_id.delete(0, 'end')
            self.staff_name.delete(0, 'end')
            self.staff_gender.delete(0, 'end')
            self.staff_position.delete(0, 'end')
            self.staff_salary.delete(0, 'end')
            self.staff_mobile_number.delete(0, 'end')
            self.staff_address.delete(0, 'end')
            self.add_staff_member()

    def add_staff_clean(self):

        self.staff_id.delete(0, 'end')
        self.staff_name.delete(0, 'end')
        self.staff_gender.delete(0, 'end')
        self.staff_position.delete(0, 'end')
        self.staff_salary.delete(0, 'end')
        self.staff_mobile_number.delete(0, 'end')
        self.staff_address.delete(0, 'end')

    ###########################################################

    def remove_staff_clean(self):

        self.staff_rid.delete(0, 'end')
        self.staff_rname.delete(0, 'end')

    def remove_staff_submit(self):

        messagebox.showinfo(title='Remove Staff Member', message='Staff Member Remove Submitted!')

        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("DELETE FROM STAFF WHERE id = ? AND name = ? ", (self.staff_rid.get(), self.staff_rname.get(),))
        conn.commit()
        c.close()
        conn.close()

        self.staff_rid.delete(0, 'end')
        self.staff_rname.delete(0, 'end')

    ###########################################################

    def main(self):
        # page four
        self.pagefour.tkraise()
        self.load = Image.open('main.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pagefour, image=self.logo)
        self.label.image = self.logo
        self.label.pack()
        Button(self.pagefour, text='Logout', command=self.home.tkraise,
               relief=GROOVE, width=20, font=('Arial', 10), bg='white', fg='#1f1f1f').place(x=46, y=700)
        Button(self.pagefour, text='Patient Registration', command=self.Patient_Registration,
               relief=GROOVE, width=20, font=('Arial', 10), fg='white', bg='#1f1f1f').place(x=46, y=250)
        Button(self.pagefour, text='Patient Information', command=self.Patient_Information,
               relief=GROOVE, width=20, font=('Arial', 10), fg='white', bg='#1f1f1f').place(x=46, y=300)
        Button(self.pagefour, text='Patient CheckOut', command=self.Patient_CheckOut,
               relief=GROOVE, width=20, font=('Arial', 10), fg='white', bg='#1f1f1f').place(x=46, y=350)
        Button(self.pagefour, text='Staff Informaiton', command=self.Staff_Informaiton,
               relief=GROOVE, width=20, font=('Arial', 10), fg='white', bg='#1f1f1f').place(x=46, y=400)
        Button(self.pagefour, text='About', command=self.About,
               relief=GROOVE, width=20, font=('Arial', 10), fg='white', bg='#1f1f1f').place(x=46, y=450)

        ##########################################################################################
        # page five
        self.pagefive.tkraise()
        self.load = Image.open('welcome.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pagefive, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

    ###########################################################

    def Patient_Registration(self):
        # page six
        self.pagesix.tkraise()
        self.load = Image.open('Patient Registration.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pagesix, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        self.patient_registration_var_gender=StringVar()
        self.patient_registration_var_pid=StringVar()
        self.patient_registration_pid = ttk.Entry(self.pagesix,textvariable=self.patient_registration_var_pid,
                                                  width=30, font=('Arial', 12))
        self.patient_registration_name = ttk.Entry(self.pagesix, width=30, font=('Arial', 12))
        self.patient_registration_gender = ttk.Combobox(self.pagesix,textvariable= self.patient_registration_var_gender,
                                                     font=('Arial', 12))
        self.patient_registration_age = ttk.Entry(self.pagesix,width=30,font=('Arial', 12))
        self.patient_registration_mobile_number = ttk.Entry(self.pagesix, width=30, font=('Arial', 12))
        self.patient_registration_address = ttk.Entry(self.pagesix, width=30, font=('Arial', 12))
        self.patient_registration_disease = ttk.Entry(self.pagesix, width=30, font=('Arial', 12))
        self.patient_registration_room_number = ttk.Entry(self.pagesix, width=30, font=('Arial', 12))

        self.patient_registration_pid.place(x=300, y=153)
        self.patient_registration_name.place(x=300, y=193)
        self.patient_registration_gender.place(x=300, y=233, width=277)
        self.patient_registration_age.place(x=300, y=273,)
        self.patient_registration_mobile_number.place(x=300, y=313)
        self.patient_registration_address.place(x=300, y=353)
        self.patient_registration_disease.place(x=300, y=393)
        self.patient_registration_room_number.place(x=300, y=433)

        self.patient_registration_gender.configure(values=('Male', 'Female'))

        Button(self.pagesix, text='Submit', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_registration_submit_button).place(x=650, y=500)
        Button(self.pagesix, text='Clean', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_registration_clean_button).place(x=790, y=500)

        try:
            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            c.execute('select pid FROM PATIENT')
            data = c.fetchall()
            c.close()
            conn.close()
            temp=[]
            for i in data:
                i=i[0]
                temp.append(i+1)
            self.pid=max(temp)
       

        except Exception:
            self.pid = 1
        
        self.patient_registration_pid.state(['disabled'])
        self.patient_registration_var_pid.set(self.pid)

    def patient_registration_submit_button(self):
        date = datetime.datetime.now()
        try:
            name = self.patient_registration_name.get()
            gender = self.patient_registration_var_gender.get()
            age = int(self.patient_registration_age.get())
            mobile_number = int(self.patient_registration_mobile_number.get())
            address = self.patient_registration_address.get()
            disease = self.patient_registration_disease.get()
            room_number = int(self.patient_registration_room_number.get())
            date_in = date.strftime('%Y/%m/%d %H:%M')

            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()

            c.execute(" INSERT INTO PATIENT (pid,name,gender,age,"
                      "mobile_number,address,disease,room_number) VALUES (NULL ,?,?,?,?,?,?,?)",
                      (name, gender, age, mobile_number, address, disease, room_number))
            c.execute(" INSERT INTO RECORD (pid,name,gender,age,"
                      "mobile_number,address,disease,room_number,date_in) VALUES (NULL ,?,?,?,?,?,?,?,?)",
                      (name, gender, age, mobile_number, address, disease, room_number, date_in))

            conn.commit()
            c.close()
            conn.close()

            messagebox.showinfo(title='MOA MEDICITY', message='Patient Registration Submitted!')

        except:

            messagebox.showwarning('NOA MEDICITY', 'Invalid Input')

            self.patient_registration_name.delete(0, 'end')
            self.patient_registration_gender.delete(0, 'end')
            self.patient_registration_age.delete(0, 'end')
            self.patient_registration_mobile_number.delete(0, 'end')
            self.patient_registration_address.delete(0, 'end')
            self.patient_registration_disease.delete(0, 'end')
            self.patient_registration_room_number.delete(0, 'end')
                

        
        else:
            self.patient_registration_name.delete(0, 'end')
            self.patient_registration_gender.delete(0, 'end')
            self.patient_registration_age.delete(0, 'end')
            self.patient_registration_mobile_number.delete(0, 'end')
            self.patient_registration_address.delete(0, 'end')
            self.patient_registration_disease.delete(0, 'end')
            self.patient_registration_room_number.delete(0, 'end')
            self.Patient_Registration()

    def patient_registration_clean_button(self):

        self.patient_registration_pid.delete(0, 'end')
        self.patient_registration_name.delete(0, 'end')
        self.patient_registration_gender.delete(0, 'end')
        self.patient_registration_age.delete(0, 'end')
        self.patient_registration_mobile_number.delete(0, 'end')
        self.patient_registration_address.delete(0, 'end')
        self.patient_registration_disease.delete(0, 'end')
        self.patient_registration_room_number.delete(0, 'end')

    ############################################################
    def Patient_Information(self):
        # page seven
        self.pageseven.tkraise()
        self.load = Image.open('Patient Information.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pageseven, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        self.patient_informaiton_ename = ttk.Entry(self.pageseven, width=25, font=('Arial', 12))
        self.patient_informaiton_pid = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_name = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_gender = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_age = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_mobile_number = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_address = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_disease = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))
        self.patient_informaiton_room_number = ttk.Entry(self.pageseven, width=30, font=('Arial', 12))

        self.patient_informaiton_ename.place(x=100, y=150)
        self.patient_informaiton_pid.place(x=625, y=153)
        self.patient_informaiton_name.place(x=625, y=193)
        self.patient_informaiton_gender.place(x=625, y=233)
        self.patient_informaiton_age.place(x=625, y=273)
        self.patient_informaiton_mobile_number.place(x=625, y=313)
        self.patient_informaiton_address.place(x=625, y=353)
        self.patient_informaiton_disease.place(x=625, y=393)
        self.patient_informaiton_room_number.place(x=625, y=433)

        self.patient_informaiton_name_list = Listbox(self.pageseven, selectmode=SINGLE, height=20, width=35)
        self.patient_informaiton_name_list.place(x=100, y=200)
        self.patient_scroll = Scrollbar(self.pageseven, orient=VERTICAL)
        self.patient_informaiton_name_list.configure(yscrollcommand=self.patient_scroll.set)
        self.patient_scroll.configure(command=self.patient_informaiton_name_list.yview)
        self.patient_scroll.place(x=310, y=200, height=324)

        Button(self.pageseven, text='Submit', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_informaiton_submit_button).place(x=360, y=147)
        Button(self.pageseven, text='Reset', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_information_clean_button).place(x=705, y=500)

        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT name FROM PATIENT")
        data = c.fetchall()
        for i in data:
            self.patient_informaiton_name_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.patient_informaiton_name_list.bind('<<ListboxSelect>>', self.patient_on_click)

    def patient_on_click(self, event):
        self.patient_informaiton_ename.delete(0, END)
        index = self.patient_informaiton_name_list.curselection()
        self.patient_select = index

        self.patient_informaiton_ename.insert(0, self.patient_informaiton_name_list.get(self.patient_select))

    def patient_informaiton_submit_button(self):
        self.patient_informaiton_ename.state(['disabled'])
        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_pid.insert(0, i)
        self.patient_informaiton_pid.state(['disabled'])
        #######################################################
        c.execute("SELECT name FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_name.insert(0, i)
        self.patient_informaiton_name.state(['disabled'])
        #########################################################
        c.execute("SELECT gender FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_gender.insert(0, i)
        self.patient_informaiton_gender.state(['disabled'])
        #########################################################
        c.execute("SELECT age FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_age.insert(0, i)
        self.patient_informaiton_age.state(['disabled'])
        #######################################################@@
        c.execute("SELECT mobile_number FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_mobile_number.insert(0, i)
        self.patient_informaiton_mobile_number.state(['disabled'])
        #######################################################@@
        c.execute("SELECT address FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_address.insert(0, i)
        self.patient_informaiton_address.state(['disabled'])
        #######################################################@@
        c.execute("SELECT disease FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_disease.insert(0, i)
        self.patient_informaiton_disease.state(['disabled'])
        #######################################################@@
        c.execute("SELECT room_number FROM PATIENT WHERE name = ? ", (self.patient_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_informaiton_room_number.insert(0, i)
        self.patient_informaiton_room_number.state(['disabled'])

        c.close()
        conn.close()

        #######################################################@@

    def patient_information_clean_button(self):
        self.patient_informaiton_ename.state(['!disabled'])
        self.patient_informaiton_pid.state(['!disabled'])
        self.patient_informaiton_name.state(['!disabled'])
        self.patient_informaiton_gender.state(['!disabled'])
        self.patient_informaiton_age.state(['!disabled'])
        self.patient_informaiton_mobile_number.state(['!disabled'])
        self.patient_informaiton_address.state(['!disabled'])
        self.patient_informaiton_disease.state(['!disabled'])
        self.patient_informaiton_room_number.state(['!disabled'])

        self.patient_informaiton_ename.delete(0, END)
        self.patient_informaiton_pid.delete(0, END)
        self.patient_informaiton_name.delete(0, END)
        self.patient_informaiton_gender.delete(0, END)
        self.patient_informaiton_age.delete(0, END)
        self.patient_informaiton_mobile_number.delete(0, END)
        self.patient_informaiton_address.delete(0, END)
        self.patient_informaiton_disease.delete(0, END)
        self.patient_informaiton_room_number.delete(0, END)

    ##############################################################

    def Patient_CheckOut(self):
        # page eight
        self.pageeight.tkraise()
        self.load = Image.open('Patient CheckOut.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pageeight, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        self.patient_checkout_ename = ttk.Entry(self.pageeight, width=25, font=('Arial', 12))
        self.patient_checkout_pid = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_name = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_gender = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_mobile_number = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_room_number = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_disease = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_unit_price = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_medicine_and_service_price = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))
        self.patient_checkout_total = ttk.Entry(self.pageeight, width=30, font=('Arial', 12))

        self.patient_checkout_ename.place(x=80, y=110)
        self.patient_checkout_pid.place(x=625, y=102)
        self.patient_checkout_name.place(x=625, y=142)
        self.patient_checkout_gender.place(x=625, y=182)
        self.patient_checkout_mobile_number.place(x=625, y=222)
        self.patient_checkout_room_number.place(x=625, y=262)
        self.patient_checkout_disease.place(x=625, y=302)
        self.patient_checkout_unit_price.place(x=625, y=342)
        self.patient_checkout_medicine_and_service_price.place(x=625, y=382)
        self.patient_checkout_total.place(x=625, y=422)

        self.patient_checkout_name_list = Listbox(self.pageeight, selectmode=SINGLE, height=20, width=35)
        self.patient_checkout_name_list.place(x=80, y=160)
        self.patient_checkout_scroll = Scrollbar(self.pageeight, orient=VERTICAL)
        self.patient_checkout_name_list.configure(yscrollcommand=self.patient_checkout_scroll.set)
        self.patient_checkout_scroll.configure(command=self.patient_checkout_name_list.yview)
        self.patient_checkout_scroll.place(x=290, y=160, height=324)

        Button(self.pageeight, text='Submit', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_checkout_submit_button).place(x=340, y=107)
        Button(self.pageeight, text='Reset', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_checkout_clean_button).place(x=565, y=500)
        Button(self.pageeight, text='Total', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_checkout_total_button).place(x=705, y=500)
        Button(self.pageeight, text='CheckOut', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.patient_checkout_checkout_button).place(x=845, y=500)

        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT name FROM PATIENT")
        data = c.fetchall()
        for i in data:
            self.patient_checkout_name_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.patient_checkout_name_list.bind('<<ListboxSelect>>', self.patient_checkout_on_click)

    def patient_checkout_on_click(self, event):
        self.patient_checkout_ename.delete(0, END)
        index = self.patient_checkout_name_list.curselection()
        self.patient_checkout_select = index

        self.patient_checkout_ename.insert(0, self.patient_checkout_name_list.get(self.patient_checkout_select))

    def patient_checkout_submit_button(self):
        self.patient_checkout_ename.state(['disabled'])
        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_pid.insert(0, i)
        self.patient_checkout_pid.state(['disabled'])
        #######################################################
        c.execute("SELECT name FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_name.insert(0, i)
        self.patient_checkout_name.state(['disabled'])
        #########################################################
        c.execute("SELECT gender FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_gender.insert(0, i)
        self.patient_checkout_gender.state(['disabled'])
        #########################################################
        c.execute("SELECT room_number FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_room_number.insert(0, i)
        self.patient_checkout_room_number.state(['disabled'])
        #######################################################@@
        c.execute("SELECT mobile_number FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_mobile_number.insert(0, i)
        self.patient_checkout_mobile_number.state(['disabled'])
        #######################################################@@
        c.execute("SELECT disease FROM PATIENT WHERE name = ? ", (self.patient_checkout_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.patient_checkout_disease.insert(0, i)
        self.patient_checkout_disease.state(['disabled'])

    def patient_checkout_checkout_button(self):
        date = datetime.datetime.now()
        try:
            date_out = date.strftime('%Y/%m/%d %H:%M')
            name = self.patient_checkout_name_list.get(self.patient_checkout_select)
            payment = int(self.patient_checkout_total.get())
            print(date)
            print(name)
            print(payment)

            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            c.execute(" UPDATE RECORD SET date_out = ? WHERE name = ?", (date_out, name,))

            c.execute(" UPDATE RECORD SET payment = ? WHERE name = ?", (payment, name,))

            c.execute("DELETE FROM PATIENT WHERE name = ? ", (name,))
            conn.commit()

            c.close()
            conn.close()

            self.patient_checkout_clean_button()
            messagebox.showinfo(title='Remove Staff Member', message='Staff Member Remove Submitted!')
        except Exception:
            messagebox.showwarning('ERROR', 'Invalid Input')
            self.patient_checkout_clean_button()

    def patient_checkout_total_button(self):

        try:
            unite_price = int(self.patient_checkout_unit_price.get())
            medicine_and_service_price = int(self.patient_checkout_medicine_and_service_price.get())
            total = unite_price + medicine_and_service_price
            self.patient_checkout_total.insert(0, total)
            self.patient_checkout_total.state(['disabled'])
        except Exception:
            self.patient_checkout_clean_button()
            messagebox.showwarning('ERROR', 'Invalid Entery')

    def patient_checkout_clean_button(self):
        self.patient_checkout_ename.state(['!disabled'])
        self.patient_checkout_pid.state(['!disabled'])
        self.patient_checkout_name.state(['!disabled'])
        self.patient_checkout_gender.state(['!disabled'])
        self.patient_checkout_mobile_number.state(['!disabled'])
        self.patient_checkout_disease.state(['!disabled'])
        self.patient_checkout_room_number.state(['!disabled'])
        self.patient_checkout_total.state(['!disabled'])

        self.patient_checkout_ename.delete(0, END)
        self.patient_checkout_pid.delete(0, END)
        self.patient_checkout_name.delete(0, END)
        self.patient_checkout_gender.delete(0, END)
        self.patient_checkout_mobile_number.delete(0, END)
        self.patient_checkout_disease.delete(0, END)
        self.patient_checkout_room_number.delete(0, END)
        self.patient_checkout_unit_price.delete(0, END)
        self.patient_checkout_medicine_and_service_price.delete(0, END)
        self.patient_checkout_total.delete(0, END)

    ############################################################

    def Staff_Informaiton(self):
        # page nine
        self.pagenine.tkraise()
        self.load = Image.open('Staff Informaiton.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pagenine, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        self.staff_informaiton_ename = ttk.Entry(self.pagenine, width=25, font=('Arial', 12))
        self.staff_informaiton_id = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_name = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_gender = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_position = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_salary = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_mobile_number = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))
        self.staff_informaiton_address = ttk.Entry(self.pagenine, width=30, font=('Arial', 12))

        self.staff_informaiton_ename.place(x=100, y=150)
        self.staff_informaiton_id.place(x=625, y=153)
        self.staff_informaiton_name.place(x=625, y=193)
        self.staff_informaiton_gender.place(x=625, y=233)
        self.staff_informaiton_position.place(x=625, y=273)
        self.staff_informaiton_salary.place(x=625, y=313)
        self.staff_informaiton_mobile_number.place(x=625, y=353)
        self.staff_informaiton_address.place(x=625, y=393)

        self.staff_informaiton_name_list = Listbox(self.pagenine, selectmode=SINGLE, height=20, width=35)
        self.staff_informaiton_name_list.place(x=100, y=200)
        self.staff_scroll = Scrollbar(self.pagenine, orient=VERTICAL)
        self.staff_informaiton_name_list.configure(yscrollcommand=self.staff_scroll.set)
        self.staff_scroll.configure(command=self.staff_informaiton_name_list.yview)
        self.staff_scroll.place(x=310, y=200, height=324)

        Button(self.pagenine, text='Submit', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.staff_informaiton_submit_button).place(x=360, y=147)
        Button(self.pagenine, text='Reset', width=15, font=('Arial', 10),
               relief=GROOVE, command=self.staff_information_clean_button).place(x=705, y=470)

        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT name FROM STAFF")
        data = c.fetchall()
        for i in data:
            self.staff_informaiton_name_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.staff_informaiton_name_list.bind('<<ListboxSelect>>', self.staff_on_click)

    def staff_on_click(self, event):
        self.staff_informaiton_ename.delete(0, END)
        index = self.staff_informaiton_name_list.curselection()
        self.staff_select = index

        self.staff_informaiton_ename.insert(0, self.staff_informaiton_name_list.get(self.staff_select))

    def staff_informaiton_submit_button(self):
        self.staff_informaiton_ename.state(['disabled'])
        conn = sqlite3.connect('Gurpreet.db')
        c = conn.cursor()
        c.execute("SELECT id FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_id.insert(0, i)
        self.staff_informaiton_id.state(['disabled'])
        #######################################################
        c.execute("SELECT name FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_name.insert(0, i)
        self.staff_informaiton_name.state(['disabled'])
        #########################################################
        c.execute("SELECT gender FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_gender.insert(0, i)
        self.staff_informaiton_gender.state(['disabled'])
        #########################################################
        c.execute("SELECT position FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_position.insert(0, i)
        self.staff_informaiton_position.state(['disabled'])
        #######################################################@@
        c.execute("SELECT salary FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_salary.insert(0, i)
        self.staff_informaiton_salary.state(['disabled'])
        #######################################################@@
        c.execute("SELECT mobile_number FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_mobile_number.insert(0, i)
        self.staff_informaiton_mobile_number.state(['disabled'])
        #######################################################@@
        c.execute("SELECT address FROM STAFF WHERE name = ? ", (self.staff_informaiton_ename.get(),))
        data = c.fetchone()
        for i in data:
            self.staff_informaiton_address.insert(0, i)
        self.staff_informaiton_address.state(['disabled'])
        c.close()
        conn.close()

        #######################################################@@

    def staff_information_clean_button(self):
        self.staff_informaiton_ename.state(['!disabled'])
        self.staff_informaiton_id.state(['!disabled'])
        self.staff_informaiton_name.state(['!disabled'])
        self.staff_informaiton_gender.state(['!disabled'])
        self.staff_informaiton_position.state(['!disabled'])
        self.staff_informaiton_salary.state(['!disabled'])
        self.staff_informaiton_mobile_number.state(['!disabled'])
        self.staff_informaiton_address.state(['!disabled'])

        self.staff_informaiton_ename.delete(0, END)
        self.staff_informaiton_id.delete(0, END)
        self.staff_informaiton_name.delete(0, END)
        self.staff_informaiton_gender.delete(0, END)
        self.staff_informaiton_position.delete(0, END)
        self.staff_informaiton_salary.delete(0, END)
        self.staff_informaiton_mobile_number.delete(0, END)
        self.staff_informaiton_address.delete(0, END)

    ##############################################################

    def About(self):
        # page ten
        self.pageten.tkraise()
        self.load = Image.open('about.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.pageten, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        self.commant = Label(self.pageten, text='For any suggestions click here..', font=('Arial', 12, 'bold'),
                             bg='#ecaf10', fg='white')
        self.commant.place(x=700, y=500)
        self.commant.bind('<ButtonPress>', self.suggestion)

    def suggestion(self, event):
        # Toplevel root
        self.root1 = Toplevel(self.root)
        self.root1.geometry('440x360+600+300')
        self.root1.title('Feedback')
        self.root1.resizable(False, False)

        self.load = Image.open('feedback.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = ttk.Label(self.root1, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0)

        Label(self.root1, text='Name', bg='#e7e7e6', font=('Arial', 12)).place(x=26, y=112)
        Label(self.root1, text='Email', bg='#e7e7e6', font=('Arial', 12)).place(x=229, y=112)
        Label(self.root1, text='Comment', bg='#e7e7e6', font=('Arial', 12)).place(x=26, y=157)

        self.name_feedentry = Entry(self.root1, width=30)
        self.name_feedentry.place(x=26, y=135)
        self.email_feedentry = Entry(self.root1, width=30)
        self.email_feedentry.place(x=229, y=135)
        self.comment_feedentry = Text(self.root1, width=55, height=8, font=('Arial', 10))
        self.comment_feedentry.place(x=25, y=180)

        Button(self.root1, width=10, text='Clean', relief=GROOVE, command=self.feedback_clean).place(x=253, y=325)
        Button(self.root1, width=10, text='Submit', relief=GROOVE, command=self.feedback_submit).place(x=338, y=325)

    def feedback_submit(self):

        try:
            conn = sqlite3.connect('Gurpreet.db')
            c = conn.cursor()
            c.execute(" INSERT INTO FEEDBACK (name,email,comment) VALUES (?,?,?)", (self.name_feedentry.get(),
                                                                                    self.email_feedentry.get(),
                                                                                    self.comment_feedentry.get(1.0,
                                                                                                               'end')))
            conn.commit()
            c.close()
            conn.close()

        except:
            messagebox.showwarning('ERROR', 'Invalid Entery')
            self.feedback_clean()

        else:
            messagebox.showinfo(title='Feedback', message='Comment Submitted!')
            self.feedback_clean()

    def feedback_clean(self):
        self.name_feedentry.delete(0, 'end')
        self.email_feedentry.delete(0, 'end')
        self.comment_feedentry.delete(1.0, 'end')


#############################################################

hospital = hospital()
hospital.root.mainloop()
