# -*- coding: utf-8 -*-
from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def cal():

    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    root.configure(bg="#222831")

    entry_font = font.Font(size=20, weight="bold")
    entry = Entry(root, justify="right", font=entry_font, bd=0, bg="#393E46", fg="#FFD369", insertbackground="#FFD369", relief="flat")
    entry.grid(row=0, column=0, columnspan=4, sticky=N + W + S + E, padx=10, pady=15, ipady=10)

    # Button styles
    cal_button_bg = '#00ADB5'
    num_button_bg = '#393E46'
    other_button_bg = '#FFD369'
    text_fg = '#EEEEEE'
    button_active_bg = '#222831'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg, font=("Arial", 16, "bold"), padx=20, pady=15, bd=0, activebackground=button_active_bg, relief="flat")
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg, font=("Arial", 16, "bold"), padx=20, pady=15, bd=0, activebackground=button_active_bg, relief="flat")
    other_button = partial(Button, root, fg="#222831", bg=other_button_bg, font=("Arial", 16, "bold"), padx=20, pady=15, bd=0, activebackground="#FFD369", relief="flat")

    # Layout grid
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    # Number buttons
    button7 = num_button(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5, padx=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5, padx=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5, padx=5)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5, padx=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5, padx=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5, padx=5)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5, padx=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5, padx=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5, padx=5)

    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5, padx=5)

    button13 = num_button(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=5, column=1, pady=5, padx=5)

    # Operator buttons
    button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=4, column=3, pady=5, padx=5)

    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5, padx=5)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3, pady=5, padx=5)

    button14 = cal_button(text='/', command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5, padx=5)

    button18 = cal_button(text='^', command=lambda: get_input(entry, '**'))
    button18.grid(row=5, column=2, pady=5, padx=5)

    # Other buttons
    button15 = other_button(text='<-', command=lambda: backspace(entry))
    button15.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

    button16 = other_button(text='C', command=lambda: clear(entry))
    button16.grid(row=1, column=2, pady=5, padx=5)

    button17 = cal_button(text='=', command=lambda: calc(entry))
    button17.grid(row=5, column=3, pady=5, padx=5)

    exit_btn = other_button(text='Quit', command=root.quit)
    exit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=5, sticky=N + S + E + W)

    root.mainloop()


if __name__ == '__main__':
    cal()
