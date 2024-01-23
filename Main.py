import os
import openpyxl
from datetime import datetime

campaign1 = "PI 70485"

pathLogFiles = "src/logs/"

actual_date = datetime.now()

date_format = " %H:%M:%S de %d/%m/%YY"

organized_date = actual_date.strftime(date_format)


def campaignExtractor(campaign):
    exibitionList = []

    for file_name in os.listdir(pathLogFiles):
        fileLog = os.path.join(pathLogFiles, file_name)

        if fileLog.endswith(".log"):
            with open(fileLog, "r", encoding="utf-16-le") as arquivo:
                linhas = arquivo.readlines()

            lineList = [word.strip("\n") for word in linhas]

            for linha in lineList:
                if campaign in linha:
                    line = linha.split("\t")
                    exibitionList.append(line)

    final_file = "Report_Template.xlsx"

    def insertDataIntoCells(sheet, dados, start_line, start_column):
        sheet.cell(row=3, column=4, value=organized_date)

        for i, linha in enumerate(dados):
            for j, valor in enumerate(linha):
                sheet.cell(row=start_line + i, column=start_column + j, value=valor)

    workbook = openpyxl.load_workbook(final_file)

    sheet = workbook.worksheets[0]

    start_line = 10
    start_column = 2

    insertDataIntoCells(sheet, exibitionList, start_line, start_column)

    workbook.save(f"Report_Template.xlsx")

    print(f"Relatório {final_file} atualizado com sucesso.")


campaignExtractor(campaign1)

# window.mainloop()
