from tkinter import*
from PIL import Image,ImageTk
from tkinter import END, END, END, NoDefaultRoot, NoDefaultRoot, NoDefaultRoot, SEL, SEL, SEL, Event, Event, Event, RIDGE, RIDGE, RIDGE, W, W, W, messagebox
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector


class Room_win:
        def __init__(self,root):
               self.root=root
               self.root.title("ROOM MANAGEMENT")
               self.root.geometry("1662x850+255+225")
                # ================variable=============
               self.var_contact=StringVar()
               self.var_checkin=StringVar()
               self.var_checkout=StringVar()
               self.var_roomtype=StringVar()
               self.var_roomavailable=StringVar()
               self.var_meal=StringVar()
               self.var_noofdays=StringVar()
               self.var_paidtax=StringVar()
               self.var_actualtotal=StringVar()
               self.var_total=StringVar()

# =========================title=========
               lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
               lbl_title.place(x=0,y=0,width=1665,height=50)


               img2=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\premium logo.png")
               img2=img2.resize((100,50))
               self.photoimg2=ImageTk.PhotoImage(img2)

               lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
               lblimg.place(x=5,y=4,width=100,height=40)

# ===============LABEL FRAME+============
        
               Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking Details",font=("arial",12,"bold"),padx=2)
               Labelframeleft.place(x=5,y=50,width=425,height=690)
# ==============lables and entries===========
# customer contact
               lbl_cust_contact=Label(Labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
               lbl_cust_contact.grid(row=0,column=0,sticky=W)

               entry_contact=ttk.Entry(Labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
               entry_contact.grid(row=0,column=1,sticky=W)

# fatch button
               btnfatch=Button(Labelframeleft,text="Fatch Data",command=self.fatch_contact,font=("arial",9,"bold"),bg="black",fg="gold",width=9)
               btnfatch.place(x=340,y=4)
 
           
 # check in date
               chk_in=Label(Labelframeleft,text="Check in Date:",font=("arial",12,"bold"),padx=2,pady=6)
               chk_in.grid(row=1,column=0,sticky=W)

               txtcheckin=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
               txtcheckin.grid(row=1,column=1)
 # check in time
               chk_in=Label(Labelframeleft,text="Check in time:",font=("arial",12,"bold"),padx=2,pady=6)
               chk_in.grid(row=2,column=0,sticky=W)

               txtcheckin=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
               txtcheckin.grid(row=2,column=1)
 # check out date
               mname=Label(Labelframeleft,text="Check out Date:",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=3,column=0,sticky=W)

               txtcheckout=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
               txtcheckout.grid(row=3,column=1)
 # check out time
               mname=Label(Labelframeleft,text="Check out time:",font=("arial",12,"bold"),padx=2,pady=6)
               mname.grid(row=4,column=0,sticky=W)

               txtcheckout=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
               txtcheckout.grid(row=4,column=1)
 # room type combobox
               label_roomtype=Label(Labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
               label_roomtype.grid(row=5,column=0,sticky=W)

               conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("select RoomType from details")
               Ide=my_cursor.fetchall()
               
               combo_roomtype=ttk.Combobox(Labelframeleft,textvariable=self.var_roomtype,font=("arial",13,"bold"),width=27,state="readonly")
               combo_roomtype["value"]=Ide
               combo_roomtype.current(0)
               combo_roomtype.grid(row=5,column=1)

 #Available room
               room_available=Label(Labelframeleft,text="Availble room:",font=("arial",12,"bold"),padx=2,pady=6)
               room_available.grid(row=6,column=0,sticky=W)
             
               conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("select RoomNo from details")
               rows=my_cursor.fetchall()

               combo_roomnumber=ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=27,state="readonly")
               combo_roomnumber["value"]=rows
               combo_roomnumber.current(0)
               combo_roomnumber.grid(row=6,column=1)

 #meal
               lblmeal=Label(Labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
               lblmeal.grid(row=7,column=0,sticky=W)

               txtmeal=ttk.Entry(Labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
               txtmeal.grid(row=7,column=1)

 #No of days
               lblnoofDays=Label(Labelframeleft,text="No. Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
               lblnoofDays.grid(row=8,column=0,sticky=W)

               txtnoofdays=ttk.Entry(Labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
               txtnoofdays.grid(row=8,column=1)

 #Paid Tax
               Lblpaidtax=Label(Labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
               Lblpaidtax.grid(row=9,column=0,sticky=W)

               txtpaidtax=ttk.Entry(Labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
               txtpaidtax.grid(row=9,column=1)

 #Sub total
               lblsubtotalamt=Label(Labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
               lblsubtotalamt.grid(row=10,column=0,sticky=W)

               txtsbttlamt=ttk.Entry(Labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
               txtsbttlamt.grid(row=10,column=1)

 #total cost
               lblttlcost=Label(Labelframeleft,text="Total cost",font=("arial",12,"bold"),padx=2,pady=6)
               lblttlcost.grid(row=11,column=0,sticky=W)

               txtttlcost=ttk.Entry(Labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
               txtttlcost.grid(row=11,column=1)
# =====bill button ============
               
               btnbill=Button(Labelframeleft,text="Bill",command=self.Total,font=("arial",15,"bold"),bg="black",fg="gold",width=10)
               btnbill.grid(row=12,column=0,padx=1,sticky=W) 

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
# =============image====================
                

               img3=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\ttttttttt.jpg")
               img3=img3.resize((700,315))
               self.photoimg3=ImageTk.PhotoImage(img3)

               lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
               lblimg.place(x=650,y=50,width=1320,height=260)

# ==========table frame and search system===========
        
               table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
               table_frame.place(x=435,y=282,width=1225,height=458)

               lbl_search_by=Label(table_frame,text="Search By:",font=("arial",13,"bold"),bg="red",fg="white",width=15)
               lbl_search_by.grid(row=0,column=0,sticky=W,padx=2)

               self.search_var=StringVar()
               combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",13,"bold"),width=27,state="readonly")
               combo_search["value"]=("Contact")
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
               details_table.place(x=0,y=50,width=1217,height=385)
               # ============== definig scroll bar===============
               scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
               scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)  

               self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","Roomtype","roomavailable","meal","no_of_days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
               scroll_x.pack(side=BOTTOM,fill=X)
               scroll_y.pack(side=RIGHT,fill=Y)
        
               scroll_x.config(command=self.room_table.xview)
               scroll_y.config(command=self.room_table.yview)


               self.room_table.heading("contact",text="Contact")
               self.room_table.heading("checkin",text="Check-in")
               self.room_table.heading("checkout",text="Check-out")
               self.room_table.heading("Roomtype",text="Room Type")
               self.room_table.heading("roomavailable",text="Room No")
               self.room_table.heading("meal",text="Meal")
               self.room_table.heading("no_of_days",text="NoOfDays")


               self.room_table["show"]="headings"

               self.room_table.column("contact",width=110)
               self.room_table.column("checkin",width=110)
               self.room_table.column("checkout",width=110)
               self.room_table.column("Roomtype",width=110)
               self.room_table.column("roomavailable",width=110)
               self.room_table.column("meal",width=110)
               self.room_table.column("no_of_days",width=110)
               self.room_table.pack(fill=BOTH,expand=1)
               self.room_table.bind("<ButtonRelease-1>",self.get_cusor)
               self.fetch_data()
                


# =================data button add===============
        def add_data(self): 
              
              if self.var_contact.get()=="" or self.var_checkin.get()=="":
                    messagebox.showerror("Error","All feilds are Required",parent=self.root)
              else:
                   try:
                
                       conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_contact.get(),
                                                                                          self.var_checkin.get(),
                                                                                          self.var_checkout.get(),
                                                                                          self.var_roomtype.get(),
                                                                                          self.var_roomavailable.get(),
                                                                                          self.var_meal.get(),
                                                                                          self.var_noofdays.get()
                                                                                    ))
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","Room booked",parent=self.root)
                   except Exception as es:
                         messagebox.showwarning("Warning",f"Something Went Worng:{str(es)}",parent=self.root)
# ==================fetch data ===========
        def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from room")
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("",END,values=i)
                    conn.commit()
              conn.close()    


      #   ================get cursor data =============
        def get_cusor(self,event=""):
              
              cursor_row=self.room_table.focus()
              content=self.room_table.item(cursor_row)
              row=content["values"]

              if row:
                    
               self.var_contact.set(row[0]),
               self.var_checkin.set(row[1]),
               self.var_checkout.set(row[2]),
               self.var_roomtype.set(row[3]),
               self.var_roomavailable.set(row[4]),
               self.var_meal.set(row[5]),
               self.var_noofdays.set(row[6])

#  ============update button ============
        def update(self):
                   
                   if self.var_contact.get()=="":
                    messagebox.showerror("Erroor","Please enter mobile number",parent=self.root)
                   else:
                                      
                     conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(                          
                                                                                                                                                       
                                                                                                                                                       self.var_checkin.get(),
                                                                                                                                                       self.var_checkout.get(),
                                                                                                                                                       self.var_roomtype.get(),
                                                                                                                                                       self.var_roomavailable.get(),
                                                                                                                                                       self.var_meal.get(),
                                                                                                                                                       self.var_noofdays.get(),
                                                                                                                                                       self.var_contact.get()
                                                                                                                                                ))
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                     messagebox.showinfo("Update","Room  details has been updated successfully",parent=self.root)
#     ======================delete button function======
        def mDelete(self):
              mDelete=messagebox.askyesno("Hotel Managment System","Do you want delete this costomer",parent=self.root)
              if mDelete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                    my_cursor=conn.cursor()
                    query="delete from room where Contact=%s"
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query, value)
              else:
                    if not mDelete:
                          return
              conn.commit()
              self.fetch_data()
              conn.close()

        def reset(self):
              
              self.var_contact.set(""),
              self.var_checkin.set(""),
              self.var_checkout.set(""),
              self.var_roomtype.set("Single"),
              self.var_roomavailable.set(""),
              self.var_meal.set(""),
              self.var_noofdays.set(""),
              self.var_paidtax.set(""),
              self.var_actualtotal.set(""),
              self.var_total.set("")



# ================ALl data fetch==================
        def fatch_contact(self):
              if self.var_contact.get()=="":
                    messagebox.showerror("Error","please enter contact number",parent=self.root)
              else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                    my_cursor=conn.cursor()   
                    query=("select name from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()


                    if row==None:
                          messagebox.showerror("Eroor","This number not found",parent=self.root)
                    else:
                          conn.commit()
                          conn.close()

                          showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                          showdataframe.place(x=455,y=55,width=300,height=220)

                          lblname=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                          lblname.place(x=0,y=0)      

                          lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl.place(x=110,y=0)      

                        # ============Gender========
                          conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                          my_cursor=conn.cursor()   
                          query=("select gender from customer where mobile=%s")
                          value=(self.var_contact.get(),)
                          my_cursor.execute(query,value)
                          row=my_cursor.fetchone()
                          
                          lblgender=Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
                          lblgender.place(x=0,y=30)      

                          lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl2.place(x=110,y=30)
                        #=============email===================
                          conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                          my_cursor=conn.cursor()   
                          query=("select email from customer where mobile=%s")
                          value=(self.var_contact.get(),)
                          my_cursor.execute(query,value)
                          row=my_cursor.fetchone()
                          
                          lblemail=Label(showdataframe,text="E-mail:",font=("arial",12,"bold"))
                          lblemail.place(x=0,y=60)      

                          lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl3.place(x=110,y=60)

                        #===========nationality============
                          conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                          my_cursor=conn.cursor()   
                          query=("select nationality from customer where mobile=%s")
                          value=(self.var_contact.get(),)
                          my_cursor.execute(query,value)
                          row=my_cursor.fetchone()
                          
                          lblnationality=Label(showdataframe,text="Nationality:",font=("arial",12,"bold"))
                          lblnationality.place(x=0,y=90)      

                          lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl4.place(x=110,y=90)

                        #===========Adress============
                          conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                          my_cursor=conn.cursor()   
                          query=("select address from customer where mobile=%s")
                          value=(self.var_contact.get(),)
                          my_cursor.execute(query,value)
                          row=my_cursor.fetchone()
                          
                          lbladdress=Label(showdataframe,text="Address:",font=("arial",12,"bold"))
                          lbladdress.place(x=0,y=120)      

                          lbl5=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl5.place(x=110,y=120)
                        #===========Adress============
                          conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                          my_cursor=conn.cursor()   
                          query=("select ref from customer where mobile=%s")
                          value=(self.var_contact.get(),)
                          my_cursor.execute(query,value)
                          row=my_cursor.fetchone()
                          
                          lblref=Label(showdataframe,text="Costomer ref.:",font=("arial",12,"bold"))
                          lblref.place(x=0,y=150)      

                          lbl6=Label(showdataframe,text=row,font=("arial",12,"bold"))
                          lbl6.place(x=110,y=150)
 # search system =======================
                          
                

        def search(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
              my_cursor=conn.cursor()

              my_cursor.execute("SELECT * FROM room WHERE Contact LIKE '%" + str(self.txt_search.get()) + "%'")

              rows=my_cursor.fetchall()
              if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                          self.room_table.insert("",END,values=i)
              conn.commit()    
              conn.close()




        def Total(self):
              inDate=self.var_checkin.get()
              outDate=self.var_checkout.get()
              inDate=datetime.strptime(inDate, "%d/%m/%y")
              outDate=datetime.strptime(outDate, "%d/%m/%y")
              self.var_noofdays.set(abs(outDate-inDate).days)
            #  bill of breakfast and single room with date
              if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
                    q1=float(300)
                    q2=float(500)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)
            #  bill of breakfast and double room with date

              elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)

            #  bill of breakfast and luxary room with date
                          
              elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxary"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)
            #  bill of lunch and single room with date
                          
              if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)
                  #  bill of lunch and double room with date
                          
              if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)
            #  bill of lunch and luxary room with date
                          
              if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxary"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)            
            #  bill of dinner and single room with date
                          
              if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)            
            #  bill of dinner and double room with date
                          
              if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)            
            #  bill of dinner and luxary room with date
                          
              if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxary"):
                    q1=float(300)
                    q2=float(700)
                    q3=float(self.var_noofdays.get())
                    q4=float(q1+q2)
                    q5=float(q3+q4)
                    tax="Rs."+str("%.2f"%((q5)*0.1))
                    ST="Rs."+str("%.2f"%((q5)))
                    TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                    self.var_paidtax.set(tax)
                    self.var_actualtotal.set(ST)
                    self.var_total.set(TT)            

                          


if __name__=="__main__":
    root=Tk()
    obj=Room_win(root)
    root.mainloop()