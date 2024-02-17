from tkinter import*
from PIL import Image,ImageTk
from tkinter import END, END, END, NoDefaultRoot, NoDefaultRoot, NoDefaultRoot, SEL, SEL, SEL, Event, Event, Event, RIDGE, RIDGE, RIDGE, W, W, W, messagebox
from tkinter import ttk
import random
import mysql.connector

class Cust_Win:
        def __init__(self,root):
               self.root=root
               self.root.title("CUSTOMER MANAGEMENT")
               self.root.geometry("1662x850+255+225")

        #        ==========variables===========
               self.var_ref=StringVar()
               x=random.randint(1000,9999)
               self.var_ref.set(str(x))

               self.var_cust_name=StringVar()
               self.var_mother=StringVar()
               self.var_father=StringVar()
               self.var_gender=StringVar()
               self.var_post_no=StringVar()
               self.var_mobile=StringVar()
               self.var_email=StringVar()
               self.var_nationality=StringVar()
               self.var_id_proof=StringVar()
               self.var_id_number=StringVar()
               self.var_Address=StringVar()

               



# ==============TITLE============
               lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
               lbl_title.place(x=0,y=0,width=1662,height=50)


               img2=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\premium logo.png")
               img2=img2.resize((100,50))
               self.photoimg2=ImageTk.PhotoImage(img2)

               lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
               lblimg.place(x=5,y=4,width=100,height=40)
# ===============LABEL FRAME+============
        
               Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
               Labelframeleft.place(x=5,y=50,width=425,height=690)
# ==============lables and entries===========
        # custref
               lbl_cust_ref=Label(Labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
               lbl_cust_ref.grid(row=0,column=0,sticky=W)

               entry_ref=ttk.Entry(Labelframeleft,width=29,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
               entry_ref.grid(row=0,column=1)
        
        # cust name 
               cname=Label(Labelframeleft,text="Customer name",font=("arial",12,"bold"),padx=2,pady=6)
               cname.grid(row=1,column=0,sticky=W)

               txtcname=ttk.Entry(Labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
               txtcname.grid(row=1,column=1)
        # mother name
               mname=Label(Labelframeleft,text="Mother name",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=2,column=0,sticky=W)

               txtmname=ttk.Entry(Labelframeleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))
               txtmname.grid(row=2,column=1)
        #father name
               fname=Label(Labelframeleft,text="Father name",font=("arial",12,"bold"),padx=2,pady=6)
               fname.grid(row=3,column=0,sticky=W)

               txtmname=ttk.Entry(Labelframeleft,textvariable=self.var_father,width=29,font=("arial",13,"bold"))
               txtmname.grid(row=3,column=1)

        # gender combobox
               label_gender=Label(Labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
               label_gender.grid(row=4,column=0,sticky=W)

               combo_geder=ttk.Combobox(Labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
               combo_geder["value"]=("Male","Female","Other")
               combo_geder.current(0)
               combo_geder.grid(row=4,column=1)

        # post code
               post_code=Label(Labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
               post_code.grid(row=5,column=0,sticky=W)

               txtpostcode=ttk.Entry(Labelframeleft,textvariable=self.var_post_no,width=29,font=("arial",13,"bold"))
               txtpostcode.grid(row=5,column=1)

        # mobile number
               mobile_num=Label(Labelframeleft,text="Mobile number",font=("arial",12,"bold"),padx=2,pady=6)
               mobile_num.grid(row=6,column=0,sticky=W)

               txtmobile_num=ttk.Entry(Labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
               txtmobile_num.grid(row=6,column=1)

        # email
               e_mail=Label(Labelframeleft,text="E-mail",font=("arial",12,"bold"),padx=2,pady=6)
               e_mail.grid(row=7,column=0,sticky=W)

               txtemail=ttk.Entry(Labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
               txtemail.grid(row=7,column=1)

        # nationality
               mname=Label(Labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=8,column=0,sticky=W)

               combo_nationality=ttk.Combobox(Labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
               combo_nationality["value"]=("Indian","American","Italian","Russian")
               combo_nationality.current(0)
               combo_nationality.grid(row=8,column=1)



        # idproof type combobox
               mname=Label(Labelframeleft,text="ID Proof type",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=9,column=0,sticky=W)

               combo_id_type=ttk.Combobox(Labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
               combo_id_type["value"]=("PAN Card","Aadhaar","Driving licence","Passport")
               combo_id_type.current(1)
               combo_id_type.grid(row=9,column=1)


        # id number
               mname=Label(Labelframeleft,text="ID number",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=10,column=0,sticky=W)

               txtidnumber=ttk.Entry(Labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
               txtidnumber.grid(row=10,column=1)


        # address
               lbl_add=Label(Labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
               lbl_add.grid(row=11,column=0,sticky=W)

               txtaddress=ttk.Entry(Labelframeleft,textvariable=self.var_Address,width=29,font=("arial",13,"bold"))
               txtaddress.grid(row=11,column=1)

# =============buttons===============
               btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
               btn_frame.place(x=0,y=500,width=412,height=55)

               btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnAdd.grid(row=0,column=0,padx=1)

               btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnupdate.grid(row=0,column=1,padx=1)

               btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btndelete.grid(row=0,column=2,padx=1)

               btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnreset.grid(row=0,column=3,padx=1)
# ==========table frame and search system===========
        
               table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
               table_frame.place(x=435,y=50,width=1225,height=690)

               lbl_search_by=Label(table_frame,text="Search By:",font=("arial",13,"bold"),bg="red",fg="white",width=15)
               lbl_search_by.grid(row=0,column=0,sticky=W,padx=2)

               self.search_var=StringVar()
               combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",13,"bold"),width=27,state="readonly")
               combo_search["value"]=("Customer_ref")
               combo_search.grid(row=0,column=1,padx=2)

               self.txt_search=StringVar()
               txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("arial",13,"bold"))
               txtsearch.grid(row=0,column=2,padx=2)

               btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",13,"bold"),bg="black",fg="gold",width=14)
               btnsearch.grid(row=0,column=3,padx=1)

               btnshow=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",13,"bold"),bg="black",fg="gold",width=14)
               btnshow.grid(row=0,column=4,padx=1)
# ===============show data table================
               details_table=Frame(table_frame,bd=2,relief=RIDGE)
               details_table.place(x=0,y=50,width=1217,height=550)

# ============== definig scroll bar===============
               scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
               scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

               self.cust_Details_table=ttk.Treeview(details_table,columns=("ref","name","mname","fname","gender","post no.","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
               scroll_x.pack(side=BOTTOM,fill=X)
               scroll_y.pack(side=RIGHT,fill=Y)
        
               scroll_x.config(command=self.cust_Details_table.xview)
               scroll_y.config(command=self.cust_Details_table.yview)


               self.cust_Details_table.heading("ref",text="Customer Ref")
               self.cust_Details_table.heading("name",text="Costomer name")
               self.cust_Details_table.heading("mname",text="Mother name")
               self.cust_Details_table.heading("fname",text="Father name")
               self.cust_Details_table.heading("gender",text="Gender")
               self.cust_Details_table.heading("post no.",text="Post Code")
               self.cust_Details_table.heading("mobile",text="Mobile number")
               self.cust_Details_table.heading("email",text="E-mail")
               self.cust_Details_table.heading("nationality",text="Nationality")
               self.cust_Details_table.heading("idproof",text="ID Proof type")
               self.cust_Details_table.heading("idnumber",text="ID number")
               self.cust_Details_table.heading("address",text="Address")

               self.cust_Details_table["show"]="headings"

               self.cust_Details_table.column("ref",width=110)
               self.cust_Details_table.column("name",width=110)
               self.cust_Details_table.column("mname",width=110)
               self.cust_Details_table.column("fname",width=110)
               self.cust_Details_table.column("gender",width=110)
               self.cust_Details_table.column("post no.",width=110)
               self.cust_Details_table.column("mobile",width=110)
               self.cust_Details_table.column("email",width=110)
               self.cust_Details_table.column("nationality",width=110)
               self.cust_Details_table.column("idproof",width=110)
               self.cust_Details_table.column("idnumber",width=110)
               self.cust_Details_table.column("address",width=110)


               self.cust_Details_table.pack(fill=BOTH,expand=1)
               self.cust_Details_table.bind("<ButtonRelease-1>",self.get_cusor)
               self.fetch_data()



        def add_data(self):
              
              if self.var_mobile.get()=="" or self.var_mother.get()=="":
                    messagebox.showerror("Error","All feilds are Required",parent=self.root)
              else:
                   try:
                
                       conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ref.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_father.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post_no.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_Address.get()
                                                
                                                                                                        ))
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","Customer Has been added",parent=self.root)
                   except Exception as es:
                         messagebox.showwarning("Warning",f"Something Went Worng:{str(es)}",parent=self.root)
                         
        def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from customer")
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                    self.cust_Details_table.delete(*self.cust_Details_table.get_children())
                    for i in rows:
                        self.cust_Details_table.insert("",END,values=i)
                    conn.commit()
              conn.close()    
       # ==========get cursor =================
        def get_cusor(self,event=""):
              cursor_row=self.cust_Details_table.focus()
              content=self.cust_Details_table.item(cursor_row)
              row=content["values"] 

              if row:
                    
                     self.var_ref.set(row[0]),
                     self.var_cust_name.set(row[1]),
                     self.var_mother.set(row[2]),
                     self.var_father.set(row[3]),
                     self.var_gender.set(row[4]),
                     self.var_post_no.set(row[5]),
                     self.var_mobile.set(row[6]),
                     self.var_email.set(row[7]),
                     self.var_nationality.set(row[8]),
                     self.var_id_proof.set(row[9]),
                     self.var_id_number.set(row[10]),
                     self.var_Address.set(row[11])

        
        def update(self):
              if self.var_mobile.get()=="":
                    messagebox.showerror("Erroor","Please enter mobile number",parent=self.root)
              else:
                                      
                     conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update customer set name=%s,mname=%s,fname=%s,gender=%s,post_no=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                                                                                                                                                                                      
                                                                                                                                                                                      self.var_cust_name.get(),
                                                                                                                                                                                      self.var_mother.get(),
                                                                                                                                                                                      self.var_father.get(),
                                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                                      self.var_post_no.get(),
                                                                                                                                                                                      self.var_mobile.get(),
                                                                                                                                                                                      self.var_email.get(),
                                                                                                                                                                                      self.var_nationality.get(),
                                                                                                                                                                                      self.var_id_proof.get(),
                                                                                                                                                                                      self.var_id_number.get(),
                                                                                                                                                                                      self.var_Address.get(),
                                                                                                                                                                                      self.var_ref.get()
                                                                                                                                                                               ))
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                     messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
        def mDelete(self):
              mDelete=messagebox.askyesno("Hotel Managment System","Do you want delete this costomer",parent=self.root)
              if mDelete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                    my_cursor=conn.cursor()
                    query="delete from customer where ref=%s"
                    value=(self.var_ref.get(),)
                    my_cursor.execute(query, value)
              else:
                    if not mDelete:
                          return
              conn.commit()
              self.fetch_data()
              conn.close()
        
        def reset(self):
              # self.var_ref.set(""),
              self.var_cust_name.set(""),
              self.var_mother.set(""),
              self.var_father.set(""),
              # self.var_gender.set(""),
              self.var_post_no.set(""),
              self.var_mobile.set(""),
              self.var_email.set(""),
              # self.var_nationality.set(""),
              # self.var_id_proof.set(""),
              self.var_id_number.set(""),
              self.var_Address.set("")

              x=random.randint(1000,9999)
              self.var_ref.set(str(x))
        

        def search(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
              my_cursor=conn.cursor()

              my_cursor.execute("SELECT * FROM customer WHERE ref LIKE '%" + str(self.txt_search.get()) + "%'")

              rows=my_cursor.fetchall()
              if len(rows)!=0:
                    self.cust_Details_table.delete(*self.cust_Details_table.get_children())
                    for i in rows:
                          self.cust_Details_table.insert("",END,values=i)
              conn.commit()    
              conn.close()




if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
        