#! /usr/bin/env python3
# coding: utf-8
from tkinter import Tk, Button, Label, StringVar
import re
import logging

#show the debug print in the console
logging.basicConfig(level=logging.DEBUG)

def graphic_interface(window):
    """UI generator"""
    SCREEN.set("")
    screen = Label(window, textvariable=SCREEN, width=12, height=2)
    screen.grid(row=0, columnspan=4)
    bt_ce = Button(window, text="CE", width=3, height=2, command=clear_screen)
    bt_ce.grid(row=1, column=0)
    bt_c = Button(window, text="C", width=3, height=2)
    bt_c.grid(row=1, column=1)
    bt_del = Button(window, text="<-", width=3, height=2, command=delete)
    bt_del.grid(row=1, column=2)
    bt_div = Button(window, text="/", width=3, height=2, command=lambda: update_screen("/"))
    bt_div.grid(row=1, column=3)
    #
    bt_seven = Button(window, text="7", width=3, height=2, command=lambda: update_screen("7"))
    bt_seven.grid(row=2, column=0)
    bt_eight = Button(window, text="8", width=3, height=2, command=lambda: update_screen("8"))
    bt_eight.grid(row=2, column=1)
    bt_nine = Button(window, text="9", width=3, height=2, command=lambda: update_screen("9"))
    bt_nine.grid(row=2, column=2)
    bt_mult = Button(window, text="*", width=3, height=2, command=lambda: update_screen("*"))
    bt_mult.grid(row=2, column=3)
    #
    bt_four = Button(window, text="4", width=3, height=2, command=lambda: update_screen("4"))
    bt_four.grid(row=3, column=0)
    bt_five = Button(window, text="5", width=3, height=2, command=lambda: update_screen("5"))
    bt_five.grid(row=3, column=1)
    bt_six = Button(window, text="6", width=3, height=2, command=lambda: update_screen("6"))
    bt_six.grid(row=3, column=2)
    bt_minus = Button(window, text="-", width=3, height=2, command=lambda: update_screen("-"))
    bt_minus.grid(row=3, column=3)
    #
    bt_one = Button(window, text="1", width=3, height=2, command=lambda: update_screen("1"))
    bt_one.grid(row=4, column=0)
    bt_two = Button(window, text="2", width=3, height=2, command=lambda: update_screen("2"))
    bt_two.grid(row=4, column=1)
    bt_three = Button(window, text="3", width=3, height=2, command=lambda: update_screen("3"))
    bt_three.grid(row=4, column=2)
    bt_plus = Button(window, text="+", width=3, height=2, command=lambda: update_screen("+"))
    bt_plus.grid(row=4, column=3)
    #
    bt_plusminus = Button(window, text="+/-", width=3, height=2, command=inverse)
    bt_plusminus.grid(row=5, column=0)
    bt_zero = Button(window, text="0", width=3, height=2, command=lambda: update_screen("0"))
    bt_zero.grid(row=5, column=1)
    bt_dot = Button(window, text=",", width=3, height=2, command=lambda: update_screen("."))
    bt_dot.grid(row=5, column=2)
    bt_equal = Button(window, text="=", width=3, height=2, command=calculate)
    bt_equal.grid(row=5, column=3)

def calculate():
    """generate the calc"""
    result = str(eval(SCREEN.get()))
    clear_screen()
    update_screen(result)

def delete():
    """delete the last char"""
    if len(SCREEN.get()) is None:
        new_screen = SCREEN.get()[:-1]
        SCREEN.set(new_screen)

def inverse():
    """add or remove -"""
    if len(SCREEN.get()) is None:
        update_screen('-')
    elif SCREEN.get()[0] == '-':
        new_screen = SCREEN.get()[1:]
        SCREEN.set(new_screen)
    else:
        new_screen = '-'+SCREEN.get()
        SCREEN.set(new_screen)

def clear_screen():
    """well..."""
    SCREEN.set("")

def update_screen(value):
    """update the label window.screen"""
    logging.debug(value)
    new_screen = SCREEN.get()+value
    SCREEN.set(new_screen)

def key_in(event):
    """look at the key press"""
    button = event.keysym
    logging.debug(button)
    if button == "KP_Enter":
        calculate()
    if button == "KP_Add":
        update_screen('+')
    if button == "KP_Divide":
        update_screen('/')
    if button == "KP_Multiply":
        update_screen('*')
    if button == "KP_Substract":
        update_screen('-')
    if button == "period":
        update_screen('.')
    if re.search(r'^KP_\d', button):
        update_screen(button[-1])

def main():
    """main function"""
    window = Tk()
    global SCREEN
    SCREEN = StringVar()
    window.title("CalcV1")
    graphic_interface(window)
    window.bind_all("<Key>", key_in)
    window.mainloop()

if __name__ == "__main__":
    """main part"""
    main()
