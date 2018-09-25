#! /usr/bin/env python3 
# coding: utf-8
from tkinter import *


def graphic_interface():
    boutton_list = [["screen"],
                    ["CE","C","Del","/"],
                    [7,8,9,"*"],
                    [4,5,6,"-"],
                    [1,2,3,"+"],
                    ["±","0",".","="]]
    print(boutton_list)

    window = Tk()
    for ui_row in boutton_list:
        for ui_colums in ui_row:
            pass


    screen = Label(window, text="coucou!", width=12, height=2)
    screen.grid(row=0,columnspan=4)

    bt_ce = Button(window, text="CE", width=3, height=2)
    bt_ce.grid(row=1, column=0)
    bt_c = Button(window, text="C", width=3, height=2)
    bt_c.grid(row=1, column=1)
    bt_del = Button(window, text="<-", width=3, height=2)
    bt_del.grid(row=1, column=2)
    bt_div = Button(window, text="/", width=3, height=2)
    bt_div.grid(row=1, column=3)

    bt_seven = Button(window, text="7", width=3, height=2)
    bt_seven.grid(row=2, column=0)
    bt_eight = Button(window, text="8", width=3, height=2)
    bt_eight.grid(row=2, column=1)
    bt_nine = Button(window, text="9", width=3, height=2)
    bt_nine.grid(row=2, column=2)
    bt_mult = Button(window, text="*", width=3, height=2)
    bt_mult.grid(row=2, column=3)

    bt_four = Button(window, text="4", width=3, height=2)
    bt_four.grid(row=3, column=0)
    bt_five = Button(window, text="5", width=3, height=2)
    bt_five.grid(row=3, column=1)
    bt_six = Button(window, text="6", width=3, height=2)
    bt_six.grid(row=3, column=2)
    bt_minus = Button(window, text="-", width=3, height=2)
    bt_minus.grid(row=3, column=3)

    bt_one = Button(window, text="1", width=3, height=2)
    bt_one.grid(row=4, column=0)
    bt_two = Button(window, text="2", width=3, height=2)
    bt_two.grid(row=4, column=1)
    bt_three = Button(window, text="3", width=3, height=2)
    bt_three.grid(row=4, column=2)
    bt_plus = Button(window, text="+", width=3, height=2)
    bt_plus.grid(row=4, column=3)

    bt_plusminus = Button(window, text="+/-", width=3, height=2)
    bt_plusminus.grid(row=5, column=0)
    bt_zero = Button(window, text="0", width=3, height=2)
    bt_zero.grid(row=5, column=1)
    bt_dot = Button(window, text=",", width=3, height=2)
    bt_dot.grid(row=5, column=2)
    bt_equal = Button(window, text="=", width=3, height=2)
    bt_equal.grid(row=5, column=3)

    window.mainloop()

def main():
    graphic_interface()

if __name__=="__main__":
    main()