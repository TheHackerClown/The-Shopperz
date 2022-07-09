from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, END, StringVar


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
def wrtBil():
    if passcode.get() in code:
            bill.config(state='normal')
            bill.delete('1.0', 'end')
            tf = open((entry_3.get()))
            data = tf.read()
            bill.insert(END, data)
            bill.config(state='disabled')
            tf.close()
            passcode.set('')
    else:
            messagebox.showerror('Passcode Error', 'Password entered was wrong or not inputted correctly. Try Again!')
            


window = Tk()
window.title('The Shopperz Bill Opener')
window.geometry("676x376")
window.configure(bg = "#FFFFFF")
passcode = StringVar()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 376,
    width = 676,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    327.0,
    0.0,
    676.0,
    376.0,
    fill="#F8F8F8",
    outline="")

canvas.create_rectangle(
    0.0,
    37.0,
    326.0,
    376.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1.0,
    0.0,
    327.0,
    376.0,
    fill="#00A3FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    161.0,
    188.0,
    image=entry_image_1
)
bill = Text(
    bd=0,
    bg="#DDFFEA",
    highlightthickness=0
)
bill.place(
    x=46.0,
    y=19.0,
    width=230.0,
    height=336.0
)

canvas.create_rectangle(
    352.0,
    142.0,
    643.0,
    220.0,
    fill="#E3E3E3",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    498.0,
    188.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    show='*',
    textvariable=passcode,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=384.5,
    y=171.0,
    width=227.0,
    height=33.0
)

canvas.create_text(
    376.0,
    145.0,
    anchor="nw",
    text="Passcode To Open",
    fill="#000000",
    font=("Inter", 12 * -1)
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
    x=465.0,
    y=269.0,
    width=76.0,
    height=76.0
)

canvas.create_rectangle(
    352.0,
    32.0,
    646.0,
    108.0,
    fill="#E3E3E3",
    outline="")

canvas.create_text(
    379.0,
    37.0,
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
    x=591.0,
    y=61.0,
    width=43.0,
    height=32.69230651855469
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    481.5,
    78.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_3.place(
    x=388.0,
    y=62.0,
    width=187.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
