# Work Log

**Student Name:** 

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

Es wurden Tags eingeführt, um Notizen besser strukturieren und kategorisieren zu können. Zusätzlich wurden verschiedene Filterfunktionen in die bestehenden Endpunkte integriert. Neben der Einführung von DELETE-, PUT- und PATCH-Endpunkten wurden auch neue GET-Endpunkte erstellt, mit denen alle Tags angezeigt oder gezielt nach bestimmten Tags gesucht werden kann. Außerdem wurden Tag-Statistiken in den Statistik-Endpunkt eingebunden.
Darüber hinaus wurde bei den Notizen eine Filterfunktion nach Datum implementiert. Ein weiterer großer Schritt war der Austausch der bisherigen JSON-Dateispeicherung durch eine SQLite-Datenbank, wodurch die Datenhaltung verbessert und effizienter gestaltet wurde. Im Zuge dieser Umstellung wurden alle vorhandenen Endpunkte überarbeitet und entsprechend neu geschrieben.


---

#### 2. 🚧 What challenges did I face?

Die Funktion für Tags wurde nicht korrekt aufgerufen, da das Problem die Wörter in der URL mit einer Notiz-ID verwechselt hat. Das führte zu einem Fehler, weil das System einen Text an einer Stelle erhielt, an der es eigentlich eine Zahl als ID erwartet hatte.
Die Implementierung der Zähllogik für einzelne Tags sowie die Berechnung der Gesamtzahl einzigartiger Tags verlief erfolgreich. Schwierigkeiten bereitete jedoch die anschließende Filterung und Sortierung der Daten, um ausschließlich die Top-5-Tags in einem spezifischen Format auszugeben.


---

#### 3. 💡 How did I overcome them?

Ich habe mir das Problem von KI erklären lassen und konnte es lösen, indem ich die Reihenfolge der Funktionen im Code angepasst und die festen Pfade über die Suche nach IDs verschoben habe. Dadurch prüft das System nun zuerst, ob ein spezieller Befehl wie „tags“ gemeint ist, bevor es versucht, den Pfad als ID zu verarbeiten.
Nachdem ich die Umsetzung der Top-5-Filterung nicht hinbekommen habe, wurde die Lösung mithilfe von KI erarbeitet. Dabei wurde der Code so angepasst, dass die Tag-Liste zuerst nach Häufigkeit sortiert und dann in das richtige Format umgewandelt wird, damit die Statistik wie gewünscht angezeigt wird.


---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 5

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 6

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 8

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 9

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---


# 🎉 Congratulations! You did it! 🎓✨













