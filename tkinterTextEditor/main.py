from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("TEXT EDITOR")

txt = Text(window, fg="darkblue", bg="light yellow", font="Calibri 14")
txt.pack()

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt.delete("1.0", END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt.insert(END, text)
    window.title(f"TEXT EDITOR - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt.get("1.0", END)
        output_file.write(text)
    window.title(f"TEXT EDITOR - {filepath}")

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save As...", command=save_file)

window.mainloop()