# Work Log

**Student Name: Andreas Moritz** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?



---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?




---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?

Ich habe es geschafft die API einzurichten, und mir die die Endpunkte aus dem Unterricht, sowie sowie aus der Hausaufgabe zu erarbeiten, nachdem ich am ersten Tag nicht anwesend sein konnte.


---

#### 2. 🚧 What challenges did I face?

Es hat mir Probleme gemacht die API zu starten da mir immer wieder angezeigt wurde, dass mir FastAPI [Standard] fehlt. Zudem stand im Fehlercode, dass ich pip install "fastapi[standard]" eingeben soll. 


---

#### 3. 💡 How did I overcome them?

Zuerst habe ich das Vibecoding fenster geöffnet und reingeschrieben, dass fastapi[standard] istalliert werden soll, nachdem das nicht funktioniert hat habe ich es mit KI probiert. Nachdem das auch nicht funktioniert hat habe ich eine Dokumentation gefunden, in der stand, dass man es durch den Befehl "uv add fastapi --extra standard" installieren kann, was dann auch funktioniert hat.


---

### Day 2

#### 1. ✅ What did I accomplish?

Ich habe die Anbindung meines VS Code Projekts an mein GitHub-Repository erfolgreich abgeschlossen. Dazu gehörte die Konfiguration der Git-Umgebung sowie das Erlernen des Workflows aus Staging, Committing und Pushing. Zudem habe ich die Notiz-Applikation mit den Methoden GET und POST implementiert, um Notizen sowohl abrufen als auch erstellen zu können. Anschließend habe ich noch die Save- und Load-Logik implementiert, die die Speicherung der Daten in einer JSON-Datei sicherstellt.


---

#### 2. 🚧 What challenges did I face?

Die größte Hürde war ein wiederkehrender Fehlercode 500. Zu diesem Zeitpunkt konnte ich mit dem Fehlercode auch nicht viel Anfangen.


---

#### 3. 💡 How did I overcome them?

Ich habe bei Kommilitonen gefragt, ob sie das selbe Problem hatten oder eine Lösung kennen würden, hier konnte mir jedoch nicht geholfen werden. Als ich anschließend KI um Rat bat, stellte sich heraus, dass meine JSON-Datei noch Notizen enthielt, die die Kategorie "category" noch nicht hatten. Nachdem ich alles rausgelöscht habe kam wieder ein Fehler, da ich den kompletten inhalt aus der JSON-Datei gelöscht hatte. Nach erneuter hilfe durch KI habe ich gelernt, dass eine JSON-Datei als Datenbasis für eine Liste dient, weshalb diese nicht absolut leer sein darf, sondern mit einem leeren Array [] initialisiert werden muss.


---

### Day 3

#### 1. ✅ What did I accomplish?

Es wurden Tags eingeführt, um Notizen besser strukturieren und kategorisieren zu können. Zusätzlich wurden verschiedene Filterfunktionen in die bestehenden Endpunkte integriert. Neben der Einführung von DELETE-, PUT- und PATCH-Endpunkten wurden auch neue GET-Endpunkte erstellt, mit denen alle Tags angezeigt werden können oder gezielt nach bestimmten Tags gesucht werden kann. Außerdem wurden Tag-Statistiken in den Statistik-Endpunkt eingebunden.
Darüber hinaus wurde bei den Notizen eine Filterfunktion nach Datum implementiert. Ein weiterer großer Schritt war der Austausch der bisherigen JSON-Dateispeicherung durch eine SQLite-Datenbank, wodurch die Datenhaltung verbessert und effizienter gestaltet wurde. Im Zuge dieser Umstellung wurden alle vorhandenen Endpunkte überarbeitet und entsprechend neu geschrieben.


---

#### 2. 🚧 What challenges did I face?

Die Funktion für Tags wurde nicht korrekt aufgerufen, da das Problem die Wörter in der URL mit einer Notiz-ID verwechselt hat. Das führte zu einem Fehler, weil das System einen Text an einer Stelle erhielt, an der es eigentlich eine Zahl als ID erwartet hatte.
Die Implementierung der Zähllogik für einzelne Tags sowie die Berechnung der Gesamtzahl einzigartiger Tags verlief erfolgreich. Schwierigkeiten bereitete jedoch die anschließende Filterung und Sortierung der Top-5-Tags.
Zusätzlich bereitete die Umstellung von der bisherigen JSON-Datenspeicherung auf eine SQLite-Datenbank Probleme. Vor allem das Anpassen der bestehenden Endpunkte und die neue Datenbankstruktur führten zunächst zu Fehlern und unerwartetem Verhalten im System.


---

#### 3. 💡 How did I overcome them?

Ich habe mir das Problem von KI erklären lassen und konnte es lösen, indem ich die Reihenfolge der Funktionen im Code angepasst und die festen Pfade über die Suche nach IDs verschoben habe. Dadurch prüft das System nun zuerst, ob ein spezieller Befehl wie „tags“ gemeint ist, bevor es versucht, den Pfad als ID zu verarbeiten.
Nachdem ich die Umsetzung der Top-5-Filterung nicht hinbekommen habe, wurde die Lösung mithilfe von KI erarbeitet. Dabei wurde der Code so angepasst, dass die Tag-Liste zuerst nach Häufigkeit sortiert und dann in das richtige Format umgewandelt wird, damit die Statistik wie gewünscht angezeigt wird.
Bei der Umstellung auf SQLite musste ich mehrere Ansätze ausprobieren, bis die Datenbank korrekt funktioniert hat. Dabei mussten die bisherigen Dateioperationen durch SQL-Abfragen ersetzt und die bestehenden Endpunkte mehrfach angepasst werden, da es anfangs zu Fehlern beim Speichern und Auslesen der Daten kam. Durch wiederholtes Testen und schrittweises Überarbeiten des Codes konnte die Umstellung schließlich erfolgreich umgestetzt werden.


---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?

Ich habe automatisierte Softwaretests unter Verwendung des pytest-Frameworks erstellt. Dabei habe ich gelernt, die Bibliothek requests zu nutzen, um meine API mit HTTP-Anfragen zu testen. Die Tests wurden nach dem "Arrange-Act-Assert"-Pattern geschrieben, um die Korrektheit meiner Endpunkte sicherzustellen. Konkret habe ich die Tests für meine POST, GET, DELETE, PUT und PATCH endpunkte geschrieben. Außerdem habe ich gelernt wie ich gezielt Fehlerfälle, wie 404-Meldungen bei nicht existierenden IDs, teste.


---

#### 2. 🚧 What challenges did I face?

Eine grundlegende Schwierigkeit liegt für mich derzeit noch im Transfer von der logischen Planung zur technischen Umsetzung. Während ich den Aufbau und die Funktionsweise von den Codes logisch nachvollziehen kann, fehlen mir oft die Kenntnis über das verfügbare "Vokabular" der Programmiersprache. Ich kann mir zwar vorstellen, wie der Ablauf eines Tests aussehen sollte, weiß aber häufig nicht, welche spezifischen Funktionen, Methoden oder Bibliotheksbefehle existieren, um dieses Ziel konkret zu implementieren.


---

#### 3. 💡 How did I overcome them?

Um diese Wissenslücken zu schließen, durchsuche ich gezielt die offiziellen Dokumentationen der Bibliotheken, um das passende Vokabular für meine Konzepte zu finden. Zudem tausche ich mich mit Kommilitonen über mögliche Lösungswege aus und nutze KI-Unterstützung (Gemini) um neue Funktionen kennenzulernen. Dadurch lerne ich schrittweise, welche Werkzeuge mir zur Verfügung stehen.


---

### Day 5

#### 1. ✅ What did I accomplish?

Ich habe die Datenvalidierung und Datenbereinigung meiner API mithilfe von Pydantic ausgebaut. Dafür habe ich Field-Constraints integriert, um Längenbegrenzungen für Strings und Wertebereiche für Zahlen zu erzwingen. 
Über ein ConfigDict habe ich das automatische Entfernen von Whitespaces und das strike Ablehnen unbekannter JSON-Felder in den Modellen aktiviert. Zudem hab ich field_validator für die Bereinigung einzelnder Felder (wie Kategorien und Tag-Listen) sowie model_validator für feldübergreifende Logik implementiert. Abschließend wurden die Validierungsregeln für PATCH-Anfragen so angepasst, dass sie auch bei optionalen Feldern greifen.


---

#### 2. 🚧 What challenges did I face?

In der Vorlesung erschien mir die Funktionsweise des field_validator noch absolut logisch. Als ich jedoch mit der Umsetzung der Hausaufgaben begonnen habe, merkte ich, dass ich den Code selbstständig noch nicht fehlerfrei niederschreiben konnte. Es fiel mir schwer, die exakte Syntax und den logischen Ablauf der Validierung ohne Hilfestellung aufzubauen.


---

#### 3. 💡 How did I overcome them?

Um diese Unsicherheiten zu beseitigen, habe ich mir das Skript des Unterrichtstages noch mehrmals gründlich durchgelesen und die gezeigten Beispiele Schritt für Schritt nachvollzogen. Dadurch konnte ich die Validierungslogik besser verinnerlichen und letztlich erfolgreich umsetzen.




---

### Day 6

#### 1. ✅ What did I accomplish?

Der Schwerpunkt des Tages lag auf der umfassenden Qualitätssicherung der API. Ich habe eine vorgegebene Test-Suite in mein Repository integriert, um die gesamte Funktionalität der Anwendung mit pytest zu prüfen. Da uns bis zu nächsten Vorlesung fünf Tage zur Verfügung standen, habe ich die Zeit genutzt, um den gesammten bisherigen Stoff intensiv zu wiederholen. Dafür habe ich ein komplett neues Repository erstellt und mich noch einmal tiefgehend mit Skript 3 befasst, um insbesondere die Umstellung von der JSON-Dateispeicherung auf die relationale SQLite-Datenbank von Grund auf eigenständig zu üben und zu verinnerlichen.


---

#### 2. 🚧 What challenges did I face?

Nach dem ersten Ausführen der neuen Test-Suite trat ein Ergebnis von 18 fehlgeschlagenen Tests, 13 bestandenen Tests und 39 Errors auf. Bei der Fehleranalyse stellte sich heraus, dass ein Großteil der Probleme durch den model_validator verursacht wurde. Dieser verhinderte das Erstellen von Notizen mit der Kategorie "work", wenn der Tag "work" fehlte. Die Test-Suite versuchte jedoch laufend, genau solche Testdaten zu generieren, wodurch auch alle darauf aufbauenden Abfragetests fehlschlugen.
Ein weiteres Problem war mein field-validator für Tags: Diese filterte zu kurze Tags einfach aus der Liste heraus, während die Test-Suite an dieser Stelle eine Fehlermeldung erwartete. Zuletzt scheiterten Test an den Parametern created_after und created_before im Notes-Endpunkt, da mein Code ein falsches Datumsformat anfangs einfach ingorierte, statt den geforderten Validierungsfehler auszugeben.


---

#### 3. 💡 How did I overcome them?

Ich habe die Blockaden gelöst, indem ich den Code schrittweise überarbeitet und an die Erwartungen der Test-Suite angepasst habe. Um den Fehler mit der Notizenerstellung zu beheben, habe ich den model_validator vollständig aus dem NoteCreate-Modell herausgelöscht. 
Da ich bei dem Problem mit dem field_validator selbstständig nicht auf die Ursache des Fehlers gekommen bin, habe ich mir hierbei Unterstützung von Gemini geholt. Dadurch konnte ich den Validator so umschreiben, dass er bei Strings unter zwei Zeichen wie gefordert einen ValueError auslöst, anstatt die Elemente eingemächtig zu löschen. Zudem habe ich die Filterlogik im GET-Endpunkt für die Notizen erweitert, sodass die Parameter created_after und created_before eingehende Datumsformate strikt prüfen und bei Fehlern den passenden HTTP-Statuscode ausgeben. Durch das Beheben dieser Kernfehler im Validierungs- und Filterprozess konnte ich die Abhängigkeiten auflösen, sodass nach und nach auch die darauf basierenden Folgetests fehlerfrei durchliefen.


---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?

Ich habe ein interaktives Web-Frontend mittels Streamlit implementiert, um Benutzereingaben zu verarbeiten und den Zustand der Anwendung über st.session_state zu verwalten. Zudem habe ich die Datei main.py aufgeräumt. Anschließend habe ich mein Repository bereinigt, indem ich ungenutzt Dateien gelöscht, Skripte in logische Unterordner verschoben und temporäre Daten in die .gitignore-Datei eingetragen habe.


---

#### 2. 🚧 What challenges did I face?

Ein Schwierigkeit lag beim Aufräumen des Codes in der Datei main.py: Ich wusste von mir aus nicht, wie der Code im Optimalfall übersichtlich sortiert und strukturiert sein sollte.


---

#### 3. 💡 How did I overcome them?

Um eine optimale Strukturierung und Sortierung des Codes in der main.py zu ermitteln habe ich Gemini als Hilfestellung herangezogen und dessen Vorschläge umgesetzt.


---


# 🎉 Congratulations! You did it! 🎓✨













