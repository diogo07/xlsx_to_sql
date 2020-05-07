from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import font
import ctypes

from src.controller.ControllerHomeScreen import ControllerHomeScreen

class HomeScreen(Frame):

    def __init__(self, width, height, title):
        Frame.__init__(self, master=None)
        self.master.title(title)
        self.set_geometry(width, height)
        self.controllerHomeScreen = ControllerHomeScreen(self)

        self.lb_arquivo = Label(self.master, text="Selecione o arquivo:")
        self.lb_arquivo.place(x=10, y=25)

        self.ent_arquivo = Text(self.master, height=1, width=60)
        self.ent_arquivo.place(x=10, y=50)

        self.btn_arquivo = Button(self.master, text="...", width = 10, height=1, command=self.controllerHomeScreen.open_browser)
        self.btn_arquivo.place(x=500, y=47)

        self.lb_campos = Label(self.master, text="Campos:")
        self.lb_campos.place(x=10, y=100)

        self.lbx_campos = Listbox(self.master, selectmode='multiple', height=12, width=40)
        self.lbx_campos.place(x=10, y=125)

        self.lb_campos_sql = Label(self.master, text="Campos do SQL:")
        self.lb_campos_sql.place(x=320, y=100)

        self.lbx_campos_sql = Listbox(self.master, selectmode='multiple', height=12, width=20)
        self.lbx_campos_sql.place(x=320, y=125)

        self.btn_add_campo = Button(self.master, text=">>>", command=self.controllerHomeScreen.add_fields)
        self.btn_add_campo.place(x=270, y= 200)

        self.btn_remove_campo = Button(self.master, text="<<<", command=self.controllerHomeScreen.remove_field)
        self.btn_remove_campo.place(x=270, y=250)

        self.label_table = Label(self.master, text="Nome da tabela:")
        self.label_table.place(x=10, y=330)

        self.text_table = Text(self.master, height=1, width=30)
        self.text_table.place(x=10, y=355)

        self.btn_gerar = Button(self.master, text = "gerar", command=self.controllerHomeScreen.generate_sql)
        self.btn_gerar.place(x = 180, y= 390, width=100)

        self.btn_limpar = Button(self.master, text="limpar")
        self.btn_limpar.place(x=290, y=390, width=100)

        self.lbl_saida = Text(self.master, height=8, width=70)
        self.lbl_saida.place(x=10, y=450)


    def set_geometry(self, width, height):
        positionRight = int(self.master.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.master.winfo_screenheight() / 2 - height / 2)
        self.master.geometry("{}x{}+{}+{}".format(width, height, positionRight, positionDown - 40))

    def browse_xlsx(self):
        fname = askopenfilename(filetypes=(("Excel files", "*.xlsx;*.xls"),
                                           ("All files", "*.*")))
        self.ent_arquivo.delete(1.0,"end-1c")
        self.ent_arquivo.insert("end-1c",fname)

    def message(self, title, description):
        ctypes.windll.user32.MessageBoxW(0, description, title, 1)

    def insert_sql(self, sql):
        self.lbl_saida.insert(END, sql)
