from logging import root
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast


def daftar(): 
    layar=Toplevel(root)
    layar = Tk()
    layar.geometry("1200x720")
    layar.title("Daftar")

    bg = ImageTk.PhotoImage(Image.open("gambarlogin.jpg"))
    Label(layar, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)

    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=400,y=60,height=360,width=400)
    atas=Label(kotak_log,text="Mendaftar",fg="#57a1f8",bg="black",font=("Times New Roman",24,"bold"))
    atas.place(x=120,y=30)
    Frame(kotak_log,width=400,height=2,bg="#57a1f8").place(x=0,y=80)
    Frame(kotak_log,width=400,height=2,bg="#57a1f8").place(x=0,y=300)
    #------------------------------------------------------------------------------------------------#
    #Sistem Daftar
    def pendaftaran():
        username=nama.get()
        password=data.get()
        confirm_password=confirm_data.get()

        if password==confirm_password:
            try:
                file=open("KumpulAkun.txt","r+")
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close

                file=open("KumpulAkun","w")
                w=file.write(str(r))

                messagebox.showinfo("Success","Pendaftaran Berhasil")

            except:
                file=open("KumpulAkun.txt","w")
                pp=str({username,password})
                file.write(pp)
                file.close()

                messagebox.showinfo("Success","Pendaftaran Berhasil")

        else:
            messagebox.showerror("Invalid","Kedua Password harus sama")
        
    def tanda():
        layar.destroy()

    #------------------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------#
    #Input Username
    def on_enter(e):
        nama.delete(0, 'end')
    def on_leave(e):
        if nama.get()=="":
            nama.insert(0,"Username")

    nama= Entry(kotak_log,width=25,fg="white",bg="gray",font=("Times New Roman",11))
    nama.place(x=110,y=120)
    nama.insert(0,"Username")
    nama.bind("<FocusIn>",on_enter)
    nama.bind("<FocusOut>",on_leave)
    
    #------------------------------------------------------------------------------------------------#
    #Input Password
    def on_enter(e):
        data.delete(0, 'end')
    def on_leave(e):
        if data.get()=="":
            data.insert(0,"Password")

    data= Entry(kotak_log,width=25,fg="white",bg="gray",font=("Times New Roman",11))
    data.place(x=110,y=150)
    data.insert(0,"Password")
    data.bind("<FocusIn>",on_enter)
    data.bind("<FocusOut>",on_leave)

    #------------------------------------------------------------------------------------------------#
    #Input Ulang Password
    def on_enter(e):
        confirm_data.delete(0, 'end')
    def on_leave(e):
        if confirm_data.get()=="":
            confirm_data.insert(0,"Konfirmasi Password")

    confirm_data= Entry(kotak_log,width=25,fg="white",bg="gray",font=("Times New Roman",11))
    confirm_data.place(x=110,y=180)
    confirm_data.insert(0,"Konfirmasi Password")
    confirm_data.bind("<FocusIn>",on_enter)
    confirm_data.bind("<FocusOut>",on_leave)
    #------------------------------------------------------------------------------------------------#
    #Ke menu login
    Button(kotak_log,width=25,pady=7,text="Daftar",bg="red",fg="white",border=0,cursor="hand2",command=pendaftaran).place(x=110,y=230)

    klik_disini=Button(kotak_log,text="Saya Sudah punya akun",bg="black",fg="#57a1f8",cursor="hand2",border=0,font=("Times New Roman",9),command=tanda)
    klik_disini.place(x=135,y=270)
    #------------------------------------------------------------------------------------------------#
    layar.mainloop()