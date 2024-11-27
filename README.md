# Hand Gesture Controlled Robot

This project uses a hand gesture recognition model to control a robot. The gestures are detected using Posenet and classified with a pre-trained TensorFlow model. Based on the detected gesture, the robot moves in the specified direction.

---

## Features

- Real-time hand gesture detection and analysis using Posenet.
- Gesture classification with a pre-trained TensorFlow model.
- Quarky robot movement based on recognized gestures:
  - **Forward**: Robot moves forward.
  - **Reverse**: Robot moves backward.
  - **Right**: Robot turns right.
  - **Left**: Robot turns left.
  - **No Gesture**: Robot stops moving.

---

## Prerequisites

1. **Hardware**
   - any Robot (in my case, i used Quarky)
   - Camera for gesture detection.

2. **Software**
   - Python 3.7 or above.
   - TensorFlow (`pip install tensorflow`).
   - NumPy (`pip install numpy`).

---

## Installation

1. Clone this repository or download the project files.
2. Ensure you have the necessary dependencies installed:
   ```bash
   pip install tensorflow numpy

## View the live demo

[Click here!](https://youtu.be/1ocnkbKCkb0)
