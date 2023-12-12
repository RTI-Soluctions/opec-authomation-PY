import csv
from Class.ReadLogs import ReadLogs



campaign = "Live"

pathFile = "logs/"

fileLog = pathFile + '2023-07-31.log'

teste = ReadLogs()

teste.campaignExtractor(fileLog, campaign)


