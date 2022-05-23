import os
from os import listdir
from os.path import isfile, join

#Nimmt sich Datum aus dem Path und bereit Dateinamen vor
path = os.path.dirname(os.path.realpath(__file__))
date_o = path[path.find("HZ ET") + 6:]
date_n = date_o[6:10] +  date_o[3:5] + date_o[:2]
file_name = "HZ_" + date_n + ".xml"

#Nimmt alle Dateien die im Ordner sind in die Dateienliste auf und wirft die Arbeitsdateien raus
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyfiles.remove('script.py')
onlyfiles.remove('run_me.cmd')

#Wirft alles aus der Dateienliste was kein PDF is
for f in onlyfiles:
    if not ".pdf" in f:
        onlyfiles.remove(f)

#Header for XML Zielen in ersteller Datei
output = '<?xml version="1.0" encoding="iso-8859-1"?>\n<classifieds customer="Gemeinsamtrauern.com/N-land.de">\n'

#XML jeder Datei aus der Dateiliste in die Zieldatei schreiben
for f in onlyfiles:
    new_snip = '  <classified>\n    <image>{}</image>\n    <email>servicecenter@hersbrucker-zeitung.de</email>\n    <attribute key="od_base_issue">HZ</attribute>\n    <attribute key="od_base_date_published">{}</attribute>\n    <attribute key="od_partner_number">Bestatter-ID</attribute>\n  </classified>\n'.format(f, date_n)
    output += new_snip

output += '</classifieds>'

#erstellen der Zieldatei
with open(file_name, 'w') as f:
    f.write(output)

#Arbeitsdatein deleten. if 20 damit sie nicht geloescht werden wenn das Script ungewollt im falschen Ordner ausgefuert wird.
if "20" in date_n:
    os.remove( path + "\script.py")
    os.remove("run_me.cmd")