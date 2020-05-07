from tkinter.filedialog import askopenfilename

from src.model.XlsxToSql import XlsxToSql
from tkinter import *

class ControllerHomeScreen:

    def __init__(self, homeScreen):
        self.homeScreen = homeScreen


    def open_browser(self):
        fname = askopenfilename(filetypes=(("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")))
        self.homeScreen.ent_arquivo.delete(1.0, "end-1c")
        self.homeScreen.ent_arquivo.insert("end-1c", fname)
        self.read_file(fname)

    def add_fields(self):
        x_position = 450
        y_position = 125
        for field in self.homeScreen.lbx_campos.curselection():
            if not self.list_fields_contains(field):
                self.homeScreen.lbx_campos_sql.insert(END, self.homeScreen.lbx_campos.get(field))

                temp = Entry(self.homeScreen.master)
                temp.place(x=x_position, y=y_position)
                y_position+=20

    def remove_field(self):
        for field in self.homeScreen.lbx_campos_sql.curselection():
            self.homeScreen.lbx_campos_sql.delete(field)

    def list_fields_contains(self, field):
        for id_field in self.homeScreen.lbx_campos_sql.get(0, END):
            if id_field == self.homeScreen.lbx_campos.get(field):
                return True
        return False

    def read_file(self, filename):
        xlsxToSql = XlsxToSql(filename)
        data = xlsxToSql.process_file()
        for d in data:
            self.homeScreen.lbx_campos.insert(END, d)