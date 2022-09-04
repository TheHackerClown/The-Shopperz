from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, END, StringVar, OptionMenu, Toplevel, messagebox
from turtle import bgcolor
from PIL import ImageTk, Image
import webbrowser
#from cryptography.fernet import Fernet

#function[declared before gui cuz gives errors]
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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


def insert(txt,d):
    #ENTRY_1 --> BILLS
    #ENTRY_2 --> LOGS
    if d == 'log':
        entry_2.insert(END,txt+'\n')
    elif d == 'bill':
        entry_1.insert(END,txt+'\n')
def initialize():
    name = entry_5.get() if entry_5.get() != '' else 'None'
    mobile = entry_6.get() if entry_6.get() != '' else 'None'
    billno = billgen()
    insert(f'============================\n||   THE SHOPPERZ & CO    ||\n============================Bill Number     :	{billno}\n Customer Name   :	{name}\n Phone Number    :	{mobile}\n Payment Done In :	Cash\n \n','bill')
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

#todolist place area
canvas.create_rectangle(
    37.0,
    316.0,
    342.0,
    473.0,
    fill="#D9D9D9",
    outline="")

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
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=357.0,
    y=293.0,
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
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=357.0,
    y=366.0,
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
    command=lambda: print("button_8 clicked"),
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
    command=lambda: print("button_9 clicked"),
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
