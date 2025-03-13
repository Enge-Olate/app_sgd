from tkinter import (
    Frame,
    Label,
    Button,
    Tk,
    Entry,
    PhotoImage,
    StringVar,
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
            column=0,
            row=0,
            pady=5,
            padx=200,
            sticky='Nw'
        )

        self.label_op = Label(
            text='Ordem de produção(OP): ',
            fg='#fff',
            bg=self.bg,
            font='Arial'
        )
        self.label_op.grid(
            column=0,
            row=1,
            sticky='NW',
            padx=50,
            pady=10
        )
        self.entry = Entry(
            bg='#fff2ff',
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
            text='Informe o produto: ',
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

        

        self.entry_produto=Entry(
            bg='#fff2ff',
            relief='flat',
            borderwidth=1,
            fg='black',
        )
        self.entry_produto.grid(
            column=0,
            row=2,
            sticky='NW',
            padx=250,
            pady=15.5
        )


        self.label_produto_seq = Label(
            text='Produto sequêncial: ',
            fg='#fff',
            bg=self.bg,
            font='Arial 14'
        )
        self.label_produto_seq.grid(
            column=0,
            row=3,
            sticky='NW',
            padx=50,
            pady=10
        )

        

        self.entry_seq_produto=Entry(
            bg='#fff2ff',
            relief='flat',
            borderwidth=1,
            fg='black',
        )
        self.entry_seq_produto.grid(
            column=0,
            row=3,
            sticky='NW',
            padx=250,
            pady=15.5
        )


                
        # self.combo_produto = ttk.Combobox(
        #     values=[
        #         'TSA06TPA',
        #         'TSA06TPB',
        #         'TSA06TCPC',
        #         'TSA7TPA',
        #         'TSA7TPB',
        #         'TSA15ETPA',
        #         'TSA15ETPB',
        #         'TSA15TPA',
        #         'TSA15TPB',
        #         'TSA15TPC',
        #         'TSA15TPD',
        #         'TSA15TPE',
        #         'TSA25ETPA',
        #         'TSA25ETPB',
        #         'TSA25TPA',
        #         'TSA25TPB',
        #         'TSA36ETPA',
        #         'TSA36TPAB',
        #         'TSA36TPC',
        #         'TSA06100',
        #         'TSA06100T',
        #         'TSAFF7',
        #         'TSAFF25F',
        #         'TSAFT21',
        #         'TSATTRS'
        #     ]
        # )
        # self.combo_produto.grid(
        #     column=0,
        #     row=2,
        #     sticky='NW',
        #     padx=250,
        #     pady=15.5
        # )
        # self.combo_produto.bind('<<ComboboxSelected>>', self.mostra_combo)

        self.botao = Button(
            text='Criar Pasta',
            cursor='clock',
            font='Arial',
            highlightcolor='#fff',
            command=self.dirs,
        )
        self.botao.grid(
            column=0,
            row=5,
            pady=5,
            padx=250,
            sticky='nw'
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
            pady=20,
            padx=200,
            sticky='nw'
        )
    def mostra_combo(self, event):
        pass
    
    
    # def resetar_campos(self, event):
    #     if self.dirs():
    #         self.entry.delete(0,END)
    
    
    def enter(self, event):
        self.dirs()

    
        

    def dirs(self):
        
        self.op = self.entry.get()
        self.produto = self.entry_produto.get()
        self.seq_produto = self.entry_seq_produto.get()    
        
        
        if not self.op:
            self.label_resultado.config(
                text='OP não pode ser vázia!',
                fg='yellow'
            )
        elif not self.produto:
            self.label_resultado.config(
                text='Produto não pode ser vázio!',
                fg='yellow'
            )
        elif not self.seq_produto:
            self.label_resultado.config(
                text='Produto sequêncial não pode ser vázio!',
                fg='yellow'
            )
        
        else:
            self.caminho = f'//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/{self.produto}/{self.seq_produto}/RELATÓRIO DE ENSAIO/'
            # self.caminho = f'c:/Users/marci/Documents/{self.produto}/{self.seq_produto}'
            self.pastas = ['TESTE', 'PDF', 'DIELETRICO']
            self.criando = Dirs(self.op, self.caminho, self.pastas)
            try:
                if self.criando.criar_pastas():
                    self.label_resultado.config(
                        text='Pasta criada com sucesso!',
                        fg='green'
                    )
                    self.entry.delete(0, END)
                    self.entry_produto.delete(0, END)
                    self.entry_seq_produto.delete(0, END)
                    self.entry.focus_force()
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
                print(f'{self.produto}')
       
    
    


    def rode_app(self):
        self.raiz.mainloop()

    