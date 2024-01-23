from tkinter import *


def on_option_selected():
    print("Você clicou!")


clientWindow = Tk()
clientWindow.geometry("1280x720")
clientWindow.title("OPEC Authomation")
# clientWindow.wm_state("zoomed")

clientWindow.tk_setPalette(background="#595959")

# clientWindow.iconbitmap('src/assets/icone.ico')

# Menu Bar
menuBar = Menu(clientWindow)
menuFile = Menu(menuBar, tearoff=0)
menuFile.add_command(label="Novo PI", command=on_option_selected)
menuFile.add_command(label="Novo Cliente", command=on_option_selected)
menuFile.add_separator()
menuFile.add_command(label="Gerar Relatório", command=on_option_selected)
menuBar.add_cascade(label="Arquivo", menu=menuFile)


clientWindow.config(menu=menuBar)
clientWindow.mainloop()
