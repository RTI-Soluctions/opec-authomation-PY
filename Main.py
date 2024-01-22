import csv
import openpyxl

campaign1 = "Live"

pathLogFiles = "src/logs/"

fileLog = pathLogFiles + "2023-07-31.log"


def campaignExtractor(fileLog, campaign):
    exibitionList = []

    with open(fileLog, "r", encoding="utf-16-le") as arquivo:
        linhas = arquivo.readlines()

    lineList = [x.strip("\n") for x in linhas]

    for linha in lineList:
        if campaign in linha:
            line = linha.split("\t")
            exibitionList.append(line)

    nome_arquivo = "Planilha.xlsx"

    workbook = openpyxl.Workbook()

    sheet = workbook.active

    for line in exibitionList:
        sheet.append(line)

    workbook.save(nome_arquivo)

    print(f"O array foi inserido no arquivo {nome_arquivo} com sucesso.")

    print(exibitionList)


# teste.campaignExtractor(fileLog, campaign)

campaignExtractor(fileLog, campaign1)

# window.mainloop()
