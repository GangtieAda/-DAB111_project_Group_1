
# DAB111 Group Project
Hello, thank you for taking the time to look at our project!
## 1-Project Overview
This project demonstrates a complete workflow for data collection, processing, database storage, and web presentation using Python. The dataset contains sample student grades, stored in a SQLite database and displayed on a Flask-based website.
## 2-Folder Structure
```
01 - Data Collection
    ├── Sample_grades.csv
    ├── data summary.ipynb
02 - Data Processing
    ├── data cleaned _ code.ipynb
03 - Database
    ├── cleaned_sample_grades.db
    ├── database_code.ipynb
04 - Website
    ├── templates/
    │   ├── about.html
    │   ├── data_table.html
    │   ├── index_links.html
    │   ├── student1.jpg
    │   ├── student2.jpg
    ├── website_code.py
05 - Readme
06 - Requirements
```
## 3-Features
1. **Data Collection**:
   - Raw data is stored in `Sample_grades.csv`.
   - Initial data analysis is provided in `data summary.ipynb`.

2. **Data Processing**:
   - Data cleaning and preprocessing are performed in `data cleaned _ code.ipynb`.
   - Cleaned data is saved into a SQLite database (`cleaned_sample_grades.db`).

3. **Database**:
   - SQLite database created and managed with `sqlite3`.
   - Database contains a table named `pd_grades` with cleaned student data.
   - Database management script: `database_code.ipynb`.

4. **Website**:
   - Built using Flask.
   - Web pages:
     - **Home (`/`)**: Links to the main sections of the website.
     - **About (`/about`)**: Information about the dataset and its variables.
     - **Student Data (`/student`)**: Displays cleaned student data in tabular format.
   - Website script: `website_code.py`.

## 4-Code Explanation

### 1. Importing Required Libraries
```python
from flask import Flask, render_template
import sqlite3
import pathlib
import pandas as pd
```
- `Flask`: The core of the Flask web framework, used to create the web application.
- `render_template`: Allows us to render HTML templates for the pages.
- `sqlite3`: Provides an interface to interact with SQLite databases.
- `pathlib`: Used for managing file paths, specifically to set the path to the SQLite database.
- `pandas`:  Can be used for data processing.

### 2. Setting Up the Database Path
```python
base_path = pathlib.Path(r'C:\Users\qianr\OneDrive\桌面\Intro to Python\Website')
db_name = "cleaned_sample_grades.db"
db_path = base_path / db_name
print(db_path)
```
- Here, we set the path to the SQLite database file `cleaned_sample_grades.db`. The `pathlib.Path` helps to construct the correct path for the database file.

### 3. Creating Flask Application Instance
```python
app = Flask(__name__)
```
- The `Flask` instance `app` is created to initialize the web application.

### 4. Defining Routes

#### Home Route (`/`)
```python
@app.route("/")
def index():
    return render_template("index_links.html")
```
- This is the default route (home page) of the website. It renders the `index_links.html` template, which contains links to other pages (such as "About" and "Student Data").

#### About Route (`/about`)
```python
@app.route("/about")
def about():
    return render_template("about.html")
```
- The "About" page is rendered by the `about.html` template. This page contains information about the project, such as the source of the data and definitions of the variables.

#### Student Data Route (`/student`)
```python
@app.route("/student")
def data():
    try:
        con = sqlite3.connect(db_path)
        cursor = con.cursor()
        students = cursor.execute("SELECT * FROM pd_grades").fetchall()
        con.close()
        return render_template("data_table.html", students=students)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return "Error connecting to the database"
```
- This route is used to display the student data. It connects to the SQLite database (`cleaned_sample_grades.db`), fetches all data from the `pd_grades` table, and then closes the connection.
- The retrieved data is passed to the `data_table.html` template to display the student information in a table format.

### 5. Running the Application
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- This block runs the Flask application in debug mode, allowing you to see detailed error messages if something goes wrong. The app starts the web server at `http://127.0.0.1:5000`.

## 5-Dataset
- **Source**: Synthetic dataset representing student grades.
- **Variables**:
  - `Student ID`: Unique identifier for each student.
  - `Grade`: Numerical score representing performance.
  - Further details can be found on the website's *About* page.

## 6-Dependencies
Dependencies required to run the project are detailed in `requirements.txt`.

## 7-Team Members
- Member Ishmael Ashitey 
- Member Nawarat Medthunyapong
- Member Diego Felipe Moreno Lara
- Member Qianru Deng
- Member Wangchen Peng

