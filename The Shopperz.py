
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1049x646")
window.configure(bg = "#DAD9D9")


canvas = Canvas(
    window,
    bg = "#DAD9D9",
    height = 646,
    width = 1049,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    523.0,
    328.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    595.0,
    271.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#F7FCB6",
    highlightthickness=0
)
entry_1.place(
    x=480.0,
    y=60.0,
    width=230.0,
    height=420.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    901.0,
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

canvas.create_rectangle(
    -1.0,
    42.0,
    423.0,
    43.0,
    fill="#000000",
    outline="")

canvas.create_text(
    849.0,
    13.0,
    anchor="nw",
    text="LOGS",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

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

canvas.create_rectangle(
    37.0,
    316.0,
    342.0,
    473.0,
    fill="#D9D9D9",
    outline="")

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

canvas.create_text(
    251.0,
    144.0,
    anchor="nw",
    text="here",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 10 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    105.5,
    101.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#C4FFAF",
    highlightthickness=0
)
entry_5.place(
    x=26.0,
    y=88.0,
    width=159.0,
    height=24.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    306.5,
    101.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#92F4F4",
    highlightthickness=0
)
entry_6.place(
    x=212.0,
    y=88.0,
    width=189.0,
    height=24.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=16.0,
    y=197.0,
    width=407.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=108.0,
    y=11.0,
    width=99.03883361816406,
    height=32.0
)

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

canvas.create_text(
    233.0,
    254.0,
    anchor="nw",
    text="QUANTITY",
    fill="#000000",
    font=("Inter ExtraBold", 13 * -1)
)

canvas.create_text(
    49.0,
    255.0,
    anchor="nw",
    text="ITEM NAME",
    fill="#000000",
    font=("Inter ExtraBold", 13 * -1)
)

canvas.create_text(
    176.0,
    516.0,
    anchor="nw",
    text="DANGER ZONE",
    fill="#FF0000",
    font=("Inter ExtraBold", 13 * -1)
)

canvas.create_text(
    482.0,
    21.0,
    anchor="nw",
    text=" Bill Preview",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
