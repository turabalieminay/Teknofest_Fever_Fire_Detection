# Teknofest_Fever_Fire_Detection

## Fire Detection System Using HaarCascade

This project demonstrates a real-time **Fire Detection System** using **HaarCascade** and **OpenCV**. The system captures video from a webcam, detects fire, and highlights the fire region on the video stream.

### Key Components:

1. **HaarCascade for Fire Detection**:
   - The fire detection is performed using a pre-trained HaarCascade model (`ates.xml`), which identifies fire in video frames.
   - The system processes each video frame to detect potential fire sources by converting the frame to grayscale and applying the fire detection model.

2. **Real-Time Video Capture**:
   - The system captures video from the webcam using **OpenCV**'s `VideoCapture` function.
   - It processes each frame in real-time to detect and highlight any fire regions.
   
3. **Drawing Bounding Boxes**:
   - When fire is detected, a bounding box is drawn around the detected region.
   - Additionally, the text "Hedef Tespit Edildi" (Target Detected) is displayed on the frame when fire is detected.

4. **Saving Detected Fire Video**:
   - The video, along with the fire detection highlights, is saved as `atestespiti.avi` using **OpenCV**'s `VideoWriter`.
   - This allows the user to review the detection results after the video stream has ended.

5. **Additional Features**:
   - A green rectangle is drawn around the main area of interest in the frame.
   - The text "G-Robotics" is displayed on every frame, representing the system's identification.
   - Servo motor control is implied in the print statement (`"Servolar Açıldı"`), indicating that when fire is detected, external systems like servos can be activated (though the actual servo control code is not present here).

### Workflow:
1. The webcam captures real-time video.
2. Each frame is processed by the **HaarCascade** fire detection model.
3. If fire is detected, a bounding box is drawn around the fire, and the detection result is saved to a video file.
4. The detection process runs in real-time until the user presses the 'q' key to stop the system.

### Dependencies:
- Python 3.x
- OpenCV (`pip install opencv-python`)
- HaarCascade XML file for fire detection (`ates.xml`)

This system is useful for early fire detection in environments where monitoring is required, such as industrial facilities, homes, or public spaces.
