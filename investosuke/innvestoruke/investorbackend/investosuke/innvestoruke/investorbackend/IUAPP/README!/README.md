# Face Recognition System - README

## Introduction

This project is a face recognition system built using OpenCV, dlib, face_recognition, and Tkinter. It enables users to:
- Capture training data from their webcam.
- Sort and organize face images into folders based on recognized faces.
- Perform facial recognition to identify individuals from the captured data.

The system is structured in a way that allows new users to easily interact with it using a graphical user interface (GUI), while also providing a detailed understanding for programmers to modify and extend its functionality.

## Features

1. **Capture Training Data**  
   Users can capture images of their face using a webcam, which are stored as training data for future facial recognition.

2. **Facial Recognition**  
   The system can identify previously captured faces by comparing the live camera feed with stored images.

3. **Sort Files**  
   Images can be sorted based on recognized faces, grouping them into folders for easier management.

4. **Pause and Resume**  
   You can pause and resume the image capture process to fine-tune the collection of training data.

5. **Stop Capture**  
   The camera capture process can be stopped at any time.

## Getting Started

### Requirements

- Python 3.x
- Libraries:
  - OpenCV
  - dlib
  - face_recognition
  - Tkinter
  - NumPy
  - JSON
  - datetime
  - shutil

You can install the required libraries using pip:

```bash
pip install opencv-python dlib face_recognition numpy