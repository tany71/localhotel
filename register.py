from tkinter import*
from tkinter import NoDefaultRoot, NoDefaultRoot, ttk
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector

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
        self.bg1=ImageTk.PhotoImage(file=r"D:\pythonproject\images\leftphoto.jpg")
    
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=70,y=220,width=470,height=550)
        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=545,y=220,width=1100,height=550)

        # label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new romen",20,"bold"),fg="black",bg="white")
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
        self.combo_security_Q["values"]=("select","your birth place","your girlfriend name","your pet name")
        self.combo_security_Q.place(x=55,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="security Answer",font=("times new romen",18,"bold"),bg="white",fg="black")
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
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=380,y=430,width=250)
        
# =========================fuction declaration ==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Eroor","all feilds are Required")

        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Passward and confirm password must be same")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and condition")
        else:
               
               conn=mysql.connector.connect(host="localhost",username="root",password="TA@#&arora12",database="management")
               my_cursor=conn.cursor()
               query=("select *from register where email=%s")
               value=(self.var_email.get(),)
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               if row!=None:
                   messagebox.showerror("Eroor","User already exist,please try another Email")
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
               messagebox.showinfo("Success","User Registered successfully")


    def return_login(self):
        self.root.destroy()



if __name__ == "__main__":
    root= Tk()
    app=Register(root)
    root.mainloop()
