import tkinter as tk


def menu_principal():
    print("Você clicou no menu principal.")


def menu_arquivo():
    print("Você clicou no menu arquivo.")


def menu_editar():
    print("Você clicou no menu editar.")


def menu_visualizar():
    print("Você clicou no menu visualizar.")


def menu_ajuda():
    print("Você clicou no menu ajuda.")


# Cria a janela principal
janela = tk.Tk()
janela.title("Aplicativo de exemplo")

# Cria os menus
menu_principal = tk.Menu(janela)
menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_editar = tk.Menu(menu_principal, tearoff=0)
menu_visualizar = tk.Menu(menu_principal, tearoff=0)
menu_ajuda = tk.Menu(menu_principal, tearoff=0)

# Adiciona ícones aos menus
menu_arquivo.add_command(label="Abrir", image="folder.png", command=menu_principal)
menu_arquivo.add_command(label="Salvar", image="save.png", command=menu_principal)
menu_arquivo.add_command(label="Sair", image="exit.png", command=janela.quit)

menu_editar.add_command(label="Copiar", image="copy.png", command=menu_principal)
menu_editar.add_command(label="Colar", image="paste.png", command=menu_principal)
menu_editar.add_command(label="Recortar", image="cut.png", command=menu_principal)

menu_visualizar.add_command(
    label="Ampliar", image="zoom-in.png", command=menu_principal
)
menu_visualizar.add_command(
    label="Reduzir", image="zoom-out.png", command=menu_principal
)

menu_ajuda.add_command(label="Sobre", image="info.png", command=menu_principal)

# Adiciona os menus à barra de menus
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_principal.add_cascade(label="Editar", menu=menu_editar)
menu_principal.add_cascade(label="Visualizar", menu=menu_visualizar)
menu_principal.add_cascade(label="Ajuda", menu=menu_ajuda)

# Adiciona cores e fontes aos menus
menu_principal.config(bg="white", fg="black")
menu_arquivo.config(bg="blue", fg="white")
menu_editar.config(bg="green", fg="white")
menu_visualizar.config(bg="yellow", fg="black")
menu_ajuda.config(bg="red", fg="white")

# Exibe a janela
janela.mainloop()
