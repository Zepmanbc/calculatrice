#! /usr/bin/env python3
# coding: utf-8
from tkinter import Tk, Button, Label, StringVar, Frame
import re
import logging

# show the debug print in the console
logging.basicConfig(level=logging.DEBUG)


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
                                command=lambda: update_screen("(+)"))
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


def calculate():
    """generate the calc"""
    # test si il manque des parentheses et les fermer
    # si il y a juste une parenthese
    # si il y a juste un signe
    # si il n'y a rien derriere un calculateur
    # ajouter un * si il y a des parentheses sans signe
    screen_state = SCREEN.get()
    for _ in range(screen_state.count("(") - screen_state.count(")")):
        update_screen(")")

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
    if SCREEN.get() is not "":
        is_dot = re.split(r"[()/*\-+]", SCREEN.get())
        if "." is is_dot[-1] and value is ".":
            logging.debug("already a dot")
            return False
        if SCREEN.get()[-1] in "/*+" and value in "/*+":
            logging.debug("already a calculator")
            return False
        # tester si il y a une ( pour la fermer
        # ne pas fermer une parenthese juste apres l'avoir ouvert
        # sinon fonction
        if SCREEN.get()[-1] is "(" and value is ")":
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
    global SCREEN
    SCREEN = StringVar()
    SCREEN.set("")
    window.title("CalcV1")
    graphic_interface(window)
    window.bind_all("<Key>", key_in)
    window.mainloop()

if __name__ == "__main__":
    main()
