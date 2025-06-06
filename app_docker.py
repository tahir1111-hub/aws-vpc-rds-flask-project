"""
Flask application connected to MySQL database (Docker version)
"""
from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    """Create and return a connection to MySQL database"""
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            port=int(os.environ.get("MYSQL_PORT", 3306))
        )
        return connection, None
    except mysql.connector.Error as err:
        return None, f"Database connection error: {err}"

@app.route('/')
def home():
    """Home page route that displays MySQL connection status and databases"""
    connection, error = get_db_connection()
    
    if error:
        return render_template('home.html', 
                              connected=False, 
                              error=error,
                              databases=[])
    
    # Get list of databases
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return render_template('home.html', 
                          connected=True, 
                          error=None,
                          databases=databases)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')