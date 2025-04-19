from tkinter import *
from tkinter import ttk

# ============ Create the main window ============
root = Tk()
root.title("Employee Management System")
root.geometry("1310x515+40+100")
root.resizable(False, False)
root.configure(bg= "#2c3e50")

# ============ Create Entries Frame ============
entries_frame = Frame(root, bg= "#2c3e50")
entries_frame.place(x=1, y=1, width=360, height=510)
title = Label(entries_frame, text= "Employee Company", font=('Calibri',18, 'bold'), bg='#9FB9D9', fg='white')
title.pack(fill=X)

lblName = Label(entries_frame, text="Name", font=('Calibri', 16), bg= "#2c3e50", fg='white')
lblName.place(x=10, y= 50, )
entryName = Entry(entries_frame, font=('Calibri', 16,), bd=2, width=20, relief='groove')
entryName.place(x=120, y=50)

lblJob = Label(entries_frame, text="Job", font=('Calibri', 16), bg= "#2c3e50", fg='white')
lblJob.place(x=10, y= 100 )
entryJob = Entry(entries_frame, font=('Calibri', 16,), bd=2, width=20, relief='groove')
entryJob.place(x=120, y=100)














root .mainloop()