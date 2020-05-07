from tkinter.filedialog import askopenfilename

from src.model.XlsxToSql import XlsxToSql
from tkinter import *
from tkinter import font

class ControllerHomeScreen:

    def __init__(self, homeScreen):
        self.homeScreen = homeScreen
        self.x_position = 450
        self.y_position = 125
        self.list_edit = []


    def open_browser(self):
        fname = askopenfilename(filetypes=(("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")))
        if fname:
            self.homeScreen.ent_arquivo.delete(1.0, "end-1c")
            self.homeScreen.ent_arquivo.insert("end-1c", fname)
            self.read_file(fname)

    def add_fields(self):

        sel = self.homeScreen.lbx_campos.curselection()

        for field in self.homeScreen.lbx_campos.curselection():
            self.homeScreen.lbx_campos_sql.insert(END, self.homeScreen.lbx_campos.get(field))

            lbl_edit = Label(self.homeScreen.master, text="Editar campo:")
            lbl_edit.place(x=450, y=100)

            size_font = font.Font(size=9)
            edit_text = Entry(self.homeScreen.master, font = size_font)
            edit_text.place(x=self.x_position, y=self.y_position)
            edit_text.insert(END, self.homeScreen.lbx_campos.get(field))
            self.y_position+=16

            self.list_edit.append(edit_text)


        for index in sel[::-1]:
            self.homeScreen.lbx_campos.delete(index)


    def remove_field(self):

        sel = self.homeScreen.lbx_campos_sql.curselection()

        for field in self.homeScreen.lbx_campos_sql.curselection():
            self.homeScreen.lbx_campos.insert(END, self.homeScreen.lbx_campos_sql.get(field))

        for index in sel[::-1]:
            self.homeScreen.lbx_campos_sql.delete(index)
            self.list_edit[-1].destroy()
            del self.list_edit[-1]
            self.y_position -=16

        for index in range(self.list_edit.__len__()):
            self.list_edit[index].delete(0, 'end')
            self.list_edit[index].insert(END, self.homeScreen.lbx_campos_sql.get(index))



    def list_fields_contains(self, field):
        for id_field in self.homeScreen.lbx_campos_sql.get(0, END):
            if id_field == self.homeScreen.lbx_campos.get(field):
                return True
        return False

    def clearFields(self):
        self.homeScreen.lbx_campos.delete(0, END)
        self.homeScreen.lbx_campos_sql.delete(0, END)
        for field in self.list_edit:
            field.destroy()
            del field
        self.x_position = 450
        self.y_position = 125

    def read_file(self, filename):
        self.clearFields()

        xlsxToSql = XlsxToSql(filename)
        data = xlsxToSql.process_file()
        for d in data:
            self.homeScreen.lbx_campos.insert(END, d)