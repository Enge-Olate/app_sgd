from tkinter import (
    Frame,
    Label,
    Button,
    Tk,
    Entry,
    PhotoImage,
    END,
    
)
from tkinter import ttk
from src.dirs import Dirs
import os
import sys

class App:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('600x350')
        self.raiz.title('SGP - Sistema Gerador de Pastas')
        # self.raiz.resizable(False, False)
        self.bg = '#0b0574'
        self.raiz.config(background=self.bg)
        if getattr(sys, 'frozen', False):
            self.logo_path = os.path.join(sys._MEIPASS, 'img', 'logo_tamura_mod.png')
        else:
            self.logo_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'logo_tamura_mod.png')

        self.logo = PhotoImage(file=self.logo_path)
        # self.frame()

    # def frame(self):
    #     self.frame_principal = Frame(
    #         master=self.raiz,
    #         borderwidth=5,
    #         relief='groove',
    #         bg=self.bg
    #     )
    #     self.frame_principal.grid(
    #         column=0,
    #         row=0,
    #         rowspan=3,
    #         columnspan=2,
    #         sticky=('W', 'E', 'N', 'S')
    #     )

        self.label_logo = Label(
            master=self.raiz,
            image=self.logo,
            background=self.bg,
        )
        self.label_logo.grid(
            # column=0,
            # row=0,
            pady=5,
            sticky='Ns'
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
            sticky='NW',
            padx=50,
            pady=10
        )
        self.entry = Entry(
            bg='#fff',
            relief='flat',
            borderwidth=1,
            fg='black',
        )
        self.entry.focus_force()
        self.entry.grid(
            column=0,
            row=1,
            sticky='NW',
            padx=250,
            pady=15.5
        )

        self.label_produto = Label(
            text='Escolha o produto: ',
            fg='#fff',
            bg=self.bg,
            font='Arial 14'
        )
        self.label_produto.grid(
            column=0,
            row=2,
            sticky='NW',
            padx=50,
            pady=10
        )
        self.combo_produto = ttk.Combobox(
            values=[
                'TSA06TCPS321',
                'TSA06TCPS320',
                'TSA06TCPS322'
            ]
        )
        self.combo_produto.grid(
            column=0,
            row=2,
            sticky='NW',
            padx=250,
            pady=15.5
        )
        self.combo_produto.bind('<<ComboboxSelected>>', self.mostra_combo)

        self.botao = Button(
            text='Criar Pasta',
            cursor='clock',
            font='Arial',
            highlightcolor='#fff',
            command=self.dirs,
        )
        self.botao.grid(
            column=0,
            row=3,
            pady=5,
        )
        self.botao.bind('<Return>', self.enter)
        

        self.label_resultado = Label(
            text='',
            font='Arial',
            bg=self.bg
        )
        self.label_resultado.grid(
            column=0,   
            row=4,
            pady=20
        )
    def mostra_combo(self, event):
        pass

    
    def enter(self, event):
        self.dirs()

    def dirs(self):
       
        self.produto_combo = self.combo_produto.get()        
        self.op = self.entry.get()
        
        if not self.op:
            self.label_resultado.config(
                text='OP não pode ser vazia!',
                fg='red'
            )
        elif not self.produto_combo:
            self.label_resultado.config(
                text='Escolha produto!',
                fg='red'
            )
        else:
            # self.caminho = f'//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/TSA06TCPS/{self.produto_combo}/RELATÓRIO DE ENSAIO/'
            self.caminho = f'c:/Users/marci/Documents/TSA06TCPS/{self.produto_combo}/RELATÓRIO DE ENSAIO'
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
                    text='Caminho de rede não encontrado!',
                    fg='red',
                    
                )
                print(f'{self.caminho}')
                print(f'{self.produto_combo}')
        # self.entry.delete(0, END)


    def rode_app(self):
        self.raiz.mainloop()

    