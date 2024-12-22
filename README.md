# Lakehouse Projekt

Dieses Projekt demonstriert die Integration von Open-Source-Komponenten, um ein Lakehouse zu erstellen, das Parquet, Delta Lake, PySpark, MinIO und Apache Superset verwendet. Das Ziel des Projekts ist es, eine leistungsfähige, skalierbare Datenarchitektur zu bauen, die es ermöglicht, große Mengen an strukturierten und unstrukturierten Daten zu verarbeiten und zu visualisieren.

## Inhaltsverzeichnis:

* [Projektbeschreibung](#projektbeschreibung)
* [Installation](#installation)
  * [Voraussetzungen](#voraussetzungen)
  * [Schritte zur Installation](#schritte-zur-installation)
* [Benutzung](#benutzung)
  * [Starten des Lakehouse](#starten-des-lakehouse)
  * [Arbeiten mit Apache Superset](#arbeiten-mit-apache-superset)
* [Docker-Setup](#docker-setup)
  * [Mit Docker Compose](#mit-docker-compose)
* [Technologien](#technologien)
* [Lizenz](#lizenz)

## Projektbeschreibung:

Das Projekt umfasst die folgenden Open-Source-Komponenten:

* **Parquet**: Ein spaltenbasiertes Dateiformat für die Speicherung und Verarbeitung von Daten.
* **Delta Lake**: Eine Storage-Layer auf Basis von Apache Spark, die ACID-Transaktionen und Versionskontrolle für Big Data ermöglicht.
* **PySpark**: Ein Framework für verteilte Datenverarbeitung.
* **MinIO**: Ein S3-kompatibles Object Storage, das als Speichersystem für das Lakehouse dient.
* **Apache Superset**: Ein Open-Source-Dashboard- und Visualisierungstool, das zur Analyse und Präsentation der Daten verwendet wird.

## Installation:

### Voraussetzungen:
Stelle sicher, dass die folgenden Software-Pakete installiert sind:
* Python 3.9 oder höher
* Docker (falls du Docker verwenden möchtest)
* Docker Compose (optional, falls du mehrere Container verwenden möchtest)

### Schritte zur Installation:

1. Klone dieses Repository:

   git clone https://github.com/dein-benutzername/lakehouse-project.git
   cd lakehouse-project

2. Erstelle eine virtuelle Umgebung (optional, aber empfohlen):

   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate

3. Installiere die benötigten Abhängigkeiten:

   pip install -r requirements.txt

## Benutzung:

### Starten des Lakehouse:

1. **Datenverarbeitung**: Um das Beispiel zu testen und Daten als Parquet und Delta zu speichern, führe das folgende Skript aus:

   python scripts/data_processing.py

2. **Docker-Container starten**: Wenn du Docker verwenden möchtest, um MinIO, PySpark und Delta zu starten, führe dieses Skript aus:

   python scripts/create_docker_containers.py

3. **Daten laden**: Um Beispiel-Daten zu laden und in das Lakehouse zu speichern, führe dieses Skript aus:

   python scripts/data_load.py

### Arbeiten mit Apache Superset:

* Starte Apache Superset, indem du den entsprechenden Container mit Docker startest oder es lokal installierst.
* Gehe zu http://localhost:8088 und melde dich mit den Standardanmeldedaten an.
* Verbinde Superset mit deinen Datenquellen (z. B. Delta Lake oder MinIO) und erstelle Dashboards.

## Docker-Setup:

Dieses Projekt enthält Docker-Container für MinIO, PySpark, Delta Lake und Parquet. Du kannst diese Container mit Docker Compose oder direkt über Docker starten.

### Mit Docker Compose:

1. Baue und starte alle Container mit dem folgenden Befehl:

   docker-compose up --build

2. Du kannst den Status der Container überprüfen mit:

   docker-compose ps

3. Um alle Container zu stoppen:

   docker-compose down

## Technologien:

* **Python**: Die Hauptsprache für die Datenverarbeitung und Automatisierung.
* **Apache Spark (PySpark)**: Verwendet für die verteilte Verarbeitung von Daten.
* **Delta Lake**: Ermöglicht ACID-Transaktionen und Versionskontrolle.
* **MinIO**: Objektbasierter Speicher für die Speicherung von Daten.
* **Apache Superset**: Visualisierungs- und Dashboard-Tool.

## Lizenz:

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE-Datei für Details.
