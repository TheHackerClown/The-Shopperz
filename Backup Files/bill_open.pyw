from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

ws = Tk()
ws.title("Shopperz Opener")
ws.geometry("400x450")
bg = ImageTk.PhotoImage(Image.open("Icons/bg.png"))
lbl = Label(ws,image=bg)
lbl.place(x=0,y=0)
fram1 = Frame(ws)
fram1.pack()

txtarea = Text(ws, width=45, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="Bills/", 
        title="Open Bill File", 
        filetypes=(("Shopperz Files (Secure)", "*.sprz"),('Text (Unsecure)', '*.txt'))
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    txtarea.config(state=DISABLED)
    tf.close()

saveimg = PhotoImage(file='Icons/open_folder.png')
save = saveimg.subsample(5, 5)

Button(
    ws, 
    text="Open File", 
    command=openFile,
    image=save,
    compound=LEFT
    ).pack(side=RIGHT, padx=20)

ws.mainloop()
