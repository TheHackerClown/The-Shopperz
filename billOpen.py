from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, END, StringVar
from cryptography.fernet import Fernet

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./IMG_Data/bill_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

global openFile
global wrtBil
def openFile():
    global tf
    entry_3.delete(0, END)
    tf = filedialog.askopenfilename(
        initialdir="Bills/",
        title='Open Sprz Bill File',
        filetypes =(('Shopperz Files (Secure)','*.sprz'),('Text (Unsecure)', '*.txt'))
        )
    entry_3.insert(END, tf)
x= open('IMG_Data/bill_assets/compiler', 'r')
code = x.read(12)
akey = open('Bills/.temp','rb')
key = akey.read()
def wrtBil():
    if passcode.get() in code:
            bill.config(state='normal')
            bill.delete('1.0', 'end')
            with open((entry_3.get()),'rb') as file:
                content = file.read()
                blah_blah = Fernet(key).decrypt(content)
            bill.insert(END, blah_blah)
            bill.config(state='disabled')
            passcode.delete(0,'end')
    else:
            messagebox.showerror('Passcode Error', 'Password entered was wrong or not inputted correctly. Try Again!')
            


window = Tk()

window.geometry("676x390")
window.configure(bg = "#FFFFFF")
window.iconbitmap('IMG_Data/bill_assets/bill.ico')
window.title('The Shopperz Bill Opener')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 390,
    width = 676,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    326.0,
    0.0,
    675.0,
    390.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    326.0,
    390.0,
    fill="#00A3FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    156.0,
    193.0,
    image=entry_image_1
)
bill = Text(
    bd=0,
    bg="#DDFFEA",
    highlightthickness=0
)
bill.place(
    x=41.0,
    y=17.0,
    width=230.0,
    height=350.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: wrtBil(),
    relief="flat"
)
button_1.place(
    x=463.0,
    y=300.0,
    width=76.0,
    height=76.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    516.0,
    214.0,
    image=image_image_1
)

canvas.create_text(
    568.0,
    360.0,
    anchor="nw",
    text="Made By Dhruv",
    fill="#000000",
    font=("Inter", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    501.0,
    186.5,
    image=entry_image_2
)
passcode = Entry(
    bd=0,
    bg="#D9D9D9",
    show='*',
    highlightthickness=0
)
passcode.place(
    x=387.5,
    y=169.0,
    width=227.0,
    height=33.0
)

canvas.create_text(
    379.0,
    145.0,
    anchor="nw",
    text="Passcode To Open",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    379.0,
    46.0,
    anchor="nw",
    text=" File Path",
    fill="#000000",
    font=("Inter", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: openFile(),
    relief="flat"
)
button_2.place(
    x=588.0,
    y=70.0,
    width=43.0,
    height=32.69230651855469
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    476.5,
    87.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_3.place(
    x=383.0,
    y=71.0,
    width=187.0,
    height=30.0
)

window.resizable(False, False)
window.mainloop()
