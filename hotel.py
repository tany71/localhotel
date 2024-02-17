from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Room_win
# from login import Login_Window
from Details import Details_win
from tkinter import NO, NO, YES, YES, messagebox

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.minsize(1920,1080)
        self.root.maxsize(1920,1080)

        # ========FIRST image======
        img1=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\1st pic.jpg")
        img1=img1.resize((1920,160))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1920,height=140)

        # =========logo=========
        img2=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\premium logo.png")
        img2=img2.resize((320,270))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        lblimg.place(x=0,y=0,width=250,height=140)

        # =========title =======
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1920,height=50)


        # =========main frame ========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1920,height=870)

        # ===========menu============
        lbl_title=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=250) 

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=250,height=190)


        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)


        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        

        details_btn=Button(btn_frame,text="DETAILS",command=self.room_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)


        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

       # ===============Right side image=============
        img3=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\hotel right image.jpg")
        img3=img3.resize((1920,1080))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=251,y=0,width=1662,height=880)

         # =====================down image ==============
        img4=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\myh.jpg")
        img4=img4.resize((250,310))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=230,width=250,height=310)

        # ===================down to down image==============
        img5=Image.open(r"D:\HOTEL MANAGEMENT SYSTEM\images\food.jpg")
        img5=img5.resize((250,310))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=540,width=250,height=310)

    def logout(self):
        logout=messagebox.askyesno("YesNO","do you really want to logout",parent=self.root)
        if logout==YES:
            self.new_window=exit(self.root)
        else:
            self.root()



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.k=Cust_Win(self.new_window)
 



    def room_booking_details(self):
        self.new_window=Toplevel(self.root)
        self.k=Room_win(self.new_window)



    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.k=Details_win(self.new_window)


    # def back_to_login(self):
    #     self.new_window=Toplevel(self.root)
    #     self.k=Login_Window(self.new_window)








if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()