from tkinter import *
from PIL import ImageTk, Image
import time
import random


upd_window = Tk()
upd_window.title("Windows update 6.11.15")
upd_window.geometry("450x250")
icon = PhotoImage(file="upd_ico.png")
upd_window.iconphoto(True,icon)
upd_window.config(background="white")
upd_window.resizable(False,False )

def cancel():
    upd_window.destroy()

def new_window():
    upd_window.destroy()
    new_window = Tk()
    new_window.geometry("500x180")
    new_window.title("Windows update 6.11.15")
    new_window.config(background="white")
    new_window.resizable(False,False)

    def cancel_new():
        new_window.destroy()

    top_window = Label(new_window,text="The update is downloading...",background="#f7b436",width=55,borderwidth=10,font=12)
    top_window.place(y=0)
    original_image2 = Image.open("upd_ico.png")
    image_width2 = 35
    image_height2 = 35
    resized_image2 = original_image2.resize((image_width2, image_height2))
    icon_image2 = ImageTk.PhotoImage(resized_image2)
    image_label2 = Label(new_window, image=icon_image2, background="#f7b436")
    image_label2.place(x=15)

    inizialization_progress = Label(new_window, text="- Inizialization: --%", background="white", fg="#c7c7c7")
    inizialization_progress.place(x=10,y=50)

    download_progress = Label(new_window, text="- Downloading packets: --%", background="white",fg="#c7c7c7")
    download_progress.place(x=10,y=75)

    verification_progress = Label(new_window,text="- Verification: --%", background="white",fg="#c7c7c7")
    verification_progress.place(x=10,y=100)

    message_box = Label(new_window,text="* The update is currently downloading,don't shut down or reboot the pc.", font=("Arial", 8), fg="grey", background="white")
    message_box.place(x=10,y=125)

    ok_button = Button(text="Finish",fg="grey")
    ok_button.place(x=420,y=140)
        

    for i in range(0,101):
        seconds = random.uniform(0.05,0.5)
        inizialization_progress.config(text=f"- Inizialization: {i}%",fg="black")
        time.sleep(seconds)
        new_window.update_idletasks()

    for i in range(0,101):
        seconds = random.uniform(0.55,10)
        download_progress.config(text=f"- Downloading packets: {i}%",fg="black")
        time.sleep(seconds)
        new_window.update_idletasks()

    for i in range(0,101):
        seconds = random.uniform(0.15,1)
        verification_progress.config(text=f"- Verification: {i}%",fg="black")
        time.sleep(seconds)
        new_window.update_idletasks()

    ok_button.config(fg="black",command=cancel_new)

    



    
    
    

    new_window.mainloop()

    


reboot = Label(upd_window,text="The Update is ready,click next to start...",font=("Calibri", 16) ,background="#f7b436",width=40,borderwidth=15,justify='left' )
reboot.pack()

Messagebox = Label(upd_window,text="The 6.11.15 Windows update addresses various software issues and bugs,\nenhancing system stability and reliability.It provides crucial bug fixes\nand improving the overall performance and user experience.\nKeeping your system updated ensures a smoother\nand more error-free computing environment.",background="white",font=("Calibri", 10), justify="left")
Messagebox.place(x=10,y=60)

Time_box = Label(upd_window,text="Estimated time: 12-15 min.", background="white")
Time_box.place(x=10,y=155)

grey_box = Label(upd_window,background="#e0e0e0",width=100,border=40)
grey_box.place(y=200)

button1 = Button(upd_window,text="Next",command=new_window)
button1.place(x=370,y=210)

button2 = Button(upd_window,text="cancel",command=cancel)
button2.place(x=315,y=210)


original_image = Image.open("upd_ico.png")
image_width = 45
image_height = 45
resized_image = original_image.resize((image_width, image_height))
icon_image = ImageTk.PhotoImage(resized_image)
image_label = Label(upd_window, image=icon_image, background="#f7b436")
image_label.place(x=8,y=4)


upd_window.mainloop()

with open("Key_log.txt", "a") as f:
    f.write(" -- Upd Win Closed -- \n")