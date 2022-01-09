# ML_Kinderzeichnung: Training

## Training
Mithilfe der Bilder in [`ML_Kinderzeichnung/Data/Source_Images/Training_Images`](/Data/Source_Images/Training_Images) und dem vorher generierten Annotationsfile [`data_train.txt`](/Data/Source_Images/Training_Images/Training_Data) können wir unseren YOLO-Detektor nun trainieren. 

## Download und Konvertierung Pre-Trained Weights
Vor dem Training müssen noch die vortrainierten Gewichte heruntergeladen und ins keras-Format konvertiert werden. Dafür wird das Script im Ordner [`TrainYourOwnYOLO/2_Training`](/2_Training/) ausgeführt:

```
python Download_and_Convert_YOLO_weights.py
```
Falls mit den Gewichten von YOLOv4 trainiert werden möchte, sind diese bereits vorhanden. Dazu müsste dann aber im Script "Train_YOLO.py" Linie 73 folgendermassen angepasst werden:
weights_path = os.path.join(keras_path, "yolo.h5") < weights_path = os.path.join(keras_path, "yolov4.h5")

## Train YOLO-Detektor
Um das Training zu starten, muss das Script im Ordner [`ML_Kinderzeichnung/2_Training`](/2_Training/) ausgeführt werden:
```
python Train_YOLO.py 
```
Je nach Setup dauert dieser Vorgang von einigen Minuten bis zu einigen Stunden. Die finalen Gewichte werden in [`ML_Kinderzeichnung/Data/Model_weights`].

### Training beendet! 
Als nächstes, wechsle in den Ordner [`ML_Kinderzeichnung/3_Inference`](/3_Inference) um die Maschine zu testen.

