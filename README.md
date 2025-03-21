Face Recognition System - README
Introduction
This project is a face recognition system built using OpenCV, dlib, face_recognition, and Tkinter. It enables users to:
Capture training data from their webcam.
Sort and organize face images into folders based on recognized faces.
Perform facial recognition to identify individuals from the captured data.
The system is structured in a way that allows new users to easily interact with it using a graphical user interface (GUI), while also providing a detailed understanding for programmers to modify and extend its functionality.

Features
1. Capture Training Data
Users can capture images of their face using a webcam, which are stored as training data for future facial recognition.
2. Facial Recognition
The system can identify previously captured faces by comparing the live camera feed with stored images.
3. Sort Files
Images can be sorted based on recognized faces, grouping them into folders for easier management.
4. Pause and Resume
You can pause and resume the image capture process to fine-tune the collection of training data.
5. Stop Capture
The camera capture process can be stopped at any time.

Getting Started
Requirements
Python 3.x
Libraries:
OpenCV
dlib
face_recognition
Tkinter
NumPy
JSON
datetime
shutil
You can install the required libraries using pip:
bash
Kopier
pip install opencv-python dlib face_recognition numpy

You will also need to download the following files:
shape_predictor_68_face_landmarks.dat (for detecting facial landmarks)
dlib_face_recognition_resnet_model_v1.dat (for face recognition)
Ensure these files are placed in the appropriate directories as specified in the code (for example, C:/Users/Dennis/Desktop/Repositories/).

Usage
Running the Application
 The main application runs a Tkinter-based GUI that includes buttons for each of the core functions:


Take Training Data: Starts the webcam to capture training data.
Sort Files: Allows you to sort images into folders based on face recognition.
Facial Recognition: Starts the webcam for live facial recognition.
Pause/Resume Capture: Pauses and resumes the data capture process.
Stop Camera: Stops the camera feed.
Workflow


First, you need to capture training data by clicking the "Take Training Data" button. You will be prompted to enter your name, and the system will capture and save images of your face.
After capturing data, use the "Facial Recognition" button to start recognizing faces from the webcam.
If needed, you can sort your images by clicking the "Sort Files" button, which will automatically organize them into folders based on recognition results.

Detailed Explanation for Programmers
1. Importing Libraries
The code uses several libraries for different tasks:
cv2: For capturing images and video from the webcam.
dlib: For face detection and face landmark prediction.
face_recognition: For face recognition and comparison.
tkinter: For creating the graphical user interface (GUI).
numpy, json, datetime: For processing data and saving information.
2. Paths and Directories
Several folders are set for storing detected faces, sorted faces, and related information:
python
Kopier
detected_faces_folder = "C:/Users/Dennis/Desktop/Repositories/detected_faces"
sorted_faces_folder = "C:/Users/Dennis/Desktop/Repositories/sorted_faces"
detected_faces_info_folder = "C:/Users/Dennis/Desktop/Repositories/detected_faces/detected_faces_info"

These paths can be customized to suit your needs.
3. Face Detection and Recognition Models
The system uses dlib for detecting faces and facial landmarks, and a pre-trained model for face recognition:
python
Kopier
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

4. Camera Setup and Image Capture
The take_training_data() function captures images from the webcam, detects faces, and saves them to the specified folder. It uses dlib's face detector to identify faces, and then captures and saves the images with face descriptors:
python
Kopier
faces = detector(rgb_frame)
face_descriptor = face_recognition_model.compute_face_descriptor(rgb_frame, shape)

5. Facial Recognition
The start_recognition() function loads saved face encodings from the "sorted_faces" folder and compares them with faces detected in the live video feed:
python
Kopier
matches = face_recognition.compare_faces(known_face_encodings, face_descriptor)
distances = face_recognition.face_distance(known_face_encodings, face_descriptor)

If a match is found, the recognized face is displayed along with the name and match distance.
6. Sorting Images
The sort_files() function allows users to sort images based on facial recognition. It compares newly selected images with previously sorted images and moves them into appropriate folders:
python
Kopier
if distance < 0.4:  # Threshold for matching
    matched_folder = folder_name

If no match is found, a new folder is created for that face.
7. Pause/Resume and Stop Functions
The system supports pausing and stopping the image capture process using global flags (paused, capturing):
python
Kopier
paused = not paused  # Toggle pause state
capturing = False  # Stop capturing


Conclusion
This face recognition system provides a user-friendly interface for capturing, sorting, and recognizing faces. It can be extended by adding features like saving multiple faces per user, improving recognition accuracy, or integrating with other applications. This README should serve as an introduction to both users and developers who want to understand or modify the underlying code.
