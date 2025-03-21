# Fennoscandia Studios Backend

This repository contains the backend Python code for Fennoscandia Studios, a platform that leverages facial recognition technology to offer AI-based identity detection. The backend handles user authentication, signup, data encryption, and interaction with the AI model.

## Features & Routes:

1. **/ (Home Page)**  
   **Description**: Serves the landing page (index.html).

2. **/home (Dashboard)**  
   **Description**: Renders the sidebar page (sidebar.html) after the user logs in.

3. **/login (Login Page)**  
   **Description**: Displays the login form (login.html).

4. **/signup (Signup Page)**  
   **Description**: Displays the signup form (signup.html).

5. **/form_signup (Signup Handling)**  
   **POST Method**: Handles the signup process.  
   **Features**:
   - Checks if the email or username already exists in the `data.json` database.
   - Hashes the password with bcrypt and stores the user data (username, email, hashed password).
   - Saves the updated database into the `data.json` file.

6. **/form_login (Login Handling)**  
   **POST Method**: Handles the login process.  
   **Features**:
   - Validates the username and password.
   - Compares the hashed password using bcrypt for secure authentication.
   - If valid, redirects the user to the lounge page (lounge.html).

7. **/run-ai-model (AI Model Execution)**  
   **POST Method**: Executes the facial recognition AI model using a Jupyter notebook.  
   **Features**:
   - Runs the Jupyter notebook using subprocess and the specified Conda environment (AnacondaOptimised).
   - Returns a success or error message along with the execution output.

## Encryption and Decryption Functions

This backend also includes encryption for sensitive data using Fernet (from the cryptography module), as well as a slow hashing function with PBKDF2 for added security:

### Encryption with Fernet:
- **Encrypt**: Encrypts sensitive data (e.g., passwords or other sensitive user data) before saving it to the database.
- **Decrypt**: Decrypts the encrypted data when needed.

### Slow Hashing with PBKDF2:
- **Hashing**: Generates a slow hash using PBKDF2, which can be used to securely store cryptographic keys.
- **Salting**: Generates a salt to add an additional layer of security when hashing the data.

## Important Code Sections:

### 1. Setup and Configuration

```python
import os
import json
import bcrypt
import base64
import subprocess
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

data_file_path = r'C:\path\to\data.json'

if not os.path.exists(data_file_path):
    with open(data_file_path, "w") as file:
        json.dump({"people": []}, file, indent=4)
