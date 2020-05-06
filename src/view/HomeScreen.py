from tkinter import *
from tkinter.filedialog import askopenfilename

class HomeScreen(Frame):

    def __init__(self, width, height, title):
        Frame.__init__(self, master=None)
        self.master.title(title)
        self.set_geometry(width, height)

        self.lb_arquivo = Label(self.master, text="Selecione o arquivo:")
        self.lb_arquivo.place(x=10, y=25)

        self.ent_arquivo = Text(self.master, height=1, width=60)
        self.ent_arquivo.place(x=10, y=50)

        self.btn_arquivo = Button(self.master, text="...", width = 10, height=1, command=self.browse_xlsx)
        self.btn_arquivo.place(x=500, y=47)

        self.lb_campos = Label(self.master, text="Campos:")
        self.lb_campos.place(x=10, y=100)

        self.lbx_campos = Listbox(self.master, selectmode='multiple', height=15, width=40)
        self.lbx_campos.place(x=10, y=125)

        #self.rightBT3.curselection() pegar os valores selecionados

        self.lbx_campos.insert(END, "a list entry")
        self.lbx_campos.insert(END, "a list entry")

        self.lbx_campos_sql = Label(self.master, text="Campos do SQL:")
        self.lbx_campos_sql.place(x=320, y=100)

        self.lbx_campos_sql = Listbox(self.master, height=15, width=40)
        self.lbx_campos_sql.place(x=320, y=125)

        self.btn_add_campo = Button(self.master, text=">>>")
        self.btn_add_campo.place(x=270, y= 200)

        self.btn_remove_campo = Button(self.master, text="<<<")
        self.btn_remove_campo.place(x=270, y=250)

        self.btn_gerar = Button(self.master, text = "gerar")
        self.btn_gerar.place(x = 180, y= 390, width=100)

        self.btn_limpar = Button(self.master, text="limpar")
        self.btn_limpar.place(x=290, y=390, width=100)

        self.lbl_saida = Text(self.master, height=10, width=70)
        self.lbl_saida.place(x=10, y=425)




    def set_geometry(self, width, height):
        positionRight = int(self.master.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.master.winfo_screenheight() / 2 - height / 2)
        self.master.geometry("{}x{}+{}+{}".format(width, height, positionRight, positionDown))

    def browse_xlsx(self):
        fname = askopenfilename(filetypes=(("Excel files", "*.xlsx;*.xls"),
                                           ("All files", "*.*")))
        self.ent_arquivo.delete(1.0,"end-1c")
        self.ent_arquivo.insert("end-1c",fname)
