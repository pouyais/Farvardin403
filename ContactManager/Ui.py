from tkinter import *
from tkinter import messagebox
from Database import *

db = Database("D:/PythonTerm3/NorozHomeWork/ContacManagerFarsi/mydatabase.db")


# *********************************** Def ********************************************************
def add():
    if ent_fname.get() == "" or ent_lname.get() == "" or ent_address.get() == "" or ent_phone.get() == "":
        messagebox.showerror(title="خطا",message="لطفا جاهای خالی رو پر کنید")

        if ent_fname.get() == "":
            lbl_fname_redstar.config(text="*")
        else:
            lbl_fname_redstar.config(text="")
        if ent_lname.get() == "":
            lbl_lname_redstar.config(text="*")
        else:
            lbl_lname_redstar.config(text="")
        if ent_address.get() == "":
            lbl_address_redstar.config(text="*")
        else:
            lbl_address_redstar.config(text="")
        if ent_phone.get() == "":
            lbl_phone_redstar.config(text="*")
        else:
            lbl_phone_redstar.config(text="")
        return
    
    elif ent_phone.get().isdigit() == False or len(ent_phone.get()) != 8:
        messagebox.showerror(title="اخطار",message="لطفا جا های خالی رو به درستی پر کنید")
        if ent_phone.get().isdigit() == False:
            lbl_phone_redstar.config(text="*")
        elif ent_phone.get().isdigit() == True:
            lbl_phone_redstar.config(text="")
        return
    
    elif ent_fname.get().isalpha() == False or ent_lname.get().isalpha() == False or ent_address.get().isalpha() == False:
        messagebox.showerror(title="اخطار",message="لطفا جا های خالی رو به درستی پر کنید")
        if ent_fname.get().isalpha() == False:
            lbl_fname_redstar.config(text="*")
        elif ent_fname.get().isalpha() == True:
            lbl_fname_redstar.config(text="")
        if ent_lname.get().isalpha() == False:
            lbl_lname_redstar.config(text="*")
        elif ent_lname.get().isalpha() == True:
            lbl_lname_redstar.config(text="")
        if ent_address.get().isalpha() == False:
            lbl_address_redstar.config(text="*")
        elif ent_address.get().isalpha() == True:
            lbl_address_redstar.config("")
        return
    
    else:
        db.insert(ent_fname.get(),ent_lname.get(),ent_address.get(),int(ent_phone.get()))
        lbl_fname_redstar.config(text="")
        lbl_lname_redstar.config(text="")
        lbl_address_redstar.config(text="")
        lbl_phone_redstar.config(text="")
        
    clear()
    publish_list()

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)

def select_item(event):
    try:
        global item 
        item = lst_box.get(lst_box.curselection()).split(",")
        ent_fname.delete(0,END)
        ent_fname.insert(END,item[1])
        ent_lname.delete(0,END)
        ent_lname.insert(END,item[2])
        ent_address.delete(0,END)
        ent_address.insert(END,item[3])
        ent_phone.delete(0,END)
        ent_phone.insert(END,item[4])
    except IndexError:
        pass

def publish_list():
    lst_box.delete(0,END)
    records = db.fetch()
    for record in records:
        lst_box.insert(END,f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}")

def delete():
    db.remove(item[0])
    clear()
    publish_list()

def update():
    db.update(item[0],ent_fname.get(),ent_lname.get(),ent_address.get(),int(ent_phone.get()))
    publish_list()

def search():
    search_result = db.search(ent_search.get())
    lst_box.delete(0,END)
    for row in search_result:
        lst_box.insert(END,row)
        ent_search.delete(0,END)

def cleaner():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)
    lst_box.delete(0,END)


# *********************************** Ui(Root Section) ********************************************************
root = Tk()
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
cx = screen_x / 2
cy = screen_y / 2
ww = 700
wh = 410
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)
root.geometry(f"{ww}x{wh}+{wx}+{wy}")
root.title("مدیریت مخاطبین")
root.config(bg="#6FA6FF")
root.iconbitmap('D:/PythonTerm3/NorozHomeWork/ContacManagerFarsi/Roundicons-100-Free-Solid-Contact.ico')


# *********************************** Labels ********************************************************
lbl_fname = Label(root,text="نام : ",font="Arial 14 bold",bg="#6FA6FF")
lbl_fname.place(x=30,y=10)
lbl_fname_redstar = Label(root,text="",fg="red",bg="#6FA6FF",font="Arial 14 bold")
lbl_fname_redstar.place(x=230,y=15)

lbl_lname = Label(root,text="نام خانوادگی : ",font="Arial 14 bold",bg="#6FA6FF")
lbl_lname.place(x=350,y=10)
lbl_lname_redstar = Label(root,text="",fg="red",bg="#6FA6FF",font="Arial 14 bold")
lbl_lname_redstar.place(x=610,y=15)


lbl_address = Label(root,text="آدرس : ",font="Arial 14 bold",bg="#6FA6FF")
lbl_address.place(x=10,y=80)
lbl_address_redstar = Label(root,text="",fg="red",bg="#6FA6FF",font="Arial 14 bold")
lbl_address_redstar.place(x=230,y=85)

lbl_phone = Label(root,text="تلفن : ",font="Arial 14 bold",bg="#6FA6FF")
lbl_phone.place(x=400,y=80)
lbl_phone_redstar = Label(root,text="",fg="red",bg="#6FA6FF",font="Arial 14 bold")
lbl_phone_redstar.place(x=610,y=85)


# *********************************** Entries ********************************************************
ent_fname = Entry(root,bg="#FBD2D2",font="Arial 10 bold")
ent_fname.place(x=80,y=15)

ent_lname = Entry(root,bg="#FBD2D2",font="Arial 10 bold")
ent_lname.place(x=460,y=15)

ent_address = Entry(root,bg="#FBD2D2",font="Arial 10 bold")
ent_address.place(x=80,y=85)

ent_phone = Entry(root,bg="#FBD2D2",font="Arial 10 bold")
ent_phone.place(x=460,y=85)

ent_search = Entry(root,bg="#FBD2D2",font="Arial 10 bold")
ent_search.place(x=380,y=170)


# *********************************** Buttons ********************************************************
btn_add = Button(root,text="اضافه کردن",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=add)
btn_add.place(x=560,y=170)

btn_delete = Button(root,text="حذف کردن",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=delete)
btn_delete.place(x=560,y=210)

btn_update = Button(root,text="بروزرسانی",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=update)
btn_update.place(x=560,y=250)

btn_clear = Button(root,text="پاک کردن ورودی ها",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=clear)
btn_clear.place(x=560,y=290,)

btn_showlist = Button(root,text="نمایش لیست",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=publish_list)
btn_showlist.place(x=560,y=330)

btn_search = Button(root,text="جستجو",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=search)
btn_search.place(x=395,y=195)

btn_cleaner = Button(root,text="پاکسازی",font="Arial 11 bold",width=12,height=1,bg="#82FFB6",command=cleaner)
btn_cleaner.place(x=560,y=370)
# *********************************** ListBox ********************************************************
lst_box = Listbox(root,width=55,height=16,bg="#E6FBD2")
lst_box.place(x=30,y=140)

# *********************************** BindingListBox ********************************************************
lst_box.bind("<<ListboxSelect>>",select_item)



root.mainloop()