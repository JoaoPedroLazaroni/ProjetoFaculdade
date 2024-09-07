# -*- coding: iso-8859-1 -*-
import pandas as pd
import tkinter as tk
import sqlite3

# Banco de dados 

# conexao = sqlite3.connect('cliente.db')
# mensageiro = conexao.cursor()
#
# mensageiro.execute(''' CREATE TABLE clientes (
#    nome text,
#    sobrenome text,
#    telefone text,
#    endereço text
#    )
# ''')
#
# conexao.commit()
#
# conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect('cliente.db')
    mensageiro = conexao.cursor()

    mensageiro.execute(" INSERT INTO clientes VALUES (:nome, :sobrenome, :telefone, :endereço)",
                    {
                       'nome':entry_nome.get(),
                       'sobrenome':entry_sobrenome.get(),
                       'telefone':entry_telefone.get(),
                       'endereço':entry_endereço.get()
                    }    
                    )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_endereço.delete(0,"end")

def exportar_planilha():
    conexao = sqlite3.connect('cliente.db')
    mensageiro = conexao.cursor()

    mensageiro.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados=mensageiro.fetchall()
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados, columns=['Nome','Sobrenome','Telefone','Endereço','Id_cliente'])
    clientes_cadastrados.to_csv('banco_clientes.xlsx')
    conexao.commit()

    conexao.close()

interface = tk.Tk()
interface.title('Cadastro de Clientes')

# titulos

label_nome=tk.Label(interface, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome=tk.Label(interface, text='Sobrenome:')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_telefone=tk.Label(interface, text='Telefone:')
label_telefone.grid(row=2, column=0, padx=10, pady=10)

label_endereço=tk.Label(interface, text='Endereço:')
label_endereço.grid(row=3, column=0, padx=10, pady=10)

# entradas

entry_nome=tk.Entry(interface, text='Nome:', width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome=tk.Entry(interface, text='Sobrenome:', width=40)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_telefone=tk.Entry(interface, text='Telefone:', width=40)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

entry_endereço=tk.Entry(interface, text='Endereço:', width=40)
entry_endereço.grid(row=3, column=1, padx=10, pady=10)

# Botões

botao_cadastrar=tk.Button(interface, text='Cadastrar', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=1, padx=10, pady=10)

botao_planilha = tk.Button(interface, text='Planilha', command=exportar_planilha)
botao_planilha.grid(row=5, column=1, padx=10, pady=10)

interface.mainloop()




