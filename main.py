from PIL import Image
from SysTrayIcon import SysTrayIcon
import os, threading, keyboard, time
import multiprocessing as mp

if __name__ == "__main__":
    default_path = r"C:\Users\Work.HANSPC\Desktop\test.js"
    icon = "./assets/AutoActivity.ico"
    hover_text = "SysTrayIcon.py Demo"

    def start(sysTrayIcon): 
        print('Starting...')
        open(default_path, 'w+')
        os.startfile(default_path)

    def pause(sysTrayIcon):
        print('Pausing...')

    def quit(sysTrayIcon): 
        print('Quiting...')
        try:
            os.remove(default_path)
        except OSError:
            pass
    

    menu_options = (('Start', None, start), ('Pause', None, pause))
    SysTrayIcon(icon, hover_text, menu_options, on_quit=quit, default_menu_index=1)



# def hello(sysTrayIcon): print("Hello World.")
# def simon(sysTrayIcon): print("Hello Simon.")
# menu_options = (('Say Hello', next(icons), hello),
#                 ('Switch Icon', None, switch_icon),
#                 ('A sub-menu', next(icons), (('Say Hello to Simon', next(icons), simon),
#                                               ('Switch Icon', next(icons), switch_icon),
#                                              ))
#                )