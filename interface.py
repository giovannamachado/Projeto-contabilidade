import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import projeto_cont as dados_tabela

def search(tabela, get_value_estado):
    print(get_value_estados)
    if get_value_estado != '':
        resultados =  dados_tabela.get_uf(tabela, get_value_estado, dados_tabela.coluna_interesse, dados_tabela.contas_interesse)
        treeview = ttk.Treeview(app)
        treeview['columns'] = list(resultados.index.values)
        for column in resultados.index.values:
            treeview.column(column, width=100)
            treeview.heading(column, text=column)
        for index, row in enumerate(resultados.columns.array):
            treeview.insert('', index, values=list(row), text=row)
        treeview.pack()
        return treeview
    
#pegar tabela do arquivo dados_tabela
tabela = dados_tabela.get_tabela()

app = ttk.Window(themename='cyborg')
app.geometry('900x1200')

label = ttk.Label(app, text='Projeto Contabilidade')
label.pack(pady=30)
label.config(font=('Arial', 20, 'bold'))

#municipio = ttk.Frame(app)
#municipio.pack(pady = 15, padx = 10, fill = 'x')
#ttk.Label(municipio, text='Cidade').pack(side='left', padx =5)
#ttk.Entry(municipio).pack(side='left', fill= 'x', expand=True, padx =5)

# RadioButtons (Estados ou Municípios)
def event_RadioButton():
    if var.get() == "Estados":
        print("Checkbox Estado")
    else:
        print("Checkbox Municícipos")

var = tk.StringVar()
option1 = ttk.Radiobutton(app, text="Estados", variable=var, value="Estados", command=event_RadioButton)
option1.pack(side=tk.LEFT, padx=(0, 20))
option2 = ttk.Radiobutton(app, text="Municípios", variable=var, value="Municípios", command=event_RadioButton)
option2.pack(side=tk.LEFT)

#Combobox municipios
todos_municipios = dados_tabela.get_all_municipios(tabela)

lb_municipio=ttk.Label(app, text='Município').pack(side='left', padx=10)
cb_municipio = ttk.Combobox(app, values=todos_municipios)
cb_municipio.set('Selecione o Município')
cb_municipio.pack(pady = 15, padx = 10, fill = 'x')

#Combobox estados
todos_uf = dados_tabela.get_all_uf(tabela)

lb_estados=ttk.Label(app, text='Estados').pack(side='left', padx=10)
cb_estados = ttk.Combobox(app, values=todos_uf)
cb_estados.set('Selecione o Estado')
cb_estados.pack(pady = 15, padx = 10, fill = 'x')

get_value_estados = cb_estados.get()
#estado = ttk.Entry(cb_estados).pack(side='left', fill= 'x', expand=True, padx =5)

#estados = ttk.Frame(app)
#estados.pack(pady = 15, padx = 10, fill = 'x')
#ttk.Label(estados, text='Estado').pack(side='left', padx =5)
#estado = ttk.Entry(estados).pack(side='left', fill= 'x', expand=True, padx =5)

checkbox_frame = ttk.Frame(app)
checkbox_frame.pack(pady=15, padx=10, fill='x')
ttk.Checkbutton(checkbox_frame, bootstyle='info-round-toggle', text='Salvar informação').pack(side='left', padx=10)


button_frame = ttk.Frame(app)
button_frame.pack(pady=50, fill='x')
ttk.Button(button_frame, text='Pesquisar', bootstyle = 'SUCCESS-OUTLINE', command=search(tabela, get_value_estados)).pack(side='top', padx=10)


app.mainloop()
# filedialog