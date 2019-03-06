## main.py
- fuzzywuzzy Bibliothek muss vor der Ausführung installiert werden. *pip install fuzzywuzzy*
- input.json entsprechend durch Response der Google Search Console API ersetzen.
## request_api.py
- Bei https://console.cloud.google.com anmelden
- Ein neues Dienstkonto (Service Account) erstellen (Unter Menüpunkt: IAM & Verwaltung)
- Name des Dienstkonto erstellen
- Schlüssel erstellen und JSON wählen
- Der Schlüssel ist eine JSON Datei, die in das Stammverzeichnis des Programms muss.
- Die ID des Dienstkonto (E-Mail Adresse) muss als lesender Benutzer zu der entsprechenden GSC Property hinzugefügt werden.
