import csv


class ReadLogs:
    def campaignExtractor(self, fileLog, campaign):
        exibitionList = []

        with open(fileLog, "r", encoding="utf-16-le") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            if campaign in linha:
                # linha.strip()
                line = linha.split("\t")
                
                for word in line:
                    newWord = word.replace("\n", "")
                
                # exibitionList.append(lineList)
                print(line)

        # print(exibitionList)
        
        # with open("exemplo.csv", "w", newline="") as arquivo_csv:
        #     escritor_csv = csv.writer(arquivo_csv)

        #     escritor_csv.writerows(exibitionList)

        # print("Arquivo CSV criado com sucesso.")
