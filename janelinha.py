import tkinter as tk
import ttkbootstrap as ttk


def criar_callback(callback, *args):
    return lambda: callback(*args)


class Lista(tk.Frame):
    def __init__(self, root, lista_opcoes, set_selecionados, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        self.set_selecionados = set_selecionados

        self.vsb = tk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=40, height=20,
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        for opcao in lista_opcoes:
            cb = tk.Checkbutton(self, text=opcao, command=criar_callback(
                self.checkbutton_event, opcao))

            if opcao in self.set_selecionados:
                cb.select()

            self.text.window_create("end", window=cb)
            self.text.insert("end", "\n")  # to force one checkbox per line

    def checkbutton_event(self, opcao):
        if opcao in self.set_selecionados:
            self.set_selecionados.remove(opcao)
        else:
            self.set_selecionados.add(opcao)


class Janela(tk.Toplevel):
    def __init__(self, parent, lista_opcoes, set_selecionados, callback):
        super().__init__(parent)

        self.geometry('500x800')
        self.title('Toplevel Window')

        def call_callback():
            callback()
            self.destroy()

        ttk.Button(self,
                   text='Aplicar',
                   command=call_callback
                   ).pack(expand=True)
        
        Lista(self, lista_opcoes, set_selecionados).pack(
            side="top",
            fill="both",
            expand=True
        )
