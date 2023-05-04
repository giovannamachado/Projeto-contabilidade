import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import numpy as np
import projeto_cont as dados_tabela
    
class Interfazinha:
    def __init__(self):
        self.criar_janela()

    def criar_janela(self):
        self.app = ttk.Window(themename='cyborg')
        self.app.geometry('900x1200')

        self.label = ttk.Label(self.app, text='Projeto Contabilidade')
        self.label.pack(pady=30)
        self.label.config(font=('Arial', 20, 'bold'))

        # RadioButtons (Estados ou Municípios)

        self.var = tk.StringVar()
        self.header = ttk.Frame(self.app)
        self.header.pack(side='top', fill='y')

        self.option1 = ttk.Radiobutton(
            self.header, text="Estados", variable=self.var, value="Estados", command=self.event_RadioButton)
        self.option1.pack(side=tk.LEFT, padx=20, pady=10)
        self.option2 = ttk.Radiobutton(
            self.header, text="Municípios", variable=self.var, value="Municípios", command=self.event_RadioButton)
        self.option2.pack(side=tk.LEFT, padx=20, pady=10)

        self.cb_input_principal = ttk.Combobox(self.header, width=50)
        self.cb_input_principal.set('Selecione a opção')
        self.cb_input_principal.pack(pady=10, padx=10, side='left')

        self.style = ttk.Style()
        self.style.configure('Treeview',
            background = '#371c4b',
            foreground = 'white',
            rowheight=25,
            
        )
        self.style.map('Treeview',
            background=[('selected', '#232323')]
        )

        button_frame = ttk.Frame(self.app)
        button_frame.pack(side='top', pady=10)
        self.treeview = ttk.Treeview( button_frame, columns=['Tipo da Conta']+['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas', 'Seguridade Social'])

        processar_btn = ttk.Button(self.header,
                                   text='Processar',
                                   bootstyle='SUCCESS-OUTLINE',
                                   command=lambda: self.search(
                                       tabela, self.cb_input_principal.get())
                                   )
        processar_btn.pack(pady=10, padx=10, side='left')

    def event_RadioButton(self):
        if self.var.get() == "Estados":
            todos_uf = dados_tabela.get_all_uf(tabela)
            self.cb_input_principal['values'] = todos_uf
            self.cb_input_principal.set('Selecione o Estado')
        else:
            todos_municipios = dados_tabela.get_all_municipios(
                tabela)  
            self.cb_input_principal['values'] = todos_municipios
            self.cb_input_principal.set('Selecione o Município')

    def search(self, tabela, cb_input_principal: str):
        if len(cb_input_principal) == 2:
            resultados =  dados_tabela.get_uf(tabela, cb_input_principal, dados_tabela.contas_interesse, dados_tabela.coluna_interesse)
        elif len(cb_input_principal) > 2: 
            resultados = dados_tabela.get_cidade(tabela, cb_input_principal, dados_tabela.contas_interesse, dados_tabela.coluna_interesse)
        
        self.treeview['show'] = 'headings'
        self.reset_treeview()

        for column in self.treeview['columns']:
            self.treeview.column(column, width=180)
            self.treeview.heading(column, text=column)

        for index, row in enumerate(resultados.index.values):
            lista_valores = list(resultados.iloc[index])

            for index_lista in range(len(lista_valores)):
                if isinstance(lista_valores[index_lista], np.ndarray):
                    lista_valores[index_lista] = f'R$ 0'
                else:
                    lista_valores[index_lista] = f'R$ {lista_valores[index_lista]:,.2f}'

            self.treeview.insert('', 'end', values=[row]+lista_valores)

        self.treeview.pack(pady=50, padx=100)
        return self.treeview
    
    def reset_treeview(self):
        self.treeview.delete(*self.treeview.get_children())


if __name__ == "__main__":
    # pegar tabela do arquivo dados_tabela
    tabela = dados_tabela.get_tabela()

    interface = Interfazinha()
    interface.app.mainloop() 