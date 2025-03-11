from tkinter import (
    Frame,
    Label,
    Button,
    Tk,
    Entry,
    PhotoImage,
    END
)
from src.dirs import Dirs
import os
import sys

class App:
    def __init__(self):
        self.raiz = Tk()
        # self.raiz.geometry('600x300')
        self.raiz.title('SGP - Sistema Gerador de Pastas')
        # self.raiz.resizable(False, False)
        self.bg = '#0b0574'
        if getattr(sys, 'frozen', False):
            self.logo_path = os.path.join(sys._MEIPASS, 'img', 'logo_tamura_mod.png')
        else:
            self.logo_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'logo_tamura_mod.png')

        self.logo = PhotoImage(file=self.logo_path)
        self.frame()

    def frame(self):
        self.frame_principal = Frame(
            master=self.raiz,
            borderwidth=5,
            relief='groove',
            width=600,
            height=200,
            bg=self.bg
        )
        self.frame_principal.grid(
            column=0,
            row=0,
            rowspan=3,
            columnspan=2,
            sticky=('W', 'E', 'N', 'S')
        )

        self.label_logo = Label(
            master=self.raiz,
            image=self.logo,
            background=self.bg,
        )
        self.label_logo.grid(
            column=0,
            row=0,
            pady=10
        )
        self.label_op = Label(
            text='Digite o número da op: ',
            fg='#fff',
            bg=self.bg,
            font='Arial 14'
        )
        self.label_op.grid(
            column=0,
            row=1,
            sticky=('N', 'W'),
            padx=50,
            pady=100
        )
        self.entry = Entry(
            bg='#fff',
            relief='sunken',
            borderwidth=1,
            fg='black',
        )
        self.entry.focus_force()
        self.entry.grid(
            column=0,
            row=1,
            sticky=('N', 'W'),
            padx=250,
            pady=100
        )
        self.botao = Button(
            text='Criar Pasta',
            cursor='arrow',
            font='Arial',
            highlightcolor='#fff',
            command=self.dirs,
        )
        self.botao.grid(
            column=0,
            row=1,
            pady=150,
        )

        self.label_resultado = Label(
            text='',
            font='Arial 14 bold',
            bg=self.bg
        )
        self.label_resultado.grid(
            column=0,
            row=2,
            pady=20
        )

    def dirs(self):
        self.op = self.entry.get()

        if not self.op:
            self.label_resultado.config(
                text='OP não pode ser vazia!',
                fg='red'
            )
        else:
            self.caminho = '/home/enge-olate/Documentos'
            self.pastas = ['TESTE', 'PDF', 'DIELETRICO']
            self.criando = Dirs(self.op, self.caminho, self.pastas)
            try:
                if self.criando.criar_pastas():
                    self.label_resultado.config(
                        text='Pasta criada com sucesso!',
                        fg='green'
                    )
                else:
                    self.label_resultado.config(
                        text='Pasta já existe',
                        fg='red'
                    )
            except Exception as e:
                self.label_resultado.config(
                    text=f'{e}',
                    fg='red'
                )
        self.entry.delete(0, END)

    def rode_app(self):
        self.raiz.mainloop()

