from tkinter import (
    Frame,
    Label,
    Button,
    Tk,
    Entry,
    PhotoImage,
    StringVar,
    Menu,
    Toplevel,
    messagebox,
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
        self.raiz.resizable(False, False)
        self.bg = '#0b0574'
        self.raiz.config(background=self.bg)
        
        if getattr(sys, 'frozen', False):
            self.logo_path = os.path.join(sys._MEIPASS, 'img', 'logo_tamura_mod.png')
        else:
            self.logo_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'logo_tamura_mod.png')

        self.logo = PhotoImage(file=self.logo_path)

        self.tc_produto = []
        try:
            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/tc.txt', 'a', encoding='utf-8', closefd=True):
                pass
            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/tc.txt', 'r', closefd=True, encoding='utf-8')  as tc_produto:
                for item in tc_produto:
                    self.tc_produto.append(item.strip())
            
        except FileNotFoundError:
            pass

        self.tp_produto=[]
        try:
            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TP/tp.txt', 'a', encoding='utf-8', closefd=True):
                pass
            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TP/tp.txt', 'r', closefd=True, encoding='utf-8')  as tp_produto:
                for item in tp_produto:
                    self.tp_produto.append(item.strip())
            
        except FileNotFoundError:
            pass
        

        self.menu_bar = Menu(self.raiz)
        self.raiz.config(
            menu=self.menu_bar,
        )
        self.tc = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='TC', menu=self.tc)
        for self.items in self.tc_produto:
            self.tc.add_cascade(label=self.items, command=lambda i=self.items: self.item_sel(item=i))

        self.tP = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='TP', menu=self.tP)
        for self.items in self.tp_produto:
            self.tP.add_cascade(label=self.items, command=lambda i=self.items: self.item_sel(item=i))
            
        self.add_produto = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Add Produto', menu=self.add_produto)
        self.add_produto.add_cascade(label='TC', command=self.add_tc)
        self.add_produto.add_cascade(label='TP', command=self.add_tp)


        self.ajuda_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Ajuda', menu=self.ajuda_menu)
        self.ajuda_menu.add_command(label='Manual', command=self.mostra_ajuda)
    
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
            fg='#fff2ff',
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
        self.entry_op = Entry(
            bg='#fff2ff',
            relief='flat',
            borderwidth=1,
            fg='black',
        )
        self.entry_op.focus_force()
        self.entry_op.grid(
            column=0,
            row=1,
            sticky='NW',
            padx=250,
            pady=15.5
        )

        self.label_produto_seq = Label(
            text='Produto: ',    
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

        self.botao = Button(
            text='Criar Pasta',
            cursor='Arrow',
            font='Arial',
            highlightcolor='#fff',
            state='active'
        )
        self.botao.grid(
            column=0,
            row=5,
            pady=5,
            padx=250,
            sticky='nw'
        )
        self.botao.bind('<Return>', self.dirs)
        self.botao.bind('<Button-1>', self.dirs)

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
    
    def add_tc(self):
        
        self.adiciona_produto = Toplevel(
            self.raiz,
        )
        self.adiciona_produto.resizable(False, False)
        self.adiciona_produto.title('TC')
        self.adiciona_produto.focus_force()
        self.label_add_produto = Label(
            self.adiciona_produto,
            text='Adicione TC:',
            font='arial',
            fg='black'
        )
        self.label_add_produto.pack(
            pady=5
        )
        self.entry_tc_produto = Entry(
            self.adiciona_produto,
            relief='solid',
            justify='left',
            font='Arial',
            fg='black'
        )
        self.entry_tc_produto.pack(
            pady=5,
        )
        self.entry_tc_produto.focus_force()

        self.botao_add_tc = Button(
            self.adiciona_produto,
            text='Add',
            font='Arial',
            fg='green',
            relief='ridge',
            borderwidth=2,
            bd=2,
            background='skyblue',
         
            
        )
        
        self.botao_add_tc.pack(
            pady=5,
        )
        self.botao_add_tc.bind('<Return>', self.result_add_tc)
        self.botao_add_tc.bind('<Button-1>', self.result_add_tc)
        self.result_label_tc = Label(
            self.adiciona_produto,
            text='',
            font='Arial', 
            fg='green'
        )
        self.result_label_tc.pack(
            pady=5,
        )

    
    def result_add_tc(self, event):
        self.tc_entry_produto_add = self.entry_tc_produto.get()
        if not self.tc_entry_produto_add:
            self.result_label_tc.config(
                text='Adicione um produto!',
                fg='red'
        )
        else:
            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/tc.txt', 'a', encoding='utf-8', closefd=True) as tc_produto:
                tc_produto.write(f'{self.tc_entry_produto_add}\n')
            self.tc.add_cascade(
                label=self.tc_entry_produto_add,
                command=lambda i= self.tc_entry_produto_add: self.item_sel(item=i)
            )
            self.result_label_tc.config(
                text='Produto cadastrado com sucesso!',
                fg='green'
            )
            self.raiz.update()           
    

    def add_tp(self):
        
        self.adiciona_produto = Toplevel(
            self.raiz,
        )
        self.adiciona_produto.resizable(False, False)
        self.adiciona_produto.title('TP')
        self.adiciona_produto.focus_force()
        self.label_add_produto = Label(
            self.adiciona_produto,
            text='Adicione TP:',
            font='arial',
            fg='black'
        )
        self.label_add_produto.pack(
            pady=5
        )
        self.entry_tp_produto = Entry(
            self.adiciona_produto,
            relief='solid',
            justify='left',
            font='Arial',
            fg='black'
        )
        self.entry_tp_produto.pack(
            pady=5,
        )
        self.entry_tp_produto.focus_force()
        self.botao_add_tp = Button(
            self.adiciona_produto,
            text='Add',
            font='Arial',
            fg='green',
            relief='ridge',
            borderwidth=2,
            bd=2,
            background='skyblue',
           
        )
        
        self.botao_add_tp.pack(
            pady=5,
        )
        self.botao_add_tp.bind('<Return>', self.result_add_tp)        
        self.botao_add_tp.bind('<Button-1>', self.result_add_tp)        
        self.result_label_tp = Label(
            self.adiciona_produto,
            text='',
            font='Arial', 
            fg='green'
        )
        self.result_label_tp.pack(
            pady=5,
        )
        
   
            
    def result_add_tp(self, event):
        self.tp_entry_produto_add = self.entry_tp_produto.get()
        if not self.tp_entry_produto_add:
            self.result_label_tp.config(
                text='Adicione um produto!',
                fg='red'
        )
        else:

            with open('//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TP/tp.txt', 'a',  encoding='utf-8', closefd=True) as tp_produto:
                tp_produto.write(f'{self.tp_entry_produto_add}\n')
            
            self.tP.add_cascade(
                label=self.tp_entry_produto_add,
                command=lambda i=self.tp_entry_produto_add: self.item_sel(item=i)
            )
            self.result_label_tp.config(
                text='Produto cadastrado com sucesso!',
                fg='green'
            )
           


    def mostra_ajuda(self):
        self.ajuda = messagebox.showinfo(
            'Ajuda',
            """ 
        Olá, seja bem-vindo ao app_SGP (app - Sistema Gerador de Pastas). 
        Para sua utilização, tenha sempre em mãos a ordem de produção.

        Menu:

            -> 'TC', 'TP': deverá ser selecionado o produto;

            -> 'Add Produto': irá abrir uma nova janela para adicionar produtos a 'TC' e 'TP'. (OBS: O PRODUTO DEVERÁ ESTAR SEM A SUA SEQUÊNCIA ORDINAL).

            -> 'Ajuda': mostra este manual.

        Tela Principal:

            Na primeira caixa de texto, "Ordem de produção (OP)", deverá ser inserido o número da OP.
            
            Na segunda caixa de texto, deverá ser inserido o nome do produto com a sequência numérica.
            
            Por fim, clique no botão 'Criar Pasta' para criar a pasta da OP informada, com as pastas no local devido.

        Para dúvidas e sugestões, contactar o desenvolvedor pelo e-mail: marcioalexisolate@live.com
            
            """         
        )
        
    
    # def enter(self, event):
    #     self.dirs()
        

    def item_sel(self, item):
        self.produto = item
       
        

    def dirs(self, event):
        
        self.op = self.entry_op.get()
        self.seq_produto = self.entry_seq_produto.get()    
        
        
        if not self.op:
            self.label_resultado.config(
                text='OP não pode ser vázia!',
                fg='yellow'
            )
       
        elif not self.seq_produto:
            self.label_resultado.config(
                text='Produto não pode ser vázio!',
                fg='yellow'
            )
        elif not hasattr(self, 'produto') or not self.produto:
                self.label_resultado.config(
                text='Selecione produto no menu TC ou TP!', 
                fg='yellow'
            )
        elif self.caminho == f'//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TC/{self.produto}/{self.seq_produto}/RELATÓRIO DE ENSAIO/':
             # self.caminho = f'c:/Users/marci/Documents/{self.produto}/{self.seq_produto}'
            self.pastas = ['TESTE', 'PDF', 'DIELETRICO']
            self.criando = Dirs(self.op, self.caminho, self.pastas)
            try:
                if self.criando.criar_pastas():
                    self.label_resultado.config(
                        text='Pasta criada com sucesso!',
                        fg='green'
                    )
                   
                    self.entry_op.focus_force()
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
            
        else:
            self.caminho = f'//Srvtib-nas01/engenharia/TC_TP - PROJETOS/ELETRICOS_TC_TP/TP/{self.produto}/{self.seq_produto}/RELATÓRIO DE ENSAIO/'
            # self.caminho = f'c:/Users/marci/Documents/{self.produto}/{self.seq_produto}'
            self.pastas = ['TESTE', 'PDF', 'DIELETRICO']
            self.criando = Dirs(self.op, self.caminho, self.pastas)
            try:
                if self.criando.criar_pastas():
                    self.label_resultado.config(
                        text='Pasta criada com sucesso!',
                        fg='green'
                    )
                   
                    self.entry_op.focus_force()
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
            self.produto = ''
            self.raiz.update()      

    def rode_app(self):

        self.raiz.mainloop()

    