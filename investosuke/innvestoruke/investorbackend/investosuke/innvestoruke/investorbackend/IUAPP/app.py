from flask import Flask, request, render_template, jsonify
import json
import os
import bcrypt
import base64
import subprocess

app = Flask(__name__)

@app.route("/")
def startsite():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("sidebar.html")

data_file_path = r'C:\Users\Dennis\Desktop\Repositories\investosuke\innvestoruke\investorbackend\IUAPP\data.json'

if not os.path.exists(data_file_path):
    with open(data_file_path, "w") as file:
        json.dump({"people": []}, file, indent=4)

def load_database():
    try:
        with open(data_file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"people": []}

database = load_database()

@app.route('/login')
def loginSite():
    return render_template("login.html")

@app.route('/signup')
def signupSite():
    return render_template("signup.html")

@app.route('/form_signup', methods=['POST'])
def signup():
    name1 = request.form['username']
    pwd = request.form['password']
    gmail1 = request.form['gmail']

    for user in database["people"]:
        if user["gmail"] == gmail1:
            return render_template('signup.html', info='Gmail already in use.')

    for user in database["people"]:
        if user["username"] == name1:
            return render_template('signup.html', info='Username already taken.')
    
    hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    hashed_pwd_str = base64.urlsafe_b64encode(hashed_pwd).decode('utf-8')

    database["people"].append({"username": name1, "password": hashed_pwd_str, "gmail": gmail1})

    with open(data_file_path, "w") as file:
        json.dump(database, file, indent=4)
        
    return render_template('login.html', info='Signup successful! Please log in.')

@app.route('/form_login', methods=['POST'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']

    for user in database["people"]:
        if user["username"] == name1:
            stored_hash = base64.urlsafe_b64decode(user["password"])
            if bcrypt.checkpw(pwd.encode('utf-8'), stored_hash):
                return render_template('lounge.html', name=name1)
            else:
                return render_template('login.html', info='Invalid Password')

    return render_template('login.html', info='Invalid User')

@app.route('/run-ai-model', methods=['POST'])
def run_ai_model():
    try:
        # Path to the conda environment's python executable
        conda_python = r"C:\Users\Dennis\anaconda3\envs\AnacondaOptimised\python.exe"
        
        # Path to the Jupyter notebook you want to run
        notebook_path = '"C:\\Users\\Dennis\\Desktop\\Repositories\\Kamera AI Model.ipynb"'
        
        # Command to activate the conda environment and run the Jupyter notebook
        command = [
            r"C:\Users\Dennis\anaconda3\Scripts\activate.bat",  # Path to activate.bat
            "AnacondaOptimised",  # Conda environment name
            "&&",  # Ensure next command runs after activation
            conda_python,  # Path to the Python executable in the conda environment
            "-m", "jupyter", "nbconvert",  # Run nbconvert to execute the notebook
            "--to", "notebook",  # Convert to notebook format
            "--execute",  # Execute the notebook
            "--inplace",  # Modify the notebook in place
            notebook_path  # Path to the notebook
        ]

        # Run the command
        result = subprocess.run(" ".join(command), capture_output=True, text=True, check=True, shell=True)

        return jsonify({
            "message": "AI Model executed successfully!",
            "output": result.stdout
        }), 200

    except subprocess.CalledProcessError as e:
        return jsonify({
            "message": "Error executing AI Model.",
            "error": e.stderr
        }), 500

    except Exception as e:
        return jsonify({
            "message": "Unexpected error occurred.",
            "error": str(e)
        }), 500
    
if __name__ == "__main__":
    app.run(debug=True)
