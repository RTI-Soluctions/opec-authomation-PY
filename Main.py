from Class.ReadLogs import ReadLogs
from Layout.MainWindow import window

campaign = "Live"

pathLogFiles = "logs/"

fileLog = pathLogFiles + "2023-07-31.log"

teste = ReadLogs()

# teste.campaignExtractor(fileLog, campaign)

window.mainloop()
