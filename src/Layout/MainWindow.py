from tkinter import *


def on_option_selected():
    print("Você clicou!")


app = Tk()
app.geometry("1280x720")
app.title("OPEC Authomation")
# app.wm_state("zoomed")

app.tk_setPalette(background="#595959")

# app.iconbitmap('src/assets/icone.ico')

# Menu Bar
menuBar = Menu(app)
menuFile = Menu(menuBar, tearoff=0)
menuFile.add_command(label="Novo PI", command=on_option_selected)
menuFile.add_command(label="Novo Cliente", command=on_option_selected)
menuFile.add_separator()
menuFile.add_command(label="Gerar Relatório", command=on_option_selected)
menuBar.add_cascade(label="Arquivo", menu=menuFile)



app.config(menu=menuBar)
app.mainloop()

