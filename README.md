# FastNotes API

Dieses Projekt umfasst das Backend für eine leistungsstarke und robuste Notiz-Applikation. Es basiert auf **FastAPI** für die Bereitstellung der REST-Endpunkte und nutzt eine relationale **SQLite-Datenbank** für die permanente Datenhaltung. Zusätzlich enthält das Projekt ein einfaches, im Unterricht erarbeitetes Frontend mittels **Streamlit**.

## 🚀 Features

### Backend & API (FastAPI)
- **Vollständige CRUD-Operationen:** Erstellen, Lesen, Aktualisieren und Löschen von Notizen (`POST`, `GET`, `PUT`, `PATCH`, `DELETE`).
- **Erweiterte Datenvalidierung:** Strikte Typ- und Datenprüfung an der Tür mittels **Pydantic V2** (Längenbegrenzungen für Strings, Wertebereiche für Zahlen und Fehlermeldungen bei unzulässigen Formaten).
- **Datenbereinigung:** Automatisches Entfernen von Whitespaces und striktes Verbot unbekannter JSON-Felder (`extra="forbid"`).
- **Such- & Filterfunktionen:** Filtern der Notizen nach Kategorien, Tags sowie Erstellungszeiträumen (`created_after` / `created_before`).
- **Statistik-Endpunkt:** Aggregierte Auswertungen über die Gesamtzahl der Notizen, Tags sowie eine Top-5-Auswertung der am häufigsten genutzten Tags.
- **Datenhaltung:** Lokale, permanente Speicherung in einer relationalen SQLite-Datenbank (`notes.db`).
- **Qualitätssicherung:** Umfassende Validierung aller Endpunkte und Randfälle durch eine integrierte Test-Suite mit `pytest`.

### Frontend (Streamlit)
- Eine erste, exemplarische Benutzeroberfläche zur Demonstration von Input-, Output- und Button-Funktionalitäten in Streamlit.
- Verwaltung des Anwendungszustands über den `st.session_state`.

---

## 🛠️ Installation & Setup

Das Projekt wird mit dem modernen Python-Paketmanager `uv` verwaltet.

1. **Repository klonen:**
   ```bash
   git clone <DEIN_REPOSITORY_URL>
   cd <DEIN_PROJEKTORDNER>

2. **Abhängigkeiten installieren:**
    ```bash
    uv sync

---

## 💻 Anwendung starten 

Um das System lokal auszuführen, kannst du das Backend und die Test-UI in separaten Terminal-Fenstern starten.

1. **API-Backend (FastAPI) starten**
    ```bash
    uv run fastapi dev main.py

Nach dem Start ist die interaktive API-Dokumentation im Browser unter http://127.0.0.1:8000/docs erreichbar. Hier können alle Endpunkte direkt getestet werden.

2. **Test-Frontend (Streamlit) starten**
    ```bash
    uv run streamlit run frontend.py

Die Streamlit-Oberfläche öffnet sich automatisch unter http://localhost:8501.

## 🧪 Tests ausführen

Die automatisierte Test-Suite prüft die Korrektheit der Routen, Filter und Validierungsregeln:
   ```bash
    cd exploration
    uv run pytest test2_main.py

