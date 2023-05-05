import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import numpy as np
import pandas as pd
import projeto_cont as dados_tabela
import pathlib

from janelinha import Janela


class Interfazinha:
    def __init__(self):
        self.tabela = None
        self.contas_selecionadas = set(dados_tabela.contas_interesse)

    def abrir_janela_especial(self):
        if type(self.tabela) != type(None):
            janela = Janela(self.app, self.contas,
                            self.contas_selecionadas, self.update_tabela)
            janela.grab_set()
        else:
            messagebox.showerror(
                "Sem planilha", "Você precisa carregar uma planilha.")

    def carregar_tabela(self, tabela):
        self.tabela = tabela
        self.cb_input_uf['values'] = dados_tabela.get_all_uf(self.tabela)
        self.contas = sorted(list(self.tabela["Conta"].unique()))

    def update_tabela(self):
        print("Update tabela")
        self.processar()

    def criar_janela(self):
        self.app = ttk.Window(themename='cyborg')
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        self.app.geometry("{}x{}".format(screen_width, screen_height))

        self.label = ttk.Label(self.app, text='Projeto Contabilidade')
        self.label.pack(pady=30)
        self.label.config(font=('Arial', 20, 'bold'))

        # RadioButtons (Estados ou Municípios)

        self.option_selected = tk.StringVar()
        self.header = ttk.Frame(self.app)
        self.header.pack(side='top', fill='y')

        self.radio_option_estado = ttk.Radiobutton(
            self.header, text="Estados", variable=self.option_selected, value="Estados", command=self.event_RadioButton)  # Chama essa callback quando o botao radio é mudado(selecionado)
        self.radio_option_estado.pack(side=tk.LEFT, padx=10, pady=10)

        self.radio_option_municipio = ttk.Radiobutton(
            self.header, text="Municípios", variable=self.option_selected, value="Municípios", command=self.event_RadioButton)  # Chama essa callback quando o botao radio é mudado(selecionado)
        self.radio_option_municipio.pack(side=tk.LEFT, padx=10, pady=10)

        # Opção Estados
        self.cb_input_uf = ttk.Combobox(self.header, width=10)
        self.cb_input_uf.set('UF')
        self.cb_input_uf.pack(pady=10, padx=10, side='left')

        # Chama essa callback quando um elemento é mudado no ComboBox
        self.cb_input_uf.bind("<<ComboboxSelected>>", self.TextBoxUpdate)

        # Opção Município
        self.cb_input_municipio = ttk.Combobox(self.header, width=50)
        self.cb_input_municipio.set('Selecionar Município')
        self.cb_input_municipio.pack(pady=10, padx=10, side='left')

        self.cb_input_municipio.configure(state="disabled")
        self.cb_input_uf.configure(state="disabled")

        self.style = ttk.Style()
        self.style.configure('Treeview',
                             background='#371c4b',
                             foreground='white',
                             rowheight=35,

                             )
        self.style.map('Treeview',
                       background=[('selected', '#232323')]
                       )

        self.tabela_frame = ttk.Frame(self.app)
        self.tabela_frame.pack(side='top', pady=10)

        self.treeview = ttk.Treeview(self.tabela_frame, columns=['Tipo da Conta']+ dados_tabela.coluna_interesse)
        self.treeview['show'] = 'headings'
        
        self.treeview.column('Tipo da Conta', width=315)
        self.treeview.heading('Tipo da Conta', text='Tipo da Conta')

        # Outras colunas
        for column in self.treeview['columns'][1:]:
            self.treeview.column(column, width=200, anchor='center')
            self.treeview.heading(column, text=column)

        processar_btn = ttk.Button(self.header,
                                   text='Processar',
                                   bootstyle='SUCCESS-OUTLINE',
                                   command=self.processar
                                   )
        processar_btn.pack(pady=10, padx=10, side='left')

        self.carregar_btn = ttk.Button(self.header,
                                       text='Carregar',
                                       bootstyle='SUCCESS-OUTLINE',
                                       command=self.carregar_planilha
                                       )
        self.carregar_btn.pack(pady=10, padx=10, side='left')

        self.edit_opcoes_btn = ttk.Button(self.header,
                                          text='Editar',
                                          bootstyle='SUCCESS-OUTLINE',
                                          command=self.abrir_janela_especial
                                          )
        self.edit_opcoes_btn.pack(pady=10, padx=10, side='left')


    def event_RadioButton(self):  # Chamado quando algum radio button é pressionado
        print("Radio btn pressionado")

        if self.option_selected.get() == "Estados":
            self.cb_input_municipio.configure(state="disabled")
            self.cb_input_uf.configure(state="normal")

            # self.cb_input_uf['values'] = self.todos_uf # Isso só precisa ser feito uma vez, quando a planilha é carregada

        elif self.option_selected.get() == "Municípios":
            self.cb_input_uf.configure(state="normal")
            self.cb_input_municipio.configure(state="normal")

            # self.cb_input_uf['values'] = self.todos_uf # Isso só precisa ser feito uma vez, quando a planilha é carregada
            self.cb_input_municipio['values'] = dados_tabela.get_uf_municipios(
                tabela=self.tabela,
                estado=self.cb_input_uf.get()
            )

    def TextBoxUpdate(self, event):  # Chamado quando algum estado é selecionado
        self.cb_input_municipio.set("Selecionar Município")
        self.cb_input_municipio['values'] = dados_tabela.get_uf_municipios(
            tabela=self.tabela,
            estado=self.cb_input_uf.get()
        )

    def processar(self):
        if self.option_selected.get() == "Estados":
            resultados = dados_tabela.get_uf(self.tabela, self.cb_input_uf.get(
            ), self.contas_selecionadas, dados_tabela.coluna_interesse)
        elif self.option_selected.get() == "Municípios":
            resultados = dados_tabela.get_cidade(self.tabela, self.cb_input_municipio.get(
            ), self.contas_selecionadas, dados_tabela.coluna_interesse)

        self.reset_treeview()

        for index, row in sorted(enumerate(resultados.index.values), key=lambda ir: ir[1]):
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

    def carregar_planilha(self):
        self.carregar_btn['text'] = "Carregando..."
        self.carregar_btn.config(state='disabled')

        try:
            filename = filedialog.askopenfilename(
                initialdir=pathlib.Path(),
                title="Select a File",
                filetypes=(
                    ("Supported files", ["*.csv*", "*.xlsx*", "*.xls*", "*.xlsx*",
                                         "*.xlsm*", "*.xlsb*", "*.odf*", "*.ods*", "*.odt*"]),
                    ("all files", "*.*")
                )
            )

            if (len(filename) == 0):
                raise Exception("User cancelou")

            path_file = pathlib.Path(filename)

            if path_file.suffix == ".csv":
                df = pd.read_csv(path_file)
            else:  # Excel
                df = pd.read_excel(
                    path_file, skiprows=4)

            self.carregar_tabela(df)

            messagebox.showinfo("Planilha Carregada",
                                "Planilha Carregada com Sucesso!")
        except KeyError as e:
            messagebox.showerror(
                "Error ao carregar planilha", "Ocorreu algum problema ao tentar carregar a planilha!\n" +
                f"\nColuna ('{e.args[0]}') não foi encontrada.\n" +
                "\nVerifique se você informou corretamente a linha das colunas.")
        except Exception as e:
            messagebox.showerror(
                "Error ao carregar planilha", "Ocorreu algum problema ao tentar carregar a planilha!")

        self.carregar_btn['text'] = "Carregar planilha"
        self.carregar_btn.config(state='normal')


if __name__ == "__main__":
    # pegar tabela do arquivo dados_tabela

    interface = Interfazinha()
    interface.criar_janela()
    
    try:
        interface.carregar_tabela(dados_tabela.get_tabela())
    except:
        print("Deu erro ao carregar a tabela, isso deve acontecer no pc do cara, deboa.")
    
    interface.app.mainloop()
