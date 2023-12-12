

class ReadLogs():

    def campaignExtractor(self, fileLog, campaign):
        with open( fileLog, 'r', encoding="utf-16-le") as arquivo:
            linhas = arquivo.readlines()
    
        for linha in linhas:
            if campaign in linha:
                
                print(linha.strip())