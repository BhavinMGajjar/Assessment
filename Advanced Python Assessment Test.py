from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

root = Tk()
root.geometry("390x390")
root.title("Hotel Management")
root.resizable(width=False,height=False)
    

def create_conn():
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel_management")

  
def checkin_window():
    checkin = Toplevel(root)
    checkin.geometry("390x390")
    checkin.title("Check in")
    checkin.resizable(width=False,height=False)
    gen= StringVar()
    delux = StringVar()
    rd = BooleanVar()
    fulldelux = StringVar()
    joint= StringVar()
    
   

def insert_data():
        if e_name.get()=="" or e_name.get()=="" or e_days.get()=="" or e_mobile.get()=="":
            msg.showinfo("Insert Status","All fields are mandatory")
        else:
            conn=create_conn()
            cursor=conn.cursor()
            query="insert into check_in(name,address,mobile,days,room,payment) values(%s, %s, %s, %s, %s, %s)"
            args=(e_name.get(), e_address.get(), e_mobile.get(), e_days.get(), gen.get(), rd.get())
            cursor.execute(query,args)
            conn.commit()
            conn.close()
            e_name.delete(0,'end')
            e_address.delete(0,'end')
            e_mobile.delete(0,'end')
            e_days.delete(0,'end')
            msg.showinfo("Insert Status","Data Inserted Successfully")

    
    #lables
        l_name = Label(checkin,text="Enter Name")
        l_name.place(x=50,y=50)
        l_address = Label(checkin,text="Enter Address")
        l_address.place(x=50,y=80)
        l_mobile = Label(checkin, text="Enter mobile number")
        l_mobile.place(x=50,y=110)
        l_days=Label(checkin, text="Number of Days")
        l_days.place(x=50,y=140)
        l_room=Label(checkin,text="Choose your room")
        l_room.place(x=120,y=180)
        l_payment=Label(checkin,text="Choose your Payment method")
        l_payment.place(x=100,y=250)
       
        chk1= Checkbutton(checkin, text="General",onvalue=1, variable=gen, offvalue=0, height=3, width=5)
        chk1.place(x=40,y=200)
        
        chk2= Checkbutton(checkin, text="Delux",onvalue=1, variable=delux, offvalue=0, height=3, width=5)
        chk2.place(x=110,y=200)
        
        
        chk3= Checkbutton(checkin, text="Full Delux",onvalue=1,variable=fulldelux,  offvalue=0, height=3, width=7)
        chk3.place(x=190,y=200)
        
        chk4= Checkbutton(checkin, text="Joint",onvalue=1, variable=joint, offvalue=0, height=3, width=5)
        chk4.place(x=280,y=200)

        rad1= Radiobutton(checkin, text="Cash", value="Cash", height=3, width=5, variable="rd")
        rad1.place(x=50,y=270)
        
        rad2= Radiobutton(checkin, text="Credit/Debit Card",value="Credit/Debit card", variable="rd", height=3, width=15)
        rad2.place(x=120,y=270)

        insert=Button(checkin,text="Submit", fg="Blue", bg="white", font=('arial','10','bold'), width='20', command=insert_data)
        insert.place(x=100, y=330)

       

        #text boxes/Enteies    
        e_name= Entry(checkin)
        e_name.place(x=200,y=50)
        e_address= Entry(checkin)
        e_address.place(x=200,y=80)
        e_mobile= Entry(checkin)
        e_mobile.place(x=200,y=110)
        e_days= Entry(checkin)
        e_days.place(x=200,y=140)
    

def show_guest():
    showguest = Toplevel(root)
    showguest.geometry("390x390")
    showguest.title("Showing Guest list")
    showguest.resizable(width=False,height=False)
    e_name= Entry(showguest)
    e_name.place(x=200,y=50)
    e_address= Entry(showguest)
    e_address.place(x=200,y=80)
    e_mobile= Entry(showguest)
    e_mobile.place(x=200,y=110)
    e_days= Entry(showguest)
    e_days.place(x=200,y=140)
    
    conn=create_conn()
    cursor=conn.cursor()
    query="select * from check_in"
    cursor.execute(query)
    row=cursor.fetchall()
   
    for i in row:
                e_name.insert(0,i[1])
                
            
def search_data():
    search_data = Toplevel(root)
    search_data.geometry("390x390")
    search_data.title("Getting info of guest")
    search_data.resizable(width=False,height=False)
    e_name= Entry(search_data)
    e_name.place(x=150,y=50)
    e_address= Entry(search_data)
    e_address.place(x=150,y=80)
    e_mobile= Entry(search_data)
    e_mobile.place(x=150,y=110)
    e_days= Entry(search_data)
    e_days.place(x=150,y=140)
    
    
    def exe_search():
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from check_in where name=%s"
        args=(e_name.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        
        
        if row:
                for i in row:
                    e_name.insert(0,i[1])
                    e_address.insert(0,i[2])
                    e_mobile.insert(0,i[3])
               
        else:
              e_fname.delete(0,'end')
              e_lname.delete(0,'end')
              e_mobile.delete(0,'end')
                     
              msg.showinfo("Insert Status","Data searched Successfully")
              conn.close()
    e_name= Entry(search_data)
    e_name.place(x=200,y=50)
    e_address= Entry(search_data)
    e_address.place(x=200,y=80)
    e_mobile= Entry(search_data)
    e_mobile.place(x=200,y=110)
    e_days= Entry(search_data)
    e_days.place(x=200,y=140)   
    btn_search=Button(search_data,text="Search",command=exe_search)
    btn_search.place(x=200, y=160)

def Exit():
    
    root.destroy()


def check_out():
    check_out = Toplevel(root)
    check_out.geometry("390x390")
    check_out.title("Check Out")
    check_out.resizable(width=False,height=False)
    e_name= Entry(check_out)
    e_name.place(x=200,y=50)
    e_address= Entry(check_out)
    e_address.place(x=200,y=80)
    e_mobile= Entry(check_out)
    e_mobile.place(x=200,y=110)
    e_days= Entry(check_out)
    e_days.place(x=200,y=140)
    

    def exe_chkout():
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from check_in where name=%s"
        args=(e_name.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Check out Status","Checked out Successfully")

    chk_btn = Button(check_out, text= "Check out", command=exe_chkout)
    chk_btn.place(x=200,y=160)





    

wlcm=Label(root, text="Welcome To Hotel Managemnt", font=('arial','15','bold'), fg="grey", anchor="center")
wlcm.place(x=50,y=30)
wlcm=Label(root, text="Python Tkinter",font=('arial','15','bold'), fg="grey")
wlcm.place(x=80,y=60)
wlcm=Label(root, text="GUI", font=('arial','17','bold'), fg="blue",anchor="center" )
           
wlcm.place(x=140,y=90)

insert=Button(root,text="Check in", fg="black", bg="white", font=('arial','10','bold'), width='20', command=checkin_window)
insert.place(x=100, y=150)

insert=Button(root,text="Show Guest list", fg="black", bg="white", font=('arial','10','bold'), width='20', command=show_guest)
insert.place(x=100, y=200)

insert=Button(root,text="Check out", fg="black", bg="white", font=('arial','10','bold'), width='20', command=check_out)
insert.place(x=100, y=250)

insert=Button(root,text="Get info of any Guest", fg="black", bg="white", font=('arial','10','bold'), width='20', command=search_data)
insert.place(x=100, y=300)

insert=Button(root,text="Exit", fg="black", bg="white", font=('arial','10','bold'), width='20', command=Exit)
insert.place(x=100, y=350)











