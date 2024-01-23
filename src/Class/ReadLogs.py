import csv


class ReadLogs:
    def campaignExtractor(self, fileLog, campaign):
        exibitionList = []

        with open(fileLog, "r", encoding="utf-16-le") as arquivo:
            linhas = arquivo.readlines()
        
        lineList = [x.strip('\n') for x in linhas]
        
        for linha in lineList:
            if campaign in linha:
                line = linha.split("\t")
                exibitionList.append(line)

        print(exibitionList)

        # with open("exemplo.csv", "w", newline="") as arquivo_csv:
        #     escritor_csv = csv.writer(arquivo_csv)

        #     escritor_csv.writerows(exibitionList)

        # print("Arquivo CSV criado com sucesso.")
