from ctypes.wintypes import SIZE
from optparse import Values
import PySimpleGUI as sg
import sqlite3 as bbb

conn = bbb.connect("Desktop/FelipeVitor/clientes.db")
c = conn.cursor()

layout = [

    [sg.Button("Cadastrar")]
    
]

font_programa = ('Arial',25)

window = sg.Window("Sistema de cadastro de clientes",layout,size=(1024,728),font=font_programa,resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Cadastrar":

        cadastro_layout = [
            [sg.Text("Nome")],
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("Endereco")],
            [sg.InputText(key="Endereco")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        cadastro_window = sg.Window ("Cadastro de Clientes",cadastro_layout,size = (1024,728))

        while True:
            event, values = cadastro_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                cadastro_window.close()
                break

            c.execute("INSERT INTO clientes (Nome, CPF, Endereco, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereco"], values["Telefone"], values["Cidade"], values["Estado"]))
            conn.commit()


            cadastro_window["Nome"].update("")
            cadastro_window["CPF"].update("")
            cadastro_window["Endereco"].update("")
            cadastro_window["Telefone"].update("")
            cadastro_window["Cidade"].update("")
            cadastro_window["Estado"].update("")

            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
          
           
        

conn.close()