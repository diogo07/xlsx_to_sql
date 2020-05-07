import pandas as pd


class XlsxToSql:

    def __init__(self, filename):
        self.filename = filename


    def process_file(self):
        xlsx = pd.ExcelFile(self.filename)
        movies_sheets = []
        for sheet in xlsx.sheet_names:
            movies_sheets.append(xlsx.parse(sheet))
        movies = pd.concat(movies_sheets)
        return movies





