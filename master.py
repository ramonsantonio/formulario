import sqlite3 
from tkinter import *
from tkinter import ttk
from turtle import width 
from view import *

################# cores ###############

co0 = "#000000"  # Preta
co1 = "#feffff"  # branca
co2 = "#7ed957"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#004aad"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue

# Config Principal do Software

master = Tk()

my_tree = ttk.Treeview(master)
master.title('Ramon Antonio') # Nome do software
master.geometry('1200x650+0+0')
master.config(bg= co9) # cor do background
#master.iconphoto(False, PhotoImage(file='')) # icone do software


# Frame 

frame_title = Frame (master, width=430, height=100, bg=co2, relief='flat')
frame_title.grid(row=0, column=0)

frame_campus = Frame (master, width=430, height=790, bg=co1, relief='flat')
frame_campus.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_dados = Frame (master, width=790, height=790, bg=co9, relief='flat')
frame_dados.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


# Label frame_title

app_nome = Label (frame_title, text='Finanças da Família', anchor=NW, font=('bebas', 30), bg= co2, fg=co1)
app_nome.place(x=10, y=20)

# Label frame_campus

nome_label = Label(frame_campus, text='NOME *', font=('Poppins, 10'), bg='white')
nome_label.place(x=10, y=10)
nome_entry = Entry(frame_campus, width=50, bd=5, font=('poppins, 10'))
nome_entry.place(x=10, y=40)



origem_label = Label(frame_campus, text='ORIGEM *', font=('Poppins, 10'), bg='white')
origem_label.place(x=10, y=120)
origem_entry = Entry(frame_campus, width=50, bd=5, font=('poppins, 10'))
origem_entry.place(x=10, y=150)


mes_label = Label(frame_campus, text='MÊS *', font=('Poppins, 10'), bg='white')
mes_label.place(x=10, y=210)
mes_entry = Entry(frame_campus, width=50, bd=5, font=('poppins, 10'))
mes_entry.place(x=10, y=240)

valor_label = Label(frame_campus, text='VALOR *', font=('Poppins, 10'), bg='white')
valor_label.place(x=10, y=320)
valor_entry = Entry(frame_campus, width=50, bd=5, font=('poppins, 10'))
valor_entry.place(x=10, y=350)

# função inserir 
#variavel tree global 
global tree

# Inserindo info no frame_dados
def inserir(): 
    nome = nome_entry.get()
    origem = origem_entry.get()
    mes = mes_entry.get()
    valor = valor_entry.get()

    lista = [nome, origem, mes, valor]

    if nome=='':
        messagebox.showerror('Campo Obrigatório')  # informação de erro 
    else:
        inserir_info(lista)
        messagebox.showinfo('PRONTO', 'Inserido Com sucesso') # informaação de sucesso 

        nome_entry.delete(0, 'end')         # server para limpar o campos após ser inserido com sucesso
        origem_entry.delete(0, 'end')
        mes_entry.delete(0, 'end')
        valor_entry.delete(0, 'end')

    for widget in frame_dados.winfo_children():
        widget.destroy()

    mostrar()


# atualizando info frame_dados

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']


        valor = tree_lista[0]

        nome_entry.delete(0, 'end')         # server para limpar o campos após ser inserido com sucesso
        origem_entry.delete(0, 'end')
        mes_entry.delete(0, 'end')
        valor_entry.delete(0, 'end')

        nome_entry.insert(0, tree_lista[1])         # server para limpar o campos após ser inserido com sucesso
        origem_entry.insert(0, tree_lista[2])
        mes_entry.insert(0, tree_lista[3])
        valor_entry.insert(0, tree_lista[4])


        # Inserindo info no frame_dados

        def update(): 
            nome = nome_entry.get()
            origem = origem_entry.get()
            mes = mes_entry.get()
            valor = valor_entry.get()

            lista = [nome, origem, mes, valor]

            if nome=='':
                messagebox.showerror('ERRO','Campo Obrigatório')  # informação de erro 
            else:
                atualizar_info(lista)
                messagebox.showinfo('PRONTO', 'Dados atualizados Com sucesso') # informaação de sucesso 

                nome_entry.delete(0, 'end')         # server para limpar o campos após ser inserido com sucesso
                origem_entry.delete(0, 'end')
                mes_entry.delete(0, 'end')
                valor_entry.delete(0, 'end')

            for widget in frame_dados.winfo_children():
                widget.destroy()

            mostrar()

        #Botão atualizar 
            up_confirmar = Button (master, command=update, text='Confirmar', width=8, bd=3, font=('poppins, 10'), bg= co6, fg=co1, padx=5, pady=5)
            up_confirmar.place(x=140, y=540)


    except IndexError:
        messagebox.showerror('ERRO', 'Selecione um dado  da tabela para ser alterado')  # informação de erro 



# Função deletar

def deletar_info():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']


        valor_id = tree_lista[0]
    
    except IndexError:
        messagebox.showerror('ERRO', 'Selecione um dado para ser alterado')  # informação de erro 



# Botões

botao_enviar = Button (master, command=inserir, text='ENVIAR', width=8, bd=3, font=('poppins, 10'), bg='green',fg=co1, padx=5, pady=5)
botao_enviar.place(x=10, y=540)


up_enter = Button (master, command=atualizar, text='ATUALIZAR', width=8, bd=3, font=('poppins, 10'), bg= co6, fg=co1, padx=5, pady=5)
up_enter.place(x=140, y=540)

del_enter = Button (master,command=deletar_info, text='DELETAR', width=8, bd=3, font=('poppins, 10'), bg='red', fg=co1, padx=5, pady=5)
del_enter.place(x=270, y=540)


# Frame dados
 
# Lista head

def mostrar ():

    global tree

    lista = mostrar_info() #trocar para mostrar_infor()

    # Criando as informações do Head dados 
    tabela_head = ['NOME', 'ORIGEM', 'MÊS', 'VALOR']

    # Crianado a Tabale de dados 
    tree = ttk.Treeview(frame_dados, selectmode='extended', columns=tabela_head, show='headings')

    # Rolagem vertical
    vsb = ttk.Scrollbar(frame_dados, orient='vertical', command=tree.yview)

    # Rolagem horizontal 
    hsb = ttk.Scrollbar(frame_dados, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_dados.grid_rowconfigure(0, weight=12)

    hd=['center', 'center', 'center','center']
    h=[195, 195, 190, 190]
    n=0


    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)



# chamando a função mostrar 
mostrar()




master.mainloop()