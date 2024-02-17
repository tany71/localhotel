# ==============LOGIN AND REGISTERATION CODE====================
from tkinter import*
from tkinter import SEL_FIRST, SEL_FIRST, SEL_FIRST, NoDefaultRoot, NoDefaultRoot, ttk
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1920x1080+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\HOTEL MANAGEMENT SYSTEM\images\maldives-5-star-resort-1920x1080-wallpaper-12488.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=750,y=170,width=340,height=450)

        img1=Image.open(r"D:\pythonproject\images\login-logo-icon-4.jpg")
        img1 = img1.resize((100, 100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=865,y=175,width=100,height=100)

        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)


        # labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # =======ICON IMAGES=========
        img2=Image.open(r"D:\pythonproject\images\loginicon image.jpeg")
        img2 = img2.resize((22, 22))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=790,y=323,width=25,height=25)

        img3=Image.open(r"D:\pythonproject\images\passwordicon.png")
        img3 = img3.resize((22, 22))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=790,y=395,width=25,height=25)
        # LOGINBUTTON
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)
        # register button
        registerbtn=Button(frame,text="Create New Account",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=19,y=350,width=160)

        forgrotpassbtn=Button(frame,text="Forgot password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgrotpassbtn.place(x=10,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
           messagebox.showerror("Eroor","All feild required")
        elif self.txtuser.get()=="Tanuj" and self.txtpass.get()=="1153":
            messagebox.showinfo("success","welcome to code with tanuj")
            self.new_window=Toplevel(self.root)
            self.HotelManagementSystem(self.new_window)
        else:
               conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                ) )
               
               row=my_cursor.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid username & passwod")
               else:
                   open_main=messagebox.askyesno("yesNo","Access only admin")
                   if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.k=HotelManagementSystem(self.new_window)
                   else:
                       if not open_main:
                           return
               conn.commit()
               
# ==================reset forgot_password_window==============
    def reset_Password(self):
        if self.combo_security_Q.get()=="":
            messagebox.showerror("Eroor","select security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and squestion=%s and sanswer=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your Password has been reset,please login with new password",parent=self.root2)
                self.root2.destroy()

# ============forgot forgot_password_window============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Inter the email address to reset address to reset ",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if  row==None:
                messagebox.showerror("Error","Please Enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x440+750+190")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security question ",font=("times new romen",18,"bold"),bg="white",fg="black")
                security_Q.place(x=30,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new romen",18,"bold"),state="readonly")
                self.combo_security_Q["values"]=("select","your birth place","your girlfriend name","your pet name")
                self.combo_security_Q.place(x=35,y=110,width=290)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new romen",18,"bold"),bg="white",fg="black")
                security_A.place(x=30,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new romen",18,"bold"))
                self.txt_security_A.place(x=35,y=180,width=290)

                new_password=Label(self.root2,text="New Password",font=("times new romen",18,"bold"),bg="white",fg="black")
                new_password.place(x=30,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new romen",18,"bold"))
                self.txt_newpass.place(x=35,y=250,width=290)

                btn=Button(self.root2,text="Reset",command=self.reset_Password,font=("times new romen",18,"bold"),bg="green",fg="black")
                btn.place(x=125,y=320)
                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")
        # ===============variables========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

# =======background image==========
        self.bg=ImageTk.PhotoImage(file=r"D:\pythonproject\images\registerbg.jpg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# ===========left image ==========left
        self.bg1=ImageTk.PhotoImage(file=r"D:\HOTEL MANAGEMENT SYSTEM\images\myh.jpg")
        
        left_lbl=Label(self.root,image=self.bg1)
        
        left_lbl.place(x=70,y=220,width=470,height=550)
        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=545,y=220,width=1100,height=550)

        # label
        register_lbl=Label(frame,text="CREATE NEW ACCOUNT",font=("times new romen",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)

        # ==============LABLES AND ENTRY============
        # ==========ROW 1 ===========
        fname=Label(frame,text="First name",font=("times new romen",18,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new romen",15,"bold"))
        self.fname_entry.place(x=55,y=130,width=250)

        lname=Label(frame,text="last name",font=("times new romen",18,"bold"),bg="white")
        lname.place(x=500,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new romen",15,"bold"))
        self.txt_lname.place(x=505,y=130,width=250)

        # ==========ROW 2===================
        contact=Label(frame,text="Contact no.",font=("times new romen",18,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new romen",15,"bold"))
        self.txt_contact.place(x=55,y=200,width=250)


        E_mail=Label(frame,text="E-mail ",font=("times new romen",18,"bold"),bg="white")
        E_mail.place(x=500,y=170)

        self.txt_E_mail=ttk.Entry(frame,textvariable=self.var_email,font=("times new romen",15,"bold"))
        self.txt_E_mail.place(x=505,y=200,width=250)

        # ============ROW 3============
        security_Q=Label(frame,text="Select Security question ",font=("times new romen",18,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new romen",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your girlfriend/boyefrnd name","your pet name")
        self.combo_security_Q.place(x=55,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new romen",18,"bold"),bg="white",fg="black")
        security_A.place(x=505,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new romen",15,"bold")) 
        self.txt_security_A.place(x=505,y=270,width=250)

        # ==========ROW 4 ==============
        pswd=Label(frame,text="Password",font=("times new romen",18,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new romen",15,"bold"))
        self.txt_pswd.place(x=55,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new romen",18,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=500,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new romen",15,"bold"))
        self.txt_confirm_pswd.place(x=505,y=340,width=250)

        # ===========Checkbutton===========
        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new romen",10,"bold"),bg="white",onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

        # ========buttons============
        img=Image.open("D:\pythonproject\images\Register-Now.png")
        img=img.resize((250,50))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=100,y=430,width=250)

        img1=Image.open("D:\pythonproject\images\login-now-new-hi.png")
        img1=img1.resize((250,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=380,y=430,width=250)
        
# =========================fuction declaration ==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Eroor","all feilds are Required",parent=self.root)

        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Passward and confirm password must be same",parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and condition",parent=self.root)
        else:
               
               conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
               my_cursor=conn.cursor()
               query=("select *from register where email=%s")
               value=(self.var_email.get(),)
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               if row!=None:
                   messagebox.showerror("Eroor","User already exist,please try another Email",parent=self.root)
               else:
                   my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_pass.get()
                                                                                ))
               conn.commit()
               conn.close()
               messagebox.showinfo("Success","User Registered successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()
        

        


if __name__ == "__main__":
    main()
