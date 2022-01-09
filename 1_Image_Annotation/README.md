# TrainYourOwnYOLO: Image Annotation

## Dataset
Um den eigenen Yolo-Algorithmus zu trainieren, kopiere deine Bilder in den Ordner[`ML_Kinderzeichnung/Data/Source_Images/Training_Images`](/Data/Source_Images/Training_Images/).

## Annotation
Damit der Detektor lernt, braucht er gute Trainingsbeispiele. Wir benutzen labelImg um die Bilder zu annotieren. Dies kann direkt im Trainingsordner oder zuerst an einem seperaten Ort durchgeführt werden.
Für gute Resultate braucht es mehr als 1000 Bilder.

### Download labelImg
Von der Githubseite von [labelImg](https://github.com/tzutalin/labelImg) kann das Annotationstool heruntergeladen und installiert werden.
Folge den Anweisungen auf der Seite, damit die Bilder im gewünschten Format (YOLO) annotiert werden.

### Labeln und Vorbereiten Trainingsordner
Annotiere deine Bilder mit den gewünschten Klassen. Es ist wichtig, dass die Klassen während dem Prozess nicht verändert werden.

Nachdem alle Bilder annotiert worden sind, müssen die Bilder und zugehörigen .txt-Dateien in den Ordner [`ML_Kinderzeichnung/Data/Source_Images/Training_Images`](/Data/Source_Images/Training_Images/) verschoben werden (falls nicht bereits dort annotiert wurde).
Zudem müssen die Bilder (nur die Bilder) in den Ordner [`ML_Kinderzeichnung/Data/Source_Images/Training_Images/Training_Data`](/Data/Source_Images/Training_Images/Training_Data) kopiert werden.
Zuletzt muss im File [`data_classes.txt`](/Data/Model_Weights/data_classes.txt), welches im Ordner [`ML_Kinderzeichnung/Data/Model_Weights`](/Data/Model_Weights/) zufinden ist, die Klassen eingefügt werden.
Am besten wird dazu der Inhalt des Files [`classes.txt`], welches von labelImg erzeugt wird, in [`data_classes.txt`] kopiert.

### Konvertierung .txt zu einem .csv
Als nächster Schritt werden die .txt-Files in ein gemeinsames .csv übertragen. Dazu wird das Script im Ordner [`ML_Kinderzeichnung/1_Image_Annotation`](/1_Image_Annotation/) benutzt:

```
python Convert_to_csv.py
```

Dies generiert im gleichen Ordner das File [`training_data.txt`]. Dieses muss nun in den Ordner [`ML_Kinderzeichnung/Data/Source_Images/Training_Images/Training_Data`](/Data/Source_Images/Training_Images/Training_Data) verschoben werden.

## Konvertierung ins YOLO Format
Als letzter Schritt wird das csv in das YOLO-Format übertragen. Dazu wird folgendes Script im Ordner [`ML_Kinderzeichnung/1_Image_Annotation`](/1_Image_Annotation/) ausgeführt:

```
python Convert_to_YOLO_format.py
```
So erhalten wir das File[`data_train.txt`](/Data/Source_Images/Training_Images/Training_Data/data_train.txt) im Ordner [`ML_Kinderzeichnung/Data/Source_Images/Training_Images/Training_Data`](/Data/Source_Images/Training_Images/Training_Data).

### Fertig Annotation! 
Als nächstes, wechsle zu [`ML_Kinderzeichnung/2_Training`](/2_Training) um das Modell zu trainieren.