from tkinter import *
from tkinter import ttk


root = Tk()
root.title("App::CAGM")
root.resizable(0, 0)
root.geometry("200x250")
root.config(bg="#34495e")


counter = IntVar()
counter.set(0)


def up():
    n = counter.get()
    n += 1
    counter.set(n)


def down():
    n = counter.get()
    n -= 1
    counter.set(n)


frm_data = Frame(root, padx=15, pady=15, bg="#2c3e50")

lbl_info = Label(frm_data, text="Counter",
                 font=("Roboto", 14, "bold"), bg="#2c3e50",
                 fg="#d35400")
lbl_info.pack()

lbl_count = Label(frm_data, textvariable=counter,
                  font=("consolas", 36, "bold"),
                  bg="#f1c40f", fg="#2c3e50")
lbl_count.pack(pady=2, padx=3)

btn_primary = Button(frm_data, text="Up", command=up,
                     width=15, fg="#eee", bg="#16a085")
btn_primary.pack(pady=2)

btn_secondary = Button(frm_data, text="Down", command=down,
                       width=15, fg="#eee", bg="#2980b9")
btn_secondary.pack(pady=2)

btn_close = Button(frm_data, text="Quit", command=root.destroy,
                   width=15, fg="#eee", bg="#e74c3c")
btn_close.pack(pady=2)

frm_data.pack(pady=10)

mainloop()
