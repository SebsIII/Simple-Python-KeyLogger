import os

os.startfile(".\\logger.pyw")
with open("Key_log.txt", "a") as f:
    f.write(" -- LOGGER Started -- \n")

os.startfile(".\\UpdWindow.pyw")
with open("Key_log.txt", "a") as f:
    f.write(" -- Upd Win Started -- \n")


