import tkinter as tk

fonts=('ISOCTEUR', 12)
	
root=tk.Tk()
root.title('karan')
#root.iconbitmap(r"C:\Users\LENOVO\Downloads\Icons8-Ios7-Network-Wifi-Logo.ico")
canvas=tk.Canvas(root, height=15, width=200, bg='grey').pack(fill='both', expand='True')
background_image=tk.PhotoImage(file=r"C:\Users\KARAN\Pictures\Screenshots\Screenshot (5).png")
background_label=tk.Label(root, image=background_image).place(relheight=1, relwidth=1 )
# frame=tk.Frame(root, bg='blue')
# frame.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

butoon=tk.Button(root, text='search', font=fonts, bg='grey').pack()
#butoon.grid(row=1, column=1)
# butoon1=tk.Button(root, text='Disconnect', command=diconnect, font=fonts, bg='red').pack(fill='both', expand=True, side='bottom')
entry=tk.Entry(root, font=40).place(relx=0.2, relheight=0.05, relwidth=0.3)
root.mainloop()
