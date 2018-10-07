#! /usr/bin/env python3
# coding: utf-8
from tkinter import Tk, Button, Label, StringVar, Frame
import re
import logging

# show the debug print in the console
# logging.basicConfig(level=logging.DEBUG)


def graphic_interface(window):
    """UI generator"""

    frame1 = Frame(window)
    frame1.pack()
    screen = Label(frame1, textvariable=SCREEN, height=2)
    screen.pack()

    frame2 = Frame(window)
    frame2.pack(side="left")
    bt_ce = Button(frame2, text="CE", width=5, height=2,
                   command=clear_screen)
    bt_ce.grid(row=1, columnspan=2)
    bt_c = Button(frame2, text="C", width=5, height=2)
    bt_c.grid(row=1, column=2)
    bt_del = Button(frame2, text="<-", width=5, height=2,
                    command=delete)
    bt_del.grid(row=1, column=3)
    bt_div = Button(frame2, text="/", width=5, height=2,
                    command=lambda: update_screen("/"))
    bt_div.grid(row=1, column=4)
    #
    bt_seven = Button(frame2, text="7", width=5, height=2,
                      command=lambda: update_screen("7"))
    bt_seven.grid(row=2, columnspan=2)
    bt_eight = Button(frame2, text="8", width=5, height=2,
                      command=lambda: update_screen("8"))
    bt_eight.grid(row=2, column=2)
    bt_nine = Button(frame2, text="9", width=5, height=2,
                     command=lambda: update_screen("9"))
    bt_nine.grid(row=2, column=3)
    bt_mult = Button(frame2, text="*", width=5, height=2,
                     command=lambda: update_screen("*"))
    bt_mult.grid(row=2, column=4)
    #
    bt_four = Button(frame2, text="4", width=5, height=2,
                     command=lambda: update_screen("4"))
    bt_four.grid(row=3, columnspan=2)
    bt_five = Button(frame2, text="5", width=5, height=2,
                     command=lambda: update_screen("5"))
    bt_five.grid(row=3, column=2)
    bt_six = Button(frame2, text="6", width=5, height=2,
                    command=lambda: update_screen("6"))
    bt_six.grid(row=3, column=3)
    bt_minus = Button(frame2, text="-", width=5, height=2,
                      command=lambda: update_screen("-"))
    bt_minus.grid(row=3, column=4)
    #
    bt_one = Button(frame2, text="1", width=5, height=2,
                    command=lambda: update_screen("1"))
    bt_one.grid(row=4, columnspan=2)
    bt_two = Button(frame2, text="2", width=5, height=2,
                    command=lambda: update_screen("2"))
    bt_two.grid(row=4, column=2)
    bt_three = Button(frame2, text="3", width=5, height=2,
                      command=lambda: update_screen("3"))
    bt_three.grid(row=4, column=3)
    bt_plus = Button(frame2, text="+", width=5, height=2,
                     command=lambda: update_screen("+"))
    bt_plus.grid(row=4, column=4)
    #
    bt_open_parenthese = Button(frame2, text="(", width=1, height=2,
                                command=lambda: update_screen("("))
    bt_open_parenthese.grid(row=5, column=0)
    bt_close_parenthese = Button(frame2, text=")", width=1, height=2,
                                 command=lambda: update_screen(")"))
    bt_close_parenthese.grid(row=5, column=1)
    bt_zero = Button(frame2, text="0", width=5, height=2,
                     command=lambda: update_screen("0"))
    bt_zero.grid(row=5, column=2)
    bt_dot = Button(frame2, text=",", width=5, height=2,
                    command=lambda: update_screen("."))
    bt_dot.grid(row=5, column=3)
    bt_equal = Button(frame2, text="=", width=5, height=2,
                      command=calculate)
    bt_equal.grid(row=5, column=4)


def test_calculate():
    """verify if calculate won't raise error"""
    # si c'est vide
    if SCREEN.get() is None:
        return False
    # si il n'y a rien derriere un calculateur ou une parenthese ouvrante
    if SCREEN.get()[-1] in r"(/*\-+":
        logging.debug("las char is not good for calculate")
        return False
    return True


def add_missing_in_calculate():
    """Add missing elements like ) or *"""
    screen_state = SCREEN.get()
    # add closing )
    for _ in range(screen_state.count("(") - screen_state.count(")")):
        update_screen(")")
    # add * if missing with parenthesis
    screen_state = SCREEN.get()
    pos = 0
    for n in screen_state:
        if n is "(" and screen_state[pos - 1] in "0123456789":
            screen_state = screen_state[:pos]+"*"+screen_state[pos:]
            SCREEN.set(screen_state)
        pos += 1


def calculate():
    """generate the calc"""
    add_missing_in_calculate()
    if test_calculate():
        result = str(eval(SCREEN.get()))
        clear_screen()
        update_screen(result)


def delete():
    """delete the last char"""
    if len(SCREEN.get()) is not None:
        SCREEN.set(SCREEN.get()[:-1])


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


def test_update_screen(value):
    """Test if there is anything, if not there's no problem
    Test if there is already a calculator, minus is not only a calculator
    Test if there is already a dot in the number"""
    # don't start with a non logic char
    if SCREEN.get() is "" and value in ")+*/":
        return False
    if SCREEN.get() is not "":
        # test if there's already a dot in the number
        is_dot = re.split(r"[()/*\-+]", SCREEN.get())
        if "." is is_dot[-1] and value is ".":
            logging.debug("already a dot")
            return False
        # test if the last char accept a calculator
        if SCREEN.get()[-1] in r"/*+(\-" and value in "/*+":
            logging.debug("already a calculator")
            return False

        if value is ")":
            # don't close an empty parenthesis
            if SCREEN.get()[-1] is "(":
                return False
            # don't close a non open parenthesis
            if SCREEN.get().count("(") <= SCREEN.get().count(")"):
                logging.debug("Don't close a non open parenthesis")
                return False
    return True


def update_screen(value):
    """update the label window.screen"""
    logging.debug("update_screen value = %s", value)
    if test_update_screen(value):
        new_screen = SCREEN.get()+value
        SCREEN.set(new_screen)


def key_in(event):
    """look at the key press"""
    button = event.char
    logging.debug("button = %s", event.char)
    if button == "\r":  # NumPad Enter
        calculate()
    if button == "\x08":  # Backspace
        delete()
    if re.search(r"[/*\-+.()\d]", button):
        update_screen(button)


def main():
    """main function"""
    window = Tk()
    window.title("CalcV1")
    global SCREEN
    SCREEN = StringVar()
    SCREEN.set("")
    graphic_interface(window)
    window.bind_all("<Key>", key_in)
    window.mainloop()

if __name__ == "__main__":
    main()
