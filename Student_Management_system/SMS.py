from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        title = Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #============All Varible===============
        self.roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.Address_var = StringVar()
        self.Search_by= StringVar()
        self.Search_txt= StringVar()



        #============ManageFrame===============
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=595)

        m_title = Label(Manage_Frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,padx=30,pady=20)

        lbl_row = Label(Manage_Frame,text="Roll No",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_row.grid(row=1,column=0,pady=10,padx=20,sticky="w") 
        txt_Roll = Entry(Manage_Frame,textvariable=self.roll_No_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        
        lbl_Name = Label(Manage_Frame, text="Name:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w") 
        txt_Name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email = Label(Manage_Frame,text="Email:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w") 
        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w") 

        lbl_Gender =Label(Manage_Frame, text="Gender:",bg="blue", fg="white",font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4,column=0, padx=20,pady=5,sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",16, "bold"),state="readonly") 
        combo_gender['values'] = ("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=5,sticky="w")

        lbl_Contact = Label(Manage_Frame,text="Contact:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w") 
        txt_Contact= Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_Dob = Label(Manage_Frame,text="D.O.B:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="w") 
        txt_Dob= Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address = Label(Manage_Frame,text="Address:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w") 
        self.txt_Address= Text(Manage_Frame,width=21, height=2,font=("times new roman",18,"bold"))
        self.txt_Address.grid(row=7,column=1,pady=5,padx=20,sticky="w")

        #================= button frame ===================
        btn_frame =Frame(Manage_Frame,bd=3,relief=RIDGE,bg="Black")
        btn_frame.place(x=15,y=525,width=410)
        
        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,text="update",width=10,command=self.update).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn = Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)



        #============Details Frame===============
        Details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Details_Frame.place(x=500,y=100,width=780,height=595)

        lbl_Search = Label(Details_Frame,text="search By",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        combo_Search = ttk.Combobox(Details_Frame,textvariable=self.Search_by,font=("times new roman",13, "bold"),width=10,state='readonly') 
        combo_Search['values'] = ("Roll_no","Name","Contact")
        combo_Search.grid(row=0,column=1,padx=20,pady=5,sticky="w")
        txt_Search= Entry(Details_Frame, textvariable=self.Search_txt,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        txt_Search.grid(row=0, column=2, padx=20,pady=5, sticky="w")

        Searchbtn = Button(Details_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Details_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #============Table Frame===============
        Table_Frame = Frame(Details_Frame,bd=4,relief=RIDGE,bg="Crimson")
        Table_Frame.place(x=10,y=70,width=750,height=500)

        scroll_x =  Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y =  Scrollbar(Table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Address",text="Address")

        self.student_table['show']='headings'
        self.student_table.column("roll",width=80)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=80)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor )
        self.fetch_data()

    def add_students(self):
        if self.roll_No_var.get()=="" or self.name_var.get()=="":
              messagebox.showerror("Error","all fields are required to fill")
        else:
         con = pymysql.connect(host="localhost",user="root",password="",database="sms2")
         cur=con.cursor()
         cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_No_var.get(),
                                                                       self.name_var.get(),
                                                                       self.email_var.get(),
                                                                       self.gender_var.get(),
                                                                       self.contact_var.get(),
                                                                       self.dob_var.get(),
                                                                       self.txt_Address.get('1.0',END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()                                                     
        con.close()
        messagebox.showinfo("success","Recored has been inserted successfully")

    def fetch_data(self):
             
        con =pymysql.connect(host="localhost", user="root", password="", database="sms2")
        cur = con.cursor()
        cur.execute("Select * from Students")
        rows = cur. fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        curosor_row = self.student_table.focus()
        contents = self.student_table.item(curosor_row)
        row =contents['values']
        self.roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
                    
    def clear(self):
        self.roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_Address.delete("1.0",END)
                        
                
    def update(self):
        con =pymysql.connect(host="localhost", user="root",password="",database="sms2")
        cur = con.cursor()
        cur.execute("Update students set name = %s, email = %s, gender = %s, contact = %s, dod = %s, address = %s where roll_no = %s",(
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.txt_Address.get('1.0',END),
                        self.roll_No_var.get()
                       ))  
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("success"," Record has been update successfully")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root",password="",database="sms2")
        cur = con.cursor()
        cur.execute("Delete from students where roll_no =%s",self.roll_No_var.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root",password="",database="sms2")
        cur = con.cursor()
        cur.execute("Select * from students where" +str(self.Search_by.get()) +" Like '%"+str(self.Search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()


class student():
     pass
root = Tk()
obj= Student(root)
root.mainloop()
        