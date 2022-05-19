import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import random
from PIL import ImageTk, Image

splash_root = tk.Tk()
splash_root.title('Loading.....')
img = ImageTk.PhotoImage(Image.open("Icons/splash.png"))
label = Label(splash_root, image = img)
label.pack()
def main():
    splash_root.destroy()
splash_root.after(2000,main)
splash_root.mainloop()


#SETUP INSTANCE
sprz = tk.Tk()
sprz.title('The Shopperz')
frame = tk.Frame(sprz,relief='raised',borderwidth=10,bg='blue')
frame.pack(side=tk.LEFT)
frame2 = tk.Frame(sprz,relief='raised',borderwidth=10,bg='red')
frame2.pack(side=tk.RIGHT)
sprz.resizable(False, False)

#Setting Item area
textarea = tk.Text(frame, width=45, height=23)
textarea.grid(row = 0, column=0)
textarea.insert(tk.END, '=============================================')
textarea.insert(tk.END, '\nArticle_Name\t|\tQuantity\t | Rate [Of 1 Item]')
textarea.insert(tk.END, '\n=============================================')
#textarea.insert(tk.END, 'macroni \t\t 2 \t\t 200')

#Variables
name = tk.StringVar()
phone = tk.IntVar()
item_name = tk.StringVar()
quantity = tk.IntVar()
rate = tk.IntVar()
paymentinfo = tk.StringVar()
paymentinfos = ('None','Paytm/Other UPI','Cash','Will Pay Later')
paymentinfo.set(paymentinfos[0])
rate_of_items = []

#functions

def generate():
    import os
    if os.path.exists('Bills/Bill Number Generator/UsedBillNumber.txt'):
        pass
    else:
        open('Bills/Bill Number Generator/UsedBillNumber.txt','x')
    usedbillwriter = open('Bills/Bill Number Generator/UsedBillNumber.txt', 'a')
    usedbillnumbers = open('Bills/Bill Number Generator/UsedBillNumber.txt', 'r')
    x = 0
    while x==0:
        x = random.randint(1000, 9999)
        if x in usedbillnumbers:
            continue
        else:
            usedbillwriter.write(str(x)+'\n')
            break
    return str(x)




#customer details
tk.Label(frame2, text='Customer Details',font=('Arial Bold',40),bg='red').grid(row=0, column=1)
tk.Label(frame2, text='Name ',font=('Arial',15),bg='red').grid(row=1, column=1)
tk.Entry(frame2, textvariable=name,width=20).grid(row=1, column=2)
tk.Label(frame2, text='Phone No. ',font=('Arial',15),bg='red').grid(row=2, column=1)
tk.Entry(frame2, textvariable=phone,width=20).grid(row=2, column=2)
tk.Label(frame2, text='Payment Done In ',font=('Arial',15),bg='red').grid(row=3,column=1)
tk.OptionMenu(frame2, paymentinfo, *paymentinfos).grid(row=3,column=2)

#article details
tk.Label(frame2, text='Article Details',font=('Arial Bold',40),bg='red').grid(row=4, column=1)
tk.Label(frame2, text='Article Name ',font=('Arial',15),bg='red').grid(row=5, column=1)
tk.Entry(frame2, textvariable=item_name,width=20).grid(row=5, column=2)
tk.Label(frame2, text='Quantity ',font=('Arial',15),bg='red').grid(row=6, column=1)
tk.Entry(frame2, textvariable=quantity,width=20).grid(row=6, column=2)
tk.Label(frame2, text='Rate ',font=('Arial',15),bg='red').grid(row=7, column=1)
tk.Entry(frame2, textvariable=rate,width=20).grid(row=7, column=2)

#lots of buttons
def mkebil():
	n=int(rate.get())
	m=int(quantity.get())
	mm = (quantity.get())*n
	l=item_name.get()
	rate_of_items.append(mm)
	if item_name.get()!='':
		textarea.insert(tk.END, f'\n{l} \t\t  {m}  \t\t {n}\n')
	else:
		tk.messagebox.showinfo('Error_404','No Item Inputed')

def clr():
	name.set('')
	phone.set(0)
	item_name.set('')
	rate.set(0)
	quantity.set(0)
	textarea.delete("1.0",tk.END)
	paymentinfo.set(paymentinfos[0])
	rate_of_items.clear()
	textarea.insert(tk.END, '=============================================\nArticle_Name\t|\tQuantity\t | Rate [Of 1 Item]\n=============================================')

def exmsys():
	op = tk.messagebox.askyesno("Exit", "Do you really want to exit?")
	if op > 0:
		sprz.destroy()

def svebil():
	x = generate()
	a = name.get()
	b = phone.get()
	c = paymentinfo.get()
	articles=textarea.get('1.0',tk.END)
	sum_of_rate = sum(rate_of_items)
	if a=='' or b==0:
		tk.messagebox.showerror('Detail Error','Customer Details Are Must!!!')
	elif c=='None':
		tk.messagebox.showerror('Payment Error', 'Mode Of Payment Not Selected!')
	else:
		hehe = tk.messagebox.askyesno('Save Bill', f'Do you want to save Bill with bill no. {x} of {a}')
		if hehe > 0:
			filer = open(f'Bills/bill {x} {a}.sprz', 'wt')
			filer.write(f"	  Welcome Krishna's Retail Shop\n\nBill Number:		{x}\nCustomer Name:		{a}\nPhone Number:		{b}\nPayment Done In:		{c}\n\n\n{articles}\n\n=============================================\nTotal Bill Amount :		      {sum_of_rate}\n\n=============================================")
			filer.close()
			
			messagebox.showinfo('Bill Saved',f'Please review the Bill with number {x} of {a} in the Bills Folder.')

#icon for button
clearimgnot = tk.PhotoImage(file='Icons/clear.png')
clearimg = clearimgnot.subsample(5,5)

exitimgnot = tk.PhotoImage(file='Icons/exit.png')
exitimg = exitimgnot.subsample(5,5)

addimgnot = tk.PhotoImage(file='Icons/add.png')
addimg = addimgnot.subsample(5,5)

saveimgnot = tk.PhotoImage(file='Icons/save.png')
saveimg = saveimgnot.subsample(5,5)

tk.Button(frame2, text='Add Item',image=addimg,borderwidth=0,bg='red', command=lambda:mkebil()).grid(row=8, column=1,columnspan=1)
tk.Button(frame2, text='Save Bill', image=saveimg,borderwidth=0,bg='red',command=lambda:svebil()).grid(row=8, column=2,columnspan=1)
tk.Button(frame2, text='Refresh Or Clear',image=clearimg,borderwidth=0,bg='red',command=lambda:clr()).grid(row=9, column=1,columnspan=1)
tk.Button(frame2, text='Exit', image=exitimg,borderwidth=0,bg='red',command=lambda:exmsys()).grid(row=9, column=2,columnspan=1)

#LOOPING
sprz.mainloop()
