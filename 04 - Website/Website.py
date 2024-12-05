# Website Link: http://127.0.0.1:5000

from flask import Flask, render_template
import sqlite3
import pathlib
import pandas as pd

# Set up database path
base_path = pathlib.Path(r'C:\Users\qianr\OneDrive\桌面\Intro to Python\Website')
db_name = "cleaned_sample_grades.db"
db_path = base_path / db_name
print(db_path)


# Create Flask instance
app = Flask(__name__)

# Define the Home route ("/")
@app.route("/")
def index():
    return render_template("index_links.html") 

# Define the About route ("/about")
@app.route("/about")
def about():
    return render_template("about.html")

# Define the Student Data route ("/student")
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

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


