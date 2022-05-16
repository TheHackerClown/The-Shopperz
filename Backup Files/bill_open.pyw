from tkinter import *
from tkinter import filedialog

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

ws = Tk()
ws.title("Shopperz Opener")
ws.geometry("400x450")
ws['bg']='red'

txtarea = Text(ws, width=45, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()
