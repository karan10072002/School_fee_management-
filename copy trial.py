import tkinter as tk
from pymongo import *
import students_sheet

height=700
width=800

def search(entry):
	print('searched: ',entry)
	pass
def stud_sheet():
	students_sheet.tries()

student_label='karan kumar chaurasia                                                             12                                                           9100589872'
header='NAME','\t'*5,'CLASS','\t'*5,'CONTACT no.'

root=tk.Tk()
#root.geometry("100, 200")
fonts=('ISOCTEUR', 12)
canvas=tk.Canvas(root, height=height, width=width).pack()
#background_image=tk.PhotoImage(file=r"C:\Users\KARAN\Pictures\Screenshots\Screenshot (5).png")
#background_label=tk.Label(root, image=background_image).place(relx=0.00001, rely=0.001, relheight=1, relwidth=1 )
frame=tk.Frame(root, bg='#80c1ff', bd=5).place(relx=0.5, rely=0.1-0.09, relwidth=0.75, relheight=0.1, anchor='n')
entry= tk.Entry(frame, font=fonts)
entry.place(rely=0.114-0.09 ,relx=0.14,relwidth=0.52, relheight=0.07)
botton=tk.Button(frame, text='Search', font=fonts, command=lambda: search(entry.get())).place(rely=0.11-0.09 ,relx=0.67, relheight=0.08, relwidth=0.2)
lower_frame=tk.Frame(root, bg='#80c1ff', bd=5).place(relx=0.01, rely=0.21-0.09, relwidth=0.98, relheight=0.85)
tab_lab=tk.Label(lower_frame, bg='grey', bd=6, text=header).place(relx=0.025, rely=0.21-0.075, relwidth=0.95, relheight=0.05)
Label=tk.Button(lower_frame, text=student_label, bg='#80c1ff', bd=1, command=stud_sheet).place(relx=0.025, rely=0.21, relwidth=0.95, relheight=0.07)
# Label.pack()

mongo=MongoClient()
db=mongo.Aman_tutorials
collection=db.students
all_studs=collection.find()
list_all_studs=''
for i in all_studs:
	list_all_studs+=str(i)
	list_all_studs+='\n'

Label=tk.Label(lower_frame, text=list_all_studs, bg='white', bd=5).place(relx=0.025, rely=0.21-0.075, relwidth=0.98-0.03, relheight=0.85-0.03)
root.mainloop()