# ML_Kinderzeichnung: Inference
In diesem Schritt testen wir unseren Detektoren an den Testbildern im Ordner [`ML_Kinderzeichnung./Data/Source_Images/Test_Images`](/Data/Source_Images/Test_Images). 
Dazu werden die gewünschten Testbilder im Ordner [`Test_Images`](/Data/Source_Images/Test_Images) abgelegt. 

## Den eigenen Detektor testen
Um Objekte auf den Bildern zu erkennen muss das Script im Ordner [`ML_Kinderzeichnung/3_Inference`](/3_Inference/) ausgeführt werden:

```
python Detector.py
```
Die Ergebnisse werden im Ordner [`ML_Kinderzeichnung/Data/Source_Images/Test_Image_Detection_Results`](/Data/Source_Images/Test_Image_Detection_Results) gespeichert .
Die Ergebnisse beinhalten die originalen Bilder mit Bounding Boxex und dem Vertrauenswert, wie auch das File [`Detection_Results.csv`](/Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv)  in welchem der Pfad der Bilder und die Koordinaten der Boxen.

### Das war's!



