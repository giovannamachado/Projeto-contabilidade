import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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
        self.header.pack(side='top', fill='x', padx=10, pady=10)

        self.option1 = ttk.Radiobutton(
            self.header, text="Estados", variable=self.var, value="Estados", command=self.event_RadioButton)
        self.option1.pack(side=tk.LEFT, padx=20, pady=10)
        self.option2 = ttk.Radiobutton(
            self.header, text="Municípios", variable=self.var, value="Municípios", command=self.event_RadioButton)
        self.option2.pack(side=tk.LEFT, padx=20, pady=10)

        self.cb_input_principal = ttk.Combobox(self.header, width=50)
        self.cb_input_principal.set('Selecione a opção')
        self.cb_input_principal.pack(pady=10, padx=10, side='left')

        self.treeview = ttk.Treeview(self.app, columns=['Tipo Conta']+['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas'])
        # button_frame = ttk.Frame(self.app)
        # button_frame.pack(side='top', pady=10)
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

    def search(self, tabela, cb_input_principal):
        print(cb_input_principal)
        if cb_input_principal:
            resultados =  dados_tabela.get_uf(tabela, cb_input_principal, dados_tabela.contas_interesse, dados_tabela.coluna_interesse)

            #treeview = ttk.Treeview(self.app, columns=['Tipo Conta']+list(resultados.columns.array))
            treeview = self.treeview
            treeview['show'] = 'headings'

            for column in treeview['columns']:
                treeview.column(column, width=180)
                treeview.heading(column, text=column)

            for index, row in enumerate(resultados.index.values):
                treeview.insert('', 'end', values=[row]+list(resultados.iloc[index]))

            treeview.pack()
            return treeview
    
    def reset_treeview(self):
        self.treeview.delete(*self.treeview.get_children())


if __name__ == "__main__":
    # pegar tabela do arquivo dados_tabela
    tabela = dados_tabela.get_tabela()

    interface = Interfazinha()
    interface.app.mainloop() 