# ML-Kinderzeichnung: YOLO Maschine für das Data Artist Projekt

Als Grundlage für diese Maschine wurde das Githubrepository von Anton Mühlemann (https://github.com/AntonMu/TrainYourOwnYOLO) mit Yolov3 benutzt.
Es wurden leichte Anpassungen angenommen, da mit einem anderen Annotationstool gearbeitet wird. Zudem wurden die vortrainierten Gewichte für Yolov4 hinzugefügt.

Diese Maschine funktioniert mit Python 3.8, Tensorflow 2.3 und Keras 2.4.

### Übersicht

Um einen eigenen YOLO-Algorithmus zu bauen und testen müssen die folgenden Schritte befolgt werden:

 1. [Image Annotation](/1_Image_Annotation/)
	 - Installiere das Annotationstool labelImg (https://github.com/tzutalin/labelImg)
	 - Annotiere Bilder
 2. [Training](/2_Training/)
 	- Vortrainierte Gewichte herunterladen(für yolov4 bereits gemacht)
 	- Das YOLO-Model an den annotierten Bildern trainieren 
 3. [Inference](/3_Inference/)
 	- Objekte in neuen Bildern erkennen

## Struktur
+ [`1_Image_Annotation`](/1_Image_Annotation/): Scripts und Anleitungen für die Annotation
+ [`2_Training`](/2_Training/): Scripts und Anleitungen für das Training des Models
+ [`3_Inference`](/3_Inference/): Scripts und Anleitungen für das Testen des Models an neuen Bildern
+ [`Data`](/Data/): Input Data, Output Data, Model Weights und Resultate
+ [`Utils`](/Utils/): Hilf-Scripts, welche von den Hauptscripts benutzt werden

### Anforderungen
Die wichtigste Anforderung ist ein funktionierendes Python 3.6, 3.7 oder 3.8.

### Installation

#### Eine virtuelle Umgebung erstellen [Linux or Mac]

Zuerst das Repository folgendermassen clonen:
```bash
git clone https://github.com/jhaeubi/ML_Kinderzeichnung
cd ML_Kinderzeichnung/
```
Virtuelle Umgebung **(Linux/Mac)** erstellen:
```bash
python3 -m venv env
source env/bin/activate
```
Ab jetzt müssen **alle Befehle innerhalb der virtuellen Umgebung gegeben werden**.

#### Packages Installieren [Windows, Mac or Linux]
Die Packages können wie folgt installiert werden:

```bash
pip install -r requirements.txt
```

## Full Start (Training und Inference)

Um den eigenen YOLO-Algorithmus zu trainieren bitte den Instruktionen in den drei Unterordnern folgen:

- [`1_Image_Annotation`](/1_Image_Annotation/),
- [`2_Training`](/2_Training/) and
- [`3_Inference`](/3_Inference/).




