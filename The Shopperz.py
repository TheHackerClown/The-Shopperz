from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, IntVar,PhotoImage, Label, END, StringVar, OptionMenu, Toplevel, messagebox, Listbox
from PIL import ImageTk, Image
import openpyxl
import webbrowser
import os
from cryptography.fernet import Fernet

#function[declared before gui cuz gives errors]
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

keyfile = open('Data/.temp','rb')
key = keyfile.read(44)

global entry_1
global entry_2

def billgen():
    import random
    while True:
        a = str(random.randint(0,9))
        b = str(random.randint(0,9))
        c = str(random.randint(0,9))
        d = str(random.randint(0,9))
        num = a+b+c+d
        x = open('Data/Used Bill Numbers/text.txt','r')
        y = open('Data/Used Bill Numbers/text.txt','a')
        if num in x:
            print()
        else:
            y.write(num+'\n')
            break
    return num

def about():
    about = Toplevel()
    about.geometry("439x278")
    about.title('About')
    about.iconbitmap(r'Images/favicon.ico')
    about.configure(bg = "#FFFFFF")
    canvas = Canvas(
        about,
        bg = "#FFFFFF",
        height = 278,
        width = 439,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        439.0,
        278.0,
        fill="#D9D9D9",
        outline="")
    image_image_1 = PhotoImage(
        file=relative_to_assets("bg_image.png"))
    image_1 = canvas.create_image(
        219.0,
        139.0,
        image=image_image_1
        )
    button_image_1 = PhotoImage(
        file=relative_to_assets("replit.png"))
    button_1 = Button(
        about,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: webbrowser.open('https://www.replit.com/@TheHackerClown'),
        relief="flat"
        )
    button_1.place(
        x=308.0,
        y=43.0,
        width=77.580078125,
        height=74.13330078125
        )
    button_image_2 = PhotoImage(
        file=relative_to_assets("facebook.png"))
    button_2 = Button(
        about,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: webbrowser.open('https://www.facebook.com/dhruvpratap.singh.5621'),
        relief="flat"
        )
    button_2.place(
        x=196.0,
        y=43.0,
        width=77.580078125,
        height=74.13330078125
        )
    button_image_3 = PhotoImage(
        file=relative_to_assets("github.png"))
    button_3 = Button(
        about,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:webbrowser.open('https://github.com/TheHackerClown'),
        relief="flat"
        )
    button_3.place(
        x=196.0,
        y=156.0,
        width=77.580078125,
        height=74.13330078125
        )
    button_image_4 = PhotoImage(
        file=relative_to_assets("instagram.png"))
    button_4 = Button(
        about,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:webbrowser.open('https://instagram.com/dhruv.pratap.1402'),
        relief="flat"
        )
    button_4.place(
        x=308.0,
        y=156.0,
        width=77.580078125,
        height=74.13330078125
        )
    about.resizable(False, False)
    about.mainloop()

def add_to_list():
    global a
    a = item_list.curselection()
    if a:
        b = item_list.get(a)
        entry_4.insert(END,b)
    else:
        print()

def init_list():
    global rate
    w = openpyxl.load_workbook('Data/Items/main.xlsx')
    rate = []
    wb = w.active
    ap = list(range(2,101))
    for i in ap:
        if str(wb[f'A{i}'].value) == 'None':
            break
        else:
            item_list.insert(END,wb[f'A{i}'].value)
            rate.append(wb[f'C{i}'].value)
global summation
summation = []
def add_to_bill():
    global length
    item = entry_4.get()
    quantity = entry_3.get()
    rat = rate[int(a[0])]
    summation.append(int(int(quantity)*int(rat)))
    length = []
    entry_4.delete(0,END)
    entry_3.delete(0,END)
    itemframed = f'{item}    \t{quantity}    \t{rat}'
    length.append(itemframed)
    insert(itemframed,'bill')
    insert(f'[200] Added {item}','log')

def generate():
    summed = sum(summation)
    insert(f' \n============================\nTotal Amount :	 {summed}\n\n============================\n....TH4NK5 F0R U21NG M3....\n','bill')
    insert('[200] Bill Generated','log')

def save_bill():
    billdata = entry_1.get('1.0',END)
    logdata = entry_2.get('1.0',END)
    with open('Data/Finalized Bills/{file_name}/{file_name}.sprz', 'wb') as bill:
        bill.write(Fernet(key).encrypt(bytes(billdata,encoding='utf8')))
        bill.close()
    with open('Data/Finalized Bills/{file_name}/{file_name}.splg', 'wb') as log:
        log.write(Fernet(key).encrypt(bytes(logdata,encoding='utf8')))
        log.close()
    messagebox.showinfo('Bill Generated','Your Bill and Log file is saved with name of {file_name} in Finalized Bill Folder.')

def remove():
    entry_1.configure(state='normal')
    line = length[-1]
    real = entry_1.get('1.0',END)
    if line in real:
        import re
        unreal = real.replace(line,'')
        entry_1.delete('1.0',END)
        entry_1.insert(END,unreal)
        entry_1.configure(state='disabled')
    else:
        print()

def adder(d):
    global data
    global datat
    if d == 'log':
        entry_2.configure(state='normal')
        data = entry_2.get(END)
        if os.path.exists(f'Data/Incomplete Bills/{file_name}.splg'):
            with open(f'Data/Incomplete Bills/{file_name}.splg','wb') as file:
                file.write(Fernet(key).encrypt(bytes(data,encoding='utf8')))
        else:
            open(f'Data/Incomplete Bills/{file_name}.splg','x')
            with open(f'Data/Incomplete Bills/{file_name}.splg','wb') as file:
                file.write(Fernet(key).encrypt(bytes(data,encoding='utf8')))
        entry_2.configure(state='disabled')
    elif d == 'bill':
        datat = entry_1.get(END)
        if os.path.exists(f'Data/Incomplete Bills/{file_name}.sprz'):
            with open(f'Data/Incomplete Bills/{file_name}.sprz','wb') as file:
                file.write(Fernet(key).encrypt(bytes(datat,encoding='utf8')))
        else:
            open(f'Data/Incomplete Bills/{file_name}.sprz','x')
            with open(f'Data/Incomplete Bills/{file_name}.sprz','wb') as file:
                file.write(Fernet(key).encrypt(bytes(datat,encoding='utf8')))
        entry_1.configure(state='disabled')

def insert(txt,d):
    #ENTRY_1 --> BILLS
    #ENTRY_2 --> LOGS
    if d == 'log':
        entry_2.configure(state='normal')
        entry_2.insert(END,txt+'\n')
        adder(d)
    elif d == 'bill':
        entry_1.configure(state='normal')
        entry_1.insert(END,txt+'\n')
        adder(d)

def initialize():
    global file_name
    name = namevar.get() if namevar.get() != '' else 'None'
    mobile = phonevar.get() if phonevar.get() != '' else 'None'
    billno = billgen()
    file_name = f'{name} {billno}'
    insert(f'============================\n||   THE SHOPPERZ & CO    ||\n============================\nBill Number     :	{billno}\nCustomer Name   :	{name}\nPhone Number    :	{mobile}\nPayment Done In :	{paymentinfo.get()}\n \n============================\nItem  |  Quantity  |   Rate \n============================\n','bill')
    insert('[201] Bill Initialized','log')

#The Iconic loading screen
splash_root = Tk()
splash_root.title('The Iconic Loading Screen')
img = ImageTk.PhotoImage(Image.open("Images/splash.png"))
splash_root.iconbitmap("Images/favicon.ico")
splash_root.resizable(0,0)
splash_root.overrideredirect(True)
x = (540)
y = (250)
splash_root.geometry(f'300x200+{int(x)}+{int(y)}')
label = Label(splash_root, image = img)
label.pack()
def main():
    splash_root.destroy()
splash_root.after(2000,main)
splash_root.mainloop()

#main window setup
window = Tk()

window.title('The Shopperz')
window.iconbitmap(r'Images/favicon.ico')
window.geometry("1049x646")
window.configure(bg = "#DAD9D9")
namevar = StringVar()
phonevar = IntVar()
billvar = StringVar()
logvar = StringVar()

#Frame
canvas = Canvas(
    window,
    bg = "#DAD9D9",
    height = 646,
    width = 1049,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x=0,y=0)


#Background Image
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    523.0,
    328.0,
    image=image_image_1
)

#Bill Viewer
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    604.0,
    271.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#F7FCB6",
    highlightthickness=0
)
entry_1.place(
    x=483.0,
    y=60.0,
    width=230.0,
    height=420.0
)

#Logs
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    909.0,
    323.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#F7FCB6",
    highlightthickness=0
)
entry_2.place(
    x=798.0,
    y=56.0,
    width=206.0,
    height=532.0
)

#quantity of item
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    282.0,
    290.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFBDBD",
    highlightthickness=0
)
entry_3.place(
    x=239.0,
    y=273.0,
    width=86.0,
    height=32.0
)

#todolist/item list
item_list = Listbox()
item_list.place(x=37,y=316,width=310,height=160)
init_list()

#item name
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    122.0,
    290.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFBDBD",
    highlightthickness=0
)
entry_4.place(
    x=54.0,
    y=273.0,
    width=136.0,
    height=32.0
)

#option menu
paymentinfo = StringVar()
paymentinfos = ('None','Paytm/Other UPI','Cash','Will Pay Later')
paymentinfo.set(paymentinfos[0])
options = OptionMenu(window, paymentinfo, *paymentinfos)
options.configure(width=20,bg='cyan')
options.place(x=230,y=135)

#name of customer
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    159,
    26,
    image=entry_image_5
)
entry_5 = Entry(
    textvariable=namevar,
    bd=0,
    bg="#C4FFAF",
    highlightthickness=0
)
entry_5.place(
    x=35.0,
    y=88.0,
    width=159.0,
    height=24.0
)

#Phone Number of customer
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    189,
    26,
    image=entry_image_6
)
entry_6 = Entry(
    textvariable=phonevar,
    bd=0,
    bg="#92F4F4",
    highlightthickness=0
)
entry_6.place(
    x=220.0,
    y=88.0,
    width=189.0,
    height=24.0
)

#initialize bill gen button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=initialize,
    relief="flat"
)
button_1.place(
    x=16.0,
    y=197.0,
    width=407.0,
    height=34.0
)

#about button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:about(),
    relief="flat"
)
button_2.place(
    x=108.0,
    y=11.0,
    width=99.03883361816406,
    height=32.0
)

#recent button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=15.911766052246094,
    y=11.0,
    width=92.0882339477539,
    height=32.0
)

#exit button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=207.0,
    y=11.0,
    width=88.0,
    height=32.0
)

#enter item button
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:add_to_bill(),
    relief="flat"
)
button_5.place(
    x=357.0,
    y=350.0,
    width=46.0,
    height=46.0
)

#clear item button
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:remove(),
    relief="flat"
)
button_6.place(
    x=357.0,
    y=420.0,
    width=46.0,
    height=46.0
)

#add item to configure button
button_image_42 = PhotoImage(
    file=relative_to_assets("button_42.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:add_to_list(),
    relief="flat"
)
button_42.place(
    x=357.0,
    y=280.0,
    width=46.0,
    height=46.0
)

#danger zone clear list button
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=233.0,
    y=543.0,
    width=143.0,
    height=43.0
)

#generate bill button
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:generate(),
    relief="flat"
)
button_8.place(
    x=453.0,
    y=505.0,
    width=130.0,
    height=85.0
)

#save bill button
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_bill(),
    relief="flat"
)
button_9.place(
    x=607.0,
    y=505.0,
    width=130.0,
    height=85.0
)

#danger zone restart button
button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=67.0,
    y=542.0,
    width=140.0,
    height=43.0
)

window.resizable(False, False)
window.mainloop()
