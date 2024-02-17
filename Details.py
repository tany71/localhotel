from tkinter import*
from PIL import Image,ImageTk
from tkinter import StringVar, StringVar, StringVar, END, END, END, NoDefaultRoot, NoDefaultRoot, NoDefaultRoot, SEL, SEL, SEL, Event, Event, Event, RIDGE, RIDGE, RIDGE, W, W, W, messagebox
from tkinter import ttk
import random
from time import sleep, strftime
from datetime import datetime
import mysql.connector


class Details_win:
        def __init__(self,root):
               self.root=root
               self.root.title("DETAILS ABOUT COSTOMER")
               self.root.geometry("1662x850+255+225")
# =========================title=========
               lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
               lbl_title.place(x=0,y=0,width=1662,height=50)


               img2=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\premium logo.png")
               img2=img2.resize((100,50))
               self.photoimg2=ImageTk.PhotoImage(img2)

               lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
               lblimg.place(x=5,y=4,width=100,height=40)

# ===============LABEL FRAME+============
        
               Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
               Labelframeleft.place(x=5,y=50,width=620,height=500)


               # blank
               lbl_floor=Label(Labelframeleft,text="  ",font=("arial",13,"bold"),padx=2,pady=6)
               lbl_floor.grid(row=0,column=0,sticky=W)


               # floor
               lbl_floor=Label(Labelframeleft,text="Floor:",font=("arial",13,"bold"),padx=2,pady=6)
               lbl_floor.grid(row=1,column=0,sticky=W)
               
               self.var_floor=StringVar()
               entry_floor=ttk.Entry(Labelframeleft,textvariable=self.var_floor,width=29,font=("arial",14,"bold"))
               entry_floor.grid(row=1,column=1,sticky=W)

               # room number
               roomnumb=Label(Labelframeleft,text="Room No.:",font=("arial",13,"bold"),padx=2,pady=6)
               roomnumb.grid(row=2,column=0,sticky=W)
               
               self.var_roomnum=StringVar()
               txtroomnumb=ttk.Entry(Labelframeleft,textvariable=self.var_roomnum,width=29,font=("arial",14,"bold"))
               txtroomnumb.grid(row=2,column=1)
               # room type
               roomtype=Label(Labelframeleft,text="Room Type:",font=("arial",13,"bold"),padx=2,pady=6)
               roomtype.grid(row=3,column=0,sticky=W)

               self.var_roomtype=StringVar()
               txtroomtype=ttk.Entry(Labelframeleft,textvariable=self.var_roomtype,width=29,font=("arial",14,"bold"))
               txtroomtype.grid(row=3,column=1)

# ===============.buttons==================
               btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
               btn_frame.place(x=450,y=35,width=100,height=200)

               btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnAdd.grid(row=0,column=0,padx=1)

               btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnupdate.grid(row=1,column=0,padx=1)
 
               btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btndelete.grid(row=2,column=0,padx=1)

               btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10,height=2)
               btnreset.grid(row=3,column=0,padx=1)


# ==========table frame and search system===========
        
               table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room details",font=("arial",12,"bold"),padx=2)
               table_frame.place(x=700,y=50,width=650,height=500)
                # =======scroll bar===========
               scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
               scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)  

               self.room_table=ttk.Treeview(table_frame,columns=("floor","RoomNo","Roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
               scroll_x.pack(side=BOTTOM,fill=X)
               scroll_y.pack(side=RIGHT,fill=Y)
        
               scroll_x.config(command=self.room_table.xview)
               scroll_y.config(command=self.room_table.yview)


               self.room_table.heading("floor",text="floor")
               self.room_table.heading("RoomNo",text="RoomNo")
               self.room_table.heading("Roomtype",text="Room Type")



               self.room_table["show"]="headings"

               self.room_table.column("floor",width=100)
               self.room_table.column("RoomNo",width=100)
               self.room_table.column("Roomtype",width=100)
               self.room_table.pack(fill=BOTH,expand=1)
               self.room_table.bind("<ButtonRelease-1>",self.get_cusor)

               self.fetch_data()


        def add_data(self): 
              
              if self.var_floor.get()=="" or self.var_roomtype.get()=="":
                    messagebox.showerror("Error","All feilds are Required",parent=self.root)
              else:
                   try:
                
                       conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                       my_cursor=conn.cursor()
                       my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                              self.var_floor.get(),
                                                                              self.var_roomnum.get(),
                                                                              self.var_roomtype.get()
                                                                                    ))
                       conn.commit()
                    #    self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                   except Exception as es:
                         messagebox.showwarning("Warning",f"Something Went Worng:{str(es)}",parent=self.root)



        def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from details")
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()    

        def get_cusor(self,event=""):
              
              cursor_row=self.room_table.focus()
              content=self.room_table.item(cursor_row)
              row=content["values"]

              if row:
                    
               self.var_floor.set(row[0]),
               self.var_roomnum.set(row[1]),
               self.var_roomtype.set(row[2]),


# ============update button ============
        def update(self):
            if self.var_floor.get() == "":
                messagebox.showerror("Error", "Please enter floor number", parent=self.root)
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="TA@#&arora12", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE details SET floor=%s, RoomType=%s WHERE RoomNo=%s", (
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomnum.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "New Room details have been updated successfully", parent=self.root)

#     ======================delete button function======
        def mDelete(self):
              mDelete=messagebox.askyesno("Hotel Managment System","Do you want delete this Specific Room Dtails",parent=self.root)
              if mDelete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
                    my_cursor=conn.cursor()
                    query="delete from details where floor=%s"
                    value=(self.var_floor.get(),)
                    my_cursor.execute(query, value)
              else:
                    if not mDelete:
                          return
              conn.commit()
              self.fetch_data()
              conn.close()


# ==============reset button function===============
        def reset(self):
              
              self.var_floor.set(""),
              self.var_roomnum.set(""),
              self.var_roomtype.set("")




if __name__=="__main__":
    root=Tk()
    obj=Details_win(root)
    root.mainloop()
