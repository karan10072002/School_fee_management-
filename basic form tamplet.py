from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tm
from pymongo import *

window = Tk()
window.title("Student Data")
window.geometry('400x200')
fonts=('Lucida Bright', 11)
#window.configure(background = "grey");
a = Label(window ,text = "Name", font=fonts).grid(row = 0,column = 0)
b = Label(window ,text = "Class", font=fonts).grid(row = 1,column = 0)
c = Label(window ,text = "Email Id", font=fonts).grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number",font=fonts).grid(row = 3,column = 0)
d = Label(window ,text = "Subjects:").grid(row = 5,column = 1)

var=IntVar()
c=Checkbutton(window, text='subject1', variable=var).grid(row=6, column=1)

a1 = Entry(window, font=fonts)
a1.grid(row = 0,column = 1)

b1 = Entry(window, font=fonts)
b1.grid(row = 1,column = 1)

c1 = Entry(window, font=fonts)
c1.grid(row = 2,column = 1)

d1 = Entry(window, font=fonts)
d1.grid(row = 3,column = 1)

e = Label(window ,text = "--",font=fonts).grid(row = 8,column = 1)

def clicked():
	stud_data=['Name: '+a1.get()+'\n', 'Class: '+b1.get()+'\n', 'Email Id: '+c1.get()+'\n','Contact Number: '+d1.get()+'\n', '\n']
	with open('students.txt','a+') as studs:
		studs.writelines(stud_data)
	mess_stud_info=''
	for i in stud_data:
		mess_stud_info+=i
	mess_stud_info=mess_stud_info.replace('\n','')

	data_set=['name', 'class', 'email_id','conntact_number']
	data_values=[a1.get(),b1.get(),c1.get(),d1.get()]
	mongo_data=dict(zip(data_set, data_values))

	mongo=MongoClient()
	db=mongo.Aman_tutorials
	collection=db.students
	collection.insert_one(mongo_data)

	tm.showinfo(title='Student added !!!', message=mess_stud_info)
	window.quit()
   # lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit", command=clicked).grid(row=9,column=1)
# ()
window.mainloop()
