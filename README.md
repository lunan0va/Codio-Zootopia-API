# Zootopia API Project

Dieses Projekt erstellt eine dynamische Website mit Tierkarten, indem es Daten von einer externen API (API Ninjas) abruft. Es ist eine Weiterentwicklung des ursprünglichen Zootopia-Projekts, das auf einer statischen JSON-Datei basierte.

## Installation

1. Repository klonen:  
   `git clone https://github.com/lunan0va/zootopia-api.git`  
   `cd zootopia-api`

2. Abhängigkeiten installieren:  
   `pip install -r requirements.txt`

3. Eine `.env`-Datei im Projektordner erstellen mit folgendem Inhalt:

```
API_KEY='DEIN_API_KEY_HIER'
```

## Usage

Das Programm fragt den Namen eines Tiers ab, ruft passende Informationen über die API ab und erstellt daraus eine `animals.html`-Datei.

Zum Ausführen:

```
python animals_web_generator.py
```

Beispiel:

```
Please enter an animal: Fox  
```

## Projektstruktur

- `animals_web_generator.py` – Generiert die HTML-Seite  
- `data_fetcher.py` – Holt die Daten von der API  
- `animals_template.html` – HTML-Vorlage mit Platzhalter  
- `.env` – Enthält den geheimen API-Schlüssel (nicht im Repo)  
- `requirements.txt` – Alle Python-Abhängigkeiten

## Contributing

Beiträge sind willkommen! Erstelle gerne einen Pull Request oder öffne ein Issue, wenn du Vorschläge oder Verbesserungen hast.
