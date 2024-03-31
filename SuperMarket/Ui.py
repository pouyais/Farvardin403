from tkinter import *
from tkinter import messagebox
from Database import *

db = Database("D:/PythonTerm3/NorozHomeWork/SuperMarketEnglish/mydatabase.db")

# ***************************** Def ******************************************
def insert():
    if ent_prodcut.get() == "" or ent_buyprice.get() == "" or ent_sellprice.get() == "" or ent_quantity.get() == "":
        messagebox.showerror(title="empty fields",message="Please fill in all the fields")
        
        if ent_prodcut.get() == "":
            lbl_product_redstar.config(text="*")
        else:
            lbl_product_redstar.config(text="")
        if ent_buyprice.get() == "":
            lbl_buyprice_redstar.config(text="*")
        else:
            lbl_buyprice_redstar.config(text="")
        if ent_sellprice.get() == "":
            lbl_sellprice_redstar.config(text="*")
        else:
            lbl_sellprice_redstar.config(text="")
        if ent_quantity.get() == "":
            lbl_quantity_redstar.config(text="*")
        else:
            lbl_quantity_redstar.config(text="")
        return
    
    elif ent_prodcut.get().isalpha() == False:
        messagebox.showerror(title="اخطار",message="لطفا جا های خالی رو به درستی پر کنید")
        if ent_prodcut.get().isalpha() == False:
            lbl_product_redstar.config(text="*")
        elif ent_prodcut.get().isalpha() == True:
            lbl_product_redstar.config(text="")
        return
    
    elif ent_buyprice.get().isdigit() == False or ent_sellprice.get().isdigit() == False or ent_quantity.get().isdigit() == False:
        messagebox.showerror(title="اخطار",message="لطفا جا های خالی رو به درستی پر کنید")
        if ent_buyprice.get().isdigit() == False:
            lbl_buyprice_redstar.config(text="*")
        elif ent_buyprice.get().isdigit() == True:
            lbl_buyprice_redstar.config(text="")
        if ent_sellprice.get().isdigit() == False:
            lbl_sellprice_redstar.config(text="*")
        elif ent_sellprice.get().isdigit() == True:
            lbl_sellprice_redstar.config(text="")
        if ent_quantity.get().isdigit() == False:
            lbl_quantity_redstar.config(text="*")
        elif ent_quantity.get().isdigit() == True:
            lbl_quantity_redstar.config("")
        return
    
    else:
        db.insert(ent_prodcut.get(),float(ent_buyprice.get()),float(ent_sellprice.get()),int(ent_quantity.get()))
        lbl_product_redstar.config(text="")
        lbl_buyprice_redstar.config(text="")
        lbl_sellprice_redstar.config(text="")
        lbl_quantity_redstar.config(text="")
        
    clear()
    publish_list()

def clear():
    ent_prodcut.delete(0,END)
    ent_buyprice.delete(0,END)
    ent_sellprice.delete(0,END)
    ent_quantity.delete(0,END)

def select_item(event):
    try:
        global selected_item
        selected_item = lst_box.get(lst_box.curselection()).split(",")
        ent_prodcut.delete(0,END)
        ent_prodcut.insert(END,selected_item[1])
        ent_buyprice.delete(0,END)
        ent_buyprice.insert(END,selected_item[2])
        ent_sellprice.delete(0,END)
        ent_sellprice.insert(END,selected_item[3])
        ent_quantity.delete(0,END)
        ent_quantity.insert(END,selected_item[4])
    except IndexError:
        pass

def publish_list():
    lst_box.delete(0,END)
    records = db.fetch()
    for record in records:
        lst_box.insert(END,f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}")

def delete():
    db.remove(selected_item[0])
    clear()
    publish_list()

def edit():
    db.update(selected_item[0],ent_prodcut.get(),float(ent_buyprice.get()),float(ent_sellprice.get()),int(ent_quantity.get()))
    publish_list()

def exit():
    root.destroy()

def search():
    search_result = db.search(ent_search.get())
    lst_box.delete(0,END)
    for row in search_result:
        lst_box.insert(END,row)
        ent_search.delete(0,END)

def cleaner():
    ent_prodcut.delete(0,END)
    ent_buyprice.delete(0,END)
    ent_sellprice.delete(0,END)
    ent_quantity.delete(0,END) 

    lst_box.delete(0,END)

# ***************************** Ui(root section) *****************************
root = Tk()
root.title("SuperMarket")
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
cx = screen_x / 2
cy = screen_y / 2
ww = 600
wh = 400
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)
root.geometry(f"{ww}x{wh}+{wx}+{wy}")
root.config(bg="#F4FFB4")
root.iconbitmap("D:/PythonTerm3/NorozHomeWork/SuperMarketEnglish/supermarket_cart_store_market_icon_180221 (1).ico")


# ***************************** Labels ******************************************
lbl_product = Label(root,text="Name : ",bg="#F4FFB4",font="Arial 10 bold")
lbl_product.place(x=20,y=10)
lbl_product_redstar = Label(root,text="",bg="#F4FFB4",fg="red",font="Arial 15 bold")
lbl_product_redstar.place(x=240,y=14)

lbl_buyprice = Label(root,text="buyprice : ",bg="#F4FFB4",font="Arial 10 bold")
lbl_buyprice.place(x=300,y=10)
lbl_buyprice_redstar = Label(root,text="",bg="#F4FFB4",fg="red",font="Arial 15 bold")
lbl_buyprice_redstar.place(x=540,y=14)

lbl_sellprice = Label(root,text="sellprice : ",bg="#F4FFB4",font="Arial 10 bold")
lbl_sellprice.place(x=20,y=120)
lbl_sellprice_redstar = Label(root,text="",bg="#F4FFB4",fg="red",font="Arial 15 bold")
lbl_sellprice_redstar.place(x=240,y=120)

lbl_quantity = Label(root,text="quantity : ",bg="#F4FFB4",font="Arial 10 bold")
lbl_quantity.place(x=300,y=120)
lbl_quantity_redstar = Label(root,text="",bg="#F4FFB4",fg="red",font="Arial 15 bold")
lbl_quantity_redstar.place(x=540,y=120)


# ***************************** Entries ******************************************
ent_prodcut = Entry(root,bg="#F3F3F3",font="Arial 10 bold")
ent_prodcut.place(x=90,y=15)

ent_buyprice = Entry(root,bg="#F3F3F3",font="Arial 10 bold")
ent_buyprice.place(x=390,y=15)

ent_sellprice = Entry(root,bg="#F3F3F3",font="Arial 10 bold")
ent_sellprice.place(x=90,y=120)

ent_quantity = Entry(root,bg="#F3F3F3",font="Arial 10 bold")
ent_quantity.place(x=390,y=120)

ent_search = Entry(root,bg="#F3F3F3",font="Arial 9 bold")
ent_search.place(x=360,y=200)


# ***************************** ListBox ******************************************
lst_box = Listbox(root,width=55,height=12,bg="#CEFFF6")
lst_box.place(x=20,y=180)


# ***************************** Binding ******************************************
lst_box.bind("<<ListboxSelect>>",select_item)


# ***************************** Buttons ******************************************
btn_add = Button(root,text="Add",width=10,height=1,command=insert,bg="#FF5C31",font="Arial 8 bold")
btn_add.place(x=510,y=200)

btn_showlist = Button(root,text="Showlist",width=10,height=1,command=publish_list,bg="#FF5C31",font="Arial 8 bold")
btn_showlist.place(x=510,y=230)

btn_delete = Button(root,text="Delete",width=10,height=1,command=delete,bg="#FF5C31",font="Arial 8 bold")
btn_delete.place(x=510,y=260)

btn_Edit = Button(root,text="Edit",width=10,height=1,command=edit,bg="#FF5C31",font="Arial 8 bold")
btn_Edit.place(x=510,y=290)

btn_exit = Button(root,text="Exit",width=10,height=1,command=exit,bg="#FF5C31",font="Arial 8 bold")
btn_exit.place(x=510,y=320)

btn_search = Button(root,text="Search",width=10,height=1,command=search,bg="#FF5C31",font="Arial 8 bold")
btn_search.place(x=390,y=230)

btn_clear = Button(root,text="Clear",width=10,height=1,command=cleaner,bg="#FF5C31",font="Arial 8 bold")
btn_clear.place(x=510,y=350)





root.mainloop()


