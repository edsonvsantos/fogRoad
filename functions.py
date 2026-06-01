import tkinter as tk
from PIL import Image, ImageTk
import cv2


def tocar_video_com_texto(root):
    # limpa menu
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(
        root,
        width=1280,
        height=720,
        highlightthickness=0
    )
    canvas.pack()

    video = cv2.VideoCapture(
        "assets/videos/tela-carregamento.mp4"
    )

    # cria imagem vazia
    imagem_id = canvas.create_image(
        0,
        0,
        anchor="nw"
    )

    # texto na frente
    texto_id = canvas.create_text(
        640,
        580,
        text="",
        fill="white",
        font=("Times New Roman", 24),
        width=1000,
        justify="center"
    )

    historia = [
        "A estrada desaparecia atrás de você.",
        "A neblina engolia tudo ao redor.",
        "Sem placas.",
        "Sem qualquer sinal de vida.",
        "Até que uma luz surgiu ao longe.",
        "Uma placa balançava lentamente.",
        "POUSADA MOONVEIL",
        "A última parada antes da estrada desaparecer outra vez."
    ]

    linha_atual = 0

    # ----------------------------
    # vídeo
    # ----------------------------
    def atualizar_video():
        ret, frame = video.read()

        if not ret:
            video.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )
            ret, frame = video.read()

        if ret:
            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            imagem = Image.fromarray(frame)
            imagem = imagem.resize((1280, 720))

            foto = ImageTk.PhotoImage(imagem)

            canvas.itemconfig(
                imagem_id,
                image=foto
            )

            canvas.image = foto

        root.after(
            33,
            atualizar_video
        )

    # ----------------------------
    # texto
    # ----------------------------
    def mostrar_proxima_linha():
        nonlocal linha_atual

        if linha_atual < len(historia):
            canvas.itemconfig(
                texto_id,
                text=historia[linha_atual]
            )

            linha_atual += 1

            root.after(
                3500,
                mostrar_proxima_linha
            )

    atualizar_video()
    mostrar_proxima_linha()


def clicar_start(root):
    tocar_video_com_texto(root)