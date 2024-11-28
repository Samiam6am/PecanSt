from flask import Flask, request, render_template
import mysql.connector

from flask import Flask, request, render_template
import psycopg2  # Import the psycopg2 library

app = Flask(__name__)  # Initialize your Flask application

conn = psycopg2.connect(  # Establish a connection to the PostgreSQL database
    host="localhost",  # The hostname or IP address of the database server
    database="pecan_street_db",  # The name of your database
    user="weeyem21",  # Your PostgreSQL username (likely your macOS username)
    password="$hitstain017!"  # Your PostgreSQL password
)

@app.route('/', methods=['GET', 'POST'])  # Define the route for the home page
def index():
    if request.method == 'POST':  # Handle form submissions
        name = request.form['name']  # Get the 'name' field from the form
        telephone = request.form['telephone']  # Get the 'telephone' field from the form
        contract = request.form['contract']  # Get the 'contract' field from the form
        with conn.cursor() as cur:  # Use a context manager for the database cursor
            cur.execute("INSERT INTO contacts (name, telephone, contract) VALUES (%s, %s, %s)", (name, telephone, contract))  # Execute the SQL INSERT statement
            conn.commit()  # Commit the changes to the database
        return "Form submitted successfully!"  # Display a success message
    return render_template('index.html')  # Render the 'index.html' template for GET requests

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode