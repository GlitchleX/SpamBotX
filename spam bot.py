from dearpygui.core import *
from dearpygui.simple import *
import pyautogui

def start(sender,data):
    print(get_value("spam text")) #for check this program is working
    print(get_value("xpos"))
    print(get_value("ypos"))
    print(get_value("count of message"))

    xpos = get_value("xpos")
    ypos = get_value("ypos")
    spam_text = get_value("spam text")
    spamtime = get_value("count of message")
    pyautogui.click(x=xpos, y=ypos, button='left')
    for n in range(spamtime):
        pyautogui.write(spam_text)
        pyautogui.press('enter')
    
def close_help():
    close_popup("help_popup")

with window("Spam"):
    
    #widget moment
    add_separator()
    add_spacing(count = 5)

    add_text("SpamBotX 1.0")

    add_spacing(count = 5)

    add_button("What is this")
    with popup("What is this", "Help", mousebutton = False, modal = True):
        add_text("SpamBotX is the spam some text you want\nand built with Python\n\nIf you start spam, the spam\nwill be start and stop after 5 sec")
        add_button("Close", callback = lambda: close_popup("Help"))

    add_spacing(count = 5)

    add_separator()

    add_spacing(count = 5)

    add_input_text(name = "spam text", hint = "Type text here which you want to spam")
    add_input_int(name = "xpos")
    add_input_int(name = "ypos")
    add_input_int(name = "count of message")
    
    add_button("Start Spam", callback = start)

    add_spacing(count = 5)
    add_separator()
    add_spacing(count = 5)
    add_text("Made by ChobojaX")
    add_spacing(count = 5)
    add_separator()

    #window settings moment
    set_main_window_size(500,500)
    set_primary_window("Spam", True)
    set_main_window_pos(200,200)
    set_main_window_resizable(False)
    set_main_window_title("SpamBotX 1.0")

start_dearpygui()
