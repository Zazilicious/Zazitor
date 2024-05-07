#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Zazitor")
root.geometry("1200x660")

global opened_name
opened_name = False

global selected
selected = False
#create new file
def new_file():
    m_text.delete("1.0", END)
    root.title("New File")
    global opened_name
    opened_name = False

#open file
def open_file():
    m_text.delete("1.0", END)
    t_file = filedialog.askopenfilename(initialdir="@/home", title="Open File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*.html"),("Python Files", "*.py"),("All Files", "*.*")))
    if t_file:
        global opened_name
        opened_name = t_file
        open_status_name = t_file
        name = t_file
        t_file = open(t_file, 'r')
        stuff = t_file.read()
        m_text.insert(END, stuff)
        t_file.close()

#save as file
def save_as_file(e=False):
    t_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="@/home", title="Save File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*.html"),("Python Files", "*.py"),("All Files", "*.*")))
    t_file = open(t_file, 'w')
    t_file.write(m_text.get(1.0, END))
    t_file.close()


#save file
def save_file(e=False):
    global opened_name
    if opened_name:
        t_file = open(opened_name, 'w')
        t_file.write(m_text.get(1.0, END))
        t_file.close()
    else:
        save_as_file()

#cut text
def cut_text(e=False):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if m_text.selection_get():
            selected = m_text.selection_get()
            m_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

#copy text
def copy_text(e=False):
    global selected
    if e:
        selected = root.clipboard_get()
    if m_text.selection_get():
        selected = m_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#paste text
def paste_text(e=False):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = m_text.index(INSERT)
            m_text.insert(position, selected)

#select all
def select_all(e=False):
    m_text.tag_add('sel', '1.0', 'end')

#clear all
def clear_all(e=False):
    m_text.delete(1.0,  END)


#frame
m_frame = Frame(root)
m_frame.pack(pady=5)

#scrollbar
t_scroll = Scrollbar(m_frame)
t_scroll.pack(side=RIGHT, fill=Y)

#textbox 
m_text = Text(m_frame, width=97, height=25, font=("Calibri", 16), selectbackground="yellow", selectforeground="black", undo=True) 
m_text.pack()


#config scrollbar

t_scroll.config(command=m_text.yview)

#menu
m_menu = Menu(root)
root.config(menu=m_menu)

#file menu
f_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="File", menu=f_menu)
f_menu.add_command(label="New", command=new_file)
f_menu.add_command(label="Open", command=open_file)
f_menu.add_command(label="Save", command=save_file)
f_menu.add_command(label="Save as", command=save_as_file)
f_menu.add_separator()
f_menu.add_command(label="Exit", command=root.quit)

#edit menu
e_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Edit", menu=e_menu)
e_menu.add_command(label="Cut   (Ctrl+X)", command=cut_text)
e_menu.add_command(label="Copy   (Ctrl+C)", command=copy_text)
e_menu.add_command(label="Paste   (Ctrl+V)", command=paste_text)
e_menu.add_separator()
e_menu.add_command(label="Undo", command=m_text.edit_undo)
e_menu.add_separator()
e_menu.add_command(label="Redo", command=m_text.edit_redo)
e_menu.add_separator()
e_menu.add_command(label="Select All", command= select_all)
e_menu.add_command(label="Clear", command=clear_all)
e_menu.add_separator()

#edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', cut_text)
root.bind('<Control-Key-v>', cut_text)
root.bind('<Control-Key-A>',select_all)
root.bind('<Control-Key-a>',select_all)
root.bind('<Control-Key-s>', save_file)
root.bind('<Control-Key-S>', save_as_file)

root.mainloop()