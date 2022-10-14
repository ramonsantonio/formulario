from operator import ne
import tkinter as tk
from tkinter import NW, ttk

master = tk.Tk()
master.geometry('400x600')
master.title('PRINT')
tree = ttk.Treeview(master)
master.config(bg='black')



nome_l = tk.Label(master, width= 10, anchor=NW, text='Nome', font=('Poppins'), bg='black', fg='white')
nome_l.place(x=0, y=50, )

nome_e = tk.Entry(master, width=35)
nome_e.place(x=0, y=80)


def obter():
    nome = nome_e.get()
    
    print(nome)


botao_n = tk.Button(master, width= 5, text='inserir', bg='green', font=('poppins'), command=obter)
botao_n.place(x=0, y=130)


tree.place(x=0, y=250)

master.mainloop()