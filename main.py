import tkinter as tk
from PIL import Image, ImageTk
from functions import clicar_start

# ----------------------------
# janela
# ----------------------------
root = tk.Tk()
root.title("Fog Road")
root.geometry("1280x720")
root.resizable(False, False)

# ícone da janela
icone_janela = tk.PhotoImage(
    file="assets/imagens/icone_do_jogo.png"
)
root.iconphoto(True, icone_janela)

# ----------------------------
# fundo
# ----------------------------
fundo_img = Image.open(
    "assets/imagens/menu.png"
)

fundo_img = fundo_img.resize((1280, 720))
fundo_tk = ImageTk.PhotoImage(fundo_img)

canvas = tk.Canvas(
    root,
    width=1280,
    height=720,
    highlightthickness=0
)

canvas.pack()

canvas.create_image(
    0,
    0,
    anchor="nw",
    image=fundo_tk
)

# ----------------------------
# botão start
# ----------------------------
botao_start = tk.Button(
    root,
    text="START",
    font=("Times New Roman", 20, "bold"),
    bg="#5b4424",
    fg="white",
    activebackground="#7a5b31",
    activeforeground="white",
    width=12,
    relief="raised",
    bd=4,
    cursor="hand2",

    # chama a função
    command=lambda: clicar_start(root)
)

canvas.create_window(
    640,
    550,
    window=botao_start
)

root.mainloop()