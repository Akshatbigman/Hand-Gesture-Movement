import numpy as np
import tensorflow as tf
import time

model = tf.keras.models.load_model(
    "num_model.h5",
    custom_objects=None,
    compile=True,
    options=None)

pose = Posenet()

try:
    pose.enablebox()
    pose.video("on", 0)
    print("Camera initialized successfully.")
except Exception as e:
    print(f"Error initializing camera: {e}")
    exit()

class_list = ['Forward', 'Reverse', 'Right', 'Left']

quarky = Quarky()

while True:
    pose.analysehand()
    coordinate_xy = []
    hand_detected = False

    for i in range(21):
        x_pos = pose.gethandposition(1, i, 0)
        y_pos = pose.gethandposition(2, i, 0)
        
        if x_pos != "NULL" and y_pos != "NULL":
            hand_detected = True
            coordinate_xy.append(int(240 + float(x_pos)))
            coordinate_xy.append(int(180 - float(y_pos)))
        else:
            coordinate_xy.append(0)
            coordinate_xy.append(0)

    if not hand_detected:
        print("No hand sign detected. Stopping the robot.")
        quarky.runrobot("FORWARD", 0)
        continue

    coordinate_xy_tensor = tf.expand_dims(coordinate_xy, 0)
    predict = model.predict(coordinate_xy_tensor)
    predict_index = np.argmax(predict[0], axis=0)
    predicted_class = class_list[predict_index]
    
    print("Predicted Class:", predicted_class)

    if predicted_class == 'Forward':
        quarky.runrobot("FORWARD", 100)
    elif predicted_class == 'Reverse':
        quarky.runrobot("BACKWARD", 100)
    elif predicted_class == 'Right':
        quarky.runrobot("RIGHT", 100)
    elif predicted_class == 'Left':
        quarky.runrobot("LEFT", 100)

    time.sleep(0)


